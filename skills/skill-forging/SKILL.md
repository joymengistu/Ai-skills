---
name: skill-forging
description: Create, improve, validate, package, version, evaluate, and retire modular AI skills with clear triggers, progressive disclosure, bounded workflows, resources, permissions, and tests. Use when designing a new skill or upgrading an existing agent capability.
---

# Skill forging

Create a focused capability package, not an unbounded “skill for anything.” Universal behavior belongs in the operating contract; domain procedures belong in specialized skills; large references belong in linked resources.

## Forge lifecycle

1. **Discover the gap.** Start from a repeated failure, user need, missing domain procedure, or measurable capability gap.
2. **Frame the outcome.** State who benefits, what changes for them, constraints, definition of done, and how success will be verified.
3. **Define the trigger.** Write metadata that says what the skill does and when it should activate. Avoid vague descriptions that trigger everywhere.
4. **Choose the scope.** List inputs, outputs, exclusions, permissions, risk class, dependencies, and failure behavior.
5. **Design progressive disclosure.** Keep `SKILL.md` concise. Move variant procedures, schemas, scripts, and templates into `references/`, `scripts/`, and `templates/`.
6. **Write the workflow.** Use imperative instructions, decision points, examples, evidence requirements, and stopping rules. Do not repeat general model knowledge.
7. **Add safety.** Define untrusted inputs, privacy boundaries, approval gates, least privilege, rollback, and human escalation.
8. **Test it.** Add representative, ambiguous, adversarial, partial-failure, and boundary cases with verifiers that accept valid alternative paths.
9. **Validate and package.** Check YAML frontmatter, line count, links, resources, scripts, examples, permissions, version, and compatibility. Run the skill validator and its tests.
10. **Assign lifecycle state.** Keep the package `proposed`, `drafted`, `experimental`, `evaluated`, `trusted`, `deprecated`, or `retired`; state changes require evidence and an authorized owner.
11. **Evaluate promotion.** Compare the candidate against the current baseline on representative, ambiguous, adversarial, partial-failure, and held-out cases. Require measurable improvement without critical safety, privacy, control, recovery, or accessibility regression.
12. **Observe and evolve.** Inspect traces and human feedback. Change the smallest layer that explains the failure, compare against a baseline, preserve provenance, and keep a tested rollback.
13. **Retire responsibly.** Mark obsolete skills, migrate dependents, preserve provenance, and remove triggers that cause stale behavior.

## Skill contract

Every skill should declare `name`, `description`, purpose, activation conditions, inputs, outputs, workflow, safety, verification, failure recovery, resources, and maintenance notes. Prefer a small number of composable skills over a huge catalog.

## Quality gate

A skill is ready only when another agent can discover when to use it, follow it without hidden context, know what not to do, fail safely, and produce an outcome that can be measured. A model-generated skill may propose changes but cannot grant itself permissions, trust, production status, or authority to weaken safeguards. Never add a skill solely because its title sounds advanced or because feature count is increasing.

Read `references/full-mode-capability-map.md` for the lifecycle's place in Ai-skills, `references/skill-engineering-intelligence.md` for example-driven improvement and self-critique, and `/home/ubuntu/skills/skill-creator/SKILL.md` for the governing authoring guidance.

## Operational deepening

Use this Skill to improve **creating narrow Skills from evidenced gaps**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is gap proof, existing alternatives, contract, examples, tests, provenance, versioning, and promotion.

### Execute

1. Inspect the request, current artifact, context, constraints, and permissions before choosing a procedure.
2. Separate explicit requirements from reversible assumptions, optional ideas, and unknowns. Preserve the user’s goal and ask one focused question when ambiguity changes architecture, cost, privacy, safety, authority, or likely value.
3. Choose the smallest sufficient workflow. Produce an observable intermediate artifact, then verify the real result against acceptance criteria and the highest-risk edge states.
4. If the result fails, reproduce the failure, classify the smallest cause, patch narrowly, rerun focused and regression checks, and record what remains uncertain.

### Evidence and boundaries

Treat generated output as a candidate, not proof. Record the evidence source, confidence, freshness, and scope of each material claim. Do not grant permissions, change safety boundaries, retain sensitive memory, or declare completion merely because this Skill was loaded. Coordinate with the host runtime for approvals, budgets, traces, isolation, and external effects.

### Decision examples

| Kind | Pattern |
|---|---|
| GOOD EXAMPLE | Apply the Skill to its stated outcome, preserve requirements, produce the smallest useful artifact, and report concrete verification evidence. |
| BAD EXAMPLE | Load the Skill everywhere, repeat generic advice, skip inspection, or treat a plausible response as proof of success. |
| BORDERLINE EXAMPLE | The workflow is directionally correct but adds an expensive step without evidence that it improves the user’s outcome; hold and test the addition. |
| EXCEPTION | For a simple, reversible task, use the focused path and smallest relevant check rather than the full high-rigor workflow. |
| TRANSFORMATION | Convert a vague or overbroad request into a scoped outcome, typed inputs/outputs, decision points, acceptance checks, recovery path, and honest completion status. |

### Composition and stopping rule

Declare expected inputs, outputs, dependencies, conflicting Skills, permission needs, evidence handoff, and fallback behavior before composing this Skill with others. Stop when the acceptance checks pass, the budget is exhausted, risk rises, the user’s authority boundary is reached, or added detail has diminishing value.
