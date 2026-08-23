# Engineering Quality, Security, Performance, and Accessibility Gates

Use these gates for code, apps, agents, data workflows, documents with executable components, and deployed artifacts. Select gates proportionally to task class; mark non-applicable gates with a reason. A gate is evidence, not a guarantee of every unseen condition.

## Gate groups

| Gate | Minimum check | Hard-stop examples |
|---|---|---|
| Correctness | Requirements, types/schemas, deterministic tests, primary journey | Core requirement fails or data is corrupted |
| Failure behavior | Invalid, empty, loading, timeout, retry, cancellation, recovery | User is trapped or failure is silently misreported |
| Security | Input validation, output encoding, authn/authz, secrets, dependency risk, egress | Credential exposure, privilege escalation, injection, unsafe default |
| Privacy | Data minimization, scope, retention, redaction, deletion, consent | Sensitive data retained or sent outside scope |
| Performance | Representative workload, latency/resource budget, network/device constraints | Unbounded loop, resource exhaustion, unusable latency |
| Accessibility | Semantics, names/roles, keyboard, focus, contrast, reflow/zoom, reduced motion, assistive path | Critical task inaccessible or focus/keyboard trap |
| Compatibility | Target browser/OS/device/runtime/version and graceful degradation | Required target cannot run or behavior diverges silently |
| Observability | Logs/traces, status, errors, correlation, redaction, actionable diagnostics | Cannot tell whether action ran or failed |
| Reproducibility | Pinned inputs/dependencies, version, fixture, environment, artifact provenance | Result cannot be repeated or traced |
| Maintainability | Clear ownership, minimal complexity, docs, rollback/migration path | Unowned critical behavior or unsafe irreversible change |

## Gate procedure

1. Map each must-have requirement to one or more gates and observable checks.
2. Inspect dependencies, data boundaries, permissions, target environment, and realistic content before implementation.
3. Run focused checks on the vertical slice, then negative and edge-state checks, then broader regression checks.
4. Verify security, privacy, accessibility, performance, and compatibility with domain-appropriate tools or manual review.
5. Record evidence, environment, versions, assumptions, omissions, and confidence through artifact provenance.
6. Classify each gate `passed`, `partial`, `failed`, `not_run`, `not_applicable`, or `not_assessable` with a reason.
7. Treat critical security, privacy, authorization, containment, accessibility, data-integrity, or recoverability failures as hard stops.
8. Repair the smallest cause, rerun focused checks and regressions, and report remaining limitations.

## Accessibility boundary

Use W3C WCAG 2.2 as a public reference for perceivable, operable, understandable, and robust content, but do not claim full accessibility from automated checks or a screenshot. Consider cognitive, linguistic, sensory, motor, device, bandwidth, and stress conditions, and use human or assistive-technology review where appropriate.

## Security boundary

Threat-model untrusted input, prompt injection, path traversal, command execution, authentication, authorization, secrets, network egress, dependencies, logs, and supply chain. Do not treat generated code, templates, webpages, or tool output as trusted. Runtime controls must enforce isolation and permissions; prompt text cannot make code safe by declaration.

## Performance boundary

Measure representative behavior within a stated environment and budget. Do not convert one fast local run into a universal latency claim. Report workload, device/runtime, warm/cold state, network assumptions, sample method, and variance when performance matters.

## Release decision

Release only when required gates pass or the user explicitly accepts a documented partial state within authority. A visually attractive result, a green build, or a high aggregate score cannot average away a critical gate failure. Report verified, partial, failed, not-run, and unknown states separately.
