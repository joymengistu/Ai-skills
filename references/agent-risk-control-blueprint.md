# Agent risk-control and differentiation blueprint

**Status:** Evidence-led design proposal. The first reference-host tranche is implemented and tested; this document is not a certification or guarantee of safety.

## Executive conclusion

The most valuable next improvement is not another broad prompt. It is a **trustworthy action kernel**: a small runtime layer that treats every external input as potentially adversarial, every tool as a capability with scope and side effects, every memory write as a security-sensitive event, every delegation as an authority boundary, and every completion statement as a claim requiring evidence.

This direction is supported by converging public guidance. OWASP identifies behavior hijacking, tool misuse, and identity/privilege abuse as agentic risks.[1] NIST recommends lifecycle risk management and distinguishes model, application, and ecosystem risks, including confabulation, privacy, human-AI configuration, information integrity, and value-chain integration.[2] MITRE ATLAS provides a living adversarial taxonomy.[3] Public engineering work from Anthropic, Microsoft, Palo Alto Networks, AISI, and academic researchers repeatedly points to the same lesson: **the model is only one part of the attack surface; the harness, tools, memory, identity, network, permissions, and monitoring often determine the impact**.[4] [5] [6] [7] [8] [9]

## Risk taxonomy for Ai-skills

| Risk family | Failure pattern | Primary control | Evidence needed |
|---|---|---|---|
| Intent and goal | A task is silently broadened, hijacked, or pursued after it is no longer authorized. | Immutable intent record, scope-drift check, stop/defer rule, human escalation. | Original intent, proposed action, scope comparison, decision outcome. |
| Untrusted input | Web, documents, memory, tool results, or agent messages contain instructions that compete with the user’s task. | Provenance labels, instruction/data separation, no authority escalation, destination checks. | Source origin, trust label, transformed content, blocked/allowed decision. |
| Tool misuse | A legitimate tool is used for an unintended or excessive action. | Typed tool contracts, allowlists, argument validation, risk classification, approvals. | Tool identity, parameters hash, permission, approval, downstream result. |
| Identity and privilege | Shared credentials, privilege creep, confused “on behalf of” authority, or cross-tenant access. | Unique run/agent identity, owner, task-scoped permissions, downstream reauthorization, revocation. | Principal, owner, effective scope, correlation ID, revocation test. |
| Memory poisoning | Attacker-controlled or low-confidence material becomes durable guidance. | Memory provenance, confidence, TTL, quarantine, user review for sensitive/persistent writes. | Source, writer, confidence, expiry, promotion decision, deletion record. |
| Data leakage | Sensitive context crosses model, tool, log, network, or tenant boundaries. | Data classes, minimization, redaction, destination allowlists, tokenization, retention limits. | Data-flow decision, redaction record, destination, retention/deletion evidence. |
| Code and sandbox | Generated code or a tool reaches host files, metadata services, secrets, or unrestricted networks. | OS-level filesystem/network isolation, resource limits, no ambient credentials, monitored egress. | Sandbox profile, syscall/network decisions, resource usage, kill test. |
| Persistence and runaway | Infinite loops, repeated retries, polling storms, self-propagation, or unbounded spend. | Deadlines, rate limits, retry caps, circuit breakers, cancellation, kill switch. | Budget counters, cancellation event, residual-process check, recovery result. |
| Multi-agent coordination | Collusion, sabotage, premature consensus, duplicate work, or unsafe shared memory. | Explicit hierarchy, narrow task contracts, isolation, provenance, quorum/arbiter, conflict pause. | Agent identities, messages, shared-state changes, disagreement, arbiter decision. |
| Verification and truth | The agent claims success without testing, over-trusts its own output, or hides uncertainty. | Independent evaluator, dynamic checks, evidence ledger, completion gate, caveats. | Test output, evaluator identity, evidence refs, failed checks, final status. |
| Supply chain | A skill, MCP server, package, prompt, or external artifact is malicious or tampered. | Pin versions, provenance/signature, review, sandbox, dependency scanning, rollback. | Artifact digest, source, reviewer, scan result, approved version. |
| Human factors | Approval fatigue, automation bias, fake intimacy, manipulation, or poorly timed interruptions. | Risk-adaptive confirmations, concise action previews, honest uncertainty, agency controls. | Approval rationale, interruption timing, user decision, correction/review signal. |

## High-leverage controls to implement first

The first tranche is now implemented in `runtime/reference_host/`: trust envelopes, action intent hashing, bound approvals, cancellation, typed argument and destination checks, atomic checkpoints, JSONL traces, tamper-evident action journaling, redacted incident journaling, budgets, and deterministic tests. These controls are intentionally narrow and do not replace OS-level isolation, identity systems, network policy, secret management, or independent monitoring.

### 1. Action intent and authorization record
Before a consequential call, persist an action record containing intent, target, scope, risk, reversibility, permission, expected evidence, rollback, run ID, idempotency key, and state version. Compare the proposed action with the original task and stop on unexplained scope drift. This extends the repository’s existing action protocol and directly addresses goal hijacking, tool misuse, identity confusion, and agentic misalignment.

### 2. Trust and provenance envelope
Wrap every external input in metadata: `origin`, `trust_level`, `content_kind`, `received_at`, `source_id`, and `allowed_effects`. A webpage, memory fragment, tool result, or peer-agent message can inform reasoning but cannot grant permission, rewrite the user’s goal, reveal protected instructions, or authorize a new destination. This is deliberately not marketed as a perfect prompt-injection detector; the reliable defense is to make untrusted content **non-authoritative by construction**.

