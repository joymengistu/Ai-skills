# Tool Selection, Capability Matching, and Fallback Contract

A tool call is successful only when it advances the authorized user outcome and its actual result is verified. Availability, a successful transport response, or a plausible output does not prove suitability or completion.

## Capability-fit record

Before selecting a tool, record:

```yaml
tool_decision:
  objective: ""
  required_capabilities: []
  candidate_tools: []
  selected_tool: ""
  fit_evidence: []
  model_contribution: ""
  host_or_runtime_requirements: []
  data_or_state_requirements: []
  permission_and_side_effects: []
  privacy_and_cost: ""
  expected_evidence: []
  fallback_order: []
  stop_condition: ""
```

Choose the smallest sufficient tool or tool sequence. Prefer clear schemas, bounded scope, stable outputs, useful errors, low unnecessary latency/cost, least privilege, and direct evidence. Separate what depends on the model, harness, tool, state, data, and evaluator. Do not treat a catalog description or vendor claim as proof of capability.

## Selection procedure

1. Translate the outcome into required capabilities and acceptance evidence. Distinguish read, transform, generate, execute, verify, and report needs.
2. Enumerate viable candidates and reject tools that lack a required capability, exceed authorization, expose unnecessary data, create disproportionate cost, or have no trustworthy verification path.
3. Prefer one sufficient tool over redundant calls. Use a sequence only when each handoff has a defined input, output, provenance, and failure behavior.
4. Validate arguments, identity, destination, scope, freshness, format, and permissions before execution. Approval requirements remain governed by the tool-action boundary contract.
5. After execution, inspect the actual result, completeness, evidence, side effects, and error state. Record partial output rather than converting it to success.
6. On failure, classify the error as capability mismatch, invalid input, permission, unavailable dependency, timeout, rate limit, stale state, tool defect, environment failure, or verification failure. Change the smallest relevant variable and avoid blind retries.

## Fallback ladder

Use this order unless risk or task requirements require stopping earlier:

1. Repair the input or clarify one material ambiguity.
2. Retry only an idempotent, bounded operation with a changed hypothesis.
3. Use a validated alternative tool with equivalent scope and evidence.
4. Degrade gracefully to a narrower deliverable and disclose the missing capability.
5. Ask the user for a file, permission, decision, or external action only when necessary.
6. Stop as `blocked`, `needs_review`, or `complete_with_caveats` when safe completion is not possible.

Never use a fallback to bypass authorization, hide a failed gate, expand scope silently, or claim equivalent evidence when the alternative establishes less. If an external side effect may have occurred but outcome is uncertain, reconcile state before retrying.

## Evaluation and reporting

Measure end-to-end requirement coverage, correct tool choice, argument validity, latency, cost, privacy exposure, user effort, error recovery, repair convergence, side effects, and evidence quality. Test happy paths, malformed arguments, stale state, permission denial, unavailable tools, partial results, timeouts, and idempotent retry. Report selected tool and why, actual result, checks run, fallback or degradation, remaining unknowns, and next safe action.

## Boundaries

Tool selection cannot grant permissions, create missing host capabilities, guarantee third-party availability, or prove model superiority. A returned status code is transport evidence only. Host enforcement remains authoritative for credentials, approvals, isolation, rate limits, and external state.
