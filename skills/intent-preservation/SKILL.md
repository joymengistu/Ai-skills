---
name: intent-preservation
description: Preserve a user's explicit requirements, implied outcome, constraints, priorities, and important details from request through implementation and delivery. Use when a vague request could be simplified into a shallow result or when many requirements must survive a long build.
---

# Intent preservation

Translate the request into a requirement ledger before building. For every item record its source, interpretation, priority, confidence, implementation location, verification method, status, and unresolved ambiguity.

Separate explicit requirements from reasonable inferences and optional ideas. Expand details that are necessary for the intended outcome, but label invented assumptions. Ask before an ambiguity changes architecture, cost, privacy, safety, external effects, or the user's likely experience. Otherwise choose a reversible, low-risk default and record it.

Before delivery, walk the ledger against the running artifact or final answer. Detect silent omission, accidental simplification, scope drift, and details that were discussed but never implemented. Report completed, partial, deferred, blocked, and rejected requirements separately.

Do not equate visual polish with intent alignment. A storefront may need data, state, cart or inquiry behavior, errors, persistence, and responsive flows; a game may need controls, feedback, progression, restart, and playability. Infer only what is justified by the user's outcome and verify it explicitly.
