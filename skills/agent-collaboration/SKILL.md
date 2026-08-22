---
name: agent-collaboration
description: Coordinate specialist agents or workstreams with clear contracts, bounded parallelism, shared evidence, handoffs, synthesis, and conflict resolution. Use when a task benefits from independent expertise or parallel side-effect-free work.
---

# Agent collaboration

Use multiple agents only when decomposition improves the user's outcome. Start with one well-contextualized agent when the task is simple or tightly coupled.

For each workstream define objective, inputs, exclusions, tools, permissions, output schema, deadline, budget, evidence requirements, and escalation rule. Parallelize only independent and side-effect-free work. Keep external mutations centralized behind approval and idempotency controls.

Handoffs must include completed work, evidence, assumptions, failures, unresolved questions, and the exact next decision. The synthesizer must check contradictions, duplicate work, missing coverage, provenance, and user requirements. Resolve disagreements by comparing evidence and task fit, not by majority vote or confident tone.

Stop subagents when their contribution is sufficient, the budget is reached, risk rises, or additional work has diminishing value. Report the collaboration outcome as one coherent result rather than exposing internal chatter.
