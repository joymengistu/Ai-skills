---
name: quality-judgment
description: Evaluate qualitative excellence such as taste, clarity, coherence, restraint, originality, hierarchy, usefulness, and appropriateness without reducing quality to an arbitrary universal score. Use for design, writing, research synthesis, product experience, and other subjective outputs.
---

# Quality judgment

Start with the user's purpose, audience, context, and quality bar. Convert vague adjectives into observable criteria. Choose only dimensions that matter: clarity, coherence, hierarchy, usefulness, appropriateness, restraint, originality, consistency, memorability, or elegance.

Use references as decomposed principles, not templates to copy. Compare alternatives against the same criteria and record concrete observations, tradeoffs, uncertainty, and evidence. Distinguish technical correctness, professionalism, beauty, minimalism, and polish; passing one does not imply the others.

Use deterministic checks for measurable properties, a separate critic for structured qualitative review, and human review for preference, cultural context, emotional response, and surprising outcomes. Avoid a single magic score. If scoring is useful, retain the dimension breakdown, confidence, examples, and hard gates.

Prioritize changes that improve the user's real outcome. Remove decorative complexity, generic patterns, and impressive-looking features that do not serve understanding, navigation, action, emotion, or trust. Re-evaluate after revision and stop when improvement plateaus or begins to harm accessibility, clarity, or intent.

## Operational deepening

Use this Skill to improve **separating subjective quality dimensions**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is criteria, evidence, context, independent critique, blockers, uncertainty, and repair.

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
