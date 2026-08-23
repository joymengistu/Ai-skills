---
name: data-analysis
description: Analyze structured data reproducibly, validate assumptions, quantify uncertainty, and produce clear tables or visualizations. Use for datasets, metrics, experiments, forecasts, and dashboards.
---

# Data analysis

Define the decision the analysis supports. Inspect schema, provenance, missingness, duplicates, units, time periods, sampling, and leakage before calculating. Keep raw data immutable and record transformations.

Choose methods appropriate to the question and data-generating process. State assumptions, denominators, uncertainty, sensitivity, and limitations. Validate results with independent calculations or sanity checks. Label estimates as estimates and avoid causal language without causal design.

Make charts readable and decision-oriented. Include a reproducible script or query, input snapshot identifier, and a concise interpretation that distinguishes observation from recommendation.

## Operational deepening

Use this Skill to improve **reproducible analysis and honest interpretation**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is data provenance, cleaning, assumptions, uncertainty, visualization, validation, and limitations.

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
