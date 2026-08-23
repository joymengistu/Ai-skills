# Executable reference host architecture

## Purpose

Ai-skills already defines a strong control plane: intent, requirements, capability routing, permissions, evidence, verification, completion, memory, and human value. The missing layer is a small executable reference host that enforces the most important contracts without becoming a competing full agent framework.

## Scope

The reference host is intentionally small and provider-agnostic. It provides:

| Component | Responsibility |
|---|---|
| Provider adapter | Convert a normalized request into a model call and return text plus usage metadata. |
| Tool registry | Register explicit tools with risk class, permission, and callable implementation. |
| Approval gate | Block tools listed in `tool_policy.approval_required` until an explicit decision is supplied. |
| Trace writer | Append schema-shaped JSONL events with sequence numbers, timestamps, actor, risk, payload, and optional evidence references. |
| Checkpoint store | Atomically persist resumable state and verify the run identifier on load. |
| Budget guard | Stop before exceeding model-call, tool-call, retry, or deadline budgets. |
| Completion gate | Require explicit verification evidence before reporting a completed run. |
| Deterministic test provider | Exercise the host without external credentials or network access. |

The host does not implement a general planner, browser, sandbox, queue, UI, distributed worker pool, or provider-specific authentication. Those remain adapters and future layers.

## Run lifecycle

```text
start
  → validate profile
  → emit run_started
  → acquire task context
  → call provider adapter
  → optionally propose tool action
  → check allowlist, risk, budget, and approval
  → execute registered tool
  → checkpoint state
  → verify explicit completion evidence
  → emit run_completed or run_stopped
```

Failure paths emit `tool_failed`, `run_paused`, or `run_stopped` and preserve the last safe checkpoint. A failed or interrupted run is not completed merely because a provider returned text.

## Safety invariants

1. A tool is unavailable unless registered and listed in the profile allowlist.
2. A tool requiring approval never runs without a matching approval decision.
3. Unknown risk is treated as approval-required and non-executable by default.
4. Budgets are checked before model and tool calls.
5. Trace events never store provider secrets; callers are responsible for redacting sensitive payloads.
6. Checkpoints are written atomically and cannot be resumed under a different run identifier.
7. Completion requires explicit evidence records; generated output alone is insufficient.
8. The host does not infer permission from a prompt, skill, tool description, or provider response.

## Extension contracts

A provider adapter implements `complete(request) -> response` and may wrap any hosted API. A tool implements `call(arguments) -> result`, while metadata remains in the registry and is never inferred from the callable. A future host can replace the JSONL trace and file checkpoint store with a database or event service without changing the run contract.

## What this proves

The reference host makes a subset of Ai-skills enforceable and testable. It does not prove that the skills improve model quality, that one provider is superior, or that the host is production-ready. Those claims require the comparative benchmark plan, real adapters, threat modeling, operational hardening, and held-out evaluations.
