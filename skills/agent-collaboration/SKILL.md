---
name: agent-collaboration
description: Coordinate specialist agents or workstreams with clear contracts, bounded parallelism, shared evidence, handoffs, synthesis, and conflict resolution. Use when a task benefits from independent expertise or parallel side-effect-free work.
---

# Agent collaboration

Use multiple agents only when decomposition improves the user's outcome after accounting for coordination, token, latency, and synthesis cost. Start with one well-contextualized agent when the task is simple, tightly coupled, or state-conflicted. Prefer focused subagents for isolated results; use communicating teams only when discussion or competing hypotheses creates clear value.

The lead owns the requirement ledger, task graph, shared decisions, synthesis, final verification, and release decision. For each workstream define objective, inputs, exclusions, tools, permissions, output schema, deadline, budget, evidence requirements, and escalation rule. Parallelize only independent and side-effect-free work; do not let multiple workers edit the same fragile files by default. Keep external mutations centralized behind approval and idempotency controls.

Handoffs must include completed work, evidence, assumptions, failures, unresolved questions, and the exact next decision. The synthesizer must check contradictions, duplicate work, missing coverage, provenance, and user requirements. Resolve disagreements by comparing evidence and task fit, not by majority vote or confident tone.

Estimate delegation value before spawning: expected quality or coverage gain minus coordination, token, latency, and conflict cost. Stop subagents when their contribution is sufficient, the budget is reached, risk rises, evidence is weak, or additional work has diminishing value. Report the collaboration outcome as one coherent result rather than exposing internal chatter.

## Operational deepening

Use this Skill to improve **safe delegation and worker handoffs**. Load it only when that outcome is relevant; do not activate it for unrelated work. The main review surface is ownership, inputs/outputs, conflict isolation, budgets, evidence, and handoff recovery.

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
