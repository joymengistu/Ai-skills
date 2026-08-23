---
name: product-strategy
description: Turn frontier AI research into original product opportunities using What-if, Why-not, 10×, magic-moment, quality-bar, and anti-feature-bloat analysis. Use when designing an AI product, agent platform, workflow, or major capability.
---

# Product strategy

Study existing products to understand why they work, where they frustrate people, what they waste, and what users wish existed. Learn from competitors without cloning them.

## What-if engine

For every important capability ask: What if this worked 10× better? What if the interface did not need this feature? What if the AI handled it automatically? What if the human needed only one decision? What would this look like without legacy assumptions? What would feel magical without becoming confusing?

## Why-not engine

For every limitation ask why it exists, whether it is technically necessary or merely conventional, whether the host system can remove it, and what new risk the removal creates.

## 10× engine

Compare the current approach, current limitation, proposed improvement, 2× version, 5× version, 10× version, and completely different approach. Prefer the option that improves the user's outcome, not the one with the most features.

## Magic moments

Look for useful moments: a critical memory appears at the right time, a complicated task becomes simple, research is completed, a hidden problem is caught, an error is prevented, a legitimate need is anticipated, a large project becomes understandable, many tools become one workflow, or work finishes hours earlier. Delight must be useful, predictable, and non-manipulative.

## Quality bar

Every feature must improve usefulness, effort, outcomes, trust, clarity, or accessibility; remain understandable and controllable; fail safely; and be measurable and maintainable. Apply the user-doesn't-care test: hide internal sophistication that does not help the person.

Use the loop **Observe → Research → Define → Question → Ideate → Prototype → Test → Measure → Critique → Improve**. Read `contributions/FORK-original.txt` for the complete user-authored doctrine.

## Operational deepening

Use this Skill to improve **turning ideas into valuable product decisions**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is user, problem, alternatives, scope, evidence, tradeoffs, risks, metrics, and learning.

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