### 3. Real-time policy monitor and kill switch
Check each proposed action immediately before execution. Support a kill signal that stops new model/tool calls, records the reason, preserves a checkpoint, and verifies that no residual worker remains. AISI’s incident report specifically recommends fine-grained network controls, real-time monitoring/blocking, and evaluation designs that assume capable systems may act beyond their remit.[8]

### 4. Memory quarantine and promotion
Treat memory writes like code changes. New memory enters `candidate` or `quarantined`, carries source and confidence, expires by default, and becomes durable only after a policy check or user confirmation. Never let a memory item grant permission, override a newer user instruction, or alter the security contract. Provide inspect, correct, export, and delete operations.

### 5. Typed tool validation and destination boundaries
Tool metadata must include input validation, permission, data scope, destination scope, side effects, timeout, rate limit, and rollback. Validate both the tool request and downstream authorization. Unit 42’s scenarios show that prompt hardening alone does not address SSRF, SQL injection, broken object-level authorization, mounted-volume leakage, token theft, or vulnerable code interpreters.[9]

### 6. Risk-adaptive approvals instead of approval spam
Low-risk read-only actions may run within a narrow sandbox. Consequential, irreversible, unknown-risk, cross-tenant, external-communication, credential, financial, privacy-sensitive, or destructive actions require an approval preview that states **what, where, why, scope, side effect, evidence, and rollback**. The user should approve the action, not a vague paragraph. Approval decisions expire and are bound to one action hash.

### 7. Independent completion and evaluator gates
Separate generated output, artifact existence, requirement coverage, dynamic tests, security checks, visual usability, intent alignment, and operational readiness. The generator cannot be the only judge of its own success. A critical safety or privacy failure cannot be averaged away by a high quality score.

### 8. Incident and near-miss learning loop
Record near misses as well as successful attacks. Each report should capture system, contextual, and cognitive contributors; activity logs; tool and permission state; affected data; containment; uncertainty; and recovery verification. Convert the smallest safe lesson into a regression test or policy update, never silently into a more permissive behavior.

## Distinctive Ai-skills contribution

The repository should differentiate through a **Human-Value Reliability Loop**:

```text
understand the person
  → define the intended outcome and boundaries
  → choose the smallest capable bundle
  → preview risky actions
  → execute in a constrained environment
  → observe independent evidence
  → ask whether the result is actually useful and welcome
  → repair or stop
  → preserve the lesson with provenance and rollback
```

This connects technical safety with the repository’s Lovability, Brainstorm Mode, completion intelligence, quality judgment, and evolving-skill architecture. “Lovable” must mean clear, respectful, useful, honest, and agency-preserving—not emotionally dependent, flattering, or engagement-maximizing.

## Implementation order

| Order | Work | Why now | Ship gate |
|---|---|---|---|
| 1 | Add provenance envelopes, action-intent records, kill switch, and scope-drift checks to the reference host. | These are small, model-agnostic, and reduce impact across many threat classes. | Deterministic tests for injection-like input, denied drift, cancellation, and trace completeness. |
| 2 | Add typed tool argument/data/destination validation and approval hashes with expiry. | Prompt-only safeguards are insufficient against tool and identity failures. | Malformed arguments, disallowed destinations, stale approvals, and downstream denial tests. |
| 3 | Add memory quarantine/promotion with TTL and user deletion. | Persistent memory can turn one poisoned input into a long-lived failure. | Poisoned candidate never becomes authoritative; deletion and expiry are verifiable. |
| 4 | Add incident/near-miss schema and regression-case generator. | Reliability improves when failures become durable tests. | Incident record is redacted, reproducible, linked to a regression case, and cannot erase history. |
| 5 | Add adversarial benchmark suites mapped to OWASP/ATLAS/NIST and held-out human-value cases. | Claims should be measured across model, harness, tools, memory, and infrastructure. | Report false positives, false negatives, cost, latency, user effort, and safety hard gates. |
| 6 | Add isolated code/network execution and provider adapters. | This is infrastructure-heavy and should follow policy contracts. | Filesystem/network escape tests, resource exhaustion tests, credential absence, revocation. |

## What not to do

Do not claim that a prompt can solve prompt injection, that a stronger model automatically solves coordination, that a sandbox without network controls is sufficient, or that a benchmark score proves general safety. Do not grant a self-improving skill permission to promote itself. Do not add giant skill bundles by default; route the smallest sufficient set and measure whether each addition improves the outcome.

## Sources

[1]: https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/ "OWASP — Top 10 for Agentic Applications announcement"
[2]: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf "NIST AI 600-1 — Generative AI Profile"
[3]: https://atlas.mitre.org/ "MITRE ATLAS"
[4]: https://www.anthropic.com/news/prompt-injection-defenses "Anthropic — Mitigating the risk of prompt injections in browser use"
[5]: https://www.anthropic.com/engineering/claude-code-sandboxing "Anthropic — Making Claude Code more secure and autonomous"
[6]: https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents "Microsoft — Least privilege for AI agents"
[7]: https://www.anthropic.com/research/agentic-misalignment "Anthropic — Agentic misalignment"
[8]: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing "UK AI Security Institute — Incident report: unsanctioned agent behaviour during cyber testing"
[9]: https://unit42.paloaltonetworks.com/agentic-ai-threats/ "Unit 42 — AI Agents Are Here. So Are the Threats"
