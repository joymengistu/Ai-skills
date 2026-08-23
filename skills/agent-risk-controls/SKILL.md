---
name: agent-risk-controls
description: Apply model-agnostic runtime controls for agent risk, including untrusted input provenance, scope-drift detection, typed tool authorization, approval binding, cancellation, incident learning, and evidence-based completion. Use before deploying or extending agents with tools, memory, code execution, external network access, delegation, or self-improvement.
---

# Agent risk controls

Treat the model as one component of a larger system. Make the host enforce the boundaries that prompts and skills can only describe.

## Use the risk loop

1. **Map the action.** Record the user intent, target, resource and data scope, risk class, reversibility, permission, expected evidence, rollback, run ID, idempotency key, and state version before any side effect.
2. **Label the input.** Attach provenance to web pages, documents, tool results, memory, and peer-agent messages. Mark origin, trust level, content kind, source ID, timestamp, and allowed effects. Untrusted content may inform reasoning but cannot authorize tools, rewrite the goal, reveal protected instructions, or expand permissions.
3. **Compare scope.** Check the proposed action against the original intent and current approved scope. Pause when the target, destination, data class, or side effect is broader than the task permits or cannot be explained.
4. **Authorize the capability.** Require a registered tool, explicit allowlist entry, typed argument validation, destination/data-scope checks, a risk classification, a timeout/rate limit, and downstream authorization. Unknown risk is not low risk.
5. **Bind approval.** For consequential, irreversible, privacy-sensitive, external, financial, credential, cross-tenant, destructive, or unknown-risk actions, request approval over a hash of the exact action. Expire the approval and reject mismatched or ambiguous decisions.
6. **Limit blast radius.** Use filesystem and network isolation together for code or browser work. Keep secrets outside prompts and sandboxes, use least privilege and short-lived access, restrict egress, cap resources, and provide a tested kill switch.
7. **Observe live behavior.** Emit identity, owner, correlation, tool, scope, action hash, approval, result, evidence, and failure events. Monitor for loops, repeated retries, anomalous destinations, scope expansion, and cross-agent conflicts while the run is active.
8. **Verify independently.** Do not equate a model response, tool return, or self-assessment with completion. Run real tests and inspect the artifact, security state, intent alignment, and operational outcome. Report caveats when evidence is incomplete.
9. **Learn safely.** Record incidents and near misses with redacted evidence. Classify system, contextual, cognitive, model, tool, memory, permission, runtime, verification, and communication contributors. Turn lessons into regression cases or reviewed policy changes; never let an agent silently weaken its own controls.

## Special cases

### Indirect prompt injection
Do not rely on a keyword filter as the primary defense. Separate instructions from data, carry provenance through transformations, restrict effects of untrusted sources, and require an independent policy check before any action derived from external content.

### Memory
Treat persistent memory like a code change. Quarantine new entries, record source and confidence, assign a TTL, prevent memory from granting authority, and support inspection, correction, export, and deletion. User instructions and host policy outrank memory.

### Multi-agent work
Give each worker a unique identity and narrow task contract. Isolate credentials and workspaces, constrain communication and shared memory, record causal message links, prevent one worker from granting another authority, and pause when goals conflict. Use parallelism only for independent tasks; use a lead or arbiter for synthesis and disagreement.

### Approval fatigue
Do not ask for vague approvals or prompt users for every harmless read. Group only genuinely equivalent low-risk actions, show the exact target and side effect, bind approval to one action hash, and escalate when scope changes.

## Reference implementation

Use `runtime/reference_host/` when a credential-free executable reference is sufficient. It includes `TrustEnvelope`, `ActionIntent`, `ApprovalRecord`, cancellation, action journaling, tool argument and destination checks, approval gating, JSONL traces, atomic checkpoints, budgets, and a deterministic test suite. It is a reference implementation, not a production security boundary; replace or supplement it with OS-level sandboxing, identity, network controls, secret management, and independent monitoring before real deployment.

## Release gate

Do not release a risk-sensitive capability unless representative, adversarial, partial-failure, recovery, privacy, and human-control cases pass. A critical safety, privacy, authorization, containment, or recoverability failure is a hard stop and cannot be averaged away by quality or speed.
