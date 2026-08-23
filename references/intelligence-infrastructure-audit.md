# Intelligence infrastructure audit

**Audit date:** 2026-08-23  
**Repository:** `joymengistu/Ai-skills`  
**Audit scope:** repository structure, executable runtime, schemas, evaluation assets, existing Skills, research records, governance controls, and release validation.

## Executive conclusion

The repository already contains a substantial **capability-engineering layer**: 60 modular Skills, a self-directing core prompt, typed skill and capability contracts, a reference host with risk controls and hash-linked traces, evidence and feedback guidance, composition rules, contextual-user-intelligence, Lovability, Fable public-evidence research, and comparative benchmark plans.

The principal weakness is not a shortage of Skills. It is the gap between **described operating principles** and **machine-checkable intelligence records and paired experiment tooling**. The highest-value next step is therefore a small, provider-agnostic intelligence kernel: schemas for claims, lessons, examples, improvement proposals, benchmark runs, and intent/communication predictions; deterministic validation; and a paired baseline-versus-candidate harness that refuses promotion when hard gates fail or evidence is insufficient.

## Inventory

| Area | Observed state | Audit status |
|---|---|---|
| Skill catalog | 60 Skills with frontmatter and a 500-line size gate | FACT: present and validated |
| Core behavior | Layered self-directing prompt, operating contract, execution loop, action protocol, Ultra modes | FACT: present; runtime enforcement is partial |
| Skill contract | JSON Schema and populated example with procedure, permissions, verification, evaluation, lifecycle, examples, limitations, uncertainty, lessons, and version history | FACT: present and validated |
| Runtime control | Reference host with trust envelopes, action intent, bound approvals, cancellation, typed tool checks, journaling, incident records, and unit tests | FACT: present; deliberately reference-only |
| Research memory | Evidence-ledger Skill and Fable-specific YAML evidence ledger with source references and claim statuses | FACT: present; generic machine schema is incomplete |
| Lesson memory | Human-feedback, self-improvement, repair-loop, and skill-forging guidance | FACT: present as prose; durable record schema is incomplete |
| Example/counterexample reasoning | Skill-contract example taxonomy and evaluation cases | FACT: present; extraction/coverage checks are incomplete |
| User intent prediction | Contextual-user-intelligence Skill and architecture reference | FACT: present as governed guidance; typed record schema is incomplete |
| Communication/Lovability | Lovability Skill, architecture, communication additions, and benchmark plan | FACT: present as governed guidance; typed trial records are incomplete |
| Fable behavioral research | Public-source research notes, evidence ledger, capability analysis, and runtime blueprint | FACT: present at public-evidence boundary |
| Benchmark suite | 76 JSONL cases, comparative benchmark plan, Lovability benchmark plan, and deterministic case validator | FACT: present; no generic paired-run result schema/harness |
| Release checks | Repository validator, per-Skill quick validation, reference-host unit tests, mirror sync, archive workflow | FACT: present; no automated promotion gate across arbitrary candidate versions |
| Composition | Skill-composition Skill with typed ports, order, permissions, evidence flow, and recovery rules | FACT: present as procedure; no executable compatibility checker |

## Evidence vocabulary

| Label | Meaning in this audit |
|---|---|
| **FACT** | Directly observed in repository files or a cited public source. |
| **EVIDENCE** | An artifact, test, source passage, or measured result that supports a claim; evidence is not itself a universal conclusion. |
| **INFERENCE** | A reasoned conclusion derived from observed artifacts and evidence. |
| **HYPOTHESIS** | A testable proposal about what will improve an agent or repository. |
| **UNKNOWN** | A question not established by current artifacts, public sources, or executed experiments. |

## Gap matrix

| Requested system | Existing coverage | Genuine gap | Minimal implementation target |
|---|---|---|---|
| Skill Evaluator | Evaluation Skill, evaluator-critic, dynamic verification, case validator | No normalized evaluation result record or hard-gate aggregation | `evaluation-record.schema.json` plus deterministic result validator |
| Skill Improvement Engine | Self-improvement, repair-loop, skill-forging, lifecycle fields | No normalized candidate/proposal record linking baseline, change, regressions, and approval | `improvement-record.schema.json` plus promotion decision logic |
| Research Memory | Evidence-ledger Skill and Fable ledger | No generic append-only claim record with expiry/conflict/dependency fields | `research-memory.schema.json` and example records |
| Lesson Memory | Human feedback and self-improvement guidance | No structured failure-to-lesson record | `lesson-memory.schema.json` and example records |
| Example/Counterexample Engine | Skill contract examples and eval cases | No validator for required example kinds or counterexample coverage | `example-record.schema.json` plus suite coverage checker |
| User Intent Prediction | Contextual architecture and Skill | No typed prediction record with alternatives, scope, expiry, correction | `intent-prediction.schema.json` and calibration cases |
| Communication/Lovability Engine | Lovability Skill and plan | No structured communication trial record or deterministic anti-manipulation checks | `communication-trial.schema.json` plus benchmark cases |
| Fable Behavioral Research | Public research package and evidence ledger | No reusable framework for classifying observed behavior across model/harness/tools/memory/unknowns | `behavior-observation.schema.json` plus research protocol |
| Benchmark Suite | JSONL cases and comparative plans | No canonical run manifest, paired comparison, or regression report | `benchmark-run.schema.json`, manifest, and deterministic comparator |

## Non-duplicative design decision

Do not create one new Skill for each row. Most requested systems are **runtime records, validators, and evaluation protocols**, not instructions that should consume model context on every task. Existing Skills remain the human-readable operating layer; the new kernel will make their claims inspectable and comparable.

## Public-source boundary

Public agent guidance distinguishes predefined workflows from agents that dynamically direct process and tools, recommends starting with the simplest effective architecture, and describes prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer patterns [1]. Public evaluation guidance distinguishes tasks, trials, graders, transcripts/trajectories, outcomes, evaluation harnesses, agent harnesses, and suites; it recommends combining code-based, model-based, and human graders and evaluating multi-turn trajectories as well as final state [2].

These sources provide **EVIDENCE about publicly described patterns**, not proof that any particular Fable-like workflow is universally better. The exact hidden implementation, prompt, model mixture, and production outcomes for proprietary systems remain **UNKNOWN**. The repository must preserve this distinction.

## Release stop conditions

Do not claim continuous self-improvement until the repository has a durable record format, paired baseline/candidate runs, held-out cases, hard safety/control gates, regression inspection, human authorization for authority/privacy/safety changes, and reproducible artifacts. Until then, describe the system as a **governed design and reference implementation**, not an autonomous production optimizer.

## References

1. [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
2. [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
