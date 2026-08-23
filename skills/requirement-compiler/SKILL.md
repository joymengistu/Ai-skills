---
name: requirement-compiler
description: Compile a short natural-language idea into explicit requirements, justified inferences, unknowns, architecture implications, acceptance criteria, and a traceable implementation plan. Use before building a complex app, game, store, workflow, or research artifact.
---

# Requirement compiler

Treat the brief as a compressed product specification. Extract the desired user outcome, actors, core journey, explicit features, quality expectations, constraints, integrations, and definition of done.

Separate each item into `explicit`, `necessary_inference`, `optional_idea`, or `unknown`. For every item record priority, confidence, dependencies, risk, artifact, test, and status. Ask before an unknown changes architecture, cost, safety, privacy, or the user's intended experience.

Compile a capability map covering interface, interactions, state, data, backend/API, persistence, identity and permissions, loading/empty/error states, accessibility, security, performance, deployment, observability, documentation, and acceptance tests. Adapt the map to the domain; do not force irrelevant features.

Choose a thin vertical slice that proves the main outcome end to end. Only after it works should the plan expand into independent feature waves. Maintain requirement conservation: no explicit requirement may disappear without implementation, deferral, rejection with reason, or a visible limitation.

## Screenshot-precision compilation

When a screenshot is supplied for HTML/CSS/JavaScript reconstruction, add a visual-evidence track to the requirement ledger. Record viewport dimensions, page regions, geometry relationships, spacing, typography metrics, colors/surfaces, asset provenance, visible controls and states, responsive evidence, and confidence for each inference. Mark screenshot facts as `observed`, behavior inferred from multiple references as `inferred`, missing assets/fonts as `approximated`, rendered comparisons as `verified`, and hidden behavior as `not assessable from screenshot`. Route execution to `skills/screenshot-reconstruction/SKILL.md`; do not let generic design adjectives override the reference.

## Operational deepening

Use this Skill to improve **compiling compressed briefs into traceable scope**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is explicit items, inferences, unknowns, capability map, vertical slice, tests, and coverage.

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
