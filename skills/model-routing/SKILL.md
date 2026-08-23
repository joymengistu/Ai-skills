---
name: model-routing
description: Select, combine, and fall back between models according to task capability, effort, latency, cost, privacy, reliability, and risk rather than brand or size. Use when an agent has multiple models or providers available.
---

# Model routing

Choose a model as part of a measurable system, not as a universal winner. Define the task, required capabilities, risk, context size, latency budget, cost ceiling, privacy requirements, and acceptable fallback.

Route routine work to the smallest model that meets the quality bar. Use a stronger strategic advisor for intent compilation, architecture, difficult ambiguity, novel planning, complex debugging, multimodal judgment, and final synthesis. Use cheaper workers for bounded extraction, formatting, routine edits, independent research, test execution, and evidence collection when their contracts are clear. Route complex reasoning, multimodal, long-horizon, or high-consequence work to a stronger model only when the expected gain justifies cost and delay. Use staged routing: classify, select, execute, verify, and escalate when evidence is insufficient.

Keep fallback behavior explicit. A refusal, timeout, tool error, or low-confidence result is not the same as model failure. Preserve context, requirement ledger, evidence, and approvals across a fallback, record the reason, and do not route around safety controls. Require a stronger reviewer or independent evaluator when a cheaper worker's evidence is incomplete. Compare model routes on held-out tasks, requirement coverage, dynamic quality, recovery, latency, tokens, cost, privacy exposure, and user effort.

## Operational deepening

Use this Skill to improve **matching models to task and risk**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is capability, privacy, cost, latency, reliability, fallback, evidence, and handoff control.

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
