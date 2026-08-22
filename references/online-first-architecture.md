# Online-first architecture

## Current priority

Ai-skills is currently optimized for hosted models and online tools. The laptop acts as a lightweight control surface: it stores the project, displays progress, captures approvals, and can run small validators. Heavy model inference, browser sessions, visual checks, builds, and long-running workers may run remotely through authorized providers or services.

## Online run topology

```text
Laptop client
  ├─ brief + approvals + progress UI
  ├─ local project files and small validators
  └─ encrypted session identity
        │
        ▼
Hosted orchestrator
  ├─ requirement compiler
  ├─ model router
  ├─ skill/context loader
  ├─ staged work queue
  ├─ tool and browser bridge
  ├─ durable state + event trace
  ├─ evaluator + repair loop
  └─ human review gate
        │
        ├─ model providers
        ├─ sandbox/build workers
        ├─ browser/vision workers
        └─ storage and deployment targets
```

## Aha-effect loop

1. Show a clear interpretation and a fast visual or functional first slice.
2. Continue in the background or through resumable hosted steps while the user can inspect progress.
3. Add detail in priority order: core experience, interaction, system behavior, edge cases, polish, and operations.
4. Run the artifact, compare it to the requirement ledger, and repair the highest-impact omissions.
5. Present a coherent result with what is complete, what is unverified, and what can be improved next.

The feeling of speed comes from parallel preparation, templates, focused skill bundles, incremental outputs, and not re-solving known problems. It must not come from skipping verification or hiding incomplete work.

## Online resource policy

Use hosted capability for expensive or high-value steps, but maintain cost and privacy controls: model and tool budgets, caching, compact context, provider fallback, prompt/version tracking, data minimization, retention expiry, per-tool scopes, approval before sensitive actions, and deletion paths. Never treat a remote provider as implicitly trusted.

## Future local-AI track

Local models are intentionally deferred, not discarded. Future work may add local model adapters, offline routing, quantized model profiles, local embeddings, hardware detection, and privacy-first execution. The local track must implement the same capability manifests, traces, verification, permissions, and human-control contracts; it is not allowed to become an untested shortcut.

## GOAT quality metrics

Measure time-to-first-usable-result, time-to-verified-complete-result, requirement coverage, intent alignment, runtime success, repair convergence, user effort, satisfaction, cost, latency, privacy exposure, and recovery quality. Optimize the full vector for each task instead of maximizing one demo metric.
