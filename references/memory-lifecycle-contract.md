# Memory Lifecycle and Forgetting Contract

Use this contract to manage research records, lessons, user preferences, project facts, conversation state, and execution checkpoints without creating an uncontrolled memory dump. Memory is scoped evidence, not authority.

## Memory classes

| Class | Purpose | Default scope | Default retention |
|---|---|---|---|
| **Conversation state** | Current objective, decisions, terminology, corrections, unresolved questions | Current conversation/task | Until task ends or context is compacted into a handoff |
| **Project memory** | Project requirements, decisions, artifacts, technical constraints, validated lessons | Named project/workspace | Until project deletion, supersession, or review expiry |
| **Research memory** | Source-grounded claims, evidence spans, provenance, contradictions, implications | Claim/topic/domain | Until outdated, contradicted, withdrawn, or review-triggered; preserve history |
| **Lesson memory** | Conditional, testable learning from failures, feedback, and experiments | Skill/workflow/task class | Provisional until replicated; expire or demote after failed replication or staleness |
| **User preference** | Explicit collaboration choices such as format, tone, accessibility, or workflow style | User and stated scope | Only with appropriate consent; easy review, correction, and deletion |
| **Execution checkpoint** | Resumable objective, requirements, active step, artifacts, approvals, tool results, errors, and next action | Run ID | Until run completion plus configured recovery window |

Do not merge these classes merely because they use similar fields. Temporary conversation state must not silently become a personal preference, and a research claim must not silently become a universal lesson.

## Memory record

```yaml
memory_record:
  memory_id: "memory-001"
  class: conversation|project|research|lesson|user_preference|checkpoint
  content: "Compact record, not an unbounded transcript"
  purpose: "Why retaining this helps"
  source_refs: []
  provenance_refs: []
  scope: "conversation/task/project/user/topic"
  sensitivity: public|internal|personal|sensitive|restricted
  consent: explicit|implicit_contextual|not_required|unknown|withdrawn
  confidence: low|medium|high
  status: provisional|active|superseded|outdated|contradicted|withdrawn|deleted
  created_at: "..."
  updated_at: "..."
  expires_at: "..."
  review_trigger: "event, date, version, correction, or user request"
  correction_path: "How to amend it"
  deletion_path: "How to remove it"
  promotion_evidence: []
  related_memory_ids: []
  retrieval_note: "Why this item was retrieved"
```

## Lifecycle

1. **Capture:** Store only a compact item with purpose, source, scope, sensitivity, consent state, and expiry/review rule.
2. **Qualify:** Label the item provisional, supported, active, or another explicit status. Record evidence and confidence; do not promote a fluent inference.
3. **Retrieve:** Retrieve the smallest relevant set. Show meaningful memory use when it could surprise the user. Keep memory clearly labeled and subordinate to the current request, safety policy, fresh evidence, and explicit correction.
4. **Apply:** Use memory to inform a draft, question, or route. Memory cannot authorize external effects, change permissions, or override current instructions.
5. **Review:** Recheck freshness, scope, contradictions, and whether the item still serves its purpose. Trigger review on user correction, source change, project change, expiry, or repeated prediction failure.
6. **Correct or supersede:** Preserve history where auditability matters, mark the old item superseded/outdated/contradicted, and create a replacement with new evidence. Do not silently rewrite the past.
7. **Forget or delete:** Remove or anonymize items when the user asks, consent is withdrawn, retention expires, the item is no longer useful, or the item is unsafe to retain. Record only the minimum deletion event needed for audit.

## Lesson promotion

A lesson should follow:

> **observation → failure or success → cause hypothesis → intervention → paired evaluation → held-out check → conditional lesson → authorized promotion**

A lesson is not truth merely because it occurred once or appears in memory. Keep it conditional: “When context C and objective O are active, response Y may help; preserve alternative Z.” Demote a lesson when evidence conflicts, the environment changes, or it causes regressions.

## Forgetting policy

Forget aggressively when information is low-value, sensitive without clear consent, speculative about a person, stale beyond its claim class, superseded, duplicated, or unrelated to the current task. Preserve provenance metadata for important deleted or withdrawn records without retaining the deleted content unless required by an authorized policy. Never store secrets or credentials as memory.

## Retrieval safeguards

Before retrieval, check purpose, scope, freshness, sensitivity, consent, and whether the memory can surprise the user. If a memory conflicts with a fresh explicit instruction, use the instruction and update only the relevant scope. If memory is uncertain or consequential, ask or present it as a tentative possibility. Do not infer sensitive traits, diagnose psychology, or use memory to pressure engagement.

## Quality checks

Measure retrieval relevance, stale-memory rate, correction responsiveness, false personalization, user effort, unnecessary interruption, lesson replication, deletion compliance, and regression rate. Optimize usefulness and controllability, not memory volume or conversation length.

## Boundaries

This is a lifecycle and governance contract, not a promise that a host retains, deletes, or exposes memory in a particular way. Runtime storage, access control, encryption, retention, and deletion must be enforced by the host environment. A prompt cannot guarantee deletion from provider logs or external systems.
