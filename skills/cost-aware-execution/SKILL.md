---
name: cost-aware-execution
description: Optimize hosted-agent work for quality per unit of cost, latency, privacy exposure, and human effort using staged routing, caching, compact context, budgets, fallbacks, and verification. Use whenever online model or tool usage has a practical resource constraint.
---

# Cost-aware execution

Define a quality floor, time budget, data sensitivity, and usage budget before selecting a route. Optimize the full value equation: verified outcome quality minus model cost, tool cost, latency, privacy exposure, failure recovery, and user effort.

Use the cheapest route that can pass the current stage: small or fast models for classification, extraction, formatting, and routine edits; stronger models for architecture, ambiguity, difficult debugging, multimodal inspection, and final review. Do not route high-risk work to a weak model merely to save cost.

Reduce waste with compact context, progressive disclosure, caching of verified stable facts, reusable recipes, focused tests, and targeted repair. Record model, tool, token, time, retry, and failure information for evaluation. Stop when acceptance criteria pass or extra work has diminishing value.

Respect provider, privacy, and approval boundaries. A fallback may reduce speed or scope, but it must not silently weaken safety, truthfulness, permissions, or verification.
