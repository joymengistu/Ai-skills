# Hosted evaluation research brief

**Date:** 2026-08-23

## Research question

What is the smallest hosted, provider-agnostic evaluation architecture that can run fair baseline-versus-candidate agent experiments while preserving matched model/tool/budget controls, complete traces, environment-grounded outcomes, held-out cases, hard safety gates, human review, reproducibility, and user privacy?

## Subquestions

1. Which public evaluation-harness components must be separated: task, trial, grader, trajectory, outcome, environment, model, harness, and release decision?
2. How should hosted adapters normalize different providers without hiding meaningful differences in model capabilities, tool behavior, latency, cost, or privacy?
3. What must be recorded to reproduce a run and attribute an improvement to a Skill, prompt, model, tool host, memory, evaluator, or environment?
4. Which metrics can be deterministic, which need model judges, and which require blinded human review?
5. How should held-out cases, repeated trials, ablations, hard gates, and regression analysis constrain promotion?
6. What practical architecture fits a modest client plus hosted workers without claiming free hosting, unlimited credits, or production security that does not exist?

## Evidence boundary

Every research note will classify statements as **FACT**, **EVIDENCE**, **INFERENCE**, **HYPOTHESIS**, or **UNKNOWN**. Public documentation can establish described interfaces and practices. It cannot establish universal superiority, hidden prompts, private implementation details, or an effect size without a measured experiment.

## Target decision

Produce a repository-ready research package that identifies:

- a minimal hosted evaluation architecture;
- a normalized run and trace contract;
- provider adapter requirements;
- benchmark execution and analysis rules;
- privacy, safety, and authorization boundaries;
- a staged implementation roadmap;
- unresolved questions and the next experiment.

## Stopping rule

Stop researching when at least three independent public sources cover evaluation design, hosted execution or tracing, and agent safety/privacy; their claims can be reconciled into implementation requirements; and remaining uncertainty is more efficiently resolved by running a controlled experiment than by collecting more general descriptions.

## Verified public evidence checkpoint

| Status | Finding | Source |
|---|---|---|
| FACT | OpenAI’s public agent-evals guidance separates trace grading for debugging from datasets and eval runs for repeatable comparisons. | [OpenAI — Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) |
| FACT | OpenAI describes a trace as the end-to-end record of model calls, tool calls, guardrails, and handoffs for one run. | [OpenAI — Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals) |
| FACT | LangSmith’s public evaluation concepts distinguish offline datasets/experiments from online runs/threads, and say experiments capture outputs, evaluator scores, and execution traces for each dataset example. | [LangSmith — Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts) |
| FACT | LangSmith describes a run as a single execution trace with inputs, outputs, intermediate child runs, and metadata; online evaluators may lack reference outputs and therefore use reference-free quality and safety checks. | [LangSmith — Evaluation concepts](https://docs.langchain.com/langsmith/evaluation-concepts) |
| INFERENCE | Ai-skills should support both offline repeatable benchmark arms and online production observation, while keeping reference-based and reference-free graders distinct. | Derived from the public documentation and repository evaluation rules. |
| HYPOTHESIS | A hosted adapter should emit a normalized trace envelope first, then attach evaluation records and benchmark-run records, rather than forcing provider-specific traces directly into the benchmark schema. | Testable architecture hypothesis. |
| UNKNOWN | Whether any provider’s trace representation can be losslessly normalized without discarding provider-specific behavior or exposing sensitive content. | Requires adapter prototypes and privacy review. |

## Interoperability and governance evidence checkpoint

| Status | Finding | Source |
|---|---|---|
| FACT | OpenTelemetry’s public GenAI observability guidance describes semantic conventions for model identity, token usage, finish reasons, and optionally structured prompts, messages, tool calls, and tool results. | [OpenTelemetry — Inside the LLM Call: GenAI Observability](https://opentelemetry.io/blog/2026/genai-observability/) |
| FACT | OpenTelemetry notes that captured prompt and tool content is valuable for debugging but can be large and sensitive, so content capture is an explicit configuration choice. | [OpenTelemetry — Inside the LLM Call: GenAI Observability](https://opentelemetry.io/blog/2026/genai-observability/) |
| FACT | NIST describes the AI Risk Management Framework as voluntary guidance for incorporating trustworthiness into the design, development, use, and evaluation of AI systems, with emphasis on risk management, measurement, monitoring, and governance responsibilities. | [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| INFERENCE | A hosted adapter should emit provider-neutral operational fields while retaining a provider-specific extension area, and should default to redacted content capture with explicit consent or debugging scope for sensitive payloads. | Derived from OpenTelemetry observability guidance and NIST governance principles. |
| HYPOTHESIS | Trace normalization plus configurable content redaction will improve cross-provider diagnosis while reducing privacy exposure compared with storing raw prompts and tool results by default. | Requires an adapter prototype and privacy red-team. |
| UNKNOWN | Which normalized fields are sufficient for attribution across providers, and when provider-specific fields materially change evaluation conclusions. | Requires matched adapter experiments. |
