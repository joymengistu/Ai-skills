---
name: requirement-compiler
description: Compile a short natural-language idea into explicit requirements, justified inferences, unknowns, architecture implications, acceptance criteria, and a traceable implementation plan. Use before building a complex app, game, store, workflow, or research artifact.
---

# Requirement compiler

Treat the brief as a compressed product specification. Extract the desired user outcome, actors, core journey, explicit features, quality expectations, constraints, integrations, and definition of done.

Separate each item into `explicit`, `necessary_inference`, `optional_idea`, or `unknown`. For every item record priority, confidence, dependencies, risk, artifact, test, and status. Ask before an unknown changes architecture, cost, safety, privacy, or the user's intended experience.

Compile a capability map covering interface, interactions, state, data, backend/API, persistence, identity and permissions, loading/empty/error states, accessibility, security, performance, deployment, observability, documentation, and acceptance tests. Adapt the map to the domain; do not force irrelevant features.

Choose a thin vertical slice that proves the main outcome end to end. Only after it works should the plan expand into independent feature waves. Maintain requirement conservation: no explicit requirement may disappear without implementation, deferral, rejection with reason, or a visible limitation.
