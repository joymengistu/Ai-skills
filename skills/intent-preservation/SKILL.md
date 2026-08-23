---
name: intent-preservation
description: Preserve a user's explicit requirements, implied outcome, constraints, priorities, and important details from request through implementation and delivery. Use when a vague request could be simplified into a shallow result or when many requirements must survive a long build.
---

# Intent preservation

Translate the request into a requirement ledger before building. For every item record its source, interpretation, priority, confidence, implementation location, verification method, status, and unresolved ambiguity. When interpretation is ambiguous, use `references/intent-resolution-contract.md` to separate candidate intents, evidence, reversibility, impact if wrong, clarification, and correction scope.

Separate explicit requirements from reasonable inferences and optional ideas. Expand details that are necessary for the intended outcome, but label invented assumptions. Ask before an ambiguity changes architecture, cost, privacy, safety, external effects, or the user's likely experience. Otherwise choose a reversible, low-risk default and record it.

Before delivery, walk the ledger against the running artifact or final answer. Detect silent omission, accidental simplification, scope drift, and details that were discussed but never implemented. Report completed, partial, deferred, blocked, and rejected requirements separately. If the user corrects an interpretation, prefer the correction and update only the relevant conversation or task scope.

Do not equate visual polish with intent alignment. A storefront may need data, state, cart or inquiry behavior, errors, persistence, and responsive flows; a game may need controls, feedback, progression, restart, and playability. Infer only what is justified by the user's outcome and verify it explicitly.

## Operational deepening

Use this Skill to improve **keeping the user’s actual goal intact**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is literal request, context, constraints, assumptions, tradeoffs, correction, and requirement coverage.

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
