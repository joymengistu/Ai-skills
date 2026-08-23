---
name: superlative-analysis
description: Translate superlatives such as best, smartest, maximum, optimal, frontier, deepest, comprehensive, reliable, powerful, and autonomous into explicit objectives, constraints, evidence, alternatives, failure modes, and stopping criteria. Use whenever a user or plan makes a high-performance claim or asks for the strongest option.
---

# Superlative analysis

Treat high-performance words as requirements, not decoration. Never answer “best” without defining the objective and the comparison.

## Compile the claim

For any superlative, identify:

1. **Objective:** best for which human or system outcome?
2. **Dimensions:** capability, accuracy, reliability, speed, cost, effort, safety, privacy, clarity, autonomy, control, accessibility, creativity, maintainability, or another relevant dimension.
3. **Constraints:** time, budget, data, compute, deployment environment, risk tolerance, scale, and lifespan.
4. **Alternatives:** current baseline, serious competitors, obscure or emerging alternatives, and the option of doing nothing.
5. **Evidence:** benchmark, test, source, user outcome, date, and known limitations.
6. **Failure modes:** where the apparent winner breaks or becomes a worse choice.
7. **Uncertainty:** missing evidence, conflicting results, assumptions, and confidence.
8. **Stopping rule:** when further discovery has diminishing expected value.

## Interpret carefully

“Most intelligent” is multidimensional: reason, plan, abstract, learn, use tools, remember, adapt, handle uncertainty, self-correct, verify, understand modalities, complete long-horizon work, decompose, and recover. “Most productive” means useful correct progress per unit of time, cost, effort, and human intervention. “Frontier” means leading edge, not automatically mature or best. “Deep” means exploring mechanism, evidence, failure, dependencies, alternatives, and implications—not writing more words. “Comprehensive” means covering decision-changing dimensions, not maximizing document length. “Autonomous” includes observation, correction, verification, stopping, and escalation.

## ULTRIA loop

Use: **Discover → Verify → Compare → Test → Synthesize → Challenge → Select → Improve**. Search beyond the first obvious result. Challenge the apparent winner with counterexamples and a lower-cost or safer alternative. Prefer a conditional conclusion such as “best for X under Y constraints” over universal superiority.

## Output

Report the objective, criteria, comparison set, evidence, result, uncertainty, and next research question. Never confuse biggest with best, newest with best, popular with best, complex with intelligent, long with deep, or more with better.

Read `references/ultria-fork-integration-map.md` for how this skill fits the larger system and `contributions/ULTRIA-original.txt` for the complete user-authored source.

## Operational deepening

Use this Skill to improve **turning absolute claims into measurable comparisons**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is objective, dimensions, baseline, evidence, confounders, uncertainty, and stop rule.

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
