---
name: progressive-delivery
description: Deliver a fast first usable result while continuing staged implementation, verification, and repair through resumable online work. Use when users value an aha moment quickly but the complete outcome requires more time.
---

# Progressive delivery

Separate **time to first usable result** from **time to verified complete result**. Deliver a coherent first slice that is honestly labeled as prototype, preview, partial, or complete.

Make the first slice vertical and valuable: it should demonstrate the core user journey, not merely a static screen. Preserve the full requirement ledger while showing what is intentionally deferred.

Continue refinement through bounded stages. Prioritize missing core behavior, broken interactions, data and persistence, errors, accessibility, security, and user-visible polish before low-value extras. Emit meaningful progress and allow pause, cancel, approval, and resume.

Never use a preview to imply production readiness. At each handoff, state what works, what is being tested, what remains unverified, and the next highest-value improvement.

## Operational deepening

Use this Skill to improve **shipping value in safe increments**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is thin slice, feature flags, blast radius, rollback, observability, user communication, and staged expansion.

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
