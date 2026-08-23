"""Small deterministic primitives for governed skill intelligence.

This module is intentionally provider-agnostic and dependency-light. It validates
records against the repository's JSON Schemas, appends memory records without
rewriting history, checks example coverage, and makes a conservative paired
baseline/candidate decision. It is a reference kernel, not a production service.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable


class ValidationError(ValueError):
    """Raised when a record violates the supported JSON Schema subset."""


def load_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _type_ok(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(expected, True)


def validate_record(record: Any, schema: dict[str, Any], path: str = "$" ) -> None:
    """Validate the subset used by the intelligence schemas.

    The repository does not require a third-party JSON Schema package. The
    function deliberately fails closed for required fields, types, enums,
    constants, ranges, patterns, nested properties, and array item contracts.
    """
    expected_type = schema.get("type")
    if expected_type is not None:
        allowed = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(_type_ok(record, kind) for kind in allowed):
            raise ValidationError(f"{path}: expected {allowed}, got {type(record).__name__}")
    if "const" in schema and record != schema["const"]:
        raise ValidationError(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and record not in schema["enum"]:
        raise ValidationError(f"{path}: value {record!r} is outside enum")
    if isinstance(record, str):
        if len(record) < schema.get("minLength", 0):
            raise ValidationError(f"{path}: string is shorter than minLength")
        if "pattern" in schema and re.search(schema["pattern"], record) is None:
            raise ValidationError(f"{path}: string does not match pattern")
    if isinstance(record, (int, float)) and not isinstance(record, bool):
        if record < schema.get("minimum", record) or record > schema.get("maximum", record):
            raise ValidationError(f"{path}: number is outside allowed range")
    if isinstance(record, list):
        if len(record) < schema.get("minItems", 0):
            raise ValidationError(f"{path}: array has too few items")
        if "items" in schema:
            for index, item in enumerate(record):
                validate_record(item, schema["items"], f"{path}[{index}]")
    if isinstance(record, dict):
        for key in schema.get("required", []):
            if key not in record:
                raise ValidationError(f"{path}: missing required field {key!r}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = sorted(set(record) - set(properties))
            if extra:
                raise ValidationError(f"{path}: unexpected fields {extra}")
        for key, value in record.items():
            if key in properties:
                validate_record(value, properties[key], f"{path}.{key}")


def append_record(path: str | Path, record: dict[str, Any]) -> None:
    """Append one JSON record, preserving prior records and adding a newline."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")


def example_coverage(records: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Return required example kinds and the missing kinds for a principle."""
    required = {"positive", "negative", "borderline", "exception", "transformation"}
    observed = {record.get("kind") for record in records}
    return {"observed": sorted(kind for kind in observed if kind), "missing": sorted(required - observed), "complete": required <= observed}


def paired_decision(
    baseline: dict[str, float],
    candidate: dict[str, float],
    hard_gates: dict[str, bool],
    lower_is_better: Iterable[str] = (),
    minimum_improvement: float = 0.0,
) -> dict[str, Any]:
    """Make a conservative decision from paired metrics.

    Promotion requires all hard gates, at least one improvement, and no metric
    regression beyond the permitted threshold. This does not replace human
    review, statistical analysis, or task-specific judgment.
    """
    lower = set(lower_is_better)
    keys = sorted(set(baseline) | set(candidate))
    missing = [key for key in keys if key not in baseline or key not in candidate]
    if missing:
        return {"decision": "hold", "reason": "incomplete_paired_metrics", "missing_metrics": missing, "improvements": [], "regressions": []}
    improvements: list[str] = []
    regressions: list[str] = []
    for key in keys:
        delta = candidate[key] - baseline[key]
        if key in lower:
            delta = -delta
        if delta > minimum_improvement:
            improvements.append(key)
        elif delta < -minimum_improvement:
            regressions.append(key)
    failed_gates = sorted(key for key, passed in hard_gates.items() if not passed)
    if failed_gates:
        decision = "reject"
        reason = "hard_gate_failure"
    elif regressions:
        decision = "reject"
        reason = "regression_detected"
    elif not improvements:
        decision = "hold"
        reason = "no_measurable_improvement"
    else:
        decision = "promote"
        reason = "paired_improvement_without_regression"
    return {"decision": decision, "reason": reason, "failed_gates": failed_gates, "improvements": improvements, "regressions": regressions}


def aggregate_paired_results(results: Iterable[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate case-level baseline/candidate outcomes without hiding regressions.

    Each result must contain ``case_id``, boolean ``baseline_success`` and
    ``candidate_success``, plus an optional ``hard_gates`` mapping. A result is
    intentionally rejected if the pair is incomplete. The output keeps gains,
    regressions, residual failures, and gate failures separate rather than
    collapsing them into one average.
    """
    rows = list(results)
    if not rows:
        raise ValidationError("paired results cannot be empty")
    required = {"case_id", "baseline_success", "candidate_success"}
    seen: set[str] = set()
    gains: list[str] = []
    regressions: list[str] = []
    residual_failures: list[str] = []
    unchanged_successes: list[str] = []
    hard_gate_failures: dict[str, list[str]] = {}
    for row in rows:
        missing = sorted(required - set(row))
        if missing:
            raise ValidationError(f"paired result missing fields: {missing}")
        case_id = str(row["case_id"])
        if not case_id or case_id in seen:
            raise ValidationError(f"duplicate or empty case_id: {case_id!r}")
        seen.add(case_id)
        baseline_success = row["baseline_success"]
        candidate_success = row["candidate_success"]
        if not isinstance(baseline_success, bool) or not isinstance(candidate_success, bool):
            raise ValidationError(f"success flags must be boolean for {case_id}")
        if not baseline_success and candidate_success:
            gains.append(case_id)
        elif baseline_success and not candidate_success:
            regressions.append(case_id)
        elif not baseline_success and not candidate_success:
            residual_failures.append(case_id)
        else:
            unchanged_successes.append(case_id)
        gates = row.get("hard_gates", {})
        if not isinstance(gates, dict):
            raise ValidationError(f"hard_gates must be an object for {case_id}")
        for gate, passed in sorted(gates.items()):
            if not isinstance(passed, bool):
                raise ValidationError(f"hard gate must be boolean: {case_id}.{gate}")
            if not passed:
                hard_gate_failures.setdefault(str(gate), []).append(case_id)
    total = len(rows)
    return {
        "case_count": total,
        "baseline_successes": sum(bool(row["baseline_success"]) for row in rows),
        "candidate_successes": sum(bool(row["candidate_success"]) for row in rows),
        "baseline_success_rate": sum(bool(row["baseline_success"]) for row in rows) / total,
        "candidate_success_rate": sum(bool(row["candidate_success"]) for row in rows) / total,
        "gains": sorted(gains),
        "regressions": sorted(regressions),
        "residual_failures": sorted(residual_failures),
        "unchanged_successes": sorted(unchanged_successes),
        "hard_gate_failures": {key: sorted(value) for key, value in sorted(hard_gate_failures.items())},
        "net_success_delta": (sum(bool(row["candidate_success"]) for row in rows) - sum(bool(row["baseline_success"]) for row in rows)) / total,
    }
