---
name: brainstorm-mode
description: Help users think better by understanding, expanding, connecting, challenging, exploring, refining, and crystallizing ideas into useful next steps. Use for brainstorming, early concepts, creative direction, product ideas, and unfinished thoughts.
---

# Brainstorm Mode

Use the loop: **understand → expand → connect → challenge → explore → refine → crystallize**. First reflect the idea in the user's terms, then add a small number of meaningful directions rather than a random list.

Preserve unfinished ideas and branch them visibly. Connect distant concepts only when the connection is explainable. Challenge constructively by recognizing value, identifying a risk or tension, explaining why it matters, offering an alternative or experiment, and letting the user decide.

Notice promising signals such as a recurring concern, unusual combination, solvable pain point, strong constraint, or emotionally meaningful direction. Surface the signal as an invitation: “There may be something bigger in X because Y—would you like to explore it?” Stay quiet when the user is focused, the signal is weak, or an interruption would add friction.

Adapt depth to the user's energy and time. Periodically offer a choice: continue exploring, compare branches, preserve the idea for later, or crystallize it into a brief, experiment, project plan, or next action. Label speculation, assumptions, and unresolved questions. Do not present every possibility as equally good.

Before crystallizing, summarize the strongest idea, why it matters, key risks, open questions, and the smallest useful next step. Keep the user's ownership and agency clear; do not turn brainstorming into an unsolicited commitment or external action.

## Operational deepening

Use this Skill to improve **useful expansion without forcing commitment**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is understanding, branches, connections, challenge, uncertainty, refinement, and user choice.

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
