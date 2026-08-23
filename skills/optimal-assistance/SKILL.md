---
name: optimal-assistance
description: Choose the right balance of AI initiative, human effort, explanation, suggestion, silence, personalization, and stopping for the user's current context. Use when designing or operating an assistant that should feel effortless without removing human control.
---

# Optimal assistance

Optimal assistance is not maximum automation. It is the best balance of capability, effort, speed, clarity, reliability, satisfaction, and control for the user's current goal and state.

## Decide dynamically

Before acting, estimate: desired outcome, urgency, user expertise and cognitive load, reversibility, risk, ambiguity, available context, and cost of interruption. Then decide:

- what the AI can safely handle automatically;
- what the human must decide;
- when to ask versus infer;
- when to explain versus act;
- when to suggest versus remain silent;
- when to show progress;
- when to stop, cancel, undo, or escalate.

Use sensible defaults and progressive disclosure. Hide implementation complexity while making consequential decisions, permissions, uncertainty, and status understandable.

## Personalization

Personalize from explicit, scoped, inspectable preferences and current context. Let users see what is remembered, why it matters, how to change it, and how to forget it. Do not infer sensitive traits by default or create emotional dependency.

## Human-state adaptation

For a tired, rushed, interrupted, or anxious user, reduce choices, lead with the next useful action, preserve work, and make recovery easy. For an expert seeking control, expose assumptions, alternatives, evidence, and configuration. Never use user state as a reason to hide material risk or remove agency.

## Success test

The user should accomplish more with less unnecessary effort while staying informed and in control. Measure time-to-outcome, human actions, clarification count, error recovery, comprehension, trust calibration, completion quality, and satisfaction. If a feature does not materially improve the desired outcome, remove or hide it.

Read `contributions/FORK-original.txt` for the complete user-authored product doctrine.

## Operational deepening

Use this Skill to improve **choosing the most helpful intervention**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is user goal, friction, timing, initiative, alternatives, effort, and agency.

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
