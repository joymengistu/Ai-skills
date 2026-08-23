# Product Completeness and Real-World Journey Contract

A product is complete only to the extent that the intended user can complete the intended journey in the stated context with the required behavior, data, states, safety, accessibility, recovery, and delivery evidence. A page, screenshot, compile, or happy-path demo is not the product.

## Journey record

```yaml
journey_record:
  objective: "User outcome"
  audience_and_context: ""
  platform_and_environment: ""
  requirements: []
  primary_journey:
    start_state: ""
    steps: []
    success_state: ""
  supporting_states: [loading, empty, invalid, error, offline, permission_denied, refresh, restart, cancel, recover]
  data_and_source_of_truth: ""
  backend_and_persistence: "verified|partial|unverified|not_applicable"
  accessibility_and_input_paths: "verified|partial|unverified|not_run"
  security_and_privacy: "verified|partial|unverified|not_run"
  observability_and_deployment: "verified|partial|unverified|not_run"
  evidence_refs: []
  unresolved_unknowns: []
  status: complete|complete_with_caveats|needs_review|blocked|failed|not_started
  next_validation: ""
```

## Completeness workflow

1. Compile the brief into roles, goals, screens, interactions, data, source of truth, state transitions, permissions, integrations, performance, accessibility, privacy, deployment, documentation, and acceptance checks. Include only dimensions relevant to the actual goal.
2. Define one thin vertical slice from entry to meaningful success. Verify it in the running system with realistic content before broadening.
3. Exercise the primary flow and the highest-risk negative, empty, loading, permission, network/tool failure, refresh/restart, keyboard or assistive, cancellation, and recovery states. Add domain-specific states for games, commerce, automation, or research as needed.
4. Keep visual fidelity, functional behavior, data/persistence, accessibility, security, resilience, and operational readiness as separate evidence categories. A mockup must be labeled a mockup; a screenshot diff must not prove backend or interaction completeness.
5. Verify the result through the user journey, not source inspection alone. Record environment, inputs, outputs, artifacts, test results, and limitations.
6. Repair the smallest missing capability, rerun the focused journey and relevant regression checks, and preserve partial or blocked states rather than silently narrowing requirements.
7. Stop when the stated acceptance bar is evidenced, the budget or authority boundary is reached, a host capability is missing, risk rises, or added breadth has diminishing value. Report the exact next validation or user decision.

## Hard gates

A critical failure in safety, privacy, authorization, data integrity, recoverability, accessibility, or the user’s must-have journey blocks a complete status. A polished surface, compile, successful API response, seed data, or one happy path cannot override a failed gate.

## Reporting

Report requirements covered, primary journey evidence, supporting states exercised, evidence by category, critical blockers, caveats, not-run or not-assessable checks, what remains unchanged, and the smallest next action. Use `verified`, `partial`, `unverified`, `deferred`, `blocked`, or `needs_review` for individual claims and the shared completion statuses for the overall outcome.

## Boundaries

This contract does not require every possible feature, guarantee every production condition, or justify checklist inflation. It does not grant deployment authority, invent backend behavior, or convert a visual prototype into a working product. Completeness is always relative to the stated user outcome and context.
