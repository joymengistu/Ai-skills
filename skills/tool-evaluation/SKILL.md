---
name: tool-evaluation
description: Evaluate whether agent tools are discoverable, well-scoped, correctly selected, efficiently called, and valuable in real multi-step tasks. Use when adding tools, debugging tool use, or comparing agent harnesses.
---

# Tool evaluation

Evaluate tools in realistic trajectories, not isolated demos. For each task record tool discovery, selected tool, arguments, permission outcome, latency, runtime, token use, output quality, error class, retries, side effects, and whether the call advanced the requirement ledger.

Prefer tools with clear names, concise descriptions, strict schemas, useful error messages, stable outputs, bounded side effects, and feedback that lets the agent adapt. Test valid alternatives, malformed arguments, stale state, partial failure, permission denial, timeouts, and idempotent retry behavior.

Measure end-to-end value: requirement coverage, successful completion, repair convergence, human effort, cost, latency, privacy exposure, and harmful or surprising side effects. A tool is not successful merely because its call returned 200 or produced output. Keep high-impact actions approval-gated and ensure logs support reconstruction without exposing secrets.
