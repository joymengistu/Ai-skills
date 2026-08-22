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
