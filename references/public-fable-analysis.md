# Public Fable capability analysis

## Scope

This is a public-information analysis, not a reconstruction of hidden system prompts. The repository does not include leaked, stolen, confidential, or access-controlled prompts, hidden chain-of-thought, or proprietary implementation details.

The user's reference to **Fable 3** could not be verified as a current public Anthropic model in the official materials reviewed. The official materials reviewed describe **Claude Fable 5** and **Claude Mythos 5**, plus earlier Claude model generations. Therefore, this document does not invent a Fable 3 specification. If the user means a different product named Fable, the product URL or vendor should be supplied before making a comparison.

## What public Fable 5 material emphasizes

Anthropic's public product page positions Claude Fable 5 for ambitious, long-running projects and describes it as thorough, proactive, and able to test its own work. It highlights multi-stage knowledge work with minimal oversight, document and visual understanding, vision-assisted evaluation of coding work, and safeguards with fallback in sensitive domains.[1]

Anthropic's public model documentation describes Fable 5 as built for demanding reasoning and long-horizon agentic work. It documents refusal responses, fallback handling, a 1M-token context window, adaptive effort, memory, tools, context editing, compaction, vision, and integration considerations for long-running work.[2]

Anthropic's public prompting guidance describes strengths in long-horizon autonomy, complex first-shot correctness, vision, enterprise workflows, code review and debugging, ambiguity navigation, and delegation/collaboration. It also recommends user-facing progress for long turns, asynchronous handling where appropriate, avoiding redundant re-derivation, keeping changes simple and within scope, and leading with the outcome.[3]

Anthropic's public announcement describes safety classifiers and fallback behavior for some high-risk domains, along with red-teaming and the possibility of false positives. This is a reminder that capability and governance must be designed together.[4]

## Original design lessons for Ai skills

| Public capability theme | Original Ultra Plan response |
|---|---|
| Long-horizon autonomy | Checkpointed execution, resumable state, budgets, stop rules, and progress updates |
| Complex and ambiguous work | Outcome framing, unknowns ledger, dependency graph, and adaptive depth |
| Self-testing | Independent acceptance tests, artifact inspection, and evidence ledger |
| Vision and document work | Context map that names files, diagrams, tables, screenshots, and provenance |
| Delegation and collaboration | Structured workstream contracts, side-effect-free parallelism, and recombination verification |
| High effort | Explicit effort/time/tool/cost budgets instead of indiscriminate overplanning |
| Safety classifiers and fallback | Risk preflight, refusal-safe alternatives, human escalation, and no authority escalation |
| Strong instruction following | Short outcome-first user updates, scope lock, and no unnecessary refactoring |

## How Ultra Plan Mode goes further

Ultra Plan Mode is not “a bigger prompt.” It is a control system around a model. It adds a preflight record, dependency graph, context and assumption ledgers, risk classes, permission boundaries, resource budgets, resumable checkpoints, evidence-grounded iteration, independent verification, and a post-task evaluation. These controls improve the host agent even when the underlying model changes.

Its central improvement is **adaptive depth**. Focused mode is direct. Deep mode adds decomposition and verification. Ultra mode adds full preflight and resumability only when the expected value justifies the cost. This addresses a common failure mode of powerful agents: spending effort on exhaustive planning, redundant explanation, or hypothetical abstractions instead of acting once enough information exists.

## Evaluation plan

Do not compare agents with a single headline score. Build a held-out suite covering long-horizon completion, ambiguity, context overload, tool errors, prompt injection, refusal/fallback behavior, delegation, document/vision tasks, and human satisfaction. Measure outcome quality, factuality, verification quality, unnecessary work, latency, token/tool cost, safety violations, approval correctness, recovery quality, and user effort.

A valid claim is conditional: “Ultra Plan Mode improved performance on this defined task suite under these budgets and safety constraints.” A universal claim that it makes any model better than Fable 5 is not justified without controlled evidence.

## References

[1]: https://www.anthropic.com/claude/fable "Anthropic — Claude Fable"

[2]: https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 "Anthropic — Introducing Claude Fable 5 and Claude Mythos 5"

[3]: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 "Anthropic — Prompting Claude Fable 5"

[4]: https://www.anthropic.com/news/claude-fable-5-mythos-5 "Anthropic — Claude Fable 5 and Claude Mythos 5"
