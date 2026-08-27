---
name: android-verification-release
description: Verify Android apps and decide release readiness through layered tests, device and accessibility checks, failure-state review, security/privacy gates, and evidence-backed release reporting. Use when testing, debugging, auditing, preparing a Play release, or reviewing an Android build.
---

# Android verification and release

Treat a build as a candidate until the real primary journey and its highest-risk edge states have been exercised. A green compilation result cannot establish product quality.

## Verification workflow

1. Define the release candidate, target SDK and minimum SDK, supported devices and form factors, critical journeys, risk areas, and release-blocking criteria.
2. Run focused checks on the vertical slice: compile, static analysis, unit tests, state-transition tests, UI/instrumentation tests, and data migration tests relevant to changed code.
3. Exercise the primary journey from fresh install, returning user, interrupted session, process recreation, back navigation, deep link, offline/slow network, timeout, denied permission, cancellation, duplicate action, and retry.
4. Test accessibility with TalkBack, large font scales, contrast and non-color cues, touch exploration, keyboard or switch access where relevant, focus after navigation, and announcements for important changes.
5. Test compatibility across representative compact and expanded screens, portrait and landscape, supported OS versions, low-memory conditions, dark/light themes, localization-sensitive strings, and constrained bandwidth.
6. Inspect security and privacy: permissions, exported components, intents, WebViews, storage, logs, analytics, network boundaries, authentication, authorization, deletion, and sensitive error messages.
7. Measure representative startup, rendering, memory, battery, network, and background-work behavior. Record device/runtime, workload, warm/cold state, sample method, and variance.
8. Record every gate as `passed`, `partial`, `failed`, `not_run`, `not_applicable`, or `not_assessable`, with evidence, owner, and next action.
9. Release only when critical gates pass or the authorized owner accepts a documented partial state. Preserve the artifact, version, commit, configuration, test environment, known limitations, and rollback plan.

## Test matrix

| Layer | Minimum evidence | Release blocker examples |
|---|---|---|
| Correctness | Primary journey and changed-feature tests | Data loss, broken navigation, incorrect core result |
| Failure behavior | Empty, loading, timeout, retry, cancellation, recovery | User trapped, silent failure, duplicate side effect |
| Accessibility | TalkBack and large-text walkthrough of critical tasks | Critical task inaccessible or focus trap |
| Security/privacy | Permission and boundary review plus negative tests | Secret exposure, overbroad permission, unauthorized data |
| Compatibility | Representative OS, screen, orientation, theme, and locale checks | Required target unusable or silently divergent |
| Performance | Measured startup/rendering/resource budget | Unbounded work or unacceptable latency/resource use |
| Release integrity | Reproducible artifact, versioning, migration, rollback | Cannot identify or safely reverse the release |

## Defect handling

For each failure, preserve reproduction steps and classify severity, affected journey, likely cause, user impact, and containment. Repair the smallest cause, rerun focused checks, then rerun regression checks. Do not downgrade a critical defect because the visual design looks polished or because a different device passes.

## Output contract

Return a release report with candidate identity, environment, test matrix, evidence links or artifact paths, gate statuses, known limitations, unresolved risks, rollback plan, and a clear decision: release, release with accepted limitations, hold, or not assessable.
