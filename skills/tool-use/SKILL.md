---
name: tool-use
description: Select, call, validate, and document tools safely and efficiently with clear schemas, permissions, error handling, and evidence. Use whenever an agent can inspect or change an environment.
---

# Tool use

Use the smallest tool that can answer the current question. Tools should have one clear purpose, descriptive parameters, predictable output, explicit error states, and minimal overlap. Namespace tools by domain and return token-efficient results with identifiers, timestamps, and provenance.

Before a call, use `references/tool-action-boundary-contract.md` to record intent, target, scope, risk, reversibility, permission, expected evidence, destination, idempotency, and rollback. After a call, validate the actual result against the plan and handle partial failure. Never infer that a tool succeeded because the call returned without an exception.

Separate read, propose, approve, execute, verify, and report operations. Apply least privilege, path and domain allowlists, rate limits, timeouts, dry-run mode, idempotency, and audit logging. Fail closed on missing approval, ambiguous identity or destination, invalid arguments, unknown risk, or uncertain non-idempotent outcome. For shell or file actions, show the exact scope and preserve a rollback path.

## Operational deepening

Use this Skill to improve **safe, efficient tool invocation**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is inspect, choose, validate arguments, scope, preview, approval, execute, verify, and recover.

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
