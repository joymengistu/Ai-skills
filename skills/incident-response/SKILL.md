---
name: incident-response
description: Detect, contain, communicate, recover from, and learn from AI-agent failures, unsafe actions, data exposure, incorrect outputs, or policy violations. Use when an agent run causes or may have caused harm or a material reliability incident.
---

# Incident response

Prioritize people, containment, evidence preservation, and honest communication. Stop or isolate the affected run, revoke or narrow permissions if needed, and prevent retries from amplifying the issue.

Classify the incident: safety, privacy, security, integrity, availability, financial, external communication, or user trust. Record timeline, run and action IDs, scope, affected assets and people, observed facts, uncertainty, containment, approvals, and external outcomes. Do not alter or delete evidence to make the trace look clean.

Notify the appropriate human owner with what happened, what is contained, what may still be affected, and the next decision needed. Use rollback, cancellation, credential rotation, data deletion, correction, or user notification as appropriate and authorized. Verify recovery independently.

After stabilization, perform blameless root-cause analysis, identify whether the failure was framing, context, tool, permission, model, memory, runtime, verification, or communication, add a regression case, and make the smallest safe change. Do not silently convert an incident into a “learning” that weakens controls.

## Operational deepening

Use this Skill to improve **containment and recovery after harmful or suspicious behavior**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is severity, evidence preservation, user control, credential safety, rollback, communication, and lessons.

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
