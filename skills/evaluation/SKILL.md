---
name: evaluation
description: Build traceable, repeatable evaluations for agent quality, tool use, safety, efficiency, robustness, and human value. Use when comparing prompts, skills, models, tools, or releases.
---

# Evaluation

Define what good looks like before changing the system. Build realistic cases from real user goals, including multi-step tasks, ambiguity, partial failure, adversarial content, and long context. Pair each case with a verifier that allows valid alternative paths.

Capture traces: model calls, tool calls, handoffs, guardrails, approvals, outputs, errors, latency, tokens, and user actions. Grade both outcomes and trajectories: task success, factuality, tool choice, safety policy compliance, unnecessary work, recovery, and communication. Use human review for dimensions that cannot be reliably automated.

Maintain train/dev/held-out cases, version prompts and tools, run regression tests, inspect failures, and change one variable at a time where possible. Add recovery cases for crashes before and after side effects, approval timeouts, ambiguous tool results, context loss, and cancellation. Evaluate release readiness with `governance/capability-risk-matrix.md`; critical safety, privacy, control, and recoverability failures are hard gates, not averages. Never use an evaluator that rewards unsupported confidence or blindly copies the system's own rationale.
