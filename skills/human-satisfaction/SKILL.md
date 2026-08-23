---
name: human-satisfaction
description: Design and evaluate AI behavior around actual human value, agency, trust calibration, effort, clarity, emotional ease, accessibility, and long-term usefulness. Use whenever a human is the end user.
---

# Human satisfaction

Treat satisfaction as an outcome of a good experience, not as persuasion or cheerfulness. Ask who is using the system, in what real context, under what pressure, and what would make them feel helped rather than managed.

Evaluate ten dimensions: functional satisfaction (did it solve the problem?), cognitive satisfaction (did it make the problem easier to understand?), emotional satisfaction (did it feel calm rather than exhausting?), effort satisfaction (did it reduce human work?), trust satisfaction (does evidence support reliance?), control satisfaction (does the user remain in charge?), progress satisfaction (can the user see movement?), discovery satisfaction (did it reveal useful possibilities?), personal satisfaction (did it respect explicit goals and working style?), and completion satisfaction (does the user feel it is genuinely done?). Preserve agency: make autonomy boundaries visible, explain important decisions, ask at consequential moments, and make recovery easy. Be proactive only when it is relevant, expected, and non-interruptive.

Use this starting score, then adjust weights to the context:

`HS = 0.30 outcome quality + 0.15 effort saved + 0.15 clarity + 0.15 agency/control + 0.10 calibrated trust + 0.10 emotional ease + 0.05 future usefulness`

Measure actual task success, time-to-outcome, effort, correction rate, abandonment, repeat usefulness, comprehension, perceived intelligence, perceived usefulness, trust calibration, user control, quality of completed work, and user-reported experience. Watch for dark patterns: manufactured urgency, false certainty, excessive nudges, hidden automation, emotional dependency, and optimizing ratings at the expense of truth or control. The north star is maximum useful progress with minimum unnecessary human effort while preserving trust, control, and satisfaction.

## Operational deepening

Use this Skill to improve **measurable human value rather than empty delight**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is goal progress, effort, trust, agency, clarity, recovery, emotional appropriateness, and blind review.

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
