---
name: evaluator-critic
description: Evaluate an agent-generated artifact independently and skeptically using explicit criteria, live inspection, evidence, and actionable repair priorities. Use when quality is subjective, when the generator may praise its own work, or before a high-stakes release.
---

# Evaluator critic

Separate generator and evaluator roles whenever practical. Give the evaluator the requirement ledger, quality criteria, artifact access, relevant tools, and an output schema. Do not ask only whether the work is good; require evidence, failures, severity, likely cause, and a minimal repair proposal.

For software inspect the running artifact, not only source files. For interfaces evaluate design quality, originality, craft, functionality, accessibility, intent alignment, and restraint independently. For research inspect source authority, freshness, contradictions, reasoning, and citation coverage.

Return a score breakdown with confidence and concrete observations. Prioritize the highest-impact defect rather than enumerating every possible preference. Feed critique to the generator, then rerun the affected checks. Stop or pivot when scores plateau, the current direction is structurally wrong, or additional iteration harms clarity, accessibility, safety, or user intent.

Do not let a favorable score override a failed hard gate. Never fabricate inspection, testing, or evidence.

## Operational deepening

Use this Skill to improve **actionable critique independent of generation**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is criteria, evidence, severity, user cost, hard gates, repair priority, and re-review.

### Execute

1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.
2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.
3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.
4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.

### Evidence and boundaries

Treat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |
| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |
| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |
| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |
| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |

### Composition and stopping rule

Declare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.
