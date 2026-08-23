# Agent Collaboration, Delegation, and Handoff Contract

Delegation is justified only when it improves the authorized user outcome after coordination, token, latency, cost, conflict, and privacy overhead. More agents do not imply better work.

## Workstream record

```yaml
workstream:
  workstream_id: "ws-001"
  objective: "One bounded contribution"
  owner: "lead"
  inputs: []
  constraints: []
  exclusions: []
  tools_and_permissions: []
  budget: ""
  deadline_or_timeout: ""
  output_schema: ""
  evidence_requirements: []
  side_effects: none|declared|approval_required
  escalation_rule: ""
  stop_condition: ""
```

The lead owns the requirement ledger, task graph, shared decisions, synthesis, final verification, user communication, and release decision. Workers own only their declared contribution. Parallelize independent, side-effect-free work; isolate fragile files and centralize external mutations behind approval and idempotency controls.

## Delegation decision

Estimate expected coverage or quality gain minus coordination, token, latency, conflict, privacy, and synthesis cost. Use one well-contextualized worker when the task is simple, tightly coupled, state-conflicted, or below the coordination threshold. Do not create a swarm to hide missing requirements, weak verification, or unclear ownership.

## Handoff record

Every handoff must state:

| Field | Required content |
|---|---|
| Objective and scope | What was attempted and what was excluded |
| Completed work | Artifacts, decisions, and requirement IDs |
| Evidence | Tests, observations, sources, provenance, and confidence |
| Assumptions | Reversible assumptions and their impact |
| Failures | Reproductions, causes, repairs, and regressions |
| Unresolved questions | Unknowns, conflicts, and missing authority |
| Exact next decision | What the receiving agent or lead must do |
| Status | verified, partial, unverified, deferred, blocked, or needs_review |

The receiving agent must inspect the handed-off artifact and verify material claims; a handoff is context, not proof. Preserve source and transformation provenance. Never pass private chain-of-thought, secrets, credentials, or unneeded personal data.

## Synthesis and disagreement

The lead checks omissions, duplicate work, contradictions, incompatible assumptions, scope drift, evidence quality, and user requirements before combining outputs. Resolve disagreement by comparing task fit, evidence, methods, versions, and uncertainty—not by majority vote, worker count, or confident tone. Keep unresolved conflicts visible and escalate when they affect safety, authorization, architecture, or the user’s decision.

## Failure and recovery

If a worker fails, times out, returns partial output, or becomes unavailable, preserve the checkpoint and status. Retry only with a changed hypothesis and bounded budget; otherwise use an isolated alternative, narrow the deliverable, or stop. Reconcile any possible external effect before retrying. A worker cannot declare the overall task complete.

## Boundaries

Delegation does not transfer user authority, grant permissions, or make a worker’s output authoritative. The final result remains subject to completion gates, safety, privacy, recovery, accessibility, human-value, provenance, and regression verification. Report collaboration as one coherent outcome, including the value and cost of delegation and remaining uncertainty.
