# Screenshot-reconstruction release report

## Mission implemented

The attached user mission requested a production-grade Skill for reconstructing provided UI screenshots as accurately as technically possible with HTML, CSS, JavaScript, and required assets. The new Skill treats the screenshot as the primary visual specification and explicitly distinguishes reconstruction from redesign, beautification, or generic professional UI generation.

## Repository changes

| Area | Change |
|---|---|
| New Skill | Added `skills/screenshot-reconstruction/SKILL.md` with forensic observation, measurement, typography and asset audit, layout inference, responsive reconstruction, same-viewport rendering, objective diffing, error triage, repair, output contract, examples, and lesson memory. |
| Architecture | Added `references/screenshot-reconstruction-architecture.md` with the measurement ledger, fidelity hierarchy, visual-validation model, responsive limits, confidence records, examples, and public-source boundary. |
| Core routing | Added `SCREENSHOT RECONSTRUCTION ROUTE` so screenshot-to-code requests load the focused Skill instead of generic UI-design guidance. |
| Benchmarks | Added five cases for screenshot forensics, reference fidelity, responsive uncertainty, mandatory render/compare/repair, and preserving unusual reference elements. |
| Attribution | Preserved the full attached mission as `contributions/screenshot-reconstruction-mission-original.txt`. |
| Release contract | Updated manifest, README, and repository validator. |

## Visual validation model

The required loop is `reference → observe → measure → implement → render → compare → identify differences → correct → rerender → verify`. Differences are triaged from global composition and geometry to spacing, typography, colors, components, assets, and micro-details. The Skill requires documenting browser, viewport, device-pixel ratio, font availability, volatile masks, evidence, confidence, and remaining uncertainty.

Public Playwright documentation supports the use of committed reference screenshots and visual comparison with configurable pixel tolerances and volatile-region styles [1]. It also warns that browser, platform, fonts, and rendering conditions can change screenshots. Therefore visual comparison is an instrument for fidelity, not proof of semantic accessibility, interaction quality, task completion, or production readiness.

## Evidence boundary

| Label | Conclusion |
|---|---|
| **FACT** | The new Skill, architecture reference, mission source, routing, benchmarks, and validator requirements are present. |
| **EVIDENCE** | The Skill passes its dedicated validator; the repository validates 62 Skills and 95 evaluation cases. |
| **INFERENCE** | A dedicated reference-first route should reduce accidental redesign and shallow screenshot-to-code output compared with routing solely through general UI taste. |
| **HYPOTHESIS** | Same-viewport rendering, objective diffs, and ordered repair will improve reconstruction fidelity on suitable tasks. |
| **UNKNOWN** | Real pixel-similarity effect size, cross-browser equivalence, font substitution error, responsive reconstruction quality from sparse screenshots, and human judgment of acceptable fidelity. |

## Limits

A static screenshot cannot reveal hidden interaction logic, backend behavior, semantic intent, or unseen responsive states. Exact pixel equality can be undesirable when rendering environments differ or when the original contains defects. The Skill must preserve the reference when reconstruction is requested, but it must still label unavailable assets, inferred behavior, approximated typography, and untested dimensions honestly.

## Validation

The final repository validation passed with **62 Skills**, **95 evaluation cases**, **17 reference-host tests**, **10 intelligence-kernel tests**, **5 benchmark-runner tests**, and all Skill validators. The benchmark runner remains `not_run` for model-quality comparison until real baseline/candidate measurements are supplied.

## Reference

1. [Playwright — Visual comparisons](https://playwright.dev/docs/test-snapshots)
