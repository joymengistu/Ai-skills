---
name: android-product-quality
description: Plan, design, or review Android apps for usefulness, clarity, platform fit, trust, and product completeness. Use when creating an Android app brief, product flow, feature set, design critique, or end-to-end app quality plan.
---

# Android product quality

Create an Android app that helps a real person complete a meaningful task with low friction and high confidence. Treat “good” as an outcome, not a visual style: the app must be understandable, useful, responsive, accessible, resilient, private, and maintainable.

## Compose this skill

Use `android-ux-accessibility` for interaction flows and inclusive design, `android-engineering` for implementation architecture and performance, and `android-verification-release` for evidence, testing, and release readiness. Use the repository’s `human-satisfaction`, `human-value-design`, `interaction-design`, `micro-ui`, `product-completeness`, `professional-taste`, `quality-judgment`, `requirement-traceability`, `dynamic-verification`, and `repair-loop` skills when available. Use `android-skill-maker` only when creating or revising this skill family.

## Workflow

1. **Frame the person and job.** State the target user, context, primary job, desired outcome, constraints, and why Android is an appropriate surface. Separate must-haves from optional delight.
2. **Map the primary journey.** Define entry, first value, repeat use, interruption, offline, permission, empty, loading, error, recovery, and completion states. Ensure each state answers: where am I, what happened, what can I do, and what happens next.
3. **Choose the smallest coherent product.** Remove features that do not strengthen the primary journey. Prefer progressive disclosure, sensible defaults, local persistence where appropriate, and clear undo or recovery over confirmation dialogs everywhere.
4. **Fit Android.** Respect system back, edge-to-edge behavior, adaptive layouts, touch targets, lifecycle recreation, keyboard/input methods, notifications, sharing, deep links, and platform permission expectations. Do not imitate iOS patterns when Android conventions provide a clearer path.
5. **Make trust visible.** Explain permissions at the moment of need, minimize collected data, state sync behavior, preserve user input, show save status, and make destructive or externally visible actions explicit before commitment.
6. **Specify quality gates.** Map each requirement to observable checks for correctness, failure behavior, security, privacy, performance, accessibility, compatibility, observability, reproducibility, and maintainability. A polished screenshot is not evidence of a good app.
7. **Review for human value.** Ask whether the app reduces effort, uncertainty, or stress. Remove decorative complexity, dead ends, surprise navigation, ambiguous icons, and feedback that arrives too late.
8. **Produce an implementation-ready handoff.** Include the user journey, state model, content rules, component inventory, data and permission boundaries, acceptance criteria, test matrix, and unresolved assumptions.

## Decision rules

| Situation | Prefer | Avoid |
|---|---|---|
| First launch | Reach first value quickly and defer optional setup | Mandatory account creation without a demonstrated benefit |
| Destructive action | Clear consequence, reversible undo, and scoped confirmation | Vague “Are you sure?” prompts with no recovery |
| Network uncertainty | Show cached state, freshness, retry, and what changed | Blank screens or silently stale data |
| Dense information | Hierarchy, grouping, progressive disclosure, and search | Tiny text or a wall of controls |
| Permission request | Explain purpose in context and degrade gracefully | Asking for every permission at launch |
| Form entry | Preserve input, validate near the field, and support keyboard flow | Clearing the form after an error |

## Acceptance evidence

Before calling the product good, show that the primary journey works from a fresh install and after process recreation; loading, empty, offline, timeout, denial, cancellation, and retry states are understandable; critical actions are accessible with TalkBack and large text; content survives expected interruptions; sensitive data and permissions are justified; and the app remains usable on the smallest supported screen and a representative large screen.

## Boundaries and recovery

Do not claim accessibility, security, or performance from design intent alone. If a requirement conflicts with platform behavior, privacy, or a quality gate, surface the conflict and propose the smallest safe alternative. If evidence is missing, label the result `not_run` or `unknown`, record the environment and assumptions, and continue only with a documented partial state.

## Output contract

Return a concise product brief or review with: target user and job, primary journey, state inventory, Android-specific decisions, quality-gate matrix, risks and assumptions, and the next verified action. Use concrete labels such as `passed`, `partial`, `failed`, `not_run`, or `not_applicable`.
