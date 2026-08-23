# Intelligence infrastructure architecture

## Purpose

The repository’s intelligence layer turns high-level capability guidance into **inspectable records and conservative experiments**. It does not attempt to make a model autonomously rewrite its own authority, safety policy, or permissions.

## Layered architecture

| Layer | Responsibility | Canonical artifact |
|---|---|---|
| Observation | Capture task, trace, environment state, user correction, or public behavior | `runtime/trace-schema.json`, `behavior-observation.schema.json` |
| Evidence | Preserve source, artifact, authority, freshness, counterevidence, scope, and uncertainty | `research-memory.schema.json` |
| Quality model | State what good and bad look like across contexts | `example-record.schema.json`, `runtime/skill-contract.schema.json` |
| Evaluation | Grade outcome and trajectory with code, model, or human evidence | `evaluation-record.schema.json` |
| Lesson | Convert a failure into a conditional, testable lesson | `lesson-memory.schema.json` |
| Intent and communication | Record bounded predictions and human-facing trial dimensions | `intent-prediction.schema.json`, `communication-trial.schema.json` |
| Improvement | Propose the smallest change, pair it with a baseline, and record regressions and rollback | `improvement-record.schema.json` |
| Benchmark | Define cases, arms, held-out separation, metrics, and hard gates | `benchmark-run.schema.json`, `evals/intelligence-benchmark.json` |
| Decision | Apply conservative promotion logic and authorized release | `runtime/intelligence/kernel.py`, governance controls |

## Governed learning loop

`observe → preserve evidence → classify status → evaluate outcome and trajectory → identify cause → write conditional lesson → propose smallest candidate → run matched baseline/candidate and held-out trials → inspect hard gates and regressions → obtain authorized decision → append provenance → review or expire memory`.

A memory record can inform a later decision but cannot override fresh user instructions, safety policy, authorization, or stronger evidence. A prediction can shape a draft or clarification but cannot authorize a side effect. A model grader can provide evidence but cannot become the release authority.

## Minimum comparison contract

A baseline/candidate comparison must identify the same model policy, tool policy, budget, environment, case suite, and grader definitions. It must preserve a held-out set, record failure examples, and report outcome and trajectory separately. The deterministic kernel returns:

| Condition | Decision |
|---|---|
| Missing paired metrics | `hold` |
| Any failed safety, privacy, authority, or recoverability gate | `reject` |
| Any metric regression beyond tolerance | `reject` |
| No measurable improvement | `hold` |
| Improvement with no regression and all gates passing | `promote` pending authorized release |

This is a **decision aid**, not a claim that statistical significance, human judgment, or task-specific validity can be automated away.

## Example and counterexample policy

For each important principle, include a positive example, negative example, borderline case, exception, and transformation. Each record states the situation, response, reason, and observable consequence. The purpose is not to make the prompt longer; it is to expose where a rule applies, where it fails, and how a bad response becomes a better one.

## Fable behavioral research boundary

Fable-inspired research is limited to public, observable behavior and public descriptions. The behavior-observation record separates model, prompt/Skill, harness, tools, memory, environment, human, and unknown layers, and requires alternative explanations and a reproduction plan. The exact hidden prompt, model mixture, internal evaluator, and proprietary mechanism remain **UNKNOWN** unless independently and lawfully established.

Public guidance describes both predefined workflows and dynamic agents, recommends starting with the simplest effective architecture, and presents evaluator-optimizer loops as one pattern among several [1]. Public evaluation guidance separates tasks, trials, graders, trajectories, outcomes, harnesses, and suites, and recommends code-based, model-based, and human grading [2]. These are design evidence, not proof of universal superiority.

## Deployment boundary

The repository currently provides a dependency-light reference kernel and schemas. It does not provide a production database, multi-tenant identity service, OS-level sandbox, network egress enforcement, live monitoring, real model adapter, or human-subject study. A hosted implementation must add those controls while preserving these records and gates.

## References

1. [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
2. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
