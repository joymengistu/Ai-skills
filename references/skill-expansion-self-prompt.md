# Efficient Skill-expansion self-prompt

## Purpose

Use this prompt to deepen an existing Skill without assuming that a longer document is better. The goal is to increase **execution value per token**: another agent should know more clearly what to do, when to do it, how to verify it, how to recover from failure, and how to compose the Skill safely.

## Copyable self-directing prompt

```text
SKILL DEEPENING MODE

Audit the existing Skill before editing it. Do not pad it, rewrite it for style alone, or make every Skill the same length. Add detail only when it provides non-obvious, task-relevant execution value.

1. PRESERVE THE CONTRACT
   - Keep the Skill’s trigger, purpose, scope, and existing correct behavior.
   - Separate explicit requirements, necessary inferences, optional ideas, and unknowns.
   - Identify what the Skill must do, may do, must not do, and must escalate.

2. FIND REAL GAPS
   - Check trigger precision, actionability, evidence, failure handling, examples, composition, human value, and restraint.
   - Search existing Skills and references before adding material.
   - Mark every proposed addition as a workflow step, decision rule, verifier, failure mode, example, exception, composition contract, safety boundary, or stopping rule.
   - Reject generic introductions, repeated repository-wide rules, motivational prose, and decorative complexity.

3. ADD HIGH-INFORMATION DETAIL
   - Add the smallest useful preflight and execution workflow.
   - Define inputs, outputs, dependencies, permissions, evidence, and handoff state.
   - Add good, bad, borderline, exception, and transformation examples when they clarify judgment.
   - Add common failure modes with the smallest repair and regression check.
   - Link variant-specific depth to references instead of overloading SKILL.md.

4. PROTECT CONTEXT AND HUMAN VALUE
   - Keep SKILL.md under the repository limit and preserve progressive disclosure.
   - Prefer concise tables or examples over repeated explanation.
   - Do not add steps merely because they are possible.
   - Optimize for useful progress, user agency, accessibility, privacy, recoverability, and calibrated trust.

5. TEST THE CHANGE
   - Create or select representative, adversarial, and boundary cases.
   - Compare the previous and expanded versions under the same prompt, model, context, and budget when a real experiment is available.
   - Track requirement coverage, outcome, trajectory, regressions, latency/cost, and human effort separately.
   - If no real paired experiment exists, report the result as structural validation only.

6. PROMOTE CONSERVATIVELY
   - Keep the prior version and a rollback path.
   - Promote only if the addition improves a measured or clearly documented gap without hard-gate regressions.
   - Hold when evidence is incomplete; reject when the change adds noise, unsafe authority, duplication, or regressions.
   - Record a lesson for every failed experiment.

CLOSING QUESTION
Does each new paragraph help an agent make a better decision or execute a safer, more complete task? If not, remove it or move it to an on-demand reference.
```

## Quality rubric

| Dimension | Strong expansion | Weak expansion |
|---|---|---|
| Trigger | Explains when to load and when not to load the Skill. | Uses broad adjectives without a task boundary. |
| Workflow | Gives an executable sequence with decision points. | Adds general advice without an order or action. |
| Evidence | Names what proves success and what remains unknown. | Claims improvement from prose length or intent. |
| Failure | Covers likely failure and smallest repair. | Says “handle errors” without a recovery path. |
| Examples | Clarifies judgment with contrasting cases. | Adds repetitive or obvious examples. |
| Composition | Defines inputs, outputs, dependencies, permissions, and conflicts. | Assumes the Skill works in isolation. |
| Human value | Reduces effort and preserves agency, accessibility, privacy, and recovery. | Optimizes for activity, verbosity, or engagement. |
| Restraint | Every addition earns its context cost. | Uniformly inflates every Skill. |

## Decision rule

Expand when the expected reduction in requirement loss, unsafe behavior, rework, or user effort exceeds the context and maintenance cost. Keep a Skill short when its purpose is narrow, its workflow is already complete, or its missing details belong in a reusable reference. A long Skill is not evidence of a strong Skill.

## Evidence boundary

The prompt is a governance and authoring procedure. It does not itself prove improved model performance. Real improvement requires matched before-versus-after evaluation under controlled conditions, held-out cases, independent grading, and explicit regression review.
