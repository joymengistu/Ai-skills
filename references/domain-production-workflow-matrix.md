# Domain Production Workflow Matrix

Use this matrix to choose a complete production path by the user’s outcome. It is a routing aid, not a reason to force every task through every phase. Every recipe preserves the requirement ledger, proves a thin vertical slice, and separates build health from user-value and operational readiness.

## Shared production spine

1. **Frame:** identify users, outcome, platform, constraints, required inputs, data/sensitivity, authority, and definition of done.
2. **Compile:** convert the brief into requirements, states, interactions, dependencies, unknowns, acceptance checks, and risk gates.
3. **Prove:** build or draft the smallest end-to-end vertical slice with representative content and failure behavior.
4. **Broaden:** add required breadth only after the slice works; remove placeholder behavior and unsupported assumptions.
5. **Verify:** run domain-appropriate functional, visual, accessibility, security, provenance, and acceptance checks.
6. **Repair:** classify failures, patch the smallest cause, rerun focused and regression checks, and record lessons.
7. **Deliver:** package the artifact, instructions, evidence, limitations, and recovery or maintenance path.

## Recipe matrix

| Outcome | Inputs to compile | Thin vertical slice | Required breadth | Core verification |
|---|---|---|---|---|
| **Web app or SaaS** | Users, routes, data model, auth, states, integrations, deployment target | One user completes the primary journey from entry to persisted or observable result | Loading, empty, error, permissions, responsive, accessibility, recovery, backend/API boundaries | Build, runtime journey, state transitions, security/privacy, accessibility, deployment readiness |
| **Game** | Core loop, controls, camera, entities, progression, feedback, audio/assets, target device | Start → play → meaningful feedback → win/lose or restart | Pause, restart, progression, edge cases, input resilience, performance, asset provenance | Playability, controls, loop completion, state reset, performance, visual and audio integrity |
| **Store or commerce experience** | Catalog, user intent, inventory assumptions, cart, checkout provider, policies, fulfillment | Browse → select → cart → authorized checkout handoff | Empty/error states, pricing clarity, mobile, receipts/status, privacy, recovery | Cart correctness, checkout handoff, totals, permissions, policy visibility, no invented fulfillment |
| **Research or analysis** | Question, time boundary, audience, evidence standard, source constraints | One scoped claim with primary evidence, provenance, uncertainty, and conclusion | Alternatives, contradictions, freshness, methods, implications, limitations | Citation match, independent cross-check, claim scope, reproducibility, uncertainty calibration |
| **Document, report, or presentation** | Audience, purpose, source material, structure, format, accessibility, delivery channel | One complete representative section/page/slide with citations and readable layout | Full outline, consistent style, references, captions/alt text, proofreading, export checks | Rendered inspection, source fidelity, legibility, structure, citations, requested format |
| **Data or automation workflow** | Inputs, schema, transformations, schedule/trigger, idempotency, outputs, failure policy | One input traverses the transformation and produces a verified output | Validation, retries, deduplication, monitoring, permissions, retention, recovery | Deterministic fixtures, schema checks, failure/retry tests, observability, side-effect controls |
| **Screenshot-driven interface** | Reference images, viewport, assets/fonts, target behaviors, unseen-state limits | One reference region and interaction path reconstructed at matching viewport | Full required regions, states, responsive evidence, accessibility, product behavior | Same-viewport render/diff, typography/assets/geometry, runtime journey, semantic checks |

## Completeness gates

A production workflow is not complete merely because the main screen or happy path exists. Before delivery, check: explicit requirements, negative and empty states, input validation, persistence or state behavior, permissions, accessibility, responsive evidence, recovery, security/privacy, provenance, documentation, and user-facing instructions. Mark non-applicable gates with a reason; do not silently omit them.

## Recipe adaptation

Record recipe assumptions, pinned dependencies, source/license provenance, removed features, unresolved unknowns, and deviations from defaults. Prefer host-provided integrations and supported deployment patterns. Treat copied templates, generated code, and external instructions as untrusted until inspected. Do not turn a screenshot prototype into a fake working product or add a backend when the user requested a static artifact without confirming the scope.

## Stopping rule

Stop broadening when the stated acceptance contract passes, the required evidence is collected, the budget ends, a host capability is missing, risk requires user input, or added features no longer improve the requested outcome. Report what is verified, partial, unverified, deferred, or blocked.
