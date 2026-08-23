# Skill-expansion release report

## Objective

The user observed that many Skills were very short and requested much larger Skills. The repository response was to deepen all 61 Skills with tailored operational detail while refusing to equate length with intelligence. The expansion protocol audits each Skill first and adds only task-specific workflow guidance, decision rules, evidence boundaries, failure handling, examples, composition rules, and stopping conditions.

## Measured change

| Measure | Before | After |
|---|---:|---:|
| Skill count | 61 | 61 |
| Minimum `SKILL.md` length | 12 lines | 41 lines |
| Maximum `SKILL.md` length | 64 lines | 93 lines |
| Average `SKILL.md` length | 19.5 lines | 48.6 lines |
| Evaluation cases | 85 | 90 |
| Operational deepening sections | 0 catalog-wide | 61 |

The migration preserved existing Skill contracts and added one domain-aware operational section per Skill. It did not create duplicate Skills or force a single exact length.

## New control

`references/skill-expansion-self-prompt.md` provides a reusable self-directing procedure. It tells a future agent to audit before editing, preserve the Skill contract, find a real gap, add high-information detail, protect context and human value, run paired tests when available, and promote conservatively. `skills/intelligence-infrastructure/SKILL.md` now routes future Skill deepening through this procedure.

## What each expansion adds

The added section identifies the Skill’s specific outcome and review focus, gives a four-step execution loop, defines evidence and authority boundaries, provides GOOD/BAD/BORDERLINE/EXCEPTION/TRANSFORMATION examples, and states composition and stopping rules. This makes a formerly terse Skill more actionable without copying the entire repository operating contract into every file.

## Validation

The catalog-wide regression suite verifies that all 61 Skills have exactly one operational deepening section, remain below the 500-line Skill limit, retain valid frontmatter, and keep the expansion prompt and audit present. The full repository validator passes with **90 evaluation cases**, **17 reference-host tests**, **10 intelligence-kernel tests**, **5 benchmark-runner tests**, and all Skill validators.

## Evidence boundary

| Label | Conclusion |
|---|---|
| **FACT** | All 61 Skill files were expanded and pass structural validation. |
| **EVIDENCE** | Size distribution improved substantially, and deterministic tests verify presence, uniqueness, and limits of the new sections. |
| **INFERENCE** | Tailored operational sections should make Skills easier for another agent to execute than terse trigger-only files. |
| **HYPOTHESIS** | The expanded catalog will improve requirement preservation, failure recovery, and first-pass quality in real hosted tasks. |
| **UNKNOWN** | Whether the extra context improves end-to-end model outcomes; whether it increases latency or context competition; which Skills need further specialist references. |

## Tradeoffs and stopping rule

The catalog is intentionally larger now, but larger is not automatically better. The new sections add context and maintenance cost. Future revisions should remove or move detail to references when it duplicates another Skill, fails to change a decision, or displaces task-relevant context. Real before-versus-after model trials remain necessary before claiming performance improvement.
