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
