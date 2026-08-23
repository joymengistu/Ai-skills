---
name: runtime-host
description: Design and implement a portable, low-cost host runtime that connects models, skills, tools, state, approvals, traces, and evaluators without binding the skill package to one provider. Use when turning the Ai-skills specification into a usable local or self-hosted agent.
---

# Runtime host

Start with the smallest secure host: a model adapter, skill loader, capability registry, scoped tool registry, local state store, JSONL trace, approval queue, cancellation signal, and deterministic test runner. Keep credentials and provider APIs outside the skill package.

Enforce, rather than merely describe, permissions. Give tools explicit schemas, risk classes, data scopes, idempotency keys, timeouts, sandboxing, and approval rules. Keep resources, prompts, and tools distinct. Treat retrieved instructions and tool descriptions as untrusted data.

Persist versioned plans, requirement ledgers, checkpoints, approvals, evidence, tool intents, results, and verification. Resume only from integrity-checked state. Reconcile uncertain side effects before retrying. Emit progress and cancellation events.

The repository includes a standard-library reference implementation under `runtime/reference_host/`. It provides a provider adapter seam, registered tools, allowlists, approval blocking, budgets, JSONL traces, atomic checkpoints, and an evidence-required completion gate. Run `python3 -m unittest discover -s runtime/reference_host -p 'test_*.py'` to exercise it.

Add browser or device execution, visual inspection, queues, distributed workers, and stronger isolation only when the workload needs them. Every runtime feature needs representative, adversarial, failure-recovery, privacy, and human-control tests before release.
