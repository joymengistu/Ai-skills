# Screenshot reconstruction architecture

## Purpose and boundary

The screenshot-reconstruction capability reconstructs a provided visual reference as HTML/CSS/JavaScript and required assets. It is **not** a general UI-design Skill, redesign Skill, or “make it beautiful” Skill. The screenshot is the primary visual specification; professional UI taste is a secondary evaluator and may not override reference fidelity.

## Evidence boundary

The user-provided mission defines the required workflow. Public Playwright documentation provides evidence that browser screenshots can be captured and compared against committed reference images, that rendering varies across browser/platform environments, and that pixel tolerances and stylesheets can be configured for deterministic comparison [1]. The repository should treat those practices as implementation evidence for a validation route, not as proof that pixel equality means good UX.

## Reconstruction pipeline

`reference intake → screenshot forensics → measurement ledger → typography/assets audit → layout model → implementation → same-viewport render → global/region diff → largest-error repair → rerender → responsive/state review → uncertainty and lessons report`.

The measurement ledger should record element, observed bounds or relationship, inferred CSS mechanism, evidence, confidence, and unresolved uncertainty. Use ratios and alignment relationships when absolute pixels are unavailable. Preserve unusual or dense reference behavior rather than “improving” it into a different design.

## Fidelity hierarchy

Prioritize differences in this order: overall composition, major geometry, spacing and proportions, typography metrics, colors and surfaces, component geometry, then micro-details. Typography is geometry: a font substitution can change wrapping and vertical positions even when the nominal font size matches. Asset provenance must distinguish original assets, provided assets, close alternatives, CSS shapes, and unavailable approximations.

## Visual validation

Render the reconstruction at the reference viewport dimensions and stable browser/environment settings. Store the reference image and generated image with metadata. Produce an overlay or difference image and calculate at least pixel-difference count or ratio when deterministic comparison is available. Use region-level checks for major shell, content, typography, and control areas so a good average cannot hide a severe local mismatch. Mask only documented volatile regions such as timestamps or randomized content; record each mask because masking can hide defects.

A screenshot diff is an instrument, not a final judge. It can detect visual mismatch but cannot establish keyboard behavior, semantic accessibility, meaningful interaction, task success, or production readiness. Pair image comparison with DOM/accessibility/runtime checks when the user requests functional behavior.

## Responsive reconstruction

For multiple references, infer rules across viewports: fixed versus fluid dimensions, wrapping, visibility, stacking, scroll behavior, breakpoints, and density changes. Do not build unrelated static screenshots. If only one screenshot exists, mark responsive behavior as inferred or unknown and avoid claiming that unseen breakpoints match.

## Required output contract

The Skill should produce: visual analysis; inferred specification; implementation plan; HTML/CSS/JavaScript as required; asset decisions; same-viewport render(s); overlay/difference evidence; ordered difference analysis; corrections; final implementation; remaining uncertainties; and lessons learned. If an interaction requirement exists, include runtime verification rather than only a screenshot.

## Anti-patterns

Do not redesign, beautify, simplify, or normalize the reference without permission. Do not invent content, replace distinctive assets casually, overuse absolute positioning when responsiveness matters, stop after the first render, or spend micro-detail effort while global geometry is wrong. Do not call a visually similar result pixel-perfect when typography, local geometry, asset identity, or responsive behavior remains unverified.

## Confidence record

Use this structure for uncertain decisions:

| Element | Assumption | Evidence | Confidence | Reversible correction |
|---|---|---|---|---|
| Font family | Closest available family | Letterforms, x-height, width, weight | Low/medium/high | Swap font token and rerender |
| Sidebar width | Measured relationship to viewport | Aligned boundaries and repeated insets | Low/medium/high | Update layout token |
| Asset identity | Original/alternative/CSS approximation | File metadata or visual match | Low/medium/high | Replace asset without changing layout |

## Examples

| Kind | Example |
|---|---|
| GOOD EXAMPLE | Measure the reference, implement a semantic layout, render at the same viewport, inspect a diff, repair typography and geometry, then report remaining uncertainty. |
| BAD EXAMPLE | Produce a fashionable dashboard with similar colors, ignore the screenshot’s unusual spacing, and call it pixel-perfect after one render. |
| BORDERLINE EXAMPLE | Match the shell and colors but use a different font that changes wrapping; the result needs typography correction before micro-spacing polish. |
| EXCEPTION | Preserve an intentionally unusual or dense visual element even if a designer would normally simplify it. |
| TRANSFORMATION | Convert “make this screenshot in HTML” into a measured visual specification, asset/typography audit, layout implementation, stable render, objective diff, ordered repairs, and evidence-backed final report. |

## References

1. [Playwright — Visual comparisons](https://playwright.dev/docs/test-snapshots)
