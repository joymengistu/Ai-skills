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
    ROOT / "references" / "lovable-agent-architecture.md",
    ROOT / "references" / "repository-comparison.md",
    ROOT / "evals" / "comparative-benchmark-plan.md",
    ROOT / "runtime" / "skill-contract.schema.json",
    ROOT / "runtime" / "skill-contract.example.json",
    ROOT / "runtime" / "reference_host" / "__init__.py",
    ROOT / "runtime" / "reference_host" / "__main__.py",
    ROOT / "runtime" / "reference_host" / "host.py",
    ROOT / "runtime" / "reference_host" / "test_host.py",
    ROOT / "runtime" / "reference_host" / "risk_controls.py",
    ROOT / "references" / "reference-host-architecture.md",
    ROOT / "references" / "agent-risk-research-notes.md",
    ROOT / "references" / "agent-risk-control-blueprint.md",
    ROOT / "references" / "professional-taste-research-notes.md",
    ROOT / "references" / "professional-taste-architecture.md",
    ROOT / "references" / "professional-ui-patterns.md",
    ROOT / "references" / "professional-ui-improvement-report-2026-08-23.md",
    ROOT / "references" / "one-shot-execution-prompt.md",
    ROOT / "references" / "one-shot-improvement-report-2026-08-23.md",
    ROOT / "references" / "skill-expansion-audit-2026-08-23.md",
    ROOT / "references" / "skill-expansion-self-prompt.md",
    ROOT / "references" / "skill-expansion-release-report-2026-08-23.md",
    ROOT / "scripts" / "deepen_skills.py",
    ROOT / "scripts" / "test_skill_expansion.py",
    ROOT / "references" / "contextual-user-intelligence-architecture.md",
    ROOT / "references" / "skill-engineering-intelligence.md",
    ROOT / "references" / "master-mission-implementation-map.md",
    ROOT / "references" / "intelligence-infrastructure-audit.md",
    ROOT / "references" / "public-agent-infrastructure-research-2026-08-23.md",
    ROOT / "references" / "intelligence-infrastructure-architecture.md",
    ROOT / "references" / "intelligence-infrastructure-self-critique.md",
    ROOT / "references" / "hosted-evaluation-research-brief-2026-08-23.md",
    ROOT / "references" / "hosted-evaluation-architecture-research-2026-08-23.md",
    ROOT / "references" / "provider-adapter-boundary.md",
    ROOT / "references" / "max-capability-gap-audit-2026-08-23.md",
    ROOT / "references" / "max-capability-improvement-report-2026-08-23.md",
    ROOT / "evals" / "lovability-benchmark-plan.md",
    ROOT / "runtime" / "risk-control.schema.json",
    ROOT / "runtime" / "normalized-trace.schema.json",
    ROOT / "runtime" / "reference_host" / "normalized_trace.py",
    ROOT / "runtime" / "reference_host" / "verifiers.py",
    ROOT / "runtime" / "reference_host" / "test_normalized_trace.py",
    ROOT / "runtime" / "intelligence" / "research-memory.schema.json",
    ROOT / "runtime" / "intelligence" / "lesson-memory.schema.json",
    ROOT / "runtime" / "intelligence" / "example-record.schema.json",
    ROOT / "runtime" / "intelligence" / "intent-prediction.schema.json",
    ROOT / "runtime" / "intelligence" / "communication-trial.schema.json",
    ROOT / "runtime" / "intelligence" / "evaluation-record.schema.json",
    ROOT / "runtime" / "intelligence" / "improvement-record.schema.json",
    ROOT / "runtime" / "intelligence" / "benchmark-run.schema.json",
    ROOT / "runtime" / "intelligence" / "behavior-observation.schema.json",
    ROOT / "runtime" / "intelligence" / "kernel.py",
    ROOT / "runtime" / "intelligence" / "test_kernel.py",
    ROOT / "examples" / "intelligence" / "records.jsonl",
    ROOT / "evals" / "intelligence-benchmark.json",
    ROOT / "scripts" / "run_intelligence_benchmark.py",
    ROOT / "scripts" / "test_intelligence_benchmark.py",
    ROOT / "contributions" / "Fable-research-mission-original.txt",
    ROOT / "contributions" / "lovability-communication-mission-original.txt",
    ROOT / "contributions" / "contextual-user-intelligence-mission-original.txt",
    ROOT / "contributions" / "master-self-improving-ai-skills-mission-original.txt",
]
for path in required:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if len(skills) < 61:
    raise SystemExit(f"expected at least 61 skills, found {len(skills)}")
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
    ROOT / "skills" / "lovability" / "SKILL.md",
    ROOT / "skills" / "brainstorm-mode" / "SKILL.md",
    ROOT / "skills" / "agent-risk-controls" / "SKILL.md",
    ROOT / "skills" / "professional-taste" / "SKILL.md",
    ROOT / "skills" / "contextual-user-intelligence" / "SKILL.md",
    ROOT / "skills" / "intelligence-infrastructure" / "SKILL.md",
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
    "RISK-CONTROL ROUTE",
    "LOVABILITY AND BRAINSTORM ROUTE",
    "INTELLIGENCE INFRASTRUCTURE ROUTE",
    "risk",
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

