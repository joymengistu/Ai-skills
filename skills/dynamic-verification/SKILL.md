---
name: dynamic-verification
description: Verify interactive software and agent outputs by executing the real artifact, exercising primary and failure flows, inspecting observable behavior, and comparing results against requirements. Use when static code inspection or a screenshot cannot prove the requested outcome.
---

# Dynamic verification

Verify the thing the user will actually use. Start from the requirement ledger and define observable checks for each must-have outcome.

For software, build or launch the artifact, inspect runtime errors, exercise the primary journey, test invalid input, empty and loading states, refresh or restart, permissions, responsive layout, accessibility path, and recovery from tool or network failure. For games, test controls, playability, progression, feedback, pause, restart, and win/lose behavior. For documents or media, inspect rendered pages, legibility, structure, and source fidelity. Treat build health, visual usability, intent alignment, and operational readiness as separate gates; passing one does not imply passing the others.

Record evidence such as URLs, screenshots, logs, traces, outputs, timestamps, and test steps. Include the exact requirement or acceptance criterion each observation supports. A project that compiles but does not respond correctly is not verified. A beautiful screen that omits the requested workflow is not complete. Do not claim an end-to-end test unless the full path was actually exercised.

When execution is unavailable, say what was inspected and what remains unverified. Never convert static plausibility into a claim of dynamic success.

## Operational deepening

Use this Skill to improve **testing the real artifact rather than static plausibility**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is primary journeys, invalid/empty/loading states, responsive behavior, permissions, recovery, and evidence.

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
