---
name: android-ux-accessibility
description: Design or review Android user experiences for clarity, adaptive layouts, accessibility, touch, input, navigation, and inclusive edge states. Use when specifying screens, Compose views, interaction flows, content design, or accessibility fixes for Android.
---

# Android UX and accessibility

Design for the conditions in which people actually use phones: one hand, interruptions, glare, poor connectivity, large text, assistive technology, different screen sizes, and uncertain attention. Keep the interface calm, legible, forgiving, and native to Android.

## Workflow

1. Identify the user’s task, confidence level, environment, input method, and consequence of failure.
2. Model each screen as a state machine: initial, loading, populated, empty, partial, offline, error, retrying, success, permission denied, and destructive-action recovery.
3. Use a clear hierarchy: one primary action per screen, descriptive titles, meaningful section labels, concise supporting text, and visible status. Do not encode essential meaning with color, position, gesture, or icon alone.
4. Design adaptive layouts for compact and expanded widths, portrait and landscape, font scaling, split-screen, foldables, keyboard visibility, and system insets. Reflow before truncating; allow scrolling before hiding content.
5. Make controls operable. Give every actionable element a meaningful accessible name, adequate touch target, visible pressed/focused state, sensible traversal order, and a non-gesture alternative. Announce important state changes without flooding the screen reader.
6. Make forms forgiving. Use the correct keyboard and input type, preserve values after errors, validate close to the field, describe constraints before entry, and provide an actionable error message.
7. Respect Android navigation. Make Back predictable, preserve scroll and draft state, avoid trapping users in modal flows, and distinguish temporary surfaces from destinations.
8. Review content. Use plain language, specific labels, concise errors, localized-friendly strings, plural rules, date/number formatting, and text that still works when translated or enlarged.

## Accessibility review matrix

| Area | Verify | Repair pattern |
|---|---|---|
| Semantics | Role, name, value, state, and action are exposed | Add semantic labels and merge only when the group is one meaningful control |
| Visual | Contrast, text scaling, non-color cues, and clipping | Use theme tokens, reflow, icons plus text, and test at large font scales |
| Motor | Reachability, target size, cancellation, and alternatives to gestures | Move primary actions into reachable regions and add explicit controls |
| Cognitive | Predictable flow, plain language, progress, and recoverable errors | Reduce choices, show next steps, and preserve work |
| Assistive tech | TalkBack order, announcements, focus after navigation, and switch access | Set focus deliberately after major transitions and test without sight |

## Android-specific heuristics

Prefer Material components and platform conventions unless a user need justifies a custom pattern. Use system bars and edge-to-edge intentionally rather than letting content collide with insets. Support system back and predictive-back behavior where applicable. Treat bottom navigation as a small set of peer destinations, not as a substitute for a complete information architecture. Use bottom sheets, dialogs, snackbars, and notifications for distinct purposes; do not hide critical information in transient messages.

## Verification

Test the primary task with TalkBack, large text, reduced motion, touch exploration, keyboard navigation where applicable, portrait and landscape, process recreation, a slow network, and a denied permission. Review screenshots at compact and expanded widths, then interact with the actual build because static visuals cannot prove focus order, announcements, hit regions, or state recovery.

## Failure boundaries

Never describe an app as accessible because it passes a linter or has content descriptions. Record which assistive technologies, font scales, devices, locales, and flows were actually checked. If a custom interaction cannot be made accessible, replace it with a native or explicit alternative rather than documenting a known trap.

## Output contract

Return a screen/state map, interaction rules, accessibility acceptance criteria, content guidance, platform decisions, and a prioritized list of repairs with evidence status.
