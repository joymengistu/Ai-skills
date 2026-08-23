# Verification, Repair, Completion, and Reporting Contract

Use this contract to close the loop from user outcome to observable evidence. Completion is a status decision supported by gates, not a feeling produced by fluent output or a green build.

## Completion record

```yaml
completion_record:
  run_id: "run-001"
  objective: "Real-world user outcome"
  requirements: []
  gates:
    outcome: passed|partial|failed|unknown|not_run
    acceptance: passed|partial|failed|unknown|not_run
    evidence: passed|partial|failed|unknown|not_run
    quality: passed|partial|failed|unknown|not_run
    safety: passed|partial|failed|unknown|not_run
    recovery: passed|partial|failed|unknown|not_run
    human_value: passed|partial|failed|unknown|not_run
  status: complete|complete_with_caveats|needs_review|blocked|not_started|failed
  evidence_refs: []
  failed_checks: []
  repairs: []
  unresolved_unknowns: []
  omitted_checks: []
  stop_reason: acceptance|budget|insufficient_evidence|risk|blocked|diminishing_value|user_decision|cancelled
  restart_condition: "What would allow safe continuation"
```

## Verification loop

1. Translate each must-have requirement into an observable acceptance check.
2. Select the smallest reliable check for each requirement and record what it cannot establish.
3. Inspect the actual artifact, runtime, source, or external state rather than trusting generation intent.
4. If a check fails, reproduce it and classify the smallest cause: requirement, context, architecture, implementation, dependency, tool, environment, permission, or verification.
5. Patch only the smallest cause that explains the failure; preserve a before state and provenance.
6. Rerun the focused check, affected requirement checks, and relevant regression checks. Check for collateral regressions and changed scope.
7. Repeat only while expected improvement justifies cost and the authorized budget remains. Escalate when the architecture, host capability, permission, or user decision is the actual blocker.
8. Assign a completion status from gates and evidence. Report what passed, failed, was not run, was not assessable, or remains unknown.

## Status meanings

| Status | Meaning |
|---|---|
| **complete** | Outcome and must-have acceptance passed; required evidence, safety, recovery, and human-value gates are adequate |
| **complete_with_caveats** | Core outcome passed, but named limitations or non-critical checks remain |
| **needs_review** | A human or domain reviewer must inspect a material quality, safety, policy, or uncertainty issue |
| **blocked** | Missing input, permission, host capability, source, environment, or decision prevents safe completion |
| **failed** | The attempted outcome or a required gate did not pass |
| **not_started** | No meaningful execution or evidence yet |

Never use `complete` to hide unknowns, skipped checks, or critical failures.

## Repair convergence

Stop repairing when acceptance passes, the user’s objective is met, the budget ends, risk rises, a required permission or decision is missing, the same failure repeats without a new hypothesis, or further changes have diminishing value. Repeated attempts are not evidence of progress. Record the repair sequence, observed delta, regressions, and remaining uncertainty.

## Human reporting

Give the user a concise outcome, completed milestone, evidence, caveats, blockers, and next safe step. Preserve their agency when a tradeoff or decision remains. Do not expose private chain-of-thought or substitute a long process log for evidence. Invite targeted correction without making the user restart the work.

## Boundaries

Verification can establish only what was checked. It does not prove unseen states, universal performance, complete accessibility, semantic equivalence, future stability, or external success without corresponding evidence. Host policy, approvals, and runtime controls remain authoritative.
