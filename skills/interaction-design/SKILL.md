---
name: interaction-design
description: Design clear, accessible, low-friction interaction flows for AI systems, tools, and interfaces. Use when the agent has a UI, conversational flow, approval step, or user-facing workflow.
---

# Interaction design

Every state should answer: where am I, what happened, what can I do, and what should I do next? Remove unnecessary steps, preserve input, use sensible defaults, and make progress and saved state visible.

Design empty, loading, success, error, retry, cancellation, approval, and rollback states. Make irreversible consequences explicit before commitment. Keep controls predictable; delight should be quiet and never hide important information. Support keyboard, screen reader, mobile, low-bandwidth, and interrupted-use scenarios where relevant.

Use the user's existing Joy patterns as inspiration for restrained hierarchy, search, responsive layout, and clean feedback—not as a reason to add decoration without value.

## Operational deepening

Use this Skill to improve **predictable user interaction and feedback**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is affordance, state transitions, focus, latency, errors, recovery, accessibility, and input method.

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
