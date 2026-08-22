---
name: model-routing
description: Select, combine, and fall back between models according to task capability, effort, latency, cost, privacy, reliability, and risk rather than brand or size. Use when an agent has multiple models or providers available.
---

# Model routing

Choose a model as part of a measurable system, not as a universal winner. Define the task, required capabilities, risk, context size, latency budget, cost ceiling, privacy requirements, and acceptable fallback.

Route routine work to the smallest model that meets the quality bar. Route complex reasoning, multimodal, long-horizon, or high-consequence work to a stronger model only when the expected gain justifies cost and delay. Use staged routing: classify, select, execute, verify, and escalate when evidence is insufficient.

Keep fallback behavior explicit. A refusal, timeout, tool error, or low-confidence result is not the same as model failure. Preserve context and approvals across a fallback, record the reason, and do not route around safety controls. Compare model routes on held-out tasks, quality, recovery, latency, tokens, cost, and user effort.
