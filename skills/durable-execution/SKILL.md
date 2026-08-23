---
name: durable-execution
description: Design and operate long-running AI tasks that survive crashes, delays, approvals, retries, and process restarts without losing state or repeating risky side effects. Use for asynchronous agents, scheduled work, multi-day tasks, or any workflow with external actions.
---

# Durable execution

Treat a long-running agent as a durable record, not a fragile conversation. Persist state at logical boundaries and make the run resumable.

## Required contract

Record the run ID, versioned plan, current state, completed work, pending work, approvals, evidence, tool intents, tool results, budgets, and integrity marker. Emit structured events using `runtime/trace-schema.json` and project visible progress through `runtime/progress-state-machine.md`.

Before a side effect, persist intent with a unique idempotency key. After execution, persist the external result and verification. On retry or restart, reconcile the key and known external state before attempting the action again. Do not assume a failed request had no effect.

Persist approval requests and decisions. A waiting run should consume no unnecessary model or tool work; use durable timers or signals where the host runtime supports them. If approval times out, the reviewer is unavailable, or state integrity is uncertain, fail closed and preserve the checkpoint.

## Recovery test

Simulate process crash before execution, during execution, after execution but before recording the result, while waiting for approval, and during verification. Confirm that recovery neither loses user work nor duplicates a side effect. Report unresolved ambiguity instead of fabricating a result.

This skill specifies behavior; the host runtime must provide durable storage, atomicity, access control, timers, and external reconciliation.

## Operational deepening

Use this Skill to improve **safe progress across interruptions and uncertain side effects**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is idempotency, checkpoints, reconciliation, retries, cancellation, and recovery evidence.

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
