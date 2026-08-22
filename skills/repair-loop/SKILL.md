---
name: repair-loop
description: Repair incomplete or failing agent-built artifacts through observed reproduction, root-cause classification, minimal patches, focused reruns, regression tests, and safe escalation. Use after build failures, broken interactions, missing requirements, tool errors, or verification failures.
---

# Repair loop

Repair from evidence, not from guesswork. Observe the failure in the running artifact, trace, test, or user report; preserve the original state; and classify the cause as requirement, architecture, context, implementation, dependency, tool, environment, permission, or verification.

Reproduce with the smallest useful test. Patch the smallest cause that explains the failure. Rerun the focused test, the affected requirement checks, and the relevant regression suite. Update the trace, requirement ledger, evidence, and incident record when the failure is material.

Do not hide missing requirements by weakening tests. Do not repeatedly retry a side effect whose outcome is uncertain; reconcile it through the durable action protocol first. Escalate when repairs reveal a wrong architecture, missing host capability, unsafe permission, or repeated non-convergence.

A repair is complete only when the original failure is gone, related behavior still works, the requirement is verified, and the user-facing status is honest.
