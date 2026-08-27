# Next Actions

## Current state

**[IMPLEMENTED]** The repository contains a validated and published five-part Android app quality skill suite. Preservation documents and the two user-provided protocols have now been added. There is no live Android sample project or dedicated Android evaluation corpus yet.

## Top recommendation

Create a small, representative Android skill evaluation fixture under `evals/` and apply the suite to it. This matters because structural validation proves package integrity but not whether another agent can use the skills to produce complete, platform-appropriate, accessible, resilient, and verifiable app plans. The expected result is a repeatable baseline with scored cases, failure examples, and evidence for future changes. It depends on choosing representative app briefs and does not require a production Android app.

## Prioritized next actions

### P0 — Critical

| Action | Reason | Expected impact | Dependencies | Difficulty | Risk | Scope | Related files |
|---|---|---|---|---|---|---|---|
| Add Android evaluation cases for primary journey, lifecycle interruption, offline behavior, permission denial, accessibility, and release readiness | Establish evidence beyond syntax and frontmatter validation | Makes skill quality measurable and exposes gaps | Existing `evals/` format and Android suite | Medium | Low | Medium | `evals/cases.jsonl`, `evals/rubric.md`, `skills/android-*` |
| Verify the published branch remains clean and the manifest lists every Android skill | Prevent catalog drift | Keeps publication reproducible | GitHub access | Small | Low | Small | `manifest.yaml`, `skills/android-*` |

### P1 — High Priority

| Action | Reason | Expected impact | Dependencies | Difficulty | Risk | Scope | Related files |
|---|---|---|---|---|---|---|---|
| Create a minimal Android sample app as a fixture | Test the skills against actual lifecycle, UI, accessibility, and build behavior | Converts guidance into runtime evidence | Android SDK/Gradle environment | Large | Medium | Large | New project linked from `meta/PROJECT_INDEX.md` |
| Add a focused Android reference covering platform-version and Compose-specific checks | Keep fast-changing implementation details out of the core skill files | Improves progressive disclosure and maintenance | Source review and version policy | Medium | Medium | Medium | `skills/android-*/references/` |

### P2 — Medium Priority

| Action | Reason | Expected impact | Dependencies | Difficulty | Risk | Scope | Related files |
|---|---|---|---|---|---|---|---|
| Add examples of good and bad Android skill outputs | Reduce ambiguity for future agents | Improves consistent application | Evaluation cases | Small | Low | Small | `evals/`, Android skill files |
| Record a release note for the Android suite | Improve discoverability of the change | Helps maintainers understand the addition | Repository release convention | Small | Low | Small | Root release documentation |

### P3 — Low Priority

| Action | Reason | Expected impact | Dependencies | Difficulty | Risk | Scope | Related files |
|---|---|---|---|---|---|---|---|
| Add optional templates for Android architecture decisions and release reports | Speed repeated work | More consistent handoffs | Proven repeated use | Small | Low | Small | `skills/android-*/templates/` |

## Blockers

The main blocker is the absence of a configured Android SDK/device environment for runtime verification. No blocker prevents documentation-only evaluation work.

## Risks

The Android platform and recommended libraries evolve; unsourced, version-specific claims can become stale. The suite may appear complete while still lacking evidence from actual devices and assistive technology. A broad skill catalog can also create routing ambiguity if triggers are not kept specific.

## Opportunities

Use the existing evaluation, dynamic-verification, quality-gate, and skill-forging patterns to compare the Android suite against a baseline. A small sample app would provide a high-value bridge between agent guidance and real Android behavior.

## Quick wins

Add six to ten JSONL evaluation cases, document expected observable coverage, and run the existing evaluator. Keep cases independent so failures identify the smallest skill or reference gap.

## Future directions

**[IDEA]** Build a portable Android quality harness that can ingest an app brief, generate a traceability matrix, inspect a project tree, and produce a release-gate report. This remains an idea until implemented and evaluated.

## What not to do yet

Do not merge the five Android skills into one file, add large generic Android tutorials, claim runtime accessibility without assistive-technology testing, or introduce a Manus-only dependency merely to automate a repository task.

## Recommended order

1. Add representative evaluation cases.
2. Run and record the baseline.
3. Repair only measured gaps in the Android skills.
4. Create a minimal Android sample fixture if the environment supports it.
5. Repeat accessibility, lifecycle, failure-state, compatibility, and release checks.
6. Publish changes with validation evidence and updated handoff documents.
