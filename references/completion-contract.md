# Outcome Completion Contract

Use this contract before declaring a task complete. Completion is a claim about a real outcome, not about producing text, code, a plausible screenshot, or a successful intermediate command.

## Required completion record

```yaml
completion_record:
  objective: "The user’s real-world outcome"
  definition_of_done: []
  requirement_coverage:
    - requirement_id: "R-001"
      status: captured|planned|implemented|verified|partial|deferred|blocked|rejected_with_reason
      artifact: "Path, URL, output, or trace"
      verification: "Observable check"
      evidence: []
  gates:
    outcome: pass|fail|unknown
    acceptance: pass|fail|unknown
    evidence: pass|fail|unknown
    quality: pass|fail|unknown
    safety: pass|fail|unknown
    recovery: pass|fail|unknown
    human_value: pass|fail|unknown
  status: complete|complete_with_caveats|needs_review|blocked|not_started
  unresolved_questions: []
  next_step: "Useful follow-up or explicit stop"
```

## Completion gates

All gates are separate. Passing one does not imply passing the others.

| Gate | Question | Passing evidence |
|---|---|---|
| **Outcome** | Did the real-world goal happen? | The intended artifact, decision support, or action exists in the expected environment |
| **Acceptance** | Are all must-have criteria satisfied? | Requirement ledger shows every must-have as verified or clearly qualified |
| **Evidence** | What proves the claim? | Artifact, test, trace, source, screenshot, user confirmation, or other scoped evidence |
| **Quality** | Is the result correct, complete enough, clear, and fit for use? | Task-specific checks and independent critique where appropriate |
| **Safety** | Were privacy, permission, approval, and authority boundaries respected? | Host controls, approval record, risk checks, and no unauthorized side effect |
| **Recovery** | Can the user correct, undo, resume, or recover? | Recovery path, checkpoint, rollback, or clear limitation |
| **Human value** | Did the work reduce unnecessary effort and preserve trust, control, accessibility, and dignity? | Human-centered checks or user feedback appropriate to the task |

## Status policy

- `complete`: all critical gates pass and evidence supports the claim.
- `complete_with_caveats`: the intended outcome is usable, but non-critical limitations or untested states remain explicitly reported.
- `needs_review`: a human or domain expert must decide whether quality, safety, taste, or interpretation is acceptable.
- `blocked`: a required input, permission, tool, environment, or evidence condition is missing.
- `not_started`: no meaningful implementation or evidence exists.

Never use “done” as a substitute for these statuses. Do not silently turn `unknown`, `partial`, or `blocked` into `complete`.

## Stopping rules

Stop and report when any of the following is true: critical acceptance criteria pass; the authorized budget ends; evidence is insufficient; risk rises; a required permission is missing; the task is blocked; the user must choose between material alternatives; recovery is uncertain; or added work has lower expected value than asking the user or delivering a qualified result.

A stopping rule is not a reason to conceal a defect. It must state what passed, what did not, what remains unknown, and what would restart or resolve the work.

## Evidence and scope

Link each claim to evidence with source, timestamp or freshness where relevant, environment, method, confidence, and scope. A screenshot can support visible appearance but not hidden interaction or accessibility. A successful build can support compilation but not product completeness. A research source can support a claim within its stated scope but not universal truth. A user statement can confirm preference or satisfaction for that user and context but not a general law.

## Minimal completion report

```text
Outcome: ...
Status: complete | complete_with_caveats | needs_review | blocked | not_started
Acceptance: ...
Evidence: ...
Quality and human value: ...
Safety and recovery: ...
Unresolved: ...
Next step: ...
```

For long work, also report the route, artifacts changed, tests run, failures repaired, regressions checked, approvals obtained, and rollback or continuation path.
