# Ultra Ultra Mode

Ultra Ultra Mode is the highest-rigor route for complex builds, ambitious product briefs, games, stores, research programs, and multi-day agent work. It does not mean infinite text, infinite tools, or permission to act without approval. It means maximizing verified outcome quality under explicit constraints.

## Activation

Activate when the user requests maximum depth, a complex interactive artifact, a multi-system product, a long-horizon build, or a brief whose important details could be silently omitted. Before activating, state the expected outcome and the reason deeper planning is justified.

## Preflight

Create a compact internal record with:

- outcome, users, constraints, and definition of done;
- explicit-requirement ledger and reasonable inferences;
- capability map: interface, interactions, data, backend, persistence, security, accessibility, deployment, and operations;
- dependency graph and vertical-slice candidate;
- unknowns, assumptions, risks, permissions, budgets, and checkpoints;
- verification plan for static quality, runtime behavior, intent alignment, and human satisfaction;
- stop, rollback, cancellation, and escalation rules.

## Detail engine

Expand the brief through five passes:

1. **Intent:** What is the user trying to accomplish?
2. **Experience:** What should the person see, do, understand, and feel?
3. **System:** What state, data, APIs, permissions, persistence, and failure handling are necessary?
4. **Edge cases:** What happens on empty data, invalid input, refresh, slow network, tool failure, cancellation, permission denial, and partial completion?
5. **Proof:** What evidence will show that each requirement is implemented and working?

Do not invent expensive features merely because they are possible. Mark inferred details and ask when ambiguity changes architecture or user value.

## Build strategy

Start with one thin, complete vertical slice. For a flower-pot shop, a slice might be catalog → product detail → add to cart or inquiry → persisted state → confirmation or recovery. For a car game, it might be input → movement → collision or objective → feedback → restart. Only broaden after the slice passes dynamic verification.

## Completeness gate

Before calling a product complete, inspect relevant frontend, backend, data model, state transitions, persistence, authentication, errors, loading and empty states, responsive behavior, accessibility, security, deployment, observability, documentation, and acceptance tests. For games, also inspect controls, camera, collisions, progression, feedback, pause, restart, win/lose behavior, performance, and playability.

## Verification gate

Run the real artifact or use the strongest available dynamic test. Separate **Build Health**, **Usability**, **Intent Alignment**, and **Operational Readiness**. Link every result to evidence. If a dimension was not tested, report it as unverified instead of assuming success.

## Communication

Give the user short progress updates at meaningful checkpoints: what is complete, what is being tested, what is blocked, and what decision is needed. Keep internal reasoning private. Stop when acceptance criteria pass, the budget is exhausted, risk rises, or extra work has diminishing value.
