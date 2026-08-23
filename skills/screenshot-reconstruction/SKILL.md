---
name: screenshot-reconstruction
description: Reconstruct a provided UI screenshot as accurately as technically possible with HTML, CSS, JavaScript, and assets. Use for screenshot-to-code work, visual reverse engineering, pixel-precision reconstruction, same-viewport rendering, image-diff comparison, and reference-fidelity correction—not for redesigning or merely making a similar interface.
---

# Screenshot reconstruction

## Core objective

Treat the screenshot as the primary visual specification. Reconstruct the smallest maintainable HTML/CSS/JavaScript system that minimizes visual difference while preserving the reference’s structure, geometry, typography, colors, assets, density, unusual details, and requested interactions. Do not substitute “professional-looking,” “beautiful,” or “modern” for matching the reference.

This Skill is a **visual reconstruction** route, not a general UI-design route. Load `references/screenshot-reconstruction-architecture.md` for the complete evidence model, output contract, confidence record, examples, and limits. Use Professional UI Taste only as a secondary evaluator; reference fidelity has priority.

## Inputs and preflight

Accept the available screenshot(s), viewport dimensions, device-pixel ratio when known, optional assets, optional fonts, existing project files, and interaction requirements. Use `references/multimodal-fidelity-contract.md` and `references/cross-modal-consistency-contract.md` to record reference locator, scaling/crop/compression, capture metadata, OCR or readability limits, observed regions, asset provenance, cross-modal agreement or conflict, and visual uncertainty. Inspect screenshots, extracted text, assets, and runtime independently before comparing. Record what is present and what is missing. If only one screenshot exists, mark unseen responsive behavior as inferred or unknown rather than inventing certainty.

Before writing UI code, create a compact visual specification:

| Area | Record |
|---|---|
| Viewport | width, height, pixel ratio, browser/rendering assumptions |
| Regions | page boundaries, shell, header, sidebar, content, overlays, footer |
| Geometry | x/y bounds, widths, heights, gaps, padding, margins, alignment edges |
| Surfaces | colors, borders, radii, shadows, opacity, gradients, backgrounds |
| Typography | family, fallback, size, weight, line-height, tracking, wrapping, alignment |
| Assets | logos, icons, images, fonts, provenance, unavailable approximations |
| Behavior | visible states, overlays, controls, scroll, collapse, interaction requirements |
| Confidence | evidence, assumption, confidence, reversible correction for uncertain items |

Use relationships and ratios when absolute measurements are uncertain. For example, record “sidebar ≈ 18% of viewport” before selecting a CSS value. Do not pretend an estimate is exact.

## Forensic workflow

1. **Observe.** Inventory every visible region, alignment line, repeated inset, surface, text role, asset, control, overlay, and unusual detail. Do not design a nicer replacement.
2. **Measure.** Estimate or derive coordinates, dimensions, ratios, gaps, padding, proportions, text bounds, and viewport coverage. Prioritize reliable repeated relationships over isolated guesses.
3. **Identify the system.** Infer whether each region is best represented by normal flow, flexbox, grid, sticky/fixed positioning, or limited absolute positioning. Choose the simplest model that reproduces the evidence and remains maintainable.
4. **Audit typography and assets.** Determine likely font metrics and fallback behavior before micro-spacing. Prefer supplied or original assets; document every approximation. Typography is geometry because font metrics change wrapping and vertical positions.
5. **Implement.** Use semantic HTML, CSS variables for repeated measured values, organized CSS, reusable components where helpful, minimal JavaScript, and no unnecessary dependencies. Do not sacrifice reference fidelity for arbitrary architectural preferences.
6. **Render.** Capture the implementation at the same viewport dimensions and stable rendering conditions as the reference. Record browser, OS, font availability, DPR, and any volatile-content masking.
7. **Compare.** Use overlay, difference image, pixel or perceptual comparison, and structured manual review. Inspect global composition first, then major geometry, spacing, typography, surfaces, components, and micro-details.
8. **Repair.** Fix the largest visual error first, rerender, compare again, and stop when improvements are negligible or evidence is exhausted. Do not spend ten minutes on a one-pixel icon offset while the main layout is wrong.

## Responsive reconstruction

