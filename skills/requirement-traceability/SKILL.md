---
name: requirement-traceability
description: Convert a natural-language brief into a durable trace from requirement to interpretation, artifact, test, evidence, and delivery status. Use for complex builds, multi-step research, product work, or any task where important details may be silently omitted.
---

# Requirement traceability

Create a ledger with one row per explicit requirement and one row per necessary inferred requirement. Record: ID, requirement, source phrase, priority, confidence, dependencies, risk, implementation artifact, verification method, evidence, status, and owner.

Use statuses `captured`, `clarifying`, `planned`, `implemented`, `verified`, `partial`, `deferred`, `blocked`, or `rejected_with_reason`. Preserve the distinction between the user's words and the agent's interpretation.

Build from the highest-value vertical slice first. At every checkpoint compare the current plan and artifact with the ledger. Before delivery, run a coverage pass, identify unimplemented or weakly verified items, and report them plainly. A requirement with no artifact or test is not complete; a test with no link to a user requirement is a candidate for unnecessary work.

Keep the ledger concise enough to maintain. Store detailed evidence in linked artifacts, traces, screenshots, logs, or test results rather than bloating the plan.

## Operational deepening

Use this Skill to improve **preserving requirements through implementation**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is source phrase, priority, confidence, artifact, test, evidence, status, and deferred work.

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
