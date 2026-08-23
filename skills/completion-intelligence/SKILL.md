---
name: completion-intelligence
description: Decide whether a task is genuinely complete rather than merely producing an output, using requirements, tests, runtime behavior, edge cases, quality, safety, and user-goal evidence. Use before declaring any complex task done.
---

# Completion intelligence

Distinguish `output_generated` from `task_complete`. Generated output means files, text, or a demo exist. Completion means the result satisfies the requirement ledger and user goal, passes relevant tests, works through the real journey, handles important states and failures, meets safety and accessibility gates, and is ready for the stated context.

Before closing, inspect explicit requirements, justified inferences, acceptance criteria, dependencies, known edge cases, and deferred work. Verify the running artifact when possible. Record evidence for each material claim and label items as verified, partially verified, unverified, deferred, blocked, or rejected with reason.

Do not mark a feature complete because it compiles, renders, looks impressive, or passed one happy path. Check integration, persistence, errors, loading, empty states, permissions, recovery, responsive behavior, and operational readiness when relevant.

Close with a concise completion report: what works, evidence, what remains, risks, and the next useful action. If the work is not complete, say so and propose the smallest path to completion.

## Operational deepening

Use this Skill to improve **distinguishing generated output from complete outcome**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is requirements, evidence, runtime behavior, edge states, safety, human experience, and status.

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
