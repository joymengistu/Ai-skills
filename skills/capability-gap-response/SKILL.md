---
name: capability-gap-response
description: Detect and respond to an evidenced capability gap by searching existing skills, researching reliable knowledge, designing a narrow candidate skill, testing it in isolation, and proposing controlled promotion. Use after repeated failures, unmet requirements, or a missing procedural capability.
---

# Capability-gap response

Open a gap record only from observable evidence: a repeated failure, unmet requirement, user correction, missing tool, or systematic evaluation deficit. Describe the affected outcome, task distribution, failure signature, severity, and plausible causes.

Search the existing skill catalog and authoritative external knowledge before creating anything. Decide whether the gap needs a skill, a tool, a model route, better context, a runtime control, or a changed requirement. Do not create a skill to compensate for a host permission or safety defect.

For a candidate skill define narrow purpose, trigger, inputs, outputs, dependencies, exclusions, permissions, provenance, verification, evaluation cases, expected improvement, cost, and rollback. Test it in an isolated sandbox against the current baseline, representative cases, ambiguous and adversarial cases, partial failures, and held-out regressions.

Keep candidates experimental until an authorized maintainer reviews evidence. Promote only when improvement clears the quality threshold without critical safety, privacy, human-control, recoverability, or accessibility regression. Register version and provenance; preserve rollback and retirement paths. A generated skill may propose its own improvement, but it cannot grant itself trust, permissions, or production status.

## Operational deepening

Use this Skill to improve **responding to repeated failures without unsafe self-expansion**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is failure evidence, existing alternatives, narrow candidate scope, tests, rollback, and authorization.

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
