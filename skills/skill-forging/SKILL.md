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

Read `references/full-mode-capability-map.md` for the lifecycle's place in Ai-skills and `/home/ubuntu/skills/skill-creator/SKILL.md` for the governing authoring guidance.
