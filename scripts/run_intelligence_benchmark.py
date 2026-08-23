#!/usr/bin/env python3
"""Validate and compare Ai-skills intelligence benchmark runs.

This runner is intentionally model/provider agnostic. It validates case-set
separation and, when supplied with measured metric JSON files, delegates the
promotion decision to the deterministic intelligence kernel. It never invents
model results and never treats a manifest validation as a quality win.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime" / "intelligence"))
from kernel import paired_decision  # noqa: E402


def load_cases(path: Path) -> set[str]:
    return {json.loads(line)["id"] for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def validate_suite(suite_path: Path, cases_path: Path) -> dict[str, object]:
    suite = json.loads(suite_path.read_text(encoding="utf-8"))
    case_ids = load_cases(cases_path)
    families = suite["families"]
    missing = sorted({case_id for ids in families.values() for case_id in ids if case_id not in case_ids})
    development = set(families["development"])
    held_out = set(families["held_out"])
    if missing:
        raise ValueError(f"benchmark references missing cases: {missing}")
    if development & held_out:
        raise ValueError(f"development and held-out cases overlap: {sorted(development & held_out)}")
    return {"suite_id": suite["suite_id"], "suite_version": suite["suite_version"], "case_count": len(case_ids), "families": {key: len(value) for key, value in families.items()}, "status": "manifest_validated"}


def compare_metrics(baseline_path: Path, candidate_path: Path, hard_gates: dict[str, bool], lower_is_better: list[str]) -> dict[str, object]:
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
    for payload, label in [(baseline, "baseline"), (candidate, "candidate")]:
        if payload.get("measurement_status") != "measured":
            raise ValueError(f"{label} metrics must explicitly declare measurement_status=measured")
        if payload.get("model_ref") != baseline.get("model_ref") or payload.get("budget_ref") != baseline.get("budget_ref"):
            raise ValueError("baseline and candidate must use the same model_ref and budget_ref")
    return paired_decision(baseline["metrics"], candidate["metrics"], hard_gates, lower_is_better=lower_is_better)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default=str(ROOT / "evals" / "intelligence-benchmark.json"))
    parser.add_argument("--cases", default=str(ROOT / "evals" / "cases.jsonl"))
    parser.add_argument("--baseline-metrics")
    parser.add_argument("--candidate-metrics")
    parser.add_argument("--hard-gate", action="append", default=[], help="name=true|false; repeatable")
    parser.add_argument("--lower-is-better", action="append", default=[])
    args = parser.parse_args()
    summary = validate_suite(Path(args.suite), Path(args.cases))
    if bool(args.baseline_metrics) != bool(args.candidate_metrics):
        raise SystemExit("provide both --baseline-metrics and --candidate-metrics, or neither")
    if args.baseline_metrics:
        gates: dict[str, bool] = {}
        for item in args.hard_gate:
            name, value = item.split("=", 1)
            gates[name] = value.lower() == "true"
        summary["comparison"] = compare_metrics(Path(args.baseline_metrics), Path(args.candidate_metrics), gates, args.lower_is_better)
        summary["status"] = "paired_comparison_completed"
    else:
        summary["comparison"] = {"status": "not_run", "reason": "no measured baseline and candidate metrics supplied"}
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
