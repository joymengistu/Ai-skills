# Capability-risk matrix

A capability is not ready because it is impressive. It is ready when the user outcome, reliability, safety, control, and recovery evidence meet the required bar.

## Risk classes

| Class | Examples | Default control |
|---|---|---|
| Read-only | Search, inspect, summarize, calculate | Scope and provenance checks |
| Reversible | Draft, local edit with rollback, sandbox experiment | Preview, bounded permission, verification |
| Consequential | Send, publish, modify shared state, schedule, change access | Explicit approval, audit, post-action verification |
| Irreversible | Delete, transfer funds, deploy to production, disclose sensitive data | Explicit approval, independent review, rollback or recovery plan |
| Unknown | Unclear target, authority, or side effect | Pause and clarify; fail closed |

## Release gate

Score each dimension from 0 to 4 and record evidence:

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| User outcome | No demonstrated value | Useful in narrow cases | Clear, repeated outcome improvement |
| Reliability | Unmeasured or unstable | Mixed held-out results | Repeated acceptable performance |
| Safety | Unbounded or bypassable | Partial controls | Threat model, least privilege, fail-closed controls |
| Privacy | Unclear collection or retention | Documented but incomplete | Minimization, access, retention, deletion, redaction |
| Human control | Hidden or surprising autonomy | Some approvals | Clear scope, approvals, cancellation, undo, escalation |
| Recoverability | Lost or duplicated side effects | Manual recovery | Durable state, idempotency, reconciliation, tested recovery |
| Observability | No trace | Partial logs | Structured trace, evidence, decisions, and outcomes |
| Human value | Adds friction or confusion | Helpful with tradeoffs | Measured effort, clarity, trust, agency, and completion gains |
| Maintainability | Prompt-only behavior | Some documentation | Versioned contract, tests, owner, rollback |

## Decision rule

For low-risk features, a weighted score can prioritize investment. For consequential or irreversible features, safety, privacy, human control, and recoverability are hard gates: a high capability score cannot compensate for a failed critical dimension.

## Required release evidence

Attach a user outcome statement, acceptance tests, representative and adversarial cases, trace samples, threat model, permissions, approval behavior, recovery test, known limitations, human-value measurement plan, version identifiers, and rollback instructions. Re-run the held-out regression suite after every change to prompts, tools, routing, memory policy, or permissions.
