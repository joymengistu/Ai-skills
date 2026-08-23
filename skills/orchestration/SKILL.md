---
name: orchestration
description: Select and coordinate workflows, bounded agent loops, specialist skills, model routes, and handoffs for complex tasks. Use when a task has multiple steps, tools, agents, or competing strategies.
---

# Orchestration

Choose the simplest architecture that can meet the success criteria. Use a deterministic workflow for predictable transformations. Use an agent loop only when the path depends on environment feedback or open-ended planning.

## Procedure

1. Define the outcome and verifier before choosing the architecture.
2. Identify independent subtasks, shared state, dependencies, and failure containment.
3. Route each subtask to the smallest capable skill or model.
4. Keep handoffs structured: objective, inputs, constraints, completed work, evidence, open risks, and expected output.
5. Bound loops with a maximum iteration count, budget, timeout, and stop condition.
6. Prefer parallel work only when subtasks are independent and side-effect free.
7. Recombine outputs with a verifier that checks contradictions, omissions, provenance, and user requirements.

Never create a multi-agent swarm to hide a missing plan. A single well-contextualized agent is often more reliable than many poorly coordinated agents.

## Operational deepening

Use this Skill to improve **composing multi-step agent workflows**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is ordering, typed artifacts, isolation, parallelism, joins, retries, ownership, and proof.

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
