---
name: cost-aware-execution
description: Optimize hosted-agent work for quality per unit of cost, latency, privacy exposure, and human effort using staged routing, caching, compact context, budgets, fallbacks, and verification. Use whenever online model or tool usage has a practical resource constraint.
---

# Cost-aware execution

Define a quality floor, time budget, data sensitivity, and usage budget before selecting a route. Optimize the full value equation: verified outcome quality minus model cost, tool cost, latency, privacy exposure, failure recovery, and user effort.

Use the cheapest route that can pass the current stage: small or fast models for classification, extraction, formatting, and routine edits; stronger models for architecture, ambiguity, difficult debugging, multimodal inspection, and final review. Do not route high-risk work to a weak model merely to save cost.

Reduce waste with compact context, progressive disclosure, caching of verified stable facts, reusable recipes, focused tests, and targeted repair. Record model, tool, token, time, retry, and failure information for evaluation. Stop when acceptance criteria pass or extra work has diminishing value.

Respect provider, privacy, and approval boundaries. A fallback may reduce speed or scope, but it must not silently weaken safety, truthfulness, permissions, or verification.

## Operational deepening

Use this Skill to improve **maximizing value under time, token, tool, and money budgets**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is expected value, escalation, caching, stopping, user effort, and cost evidence.

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
