---
name: requirement-traceability
description: Convert a natural-language brief into a durable trace from requirement to interpretation, artifact, test, evidence, and delivery status. Use for complex builds, multi-step research, product work, or any task where important details may be silently omitted.
---

# Requirement traceability

Create a ledger with one row per explicit requirement and one row per necessary inferred requirement. Record: ID, requirement, source phrase, priority, confidence, dependencies, risk, implementation artifact, verification method, evidence, status, and owner.

Use statuses `captured`, `clarifying`, `planned`, `implemented`, `verified`, `partial`, `deferred`, `blocked`, or `rejected_with_reason`. Preserve the distinction between the user's words and the agent's interpretation.

Build from the highest-value vertical slice first. At every checkpoint compare the current plan and artifact with the ledger. Before delivery, run a coverage pass, identify unimplemented or weakly verified items, and report them plainly. A requirement with no artifact or test is not complete; a test with no link to a user requirement is a candidate for unnecessary work.

Keep the ledger concise enough to maintain. Store detailed evidence in linked artifacts, traces, screenshots, logs, or test results rather than bloating the plan.