When multiple screenshots exist, infer rules between them: what stays fixed, scales, wraps, stacks, disappears, becomes scrollable, or changes density. Reconstruct the underlying responsive system rather than creating unrelated static screenshots. Test at each supplied viewport and at one intermediate width when feasible.

When only one screenshot exists, separate observed facts from responsive hypotheses. Use fluid relationships when the evidence supports them, but do not claim unseen breakpoints match. Report responsive behavior as unverified when it was not observable or tested.

## Visual validation loop

The loop is mandatory:

`reference → implement → render → compare → identify differences → fix → render again → compare again`.

Use region-based comparison when possible so a low global difference cannot hide a severe local mismatch. Mask only documented dynamic regions such as timestamps or randomized content. A mask is a tradeoff, not proof; record it explicitly. Keep reference and generated screenshots versioned with metadata.

A visual diff can establish image mismatch but cannot establish semantic accessibility, keyboard behavior, task completion, production readiness, or meaningful interaction. Use `references/multimodal-fidelity-contract.md` and `references/cross-modal-consistency-contract.md` to keep visual, text/OCR, runtime, accessibility, asset, and operational claims separate. If interaction is requested, pair screenshot comparison with runtime, DOM, keyboard, focus, loading, error, and recovery checks. If visual, OCR, asset, or runtime evidence conflicts, preserve the conflict and lower confidence until a resolving check is performed.

## Difference triage

| Priority | Inspect first |
|---:|---|
| 1 | viewport coverage, page boundaries, major composition, shell and column alignment |
| 2 | widths, heights, spacing, padding, positioning, proportions, wrapping |
| 3 | font family, size, weight, line height, letter spacing, text metrics |
| 4 | colors, borders, radii, shadows, opacity, gradients |
| 5 | controls, icons, images, asset identity, small offsets, micro-details |

Use a difference record with `region`, `symptom`, `likely cause`, `evidence`, `confidence`, `smallest correction`, and `next check`. Keep uncertain decisions reversible through tokens or isolated component rules.

## Anti-patterns

Do not redesign the screenshot, simplify a dense reference without permission, add generic AI-dashboard styling, invent content, change the hierarchy, replace distinctive icons or logos casually, add unnecessary cards or gradients, make everything larger, use arbitrary animation, rely on excessive absolute positioning when responsiveness matters, or stop after the first render. An unusual visual element may be intentional; preserve it unless the user asks for change.

## Output contract

Deliver, as applicable, the visual analysis, inferred specification, implementation plan, HTML, CSS, JavaScript, asset decisions, validation screenshot(s), comparison/difference evidence, ordered corrections, final implementation, remaining uncertainties, and lessons learned. Distinguish `observed`, `inferred`, `approximated`, `verified`, and `not assessable from screenshot`.

## Composition and boundaries

Pair with UI Vision or Professional UI Taste only after reference fidelity is established. Pair with requirement compilation when the screenshot is part of a larger product request. Pair with dynamic verification when behavior is required, and with accessibility when the artifact must be operable. The Skill cannot infer hidden interaction logic from a static screenshot and cannot guarantee cross-browser pixel identity without controlled rendering environments.

## High-information examples

| Kind | Example |
|---|---|
| GOOD EXAMPLE | Measure the screenshot, record typography and asset confidence, implement semantic layout, render at the same viewport, inspect global and regional differences, repair typography before micro-spacing, and report remaining uncertainty. |
| BAD EXAMPLE | Generate a fashionable dashboard with similar colors, omit the screenshot’s unusual spacing, and declare pixel-perfect after one render. |
| BORDERLINE EXAMPLE | Match the major shell but use a different font that changes line wrapping; defer micro-polish and correct typography first. |
| EXCEPTION | Preserve an intentionally unusual dense panel, asymmetry, or visual element even if it conflicts with a generic “professional UI” preference. |
| TRANSFORMATION | Convert “turn this screenshot into HTML” into forensic analysis, measured specification, asset/font audit, layout model, same-viewport render, objective diff, ordered repair loop, and evidence-backed final handoff. |

## Self-critique and lesson memory

After each reconstruction, ask: what is visibly different; what was assumed; what was not measured; which approximation contributes most to remaining error; did the implementation accidentally redesign the reference; and which correction has the largest expected visual effect? Record successful and failed lessons with observation, cause, evidence, lesson, action, confidence, and example. A failed experiment should change the next reconstruction workflow, not be hidden behind a final screenshot.
