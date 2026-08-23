#!/usr/bin/env python3
"""Build a conservative capability map for every repository Skill.

The audit records observable structure and keyword signals only. It does not
claim that a section is substantively correct merely because a keyword exists.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OUT_JSON = ROOT / "references" / "skill-catalog-capability-map.json"
OUT_MD = ROOT / "references" / "skill-catalog-audit-2026-08-23.md"

SIGNALS = {
    "inputs": ["input", "brief", "request", "reference", "context"],
    "outputs": ["output", "artifact", "deliverable", "result"],
    "activation": ["use when", "load when", "activate", "trigger"],
    "process": ["workflow", "step", "execute", "process", "pipeline"],
    "tools": ["tool", "browser", "shell", "api", "runtime"],
    "examples": ["good example", "bad example", "example", "transformation"],
    "failure_modes": ["failure", "fallback", "blocked", "risk", "recovery"],
    "verification": ["verify", "evidence", "test", "acceptance", "check"],
    "limitations": ["limit", "unknown", "uncertain", "not assessable", "boundary"],
}


def frontmatter_and_body(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) != 3:
        return {}, text
    metadata: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"')
    return metadata, parts[2]


def headings(body: str) -> list[str]:
    return [line.strip() for line in body.splitlines() if re.match(r"^#{1,4}\s+", line)]


def linked_paths(text: str) -> list[str]:
    return sorted(set(re.findall(r"(?:skills|references|runtime|governance|core|evals)/[A-Za-z0-9_./-]+", text)))


def signal_report(body: str) -> dict[str, bool]:
    lower = body.lower()
    return {name: any(term in lower for term in terms) for name, terms in SIGNALS.items()}


def quality_flags(meta: dict[str, str], body: str, hs: list[str]) -> list[str]:
    flags: list[str] = []
    if not meta.get("name") or not meta.get("description"):
        flags.append("missing_frontmatter")
    if len(body.splitlines()) >= 500:
        flags.append("body_at_or_over_500_lines")
    if "TODO" in body or "[TODO" in body:
        flags.append("contains_todo")
    if "## Operational deepening" not in body and meta.get("name") != "screenshot-reconstruction":
        flags.append("missing_operational_deepening")
    signals = signal_report(body)
    if not signals["verification"]:
        flags.append("missing_verification_signal")
    if not signals["examples"]:
        flags.append("missing_example_signal")
    if not signals["limitations"]:
        flags.append("missing_limitation_signal")
    return flags


def main() -> None:
    records: list[dict[str, object]] = []
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        meta, body = frontmatter_and_body(text)
        hs = headings(body)
        records.append({
            "name": meta.get("name", path.parent.name),
            "path": str(path.relative_to(ROOT)),
            "description": meta.get("description", ""),
            "line_count": len(text.splitlines()),
            "headings": hs,
            "linked_paths": linked_paths(text),
            "observable_signals": signal_report(body),
            "quality_flags": quality_flags(meta, body, hs),
            "assessment_boundary": "Structural audit only; substantive quality requires task-specific evaluation.",
        })

    summary = {
        "audit_id": "skill-catalog-audit-2026-08-23",
        "repository": str(ROOT),
        "skill_count": len(records),
        "records": records,
        "aggregate": {
            "with_quality_flags": sum(bool(r["quality_flags"]) for r in records),
            "with_verification_signal": sum(r["observable_signals"]["verification"] for r in records),
            "with_examples_signal": sum(r["observable_signals"]["examples"] for r in records),
            "with_failure_signal": sum(r["observable_signals"]["failure_modes"] for r in records),
            "with_limitations_signal": sum(r["observable_signals"]["limitations"] for r in records),
        },
    }
    OUT_JSON.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    flagged = [r for r in records if r["quality_flags"]]
    lines = [
        "# Skill Catalog Audit — 23 August 2026",
        "",
        "> This is a conservative structural audit. A keyword or heading signal is not evidence that a Skill works; task-specific evaluation is still required.",
        "",
        f"The catalog contains **{len(records)} Skills**. **{len(flagged)}** have at least one structural follow-up flag. The machine-readable map is `skill-catalog-capability-map.json`.",
        "",
        "## Aggregate signals",
        "",
        "| Signal | Count | Interpretation |",
        "|---|---:|---|",
        f"| Verification/evidence signal | {summary['aggregate']['with_verification_signal']} | A verification-related term appears; this is not proof of a passing test |",
        f"| Example signal | {summary['aggregate']['with_examples_signal']} | An example-related term appears; distinction quality requires review |",
        f"| Failure/recovery signal | {summary['aggregate']['with_failure_signal']} | A failure, fallback, risk, or recovery term appears |",
        f"| Limitation/uncertainty signal | {summary['aggregate']['with_limitations_signal']} | A boundary or uncertainty term appears |",
        f"| Any structural flag | {summary['aggregate']['with_quality_flags']} | Requires targeted review before assuming uniform quality |",
        "",
        "## Follow-up flags",
        "",
        "| Skill | Flags |",
        "|---|---|",
    ]
    if flagged:
        for record in flagged:
            lines.append(f"| `{record['name']}` | {', '.join(record['quality_flags'])} |")
    else:
        lines.append("| None | No structural flags detected |")
    lines += [
        "",
        "## Audit interpretation",
        "",
        "The repository is strongest in explicit routing, evidence boundaries, runtime control references, screenshot reconstruction, human lovability principles, and governed evaluation structure. The main systemic risk is uneven depth and uneven measurability across Skills: structural presence is not the same as validated capability. The roadmap therefore prioritizes shared contracts, measurable baseline/candidate comparisons, curation, and human review over indiscriminate expansion.",
        "",
        "The next mission should use this map to select a small representative sample for substantive review. Do not rewrite every Skill merely because a structural signal is absent; first measure whether the omission causes a task failure or meaningful context cost.",
        "",
        "## Reproducibility",
        "",
        "Run `python3 scripts/audit_skill_catalog.py` from the repository root. The script records observable metadata and signals only and should be rerun after material catalog changes.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"audited {len(records)} Skills")
    print(f"flagged {len(flagged)} Skills")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
