---
name: online-orchestration
description: Coordinate hosted models, specialist agents, remote workers, browser sessions, and long-running queues into one observable, resumable online run. Use when work exceeds a single local turn or benefits from hosted parallel execution.
---

# Online orchestration

Create one session identity, one versioned requirement ledger, and one source of truth for the run. Break work into bounded stages: compile, architect, build slice, expand, verify, repair, release.

Use hosted workers for independent research, asset preparation, isolated modules, tests, or visual checks. Keep shared-file integration centralized. Every handoff includes objective, inputs, exclusions, output schema, evidence, failures, and next decision.

Persist checkpoints, approvals, budgets, tool intents, results, and trace events. Expose meaningful progress to the user and support cancellation, pause, timeout, and resume. Do not lose the requirement ledger when changing models or workers.

Route to a stronger model or specialist only when task difficulty, risk, ambiguity, or verification evidence justifies it. Keep provider fallback and model switching inside the same permission and safety boundary.

## Operational deepening

Use this Skill to improve **coordinating hosted workers and tools**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is run identity, dependencies, budgets, queues, permissions, checkpoints, traces, and cancellation.

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
