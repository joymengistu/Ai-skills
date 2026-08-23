# Hosted-first evaluation architecture research

**Research date:** 2026-08-23  
**Status:** Design synthesis; no real model-quality claim is made.

## Executive conclusion

The smallest credible hosted evaluation system is not a giant multi-agent workflow. It is a **thin evaluation control plane** that runs the same task cases against baseline, candidate, and optional ablation arms; captures normalized traces; verifies environment outcomes; applies code/model/human graders; protects held-out cases; and produces a signed, reviewable promotion record.

Public guidance supports separating traces used for debugging from repeatable datasets and evaluation runs [1]. Public evaluation concepts also distinguish datasets, experiments, runs, threads, evaluators, and offline versus online evaluation [2]. OpenTelemetry publicly describes interoperable GenAI telemetry fields for model identity, token use, finish reasons, and optional content capture [3]. NIST publicly frames trustworthy AI around risk management, measurement, monitoring, and governance responsibilities [4]. These sources support the architecture below, but they do not prove that a specific provider, model, or Fable-like workflow is universally superior.

## Minimal control-plane architecture

| Component | Responsibility | Required record |
|---|---|---|
| Case registry | Version tasks, expected properties, allowed alternatives, development/held-out split, and sensitive-data policy | `evals/intelligence-benchmark.json` plus case records |
| Arm launcher | Run baseline, candidate, and ablation with matched model, tools, budget, environment, and trial policy | `benchmark-run.schema.json` |
| Provider adapter | Translate provider-specific calls into normalized model, tool, handoff, guardrail, usage, timing, and error events while retaining safe extensions | Existing trace schema plus provider adapter contract; future implementation |
| Trace store | Persist a complete trajectory with redaction, retention, access control, and correlation IDs | `runtime/trace-schema.json`; OpenTelemetry-compatible fields are an interoperability option |
| Outcome verifier | Inspect actual environment state, artifacts, tests, or database facts rather than trusting final prose | `evaluation-record.schema.json` plus task-specific verifiers |
| Grader layer | Combine deterministic code checks, structured model judges, and blinded human review; preserve evidence snippets | `evaluation-record.schema.json` |
| Analysis layer | Compare paired arms, inspect distributions, costs, failure examples, hard gates, and attribution confidence | `benchmark-run.schema.json`; `kernel.py` |
| Promotion gate | Reject hard-gate failures and regressions; hold incomplete or unchanged results; require authorized release | `improvement-record.schema.json` and governance controls |
| Online monitor | Sample production runs and threads for drift, safety, latency, cost, user correction, and quality degradation without reference outputs | Future hosted service; `communication-trial.schema.json` and trace records |

## Run lifecycle

1. **Freeze the experiment definition.** Record suite version, task refs, held-out refs, model policy, tool policy, budget, environment, grader versions, privacy mode, and stopping rule.
2. **Launch matched arms.** Use the same cases and controls. Randomize trial order when appropriate to reduce time or order effects. Do not tune on held-out cases.
3. **Capture the trajectory.** Record model calls, tool calls, handoffs, guardrails, timings, token usage, errors, retries, approvals, and redacted content references. Content capture must be opt-in and scoped because raw prompts and tool results may be sensitive [3].
4. **Verify the outcome.** Check artifacts and environment state independently. A final claim such as “done” is not completion evidence.
5. **Grade multiple dimensions.** Use code graders for deterministic assertions, model graders for structured qualitative criteria with evidence snippets, and human review for taste, perceived understanding, agency, emotional appropriateness, and trust calibration [1] [2].
6. **Analyze paired differences.** Report task-level results, confidence, failure examples, cost, latency, human effort, safety/privacy/control gates, and distributional regressions. Attribute gains cautiously because model, Skill, prompt, tools, harness, evaluator, and environment may all contribute.
7. **Decide conservatively.** The candidate may be promoted only if hard gates pass, no material regression appears, the paired controls are valid, held-out evidence is acceptable, and an authorized release process approves it.
8. **Monitor after release.** Keep online evaluation separate from offline reference-based tests. Sample traces and threads, detect drift, record user corrections, and create lessons without silently rewriting production behavior [2].

## Provider-neutral trace envelope

The adapter should normalize only fields needed for cross-provider comparison:

