# Ultra Planning Contract Reference

## Planning node schema

| Field | Meaning |
|---|---|
| `id` | Stable, human-readable node ID. |
| `objective` | Observable result this node is meant to produce. |
| `depends_on` | Required predecessor nodes or environment facts. |
| `inputs` | Data, artifacts, decisions, or access required. |
| `outputs` | Artifact, state change, or evidence expected. |
| `action_class` | Read-only, internal mutation, external/consequential, or denied. |
| `verification` | Concrete test, observation, evaluator, or human review. |
| `failure_path` | Repair, alternate route, pause, or stop rule. |
| `completion_evidence` | Proof required before marking complete. |

## Risk record

Use `impact × likelihood × detectability` qualitatively: low, medium, high, or unknown. Record the earliest signal, prevention, detection, recovery, owner, and approval/stop rule. Treat unknown as a reason to reduce scope or gather evidence—not as low risk.

## Decision record

Record the decision, alternatives considered, evidence, selected rationale, consequences, owner, reversibility, and revisit trigger. Do not preserve private reasoning; preserve decision-relevant evidence.

## Plan-quality gate

Approve a plan only if it has:

1. Full explicit-requirement coverage or visible defer/block reasons.
2. A proportionate depth budget and clear non-goals.
3. A chosen architecture justified against relevant alternatives.
4. Dependency-aware milestones with no unexamined critical path.
5. Authority and approval boundaries for consequential actions.
6. A verification matrix and evidence source for every important claim.
7. Recovery/stop behavior for high-risk, stateful, or long-running work.
8. A defined first action that can produce useful evidence.
