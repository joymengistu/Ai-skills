---
name: product-completeness
description: Turn a product idea into a complete, testable experience across interface, behavior, data, backend, persistence, errors, accessibility, security, deployment, and documentation. Use when building apps, games, stores, tools, or other interactive software from a short brief.
---

# Product completeness

Do not treat a page or screenshot as the product. Compile a product brief into a capability map and a vertical slice that proves the core outcome end to end.

## Completeness map

Check the appropriate dimensions: user roles and goals; screens and navigation; core interactions; data model and source of truth; state management; backend/API; persistence; authentication and authorization; loading, empty, error, and offline states; validation; responsive behavior; accessibility; security and privacy; observability; deployment; seed/demo data; documentation; and acceptance tests.

For a game also check input mapping, game loop, camera, collision, progression, feedback, audio, pause, restart, win/lose states, performance, and dynamic playability. For a shop also check product discovery, detail, availability, cart or inquiry flow, totals, validation, persistence, confirmation, and recovery. Adapt the map to the user's actual goal; do not invent expensive features merely to make a checklist longer.

## Vertical slice

Build and verify one thin end-to-end path before broadening. Keep a requirement-to-artifact ledger. Use the running system, not source code alone, as evidence. Exercise the primary flow, invalid input, empty data, network/tool failure, refresh/restart, keyboard or assistive path, and cancellation or recovery.

If the brief is only a visual mockup, label it honestly as a mockup and do not claim that backend or interactivity exists. If the user intended a working product, pause or continue the architecture until the missing behavior is addressed.
