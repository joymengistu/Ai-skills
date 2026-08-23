"""Add a parameterized operational section to each Skill exactly once.

This is a controlled catalog migration, not a request to inflate files blindly.
The generated section is intentionally short, domain-specific, and removable.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FOCUS = {
    "accessibility": ("perception, operation, understanding, and recovery", "keyboard order, focus visibility, names/roles, contrast, zoom/reflow, reduced motion, and assistive technology paths"),
    "agent-collaboration": ("safe delegation and worker handoffs", "ownership, inputs/outputs, conflict isolation, budgets, evidence, and handoff recovery"),
    "agent-risk-controls": ("bounded authority and harmful-action resistance", "trust labels, action intent, approvals, destination scope, cancellation, logging, and incident handling"),
    "brainstorm-mode": ("useful expansion without forcing commitment", "understanding, branches, connections, challenge, uncertainty, refinement, and user choice"),
    "build-recipes": ("reusable implementation recipes", "provenance, assumptions, dependencies, licenses, vertical slices, adaptation, and verification"),
    "capability-analysis": ("fairly separating model, harness, tools, state, and evaluator effects", "source quality, confounders, matched tasks, unknown mechanisms, and cautious conclusions"),
    "capability-discovery": ("selecting the smallest sufficient capability bundle", "task decomposition, triggers, dependencies, conflicts, permissions, and missing-capability escalation"),
    "capability-gap-response": ("responding to repeated failures without unsafe self-expansion", "failure evidence, existing alternatives, narrow candidate scope, tests, rollback, and authorization"),
    "coding": ("reliable software changes", "repository inspection, requirement mapping, smallest patch, tests, runtime behavior, and rollback"),
    "communication": ("clear, context-fit user communication", "intent, audience, tone, structure, uncertainty, actionability, and concise completion reporting"),
    "completion-intelligence": ("distinguishing generated output from complete outcome", "requirements, evidence, runtime behavior, edge states, safety, human experience, and status"),
    "context-engineering": ("selecting and compressing useful context", "relevance, provenance, freshness, conflicts, privacy, handoff, and context-budget tradeoffs"),
    "context-handoff": ("resumable work across workers or context resets", "objective, requirements, decisions, artifacts, evidence, failures, tests, unknowns, and next action"),
    "contextual-user-intelligence": ("scoped, correctable predictions about user intent and preferences", "evidence, alternatives, confidence, expiry, correction, sensitivity boundaries, and no authorization"),
    "cost-aware-execution": ("maximizing value under time, token, tool, and money budgets", "expected value, escalation, caching, stopping, user effort, and cost evidence"),
    "creative-work": ("original creative outcomes with purposeful constraints", "brief, references, originality, iteration, format, accessibility, and delivery checks"),
    "data-analysis": ("reproducible analysis and honest interpretation", "data provenance, cleaning, assumptions, uncertainty, visualization, validation, and limitations"),
    "design-reference-library": ("abstracting useful principles from visual references", "layout, hierarchy, tokens, interaction, originality, accessibility, and screenshot limits"),
    "durable-execution": ("safe progress across interruptions and uncertain side effects", "idempotency, checkpoints, reconciliation, retries, cancellation, and recovery evidence"),
    "dynamic-verification": ("testing the real artifact rather than static plausibility", "primary journeys, invalid/empty/loading states, responsive behavior, permissions, recovery, and evidence"),
    "evaluation": ("independent and reproducible quality evaluation", "criteria, graders, cases, controls, trajectory/outcome separation, calibration, and regression review"),
    "evaluator-critic": ("actionable critique independent of generation", "criteria, evidence, severity, user cost, hard gates, repair priority, and re-review"),
    "evidence-ledger": ("traceable claims and source-backed decisions", "claim status, provenance, authority, freshness, counterevidence, confidence, and expiry"),
    "frontier-research": ("high-signal research at the edge of known capability", "question, source hierarchy, uncertainty, reproducibility, speculation boundaries, and next experiment"),
    "hosted-tool-bridge": ("safe remote tool access", "connector identity, permissions, data scope, latency, retries, redaction, approval, and failure containment"),
    "human-feedback": ("consent-aware learning from user reactions", "feedback type, scope, persistence consent, sensitivity, correction, lesson quality, and regression risk"),
    "human-satisfaction": ("measurable human value rather than empty delight", "goal progress, effort, trust, agency, clarity, recovery, emotional appropriateness, and blind review"),
    "incident-response": ("containment and recovery after harmful or suspicious behavior", "severity, evidence preservation, user control, credential safety, rollback, communication, and lessons"),
    "intelligence-infrastructure": ("governed evaluation, memory, and improvement of capabilities", "audit, records, paired tests, hard gates, promotion, provenance, and stopping rules"),
    "intent-preservation": ("keeping the user’s actual goal intact", "literal request, context, constraints, assumptions, tradeoffs, correction, and requirement coverage"),
    "interaction-design": ("predictable user interaction and feedback", "affordance, state transitions, focus, latency, errors, recovery, accessibility, and input method"),
    "lovability": ("honest warmth that improves collaboration", "specific appreciation, useful initiative, timing, disagreement, privacy, agency, and anti-manipulation"),
    "memory": ("relevant, scoped, controllable memory", "purpose, consent, sensitivity, scope, expiry, correction, deletion, provenance, and retrieval"),
    "model-routing": ("matching models to task and risk", "capability, privacy, cost, latency, reliability, fallback, evidence, and handoff control"),
    "multimodal-reasoning": ("grounded interpretation across modalities", "source fidelity, OCR/vision limits, cross-modal conflicts, uncertainty, privacy, and verification"),
    "online-orchestration": ("coordinating hosted workers and tools", "run identity, dependencies, budgets, queues, permissions, checkpoints, traces, and cancellation"),
    "optimal-assistance": ("choosing the most helpful intervention", "user goal, friction, timing, initiative, alternatives, effort, and agency"),
    "orchestration": ("composing multi-step agent workflows", "ordering, typed artifacts, isolation, parallelism, joins, retries, ownership, and proof"),
    "outcome-completion": ("closing work only when the outcome is evidenced", "acceptance, artifact state, quality, safety, recovery, human experience, and status vocabulary"),
    "planning": ("plans that make execution safer and clearer", "outcome, dependencies, unknowns, risk, budget, checkpoints, verification, and adaptive depth"),
    "product-completeness": ("complete interactive product slices", "journey, state, data, backend, persistence, access, errors, accessibility, operations, and acceptance"),
    "product-strategy": ("turning ideas into valuable product decisions", "user, problem, alternatives, scope, evidence, tradeoffs, risks, metrics, and learning"),
    "professional-taste": ("contextual professional UI quality", "hierarchy, proportion, density, controls, states, accessibility, responsiveness, and task evidence"),
    "progressive-delivery": ("shipping value in safe increments", "thin slice, feature flags, blast radius, rollback, observability, user communication, and staged expansion"),
    "quality-judgment": ("separating subjective quality dimensions", "criteria, evidence, context, independent critique, blockers, uncertainty, and repair"),
    "repair-loop": ("smallest-cause failure recovery", "reproduction, classification, patch scope, focused tests, regression tests, evidence, and escalation"),
    "requirement-compiler": ("compiling compressed briefs into traceable scope", "explicit items, inferences, unknowns, capability map, vertical slice, tests, and coverage"),
    "requirement-traceability": ("preserving requirements through implementation", "source phrase, priority, confidence, artifact, test, evidence, status, and deferred work"),
    "research": ("reliable, efficient evidence gathering", "question, source hierarchy, extraction, contradiction, freshness, citations, synthesis, and uncertainty"),
    "runtime-host": ("provider-neutral controlled execution", "trust, intent, approvals, budgets, tool boundaries, checkpoints, traces, completion evidence, and recovery"),
    "safety-governance": ("safe capability use under uncertainty", "risk classification, authority, privacy, misuse, mitigations, monitoring, escalation, and review"),
    "self-improvement": ("evidence-backed reversible capability improvement", "baseline, smallest change, paired tests, regressions, lesson, authorization, and rollback"),
    "skill-composition": ("composing Skills without hidden conflicts", "typed interfaces, ordering, dependencies, permissions, evidence flow, parallelism, and fallback"),
    "skill-forging": ("creating narrow Skills from evidenced gaps", "gap proof, existing alternatives, contract, examples, tests, provenance, versioning, and promotion"),
    "staged-execution": ("wave-based work with clear entry and exit gates", "brief, architecture, vertical slice, integration, dynamic verification, repair, and release"),
    "superlative-analysis": ("turning absolute claims into measurable comparisons", "objective, dimensions, baseline, evidence, confounders, uncertainty, and stop rule"),
    "task-framing": ("making a vague request executable", "goal, user, constraints, definition of done, unknowns, risks, approvals, and next step"),
    "tool-evaluation": ("deciding whether a tool earns adoption", "real tasks, discovery, permissions, validity, errors, latency, privacy, cost, and end-to-end value"),
    "tool-use": ("safe, efficient tool invocation", "inspect, choose, validate arguments, scope, preview, approval, execute, verify, and recover"),
    "ui-vision": ("turning visual intent into testable interface decisions", "hierarchy, tokens, density, states, responsive behavior, accessibility, originality, and live review"),
    "ultra-plan": ("high-rigor but proportional planning", "preflight, dependencies, context budget, risk, checkpoints, verification, stop rules, and one-shot path"),
}


def section(name: str) -> str:
    outcome, checks = FOCUS.get(name, ("reliable task-specific execution", "scope, workflow, evidence, failure handling, composition, and human value"))
    return f'''\n\n## Operational deepening\n\nUse this Skill to improve **{outcome}**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is {checks}.\n\n### Execute\n\n1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.\n2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.\n3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.\n4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.\n\n### Evidence and boundaries\n\nTreat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.\n\n### Decision examples\n\n| Kind | Pattern |\n|---|---|\n| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |\n| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |\n| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |\n| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |\n| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |\n\n### Composition and stopping rule\n\nDeclare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.\n'''


def main() -> None:
    changed = []
    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if "## Operational deepening" in text:
            continue
        name = path.parent.name
        path.write_text(text.rstrip() + section(name), encoding="utf-8")
        changed.append((name, len(path.read_text(encoding="utf-8").splitlines())))
    print(f"deepened {len(changed)} Skills")
    for name, lines in changed:
        print(f"{name}: {lines} lines")


if __name__ == "__main__":
    main()