| Field group | Examples | Privacy rule |
|---|---|---|
| Identity | run ID, trace ID, parent span, provider, model reference, Skill/prompt version | Keep tenant/user identifiers pseudonymous |
| Action | event type, tool name, destination class, approval reference, risk class | Never treat a trace as authorization |
| Timing and usage | start/end, latency, input/output tokens, retries, finish reason | Use for cost/latency analysis, not quality alone |
| State | input/output references, artifact hashes, environment version, outcome verifier result | Prefer hashes or redacted pointers for sensitive payloads |
| Quality | grader refs, scores, evidence refs, confidence, hard gates | Preserve grader identity and version |
| Provider extension | provider-specific fields required for diagnosis | Keep isolated and mark non-comparable fields |

This design follows a **common core plus explicit extensions** principle. It avoids pretending that provider traces are identical while still allowing common analysis.

## Measurement model

Do not compress the system into a single score. Use a release table with hard gates and tradeoffs:

| Dimension | Preferred measurement | Limitation |
|---|---|---|
| Outcome correctness | Code/artifact/environment verifier | Requires task-specific ground truth or valid alternative paths |
| Requirement coverage | Structured requirement assertions | A checklist can miss quality or user intent |
| Factuality/evidence | Citation or source verifier plus review | A citation can be present but irrelevant |
| Trajectory quality | Trace assertions, tool/approval/recovery checks | Requires a meaningful trace and policy model |
| Safety/privacy/control | Hard gates and incident review | Never average away a critical failure |
| Repair | Before/after defect and regression cases | Short tests can miss long-run maintenance problems |
| Communication | Structured dimensions and blinded human review | Human judgment is noisy and context-sensitive |
| Efficiency | Latency, tokens, cost, retries, user effort | Lower cost is not automatically better |
| Reliability | Multiple trials, confidence intervals when justified, failure distributions | Small samples should remain explicitly uncertain |

## How this changes Ai-skills

The existing repository already contains most of the conceptual contracts: traces, risk controls, evaluation records, benchmark manifest, contextual intent records, Lovability dimensions, evidence labels, lessons, improvement records, and conservative paired decisions. The next implementation should therefore be a **hosted adapter and experiment runner**, not another Skill.

### Staged roadmap

| Stage | Deliverable | Release gate |
|---|---|---|
| 0 | Offline schema and manifest validation | All records validate; no held-out overlap; tests pass |
| 1 | One hosted provider adapter with redacted normalized traces | Trace completeness, privacy review, deterministic replay metadata |
| 2 | Two-provider adapter comparison on read-only tasks | Same suite, budgets, graders, and outcome verifiers; report non-comparable fields |
| 3 | Baseline/candidate/ablation runs with repeated trials | Held-out separation, hard gates, failure examples, cost/latency report |
| 4 | Blinded human review for Lovability and quality judgment | Inter-rater process, agency and trust checks, no engagement optimization |
| 5 | Online sampling and drift/incident loop | Consent, retention, deletion, access controls, rollback and monitoring |

## Fable-inspired interpretation

Publicly observable Fable-like outcomes should be decomposed into model capability, prompt/Skill, harness, tools, memory, environment, evaluator, and human workflow. A successful one-shot build is an observation, not proof of a secret prompt or universal mechanism. The correct research action is to reproduce bounded public workflow patterns—requirement compilation, staged execution, environment feedback, evaluator-optimizer refinement, and targeted repair—under matched conditions and ablations.

## Evidence classification

| Label | Current conclusion |
|---|---|
| **FACT** | Public sources describe traces, graders, datasets, experiments, runs, threads, GenAI telemetry fields, and risk-management responsibilities [1] [2] [3] [4]. |
| **EVIDENCE** | The linked public documentation and the repository’s existing schemas, benchmark plans, and reference tests. |
| **INFERENCE** | A normalized trace envelope plus explicit provider extensions is the smallest practical interoperability boundary. |
| **HYPOTHESIS** | This architecture will make baseline-versus-candidate improvements easier to attribute and safer to promote than provider-specific ad hoc logs. |
| **UNKNOWN** | Real effect sizes, cross-provider comparability, human-value improvement, and whether Fable-like patterns transfer across models. |

## Next experiment

Implement one read-only hosted adapter that emits normalized traces and runs a small subset of the existing suite. Compare the baseline and candidate under identical model and tool budgets, use environment-grounded verifiers, redact content by default, and publish only structural and measured results. If the adapter cannot preserve enough information for diagnosis without violating privacy, revise the trace envelope before adding more providers or more Skills.

## References

1. [OpenAI — Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)
2. [LangSmith — Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts)
3. [OpenTelemetry — Inside the LLM Call: GenAI Observability](https://opentelemetry.io/blog/2026/genai-observability/)
4. [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
5. [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
6. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
