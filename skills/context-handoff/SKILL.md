---
name: context-handoff
description: Preserve the state needed for a fresh agent or context window to continue long-running work without guessing, repeating, or declaring completion early. Use across sessions, model switches, worker handoffs, resets, and compaction.
---

# Context handoff

At the end of each stage, write a compact handoff containing the objective, current status, requirement ledger, decisions, assumptions, artifacts, tests, evidence, failures, unresolved questions, next step, and stop conditions. Keep it in durable storage outside the model context window and outside a disposable worker.

Prefer a clean context reset with a high-signal handoff when the current context is bloated, confused, or showing premature wrap-up. Use compaction only when its transformations are recoverable and preserve the material state. Retrieve context by need rather than dumping the entire history.

Use source control, checkpoints, progress files, and artifact indexes to make work reversible. The next worker must inspect the handoff and current artifact, then verify reality before editing. Never treat a memory note as authorization, a plan as proof of completion, or a prior worker's claim as evidence without checking.

Keep handoffs concise enough to load reliably, but complete enough to prevent loss of goals, constraints, and test status.

## Operational deepening

Use this Skill to improve **resumable work across workers or context resets**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is objective, requirements, decisions, artifacts, evidence, failures, tests, unknowns, and next action.

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
