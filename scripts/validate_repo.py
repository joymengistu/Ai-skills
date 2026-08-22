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
    ROOT / "core" / "layered-system-prompts.md",
    ROOT / "core" / "ultra-ultra-mode.md",
    ROOT / "runtime" / "trace-schema.json",
    ROOT / "runtime" / "capability-manifest.schema.json",
    ROOT / "runtime" / "capability-manifest.example.json",
    ROOT / "runtime" / "online-run-profile.schema.json",
    ROOT / "runtime" / "progress-state-machine.md",
    ROOT / "governance" / "capability-risk-matrix.md",
    ROOT / "references" / "peak-upgrade-design.md",
    ROOT / "references" / "absolute-best-research.md",
    ROOT / "references" / "fable-like-runtime-blueprint.md",
    ROOT / "references" / "online-first-architecture.md",
    ROOT / "references" / "online-first-research.md",
    ROOT / "references" / "ui-vision-integration-map.md",
    ROOT / "references" / "ui-vision-scorecard.md",
    ROOT / "references" / "ui-ux-research.md",
    ROOT / "references" / "fable-research-notes.md",
    ROOT / "references" / "fable5-research-report.md",
    ROOT / "references" / "fable-capability-evidence-ledger.yaml",
    ROOT / "references" / "magic-pipeline.md",
    ROOT / "references" / "evolving-skills-gap-analysis.md",
    ROOT / "references" / "evolving-skills-architecture.md",
    ROOT / "runtime" / "skill-contract.schema.json",
    ROOT / "runtime" / "skill-contract.example.json",
    ROOT / "contributions" / "Fable-research-mission-original.txt",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 55:
    raise SystemExit(f"expected at least 55 skills, found {len(skills)}")
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
    ROOT / "skills" / "intent-preservation" / "SKILL.md",
    ROOT / "skills" / "product-completeness" / "SKILL.md",
    ROOT / "skills" / "dynamic-verification" / "SKILL.md",
    ROOT / "skills" / "requirement-traceability" / "SKILL.md",
    ROOT / "skills" / "completion-intelligence" / "SKILL.md",
    ROOT / "skills" / "evaluator-critic" / "SKILL.md",
    ROOT / "skills" / "context-handoff" / "SKILL.md",
    ROOT / "skills" / "tool-evaluation" / "SKILL.md",
    ROOT / "skills" / "capability-analysis" / "SKILL.md",
    ROOT / "skills" / "skill-composition" / "SKILL.md",
    ROOT / "skills" / "quality-judgment" / "SKILL.md",
    ROOT / "skills" / "capability-gap-response" / "SKILL.md",
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
    "Ultra Ultra Mode",
    "requirement",
    "CAPABILITY LIFECYCLE",
    "output generated",
    "independent evaluator",
    "CAPABILITY ANALYSIS ROUTE",
    "EVOLVING CAPABILITY ROUTE",
]:
    if phrase.lower() not in prompt.lower():
        raise SystemExit(f"self-prompt missing principle: {phrase}")

online_profile = json.loads((ROOT / "runtime" / "online-run-profile.schema.json").read_text(encoding="utf-8"))
for key in ["run_id", "mode", "model_policy", "tool_policy", "budgets", "privacy", "delivery", "recovery"]:
    if key not in online_profile.get("required", []):
        raise SystemExit(f"online run profile schema missing required field: {key}")

trace = json.loads((ROOT / "runtime" / "trace-schema.json").read_text(encoding="utf-8"))
for key in ["schema_version", "run_id", "sequence", "timestamp", "actor", "event_type", "risk_class"]:
    if key not in trace.get("required", []):
        raise SystemExit(f"trace schema missing required field: {key}")

skill_contract = json.loads((ROOT / "runtime" / "skill-contract.schema.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "procedure", "constraints", "dependencies", "permissions", "risk_class", "verification", "evaluation", "lifecycle", "provenance", "owner", "rollback"]:
    if key not in skill_contract.get("required", []):
        raise SystemExit(f"skill contract schema missing required field: {key}")

skill_contract_example = json.loads((ROOT / "runtime" / "skill-contract.example.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "procedure", "constraints", "dependencies", "permissions", "risk_class", "verification", "evaluation", "lifecycle", "provenance", "owner", "rollback"]:
    if key not in skill_contract_example:
        raise SystemExit(f"skill contract example missing field: {key}")

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
    "intent-preservation",
    "product-completeness",
    "dynamic-verification",
    "requirement-traceability",
    "requirement-compiler",
    "build-recipes",
    "staged-execution",
    "repair-loop",
    "runtime-host",
    "online-orchestration",
    "hosted-tool-bridge",
    "progressive-delivery",
    "cost-aware-execution",
    "ui-vision",
    "design-reference-library",
    "completion-intelligence",
    "evaluator-critic",
    "context-handoff",
    "tool-evaluation",
    "capability-analysis",
    "skill-composition",
    "quality-judgment",
    "capability-gap-response",
]:
    if f"  - {name}" not in manifest:
        raise SystemExit(f"manifest missing skill: {name}")

for path in [ROOT / "contributions" / "ULTRIA-original.txt", ROOT / "contributions" / "FORK-original.txt", ROOT / "contributions" / "UI-Vision-original.txt", ROOT / "contributions" / "Fable-research-mission-original.txt"]:
    if path.stat().st_size < 1000:
        raise SystemExit(f"user source document unexpectedly small: {path}")

subprocess.run(["python3", str(ROOT / "evals" / "validate_cases.py")], check=True)
print(f"validated repository with {len(skills)} skills")
