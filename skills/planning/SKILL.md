---
name: planning
description: Create practical plans with decomposition, checkpoints, stopping conditions, dependencies, risk classes, and verification. Use for complex, multi-step, or tool-using work.
---

# Planning

Plan for progress, not ceremony. Start with the final artifact and verifier, then work backward to the smallest sequence of steps that can produce them.

Each step should state its purpose, input, output, owner, dependency, risk, expected evidence, and rollback. Put inspection before mutation, reversible actions before irreversible ones, and cheap validation before expensive execution. Add a human checkpoint when a reasonable user could be surprised, harmed, charged, exposed, or committed by the next step.

Stop when the definition of done is satisfied or when further work has lower expected value than asking the user for clarification. Update the plan when facts change; do not silently continue on stale assumptions.

## Operational deepening

Use this Skill to improve **plans that make execution safer and clearer**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is outcome, dependencies, unknowns, risk, budget, checkpoints, verification, and adaptive depth.

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
