---
name: human-feedback
description: Collect, interpret, and apply user corrections, preferences, and satisfaction feedback without overfitting, manipulation, or unwanted profiling. Use when improving an AI agent from real interactions or when a user reports that an outcome was wrong or hard to use.
---

# Human feedback

Treat feedback as evidence about a specific interaction, not automatic permission to rewrite the agent. First classify whether the issue was outcome quality, factuality, clarity, effort, trust, control, progress, personalization, completion, or safety.

Ask what the user wants changed now and whether the preference should persist. Separate one-off correction, project-scoped preference, and durable preference. Store only what is useful, consented, scoped, inspectable, and deletable. Do not infer sensitive traits or emotional profiles from a single interaction.

Record the feedback, affected behavior, hypothesis, proposed change, expected benefit, possible regressions, evaluation cases, and rollback. Test the change on representative and held-out cases. Never optimize for positive ratings by hiding uncertainty, reducing user control, or making the agent emotionally dependent.

At delivery, confirm what changed and how the user can correct or forget it. Treat explicit dissatisfaction as a valuable signal, not a failure to conceal.

## Operational deepening

Use this Skill to improve **consent-aware learning from user reactions**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is feedback type, scope, persistence consent, sensitivity, correction, lesson quality, and regression risk.

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