risk_control = json.loads((ROOT / "runtime" / "risk-control.schema.json").read_text(encoding="utf-8"))
for key in ["trust_envelope", "action_intent", "approval_record", "incident_record"]:
    if key not in risk_control.get("required", []):
        raise SystemExit(f"risk-control schema missing required record: {key}")

skill_contract = json.loads((ROOT / "runtime" / "skill-contract.schema.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "procedure", "constraints", "dependencies", "permissions", "risk_class", "verification", "evaluation", "lifecycle", "provenance", "owner", "rollback", "examples", "limitations", "uncertainty", "lessons_learned", "version_history"]:
    if key not in skill_contract.get("required", []):
        raise SystemExit(f"skill contract schema missing required field: {key}")

skill_contract_example = json.loads((ROOT / "runtime" / "skill-contract.example.json").read_text(encoding="utf-8"))
for key in ["name", "version", "purpose", "triggers", "inputs", "outputs", "procedure", "constraints", "dependencies", "permissions", "risk_class", "verification", "evaluation", "lifecycle", "provenance", "owner", "rollback", "examples", "limitations", "uncertainty", "lessons_learned", "version_history"]:
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
    "lovability",
    "brainstorm-mode",
    "agent-risk-controls",
    "professional-taste",
    "contextual-user-intelligence",
    "intelligence-infrastructure",
]:
    if f"  - {name}" not in manifest:
        raise SystemExit(f"manifest missing skill: {name}")

for path in [ROOT / "contributions" / "ULTRIA-original.txt", ROOT / "contributions" / "FORK-original.txt", ROOT / "contributions" / "UI-Vision-original.txt",     ROOT / "contributions" / "Fable-research-mission-original.txt", ROOT / "contributions" / "maximum-capability-research-mission-original.txt", ROOT / "contributions" / "lovable-ai-research-mission-original.txt", ROOT / "contributions" / "lovability-communication-mission-original.txt", ROOT / "contributions" / "contextual-user-intelligence-mission-original.txt", ROOT / "contributions" / "master-self-improving-ai-skills-mission-original.txt"]:

    if path.stat().st_size < 1000:
        raise SystemExit(f"user source document unexpectedly small: {path}")

subprocess.run(["python3", str(ROOT / "evals" / "validate_cases.py")], check=True)
subprocess.run(["python3", "-m", "unittest", "discover", "-s", "runtime/reference_host", "-p", "test_*.py"], cwd=ROOT, check=True)
subprocess.run(["python3", "-m", "unittest", "discover", "-s", "runtime/intelligence", "-p", "test_*.py"], cwd=ROOT, check=True)
subprocess.run(["python3", "scripts/run_intelligence_benchmark.py", "--suite", "evals/intelligence-benchmark.json", "--cases", "evals/cases.jsonl"], cwd=ROOT, check=True)
subprocess.run(["python3", "-m", "unittest", "-v", "scripts/test_intelligence_benchmark.py"], cwd=ROOT, check=True)
print(f"validated repository with {len(skills)} skills")
