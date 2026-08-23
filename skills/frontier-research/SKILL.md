---
name: frontier-research
description: Conduct deep, comprehensive, and frontier-oriented research across papers, repositories, protocols, architectures, benchmarks, products, and failure analyses while separating facts from hypotheses and reporting stopping criteria. Use for important discovery, technology strategy, or “what is next” questions.
---

# Frontier research

Research the leading edge without assuming that new, popular, or heavily branded means best. Start with the decision the research must support.

## Research ladder

For each important capability, move through:

**Current best → frontier alternatives → obscure alternatives → research papers → implementations → benchmarks → failure analysis → combination opportunities → architecture → next question.**

Cover mature systems and emerging prototypes. Search across official documentation, original papers, reputable repositories, standards, benchmark artifacts, direct experiments, user reports, and credible independent analysis. Keep a source ledger with URL, publisher, date, evidence type, relevance, and limitations.

## Depth questions

Ask: What is it? How does it work? Why might it work? When does it fail? What does it depend on? What competes with it? What evidence produced the claim? Can the design be improved? What would make the conclusion change?

## Comprehensive versus exhaustive

Comprehensive means the important dimensions are covered: users, mechanism, alternatives, dependencies, edge cases, negative evidence, history, current frontier, future direction, economics, safety, privacy, accessibility, reliability, and missing information. Exhaustive research is a stronger claim and requires an explicit search boundary and stopping rule. Report searched ecosystems, search dimensions, exclusions, diminishing-returns threshold, and residual uncertainty.

## Synthesis

Separate **fact**, **inference**, **hypothesis**, and **opinion**. Compare alternatives under the same task, date, constraints, and metrics. Do not present a benchmark as universal intelligence. End with the strongest justified conclusion, failure modes, open questions, and a practical next experiment.

Read `contributions/ULTRIA-original.txt` for the complete user-authored frontier loop and `references/public-fable-analysis.md` for an example of public capability analysis without copying protected internals.

## Operational deepening

Use this Skill to improve **high-signal research at the edge of known capability**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is question, source hierarchy, uncertainty, reproducibility, speculation boundaries, and next experiment.

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
