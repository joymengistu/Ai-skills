---
name: android-engineering
description: Build or review Android app implementation plans and code for architecture, state, lifecycle resilience, security, privacy, performance, and maintainability. Use when choosing Kotlin or Compose patterns, structuring an Android project, integrating APIs, or diagnosing implementation risk.
---

# Android engineering

Implement the smallest architecture that keeps state ownership clear, failures recoverable, and changes testable. Prefer boring, observable boundaries over clever abstractions.

## Workflow

1. Declare target Android versions, device classes, offline expectations, data sensitivity, authentication needs, and external effects.
2. Map the vertical slice from UI event to state update, persistence, network boundary, and rendered result. Define the source of truth for each piece of state.
3. Separate presentation, domain decisions, and data access enough to test them independently. Keep lifecycle-aware collection and cancellation explicit. Do not let UI code own durable business state.
4. Model loading, empty, success, stale, failure, retry, cancellation, and partial-result states as data rather than scattered booleans. Preserve user input across recreation and recoverable failures.
5. Minimize permissions and data. Validate untrusted input at boundaries, keep secrets out of source and logs, use least-privilege storage and network access, redact diagnostics, and define retention and deletion behavior.
6. Design for constraints: cold start, memory pressure, battery, background limits, flaky connectivity, low-end hardware, large datasets, and configuration/process recreation. Measure representative workloads rather than guessing.
7. Make dependencies explicit and reproducible. Pin versions where appropriate, document required services, add migrations, provide deterministic fixtures, and preserve rollback paths.
8. Instrument meaningful events and failures without collecting unnecessary personal data. Logs should explain what happened, correlation should be possible, and sensitive values should never be emitted.

## Architecture decisions

| Concern | Default direction | Evidence to request |
|---|---|---|
| UI | Jetpack Compose or the project’s established toolkit with unidirectional state flow | Screenshot plus interaction test and recreation test |
| State | One authoritative state model per feature and explicit event handling | State transition tests, including failure and retry |
| Data | Repository boundary with cache/network policy stated | Offline and stale-data behavior under test |
| Background work | Lifecycle- and constraint-aware work with cancellation | Restart, constraint, and duplicate-work tests |
| Navigation | Typed destinations or an equally explicit contract | Back-stack, deep-link, and process-death checks |
| Security | Least privilege, validated inputs, redacted logs, and protected secrets | Threat model and negative tests |
| Performance | Budgeted startup, rendering, memory, and network behavior | Device/runtime, workload, warm/cold state, and variance |

## Review checklist

Check for leaked coroutines, unbounded retries, duplicated sources of truth, work that assumes a screen is alive, UI state that disappears on rotation or process death, unsafe WebView or intent handling, exported components without a reason, insecure local storage, accidental PII in analytics, blocking work on the main thread, and dependency or schema changes without migration and rollback plans.

## Recovery rules

When an implementation fails, reproduce it with the smallest fixture, classify the failure as state, lifecycle, boundary, dependency, resource, or contract error, patch the smallest cause, rerun the focused test, then run the relevant regression suite. Do not silence errors, broaden permissions, disable validation, or add retries without a stop condition.

## Output contract

Return an architecture decision record or implementation review containing constraints, state and data-flow diagram, boundaries, security/privacy risks, performance budgets, test seams, migration/rollback plan, and evidence status.
