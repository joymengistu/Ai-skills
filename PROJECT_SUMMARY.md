# Project Summary

## Project

**Ai-skills** is a model-agnostic operating system and capability library for building capable, safe, evaluated, human-centered AI agents.

## Objective

Provide reusable core skills, operating contracts, references, evaluations, and contribution patterns that help an AI agent plan, research, build, verify, preserve, and improve work safely.

## Vision

Enable another AI or developer to clone the repository, understand the capability architecture, reuse focused skills, verify outcomes with evidence, and continue development without depending on the original conversation.

## Current Status

**[IMPLEMENTED]** The repository is a GitHub-hosted skill catalog with core operating documents, references, evaluation assets, a manifest, and a growing `skills/` directory. The Android app quality suite was added and pushed in commit `12f2941`.

## Implemented

The repository contains core agent contracts, planning and execution skills, research and evaluation materials, UI and product-quality guidance, and five Android-focused skills: `android-product-quality`, `android-ux-accessibility`, `android-engineering`, `android-verification-release`, and `android-skill-maker`. The manifest registers all five skills, and each package passes the official skill validator.

## Partial

**[PARTIAL]** The Android skills have structural validation and content review, but they do not yet have a dedicated automated scenario-evaluation suite or Android sample application used as a live test fixture.

## Planned

**[PLANNED]** Add representative Android skill evaluation cases, validate alternative implementation paths, and connect the suite to a real Android sample project when one is available.

## Experimental

**[EXPERIMENTAL]** The repository’s broader self-improving-agent and ULTRIA-oriented capability work is evolving and should be evaluated against explicit baselines before promotion.

## Technology

The repository is primarily Markdown, YAML, JSONL, Python validation scripts, and Git. Skills are modular directories containing a required `SKILL.md` and optional resources.

## Architecture

The root manifest declares purpose, loading principles, and registered skills. `core/` contains operating contracts and execution modes; `skills/` contains composable capabilities; `references/` contains deeper contracts and research; `evals/` contains cases, rubrics, and validators; `governance/` contains risk controls; `contributions/` preserves source contributions; `prompts/` preserves reusable user instructions; and `meta/` contains ecosystem indexes.

## Dependencies

The project depends on Git, GitHub, Python 3, PyYAML for the validation script, and the local Manus skill-authoring validator during authoring. The repository itself is designed to remain readable and usable outside Manus.

## Known Problems

The repository has no full-project automated integration test that exercises every skill. Some historical contributions and references may use evolving terminology. The Android suite’s actual runtime behavior remains **[UNKNOWN]** until applied to a concrete Android codebase.

## Important Files

| File or directory | Purpose |
|---|---|
| `manifest.yaml` | Skill catalog and loading metadata |
| `SKILL.md` | Root operating guidance |
| `core/` | Agent operating contracts and execution loops |
| `skills/` | Reusable skills, including the Android suite |
| `references/` | Detailed architecture, quality, and research references |
| `evals/` | Evaluation cases, rubrics, and validators |
| `PROJECT_SUMMARY.md` | This project-level status summary |
| `AI_HANDOFF.md` | Continuation instructions for another AI developer |
| `NEXT_ACTIONS.md` | Prioritized recommendations based on actual state |
| `prompts/` | Preserved user-provided preservation protocols |

## Important Decisions

The Android capability was split into focused, composable skills rather than one oversized guide. The skill-authoring workflow is represented by `android-skill-maker`, while shared general guidance remains in the existing repository skills and references.

## Current Priorities

The highest-value next step is to create a small evaluation fixture that applies the Android suite to representative app requirements and records whether the resulting plans cover platform fit, accessibility, lifecycle, failure behavior, security, and release evidence.

## Recommended Next Steps

Read `NEXT_ACTIONS.md` for the prioritized continuation sequence. Read `AI_HANDOFF.md` before making architectural changes.
