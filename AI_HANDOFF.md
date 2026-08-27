# AI Handoff

## Project purpose

Ai-skills is a portable, model-agnostic capability repository for capable, safe, evaluated, human-centered AI agents. It stores the actual instructions, contracts, references, evaluations, and governance needed to continue the work outside Manus.

## Vision

A future agent should be able to clone this repository, inspect `manifest.yaml`, load the relevant core contracts and skills, run validation and evaluation, and make a traceable improvement without relying on hidden conversation context.

## Current state

**[IMPLEMENTED]** The repository is on the `main` branch and the Android app quality skill suite is published in commit `12f2941`. The working tree was clean after that publication. The suite consists of five validated skills under `skills/android-*` and is registered in `manifest.yaml`.

## Architecture and file structure

| Location | Role |
|---|---|
| `manifest.yaml` | Catalog, principles, and registered skill names |
| `core/` | Operating contract, execution loop, and planning modes |
| `skills/` | Focused, composable agent capabilities |
| `references/` | Detailed contracts, research, and design patterns |
| `evals/` | JSONL cases, rubrics, and Python validators |
| `governance/` | Capability and risk controls |
| `contributions/` | Preserved source contributions and mission documents |
| `prompts/` | Preserved reusable user instructions and protocols |
| `meta/` | Global project and capability indexes |

## Important files

The Android suite is located at `skills/android-product-quality/SKILL.md`, `skills/android-ux-accessibility/SKILL.md`, `skills/android-engineering/SKILL.md`, `skills/android-verification-release/SKILL.md`, and `skills/android-skill-maker/SKILL.md`. The suite’s composition references existing skills such as `human-satisfaction`, `human-value-design`, `interaction-design`, `micro-ui`, `product-completeness`, `professional-taste`, `quality-judgment`, `requirement-traceability`, `dynamic-verification`, and `repair-loop`.

## Existing functionality

The repository provides reusable guidance for planning, research, tool use, coding, evaluation, safety, memory, orchestration, UI vision, product completeness, skill forging, and release-quality reasoning. The Android suite adds product-quality framing, Android UX and accessibility review, implementation architecture, verification and release gates, and Android-specific skill authoring.

## Unfinished functionality

**[PARTIAL]** The Android suite does not yet include a live Android sample app or a dedicated automated evaluation dataset. Runtime behavior of any app produced using the skills is therefore **[UNKNOWN]** until a concrete project is tested.

## Known bugs and limitations

No known repository-breaking bug was found during publication. The primary limitation is evidence coverage: structural skill validation passed, but broad scenario evaluation and real-device Android verification remain to be added.

## Dependencies and environment

Use Git and GitHub CLI for repository operations. Use Python 3 and PyYAML to run the official skill validator at `/home/ubuntu/skills/skill-creator/scripts/quick_validate.py`. The skills themselves are Markdown and do not require Manus at runtime. If a future workflow uses Manus-only services, document that dependency in `MANUS_DEPENDENCIES.md` before relying on it.

## Installation and running

Clone the repository, inspect `manifest.yaml`, and read `core/operating-contract.md` and `core/execution-loop.md` before loading optional skills. To validate a skill during authoring, run `python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py <skill-name>` from the local skill workspace. This repository is a knowledge and instruction library rather than a conventional executable application.

## Build and deployment

There is no compiled application build or deployment pipeline. Publication is performed by committing the actual files and pushing the Git branch to GitHub. Preserve the commit identifier and validation output in the task record or relevant release document.

## Design and architecture decisions

The Android capability was split into five focused packages instead of duplicating all general agent guidance in one large skill. `android-product-quality` orchestrates the suite; UX, engineering, verification, and skill authoring remain separately discoverable. The user’s preservation protocols are retained verbatim under `prompts/`.

## Constraints

Do not claim that an Android app is accessible, secure, performant, or release-ready without evidence. Do not silently remove existing skills or references. Keep skill files under 500 lines, use clear frontmatter triggers, preserve actual source text, and distinguish `[IMPLEMENTED]`, `[PARTIAL]`, `[PLANNED]`, `[IDEA]`, `[EXPERIMENTAL]`, `[ABANDONED]`, and `[UNKNOWN]` states.

## Manus-specific dependencies

**[PARTIAL]** Authoring used the local Manus skill-creator validator, but the published skill content is portable Markdown. Any future use of Manus APIs, hosted infrastructure, or proprietary runtime behavior must be recorded explicitly before it becomes a project dependency.

## Recommended continuation strategy

First read `PROJECT_SUMMARY.md`, `NEXT_ACTIONS.md`, `ARCHITECTURE.md`, and `DECISIONS.md`. Then add evaluation cases for the Android suite under `evals/`, run them against representative app briefs, and update the Android skills only when a measured gap justifies a change. Preserve the original files, validate every modified skill, run `git diff --check`, and publish with a descriptive commit.

## Things not to change without understanding the architecture

Do not remove core contracts, rename manifest skill entries, merge the Android packages into a monolith, or rewrite historical references without checking downstream links and catalog assumptions. Do not turn planned evaluation work into an implementation claim.
