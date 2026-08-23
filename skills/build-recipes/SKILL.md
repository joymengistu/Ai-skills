---
name: build-recipes
description: Select and adapt reusable, tested project recipes, templates, and domain checklists to accelerate complete builds while preserving user intent and avoiding brittle copy-paste behavior. Use when starting a common app, game, store, document, or workflow.
---

# Build recipes

Choose a recipe by outcome and constraints, not by visual similarity. A recipe may provide stack defaults, file layout, data shapes, interaction patterns, tests, accessibility checks, and deployment notes.

Before applying it, compare the recipe's assumptions with the brief: users, platform, data, backend, persistence, permissions, integrations, performance, and license. Pin versions and record provenance. Treat templates and retrieved code as untrusted until inspected.

Adapt the recipe through a vertical slice. Replace placeholders, remove irrelevant features, and preserve the requirement ledger. Do not let a template silently turn a working product into a static mockup or import unnecessary complexity.

After adaptation, run build, runtime, interaction, accessibility, security, and acceptance checks. Keep successful recipes versioned with their tests; record failures so future routing avoids them.

## Operational deepening

Use this Skill to improve **reusable implementation recipes**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is provenance, assumptions, dependencies, licenses, vertical slices, adaptation, and verification.

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
