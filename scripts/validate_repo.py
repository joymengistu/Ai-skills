#!/usr/bin/env python3
"""Static structural checks for the Ai skills repository."""
from pathlib import Path
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "README.md",
    ROOT / "manifest.yaml",
    ROOT / "core" / "self-directing-prompt.md",
    ROOT / "core" / "action-protocol.md",
    ROOT / "runtime" / "trace-schema.json",
    ROOT / "runtime" / "capability-manifest.schema.json",
    ROOT / "runtime" / "capability-manifest.example.json",
    ROOT / "runtime" / "progress-state-machine.md",
    ROOT / "governance" / "capability-risk-matrix.md",
    ROOT / "references" / "peak-upgrade-design.md",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 30:
    raise SystemExit(f"expected at least 30 skills, found {len(skills)}")
for path in skills:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "name:" not in text or "description:" not in text:
        raise SystemExit(f"invalid frontmatter: {path}")
    if len(text.splitlines()) > 500:
        raise SystemExit(f"skill exceeds 500 lines: {path}")

for path in [
    ROOT / "core" / "operating-contract.md",
    ROOT / "skills" / "safety-governance" / "SKILL.md",
    ROOT / "skills" / "evaluation" / "SKILL.md",
    ROOT / "skills" / "durable-execution" / "SKILL.md",
    ROOT / "skills" / "evidence-ledger" / "SKILL.md",
    ROOT / "skills" / "human-feedback" / "SKILL.md",
]:
    if not path.exists():
        raise SystemExit(f"missing governance or peak skill file: {path}")

prompt = (ROOT / "core" / "self-directing-prompt.md").read_text(encoding="utf-8")
for phrase in [
    "Never claim success",
    "Ask for approval",
    "smallest sufficient context",
    "Verify",
    "SUPERLATIVE COMPILER",
    "correct useful action",
]:
    if phrase.lower() not in prompt.lower():
        raise SystemExit(f"self-prompt missing principle: {phrase}")

trace = json.loads((ROOT / "runtime" / "trace-schema.json").read_text(encoding="utf-8"))
for key in ["schema_version", "run_id", "sequence", "timestamp", "actor", "event_type", "risk_class"]:
    if key not in trace.get("required", []):
        raise SystemExit(f"trace schema missing required field: {key}")

capability_manifest = json.loads((ROOT / "runtime" / "capability-manifest.schema.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "dependencies", "permissions", "risk_class", "tests", "owner", "rollback"]:
    if key not in capability_manifest.get("required", []):
        raise SystemExit(f"capability manifest schema missing required field: {key}")

example_manifest = json.loads((ROOT / "runtime" / "capability-manifest.example.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "dependencies", "permissions", "risk_class", "tests", "owner", "rollback"]:
    if key not in example_manifest:
        raise SystemExit(f"capability manifest example missing field: {key}")

manifest = (ROOT / "manifest.yaml").read_text(encoding="utf-8")
for name in [
    "superlative-analysis",
    "frontier-research",
    "optimal-assistance",
    "product-strategy",
    "outcome-completion",
    "durable-execution",
    "evidence-ledger",
    "human-feedback",
    "skill-forging",
    "model-routing",
    "agent-collaboration",
    "multimodal-reasoning",
    "accessibility",
    "incident-response",
    "capability-discovery",
]:
    if f"  - {name}" not in manifest:
        raise SystemExit(f"manifest missing skill: {name}")

for path in [ROOT / "contributions" / "ULTRIA-original.txt", ROOT / "contributions" / "FORK-original.txt"]:
    if path.stat().st_size < 1000:
        raise SystemExit(f"user source document unexpectedly small: {path}")

subprocess.run(["python3", str(ROOT / "evals" / "validate_cases.py")], check=True)
print(f"validated repository with {len(skills)} skills")
