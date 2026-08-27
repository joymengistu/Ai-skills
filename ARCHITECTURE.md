# Architecture

## System overview

Ai-skills is a repository of agent operating contracts and composable capability packages rather than a single runtime application. The root `manifest.yaml` is the catalog and loading map.

## Modules

| Module | Responsibility |
|---|---|
| `core/` | Required operating contract, execution loop, planning modes, and system-level behavior |
| `skills/` | Focused capabilities that activate by task and compose through explicit handoffs |
| `references/` | Larger contracts, research, patterns, and domain guidance loaded progressively |
| `evals/` | Cases, rubrics, and validation utilities for measuring capability quality |
| `governance/` | Risk matrix and safety boundaries |
| `contributions/` | Preserved source materials and mission documents |
| `prompts/` | Preserved reusable user instructions |
| `meta/` | Global indexes for projects and capabilities |

## Android skill data flow

The intended flow is `android-product-quality` → specialized handoff to `android-ux-accessibility` and `android-engineering` → evidence and release decision through `android-verification-release`. `android-skill-maker` governs creation or revision of the skill packages themselves and should not be used as a substitute for app implementation or release verification.

## Boundaries

Skills provide instructions and output contracts. They do not secretly execute Android builds, grant permissions, or establish production trust. Concrete app projects should remain in their own repository or project folder and link back to the relevant skills.

## Build and publication system

There is no compiled artifact. A skill change consists of actual Markdown/YAML/resource files, validator output, a Git commit, and a pushed repository branch. The official local skill validator checks package structure and frontmatter during authoring.

## Portability

The architecture uses plain text, YAML, JSONL, Python, and Git. The Android suite intentionally avoids a Manus-only runtime dependency. If a future integration requires Manus infrastructure, record the boundary in `MANUS_DEPENDENCIES.md` and provide a replacement path where practical.
