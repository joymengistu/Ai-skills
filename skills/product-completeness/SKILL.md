---
name: product-completeness
description: Turn a product idea into a complete, testable experience across interface, behavior, data, backend, persistence, errors, accessibility, security, deployment, and documentation. Use when building apps, games, stores, tools, or other interactive software from a short brief.
---

# Product completeness

Use `references/product-completeness-journey-contract.md`. Do not treat a page or screenshot as the product. Compile a product brief into a capability map and a vertical slice that proves the core outcome end to end.

## Completeness map

Check the appropriate dimensions: user roles and goals; screens and navigation; core interactions; data model and source of truth; state management; backend/API; persistence; authentication and authorization; loading, empty, error, and offline states; validation; responsive behavior; accessibility; security and privacy; observability; deployment; seed/demo data; documentation; and acceptance tests.

For a game also check input mapping, game loop, camera, collision, progression, feedback, audio, pause, restart, win/lose states, performance, and dynamic playability. For a shop also check product discovery, detail, availability, cart or inquiry flow, totals, validation, persistence, confirmation, and recovery. Adapt the map to the user's actual goal; do not invent expensive features merely to make a checklist longer.

## Vertical slice

Build and verify one thin end-to-end path before broadening. Keep a requirement-to-artifact ledger. Use the running system, not source code alone, as evidence. Exercise the primary flow, invalid input, empty data, network/tool failure, permission denial, refresh/restart, keyboard or assistive path, and cancellation or recovery. Keep visual, functional, data/persistence, accessibility, security, resilience, and operational evidence separate.

If the brief is only a visual mockup, label it honestly as a mockup and do not claim that backend or interactivity exists. If the user intended a working product, pause or continue the architecture until the missing behavior is addressed. A compile, screenshot, seed data, successful API response, or one happy path cannot override a failed must-have journey or hard gate.

When a reference screenshot is supplied for a working interface, add screenshot fidelity to the completeness map without confusing it with functional completeness. Route visual implementation through `skills/screenshot-reconstruction/SKILL.md`; record viewport, regions, geometry, spacing, typography, assets, visible states, and responsive evidence. Require same-viewport render/compare/repair evidence for visual claims, while separately testing interaction, accessibility, data, persistence, and recovery.

## Operational deepening

Use this Skill to improve **complete interactive product slices**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is journey, state, data, backend, persistence, access, errors, accessibility, operations, and acceptance.

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
