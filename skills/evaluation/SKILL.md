---
name: evaluation
description: Build traceable, repeatable evaluations for agent quality, tool use, safety, efficiency, robustness, and human value. Use when comparing prompts, skills, models, tools, or releases.
---

# Evaluation

Define what good looks like before changing the system. Build realistic cases from real user goals, including multi-step tasks, ambiguity, partial failure, adversarial content, and long context. Pair each case with a verifier that allows valid alternative paths.

Capture traces: model calls, tool calls, handoffs, guardrails, approvals, outputs, errors, latency, tokens, and user actions. Grade both outcomes and trajectories: task success, factuality, tool choice, safety policy compliance, unnecessary work, recovery, and communication. Use human review for dimensions that cannot be reliably automated.

Maintain train/dev/held-out cases, version prompts and tools, run regression tests, inspect failures, and change one variable at a time where possible. Add recovery cases for crashes before and after side effects, approval timeouts, ambiguous tool results, context loss, and cancellation. Evaluate release readiness with `governance/capability-risk-matrix.md`; critical safety, privacy, control, and recoverability failures are hard gates, not averages. Never use an evaluator that rewards unsupported confidence or blindly copies the system's own rationale.

## Operational deepening

Use this Skill to improve **independent and reproducible quality evaluation**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is criteria, graders, cases, controls, trajectory/outcome separation, calibration, and regression review.

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
