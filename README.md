# Ai skills

**Ai skills** is a model-agnostic capability and governance layer for building AI agents that are more reliable, useful, safe, and satisfying to work with. It is not a magic prompt and it does not make an unsupported claim to universally outperform Claude, Fable, or any other model. Its purpose is to make improvement measurable on the tasks that matter to you.

> Better AI is not only a smarter answer. It is a better outcome: correct when correctness matters, grounded in evidence, efficient with attention and tools, safe under pressure, transparent about uncertainty, and genuinely easier for a person to use.

## What is included

The repository contains a self-directing core prompt, an operating contract, a bounded execution loop, an explicit action protocol, sixty-one modular skills, adapters for the user's Joy and CLAI repositories, a human-satisfaction framework, a security and governance layer, evaluation cases, and validation scripts.

| Area | Included capability |
|---|---|
| Reasoning and execution | Task framing, planning, orchestration, context engineering |
| Continuity | Scoped memory, compaction, provenance, deletion |
| Action | Tool design, permissions, approvals, verification, recovery |
| Domains | Research, coding, data analysis, creative work, communication |
| Human value | Human satisfaction, interaction design, agency, accessibility |
| Trust | Safety governance, threat modeling, privacy, auditability, and agent-risk controls |
| Planning depth | Focused, Deep, and Ultra Plan modes with budgets, checkpoints, and resumability |
| Bestness and frontier | Superlative analysis, frontier research, evidence, alternatives, and stopping criteria |
| Assistance and product | Optimal assistance, product strategy, magic moments, quality bar, and outcome completion |
| Improvement | Traces, graders, regression cases, bounded self-improvement |
| Peak runtime | Durable execution, event traces, resumable approvals, idempotency, progress states, action-bound approvals, cancellation, and risk journaling |
| Quality gates | Capability-risk matrix, evidence ledger, human feedback, and release criteria |
| Capability extension | Skill forging, capability discovery, model routing, agent collaboration, and progressive disclosure |
| Universal access | Multimodal reasoning, accessibility, and incident response |
| Build completeness | Intent preservation, requirement traceability, product completeness, and dynamic verification |
| Fable-like acceleration | Requirement compiler, build recipes, staged execution, repair loops, and runtime host |
| Online-first operation | Hosted orchestration, remote tool bridge, progressive delivery, and cost-aware execution |
| Fable research controls | Capability analysis, context handoffs, skeptical evaluation, tool evaluation, and completion intelligence |
| Evolving capabilities | Skill discovery, typed composition, quality judgment, capability-gap response, lifecycle promotion, and rollback |
| Lovable collaboration | Honest appreciation, adaptive conversation, controllable personalization, Brainstorm Mode, constructive disagreement, anti-manipulation boundaries, and a multidimensional benchmark |
| Professional UI taste | Contextual hierarchy, proportion, density, typography, restraint, micro-states, accessibility, blind review, and separate beauty-versus-professionalism gates |
| Contextual intelligence | Separated context layers, typed intent/output/next-step predictions, ambiguity resolution, correction learning, confidence, and non-authoritative personalization |
| Skill engineering intelligence | High-information examples, contextual exceptions, conditional lessons, baseline comparison, self-critique, and governed promotion |
| Intelligence infrastructure | Machine-readable research, lesson, example, intent, communication, evaluation, improvement, benchmark, and behavioral-observation records with a deterministic paired-decision kernel |
| Hosted evaluation research | Provider-neutral trace envelope, matched baseline/candidate arms, held-out evaluation, redaction, grader separation, and staged hosted-adapter roadmap |
| Provider adapter seam | Normalized model/tool event metadata, content digests, explicit redaction markers, provider extensions, and conservative privacy defaults in the reference host |
| Risk research | OWASP, NIST, MITRE ATLAS, Anthropic, Microsoft, AISI, Unit 42, IETF, and AAAI-informed risk taxonomy and control blueprint |
| User contributions | CLAI memory/project/tool patterns and Joy interaction patterns |

## Quick start

Read `core/self-directing-prompt.md` and combine it with `core/operating-contract.md` and `core/execution-loop.md`. For a specific task, load only the relevant specialist skills. A coding task might use task framing, planning, context engineering, coding, tool use, safety governance, evaluation, and communication. A research task might use task framing, research, context engineering, evaluation, and communication.

Run the structural checks from the repository root. The current risk-review milestone adds `references/agent-risk-control-blueprint.md`, `references/agent-risk-research-notes.md`, `runtime/risk-control.schema.json`, and `skills/agent-risk-controls/SKILL.md`. The current UI/lovability milestone adds `references/professional-taste-research-notes.md`, `references/professional-taste-architecture.md`, `skills/professional-taste/SKILL.md`, and `evals/lovability-benchmark-plan.md`. The current sequential-mission milestone adds `references/contextual-user-intelligence-architecture.md`, `references/skill-engineering-intelligence.md`, `references/master-mission-implementation-map.md`, three preserved mission sources, and contextual evaluation cases. The intelligence-infrastructure milestone adds `references/intelligence-infrastructure-audit.md`, public research notes, nine runtime intelligence schemas, representative records, a deterministic kernel and tests, and one focused meta-capability Skill. The hosted-evaluation research milestone adds `references/hosted-evaluation-research-brief-2026-08-23.md` and `references/hosted-evaluation-architecture-research-2026-08-23.md`; it defines the next experiment without claiming that a provider or model is universally better. The provider-adapter milestone adds `runtime/normalized-trace.schema.json`, `runtime/reference_host/normalized_trace.py`, and `references/provider-adapter-boundary.md`; it proves only deterministic normalization and redaction behavior in the reference host, not cross-provider equivalence or production privacy compliance. The executable reference host now enforces trust labeling primitives, action intent records, bound approvals, cancellation, tool validation, destination boundaries, and redacted incident journaling.


```bash
python3 scripts/validate_repo.py
```

The skill files follow progressive disclosure: each has YAML metadata and a concise body, while detailed resources can be linked only when needed. The host agent still needs actual model APIs, tools, permission enforcement, memory storage, tracing, and evaluators. The runtime schemas in this repository define portable contracts but do not enforce them by themselves.

## Architecture

The layers are: identity and contract; request understanding; strategy; context; memory; capability routing; tools; domain execution; human experience; safety and governance; evaluation; and bounded improvement. The optional `core/ultra-plan-mode.md` adds adaptive depth, dependency mapping, budgets, checkpoints, risk gates, resumability, and independent verification. The system is deliberately modular so a failure can be diagnosed and fixed at the right layer instead of making the prompt longer by default.

## Ultra Plan Mode

Ultra Plan Mode is an original, bounded high-rigor protocol for difficult, ambiguous, long-running, or high-impact tasks. It does not expose private chain-of-thought or imitate hidden model prompts. It uses a preflight plan, dependency graph, context and assumption ledgers, risk map, resource budgets, user checkpoints, resumable state, independent verification, and safe stop rules. It automatically reduces depth when extra planning would cost more than it saves.

See `core/ultra-plan-mode.md` and `skills/ultra-plan/SKILL.md`. The peak runtime layer additionally provides durable execution, structured event traces, resumable approval state, idempotency and reconciliation rules, progress states, evidence ledgers, human feedback controls, and capability-risk release gates.

## Portable Fable-like build system

The “one-shot” effect is treated as a system, not a magic prompt: a capable hosted model plus structured requirement compilation, reusable recipes, a thin vertical slice, staged execution, dynamic verification, skeptical evaluation, targeted repair, persistent state, and a host runtime. The pipeline is **brief compiler → architecture pass → vertical slice → staged expansion → dynamic verification → skeptical evaluation → repair loop → completion gate**. See `references/fable-like-runtime-blueprint.md`, `references/magic-pipeline.md`, `references/fable5-research-report.md`, and the skills `requirement-compiler`, `build-recipes`, `staged-execution`, `dynamic-verification`, `evaluator-critic`, `repair-loop`, and `completion-intelligence`.

## Online-first now, local later

The current priority is **online agents**. A modest laptop can act as the control surface while authorized hosted workers handle model calls, browser sessions, builds, vision checks, queues, and long-running work. The new online-first layer adds hosted orchestration, a remote-tool bridge, progressive delivery, and cost-aware routing. Local-model execution is a future compatibility track; when implemented, it must follow the same capability manifests, traces, permissions, verification, privacy, and human-control contracts.

## Absolute Best standard

“Absolute best” is defined operationally as the agent that maximizes verified human outcome value across the dimensions that matter for the current task, subject to safety, privacy, time, cost, capability, and user-control constraints, while minimizing unnecessary effort and preventing silent omission of important requirements. It is not a context-free claim that one model wins every task.

## Ultra Ultra Mode

Ultra Ultra Mode is the highest-rigor route for complex interactive builds and ambitious briefs. It preserves every explicit requirement, labels reasonable inferences, expands necessary system details, builds a thin end-to-end vertical slice, and verifies the running artifact. It checks interface, interactions, state, data, backend, persistence, errors, accessibility, security, deployment, documentation, and acceptance criteria. For games it also checks controls, camera, collisions, progression, feedback, pause, restart, win/lose behavior, performance, and playability. It does not mean infinite text or permission to act without approval.

See `core/layered-system-prompts.md`, `core/ultra-ultra-mode.md`, `skills/intent-preservation/SKILL.md`, `skills/product-completeness/SKILL.md`, `skills/dynamic-verification/SKILL.md`, and `skills/requirement-traceability/SKILL.md`.

## Full-mode expansion

The full-mode release adds a skill-forging lifecycle: **discover gap → frame outcome → define trigger and scope → choose progressive disclosure → write → add resources → define permissions → test → validate → package/version → observe → improve or retire**. It also adds model routing, structured agent collaboration, multimodal reasoning, accessibility, incident response, and portable capability discovery. The goal is not to cover everything in one skill; it is to make future capabilities easier to create, discover, evaluate, control, and retire.

See `references/full-mode-capability-map.md` and `runtime/capability-manifest.schema.json`.

## Peak review

The current improvement focuses on the highest-leverage gap: converting excellent instructions into observable runtime behavior. The Fable research pass adds explicit separation between output generation and verified completion, clean context handoffs, independent critique, tool measurement, and model-versus-harness evidence analysis. `runtime/trace-schema.json` defines auditable events; `runtime/progress-state-machine.md` defines resumable states; `skills/durable-execution` protects retries and side effects; `skills/evidence-ledger` protects claims and provenance; `skills/human-feedback` turns corrections into scoped learning; and `governance/capability-risk-matrix.md` prevents capability gains from compensating for failed safety, privacy, control, or recovery gates.

## Human satisfaction

The included human-satisfaction skill defines satisfaction as actual outcome quality plus lived experience: effort saved, clarity, agency, calibrated trust, emotional ease, accessibility, and future usefulness. The new `lovability` and `brainstorm-mode` skills extend this with honest appreciation, context-sensitive initiative, branch-preserving ideation, constructive disagreement, controllable memory, and explicit anti-dependence boundaries. Measure both task outcomes and user feedback; do not optimize engagement as a proxy for human value.

## Research basis

The design is grounded in public guidance from Anthropic on effective agents, context engineering, tool design, and reusable Agent Skills [1] [2] [3] [10]; OpenAI on trace-based agent evaluation, human review, and hosted agent runners [4] [8] [15]; NIST on AI risk management and human-centered AI [5] [6]; OWASP on agentic-AI threats and mitigations [7]; Temporal on durable human-in-the-loop execution [9]; MCP on portable resources, prompts, tools, progress, cancellation, tasks, and consent [11]; OpenGame-Bench on dynamic build health, visual usability, and intent alignment [12]; and SkillsBench on focused curated skills, skill selection, and skill evaluation [13]. See `references/research-and-sources.md`, `references/absolute-best-research.md`, and `references/online-first-research.md` for the synthesis.

## Public Fable analysis

`references/fable5-research-report.md` and `references/fable-capability-evidence-ledger.yaml` summarize only publicly documented Fable 5 capabilities and turn them into original, model-agnostic design lessons. `references/fable-research-notes.md` preserves the working evidence trail. No leaked or confidential prompts are included. Public material supports both model capability and harness value, but it does not prove universal one-shot production completeness or reveal all internal mechanisms.

## Evolving skills ecosystem

The repository now treats skills as versioned procedural capabilities rather than static prompts alone. `references/evolving-skills-gap-analysis.md` compares the attached mission with existing coverage; `references/evolving-skills-architecture.md` defines discovery, typed composition, capability gaps, critics, quality judgment, human-value review, and safe promotion; and `runtime/skill-contract.schema.json` defines a portable contract. The lifecycle is **discover → compose → execute → observe → critique → verify → repair → evaluate → propose → approve → register**. Candidate skills remain experimental until they pass representative and held-out evaluation and an authorized maintainer approves promotion.

The latest user-authored additions are preserved in `contributions/ULTRIA-original.txt`, `contributions/FORK-original.txt`, `contributions/maximum-capability-research-mission-original.txt`, and `contributions/lovable-ai-research-mission-original.txt`. Their implementation maps are in `references/ultria-fork-integration-map.md`, `references/evolving-skills-architecture.md`, and `references/lovable-agent-architecture.md`; the source documents are treated as design requirements while safety, privacy, user authority, and evidence standards remain non-negotiable.

## Reuse of Joy and CLAI

`contributions/CLAI-patterns.md` translates CLAI's memory, project mapping, approval, menu, export, and compaction patterns into model-agnostic capabilities. `contributions/Joy-patterns.md` translates Joy's search, responsive layout, hierarchy, and low-friction interaction ideas into human-centered interaction guidance. These are adapters and design notes, not copied runtime code.

## Comparative position

The repository is not currently the best overall agent system. Public frameworks such as [LangGraph](https://github.com/langchain-ai/langgraph), [CrewAI](https://github.com/crewAIInc/crewAI), the [OpenAI Agents SDK](https://github.com/openai/openai-agents-python), and [OpenHands](https://github.com/All-Hands-AI/OpenHands) are substantially ahead in executable runtime, deployment, integrations, observability, and ecosystem maturity. [Anthropic Skills](https://github.com/anthropics/skills) and [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) are ahead in ready-to-use or discoverable domain-skill breadth.

Ai-skills is strongest as a **provider-agnostic quality and governance layer**: intent preservation, requirement completeness, evidence-led completion, human control, evolving-skill promotion, human-value evaluation, honest appreciation, and Brainstorm Mode. These are design advantages, not proven universal performance advantages. See `references/repository-comparison.md` for the evidence-based comparison and `evals/comparative-benchmark-plan.md` for the controlled test needed to measure whether those layers improve real outcomes. The repository now includes a minimal executable reference host under `runtime/reference_host/` with provider adapters, scoped tools, allowlists, approval blocking, budgets, JSONL traces, atomic checkpoints, and an evidence-required completion gate. Run `python3 -m unittest discover -s runtime/reference_host -p 'test_*.py'` to exercise it. It is a reference implementation rather than a production server; browser execution, queues, distributed workers, and provider authentication remain explicit future adapters.

## Safety note

Do not connect this package to unrestricted shell, filesystem, browser, messaging, payment, production, or credential tools without implementing the action protocol, least privilege, approval boundaries, logging, verification, and recovery described here. Skills improve behavior; they do not replace a secure host runtime.

## License

MIT. See `LICENSE`.

## References

[1]: https://www.anthropic.com/engineering/building-effective-agents "Anthropic — Building Effective AI Agents"
[2]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents "Anthropic — Effective context engineering for AI agents"
[3]: https://www.anthropic.com/engineering/writing-tools-for-agents "Anthropic — Writing effective tools for agents"
[4]: https://developers.openai.com/api/docs/guides/agent-evals "OpenAI — Evaluate agent workflows"
[5]: https://www.nist.gov/itl/ai-risk-management-framework "NIST — AI Risk Management Framework"
[6]: https://www.nist.gov/programs-projects/human-centered-ai "NIST — Human-Centered AI"
[7]: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ "OWASP GenAI Security Project — Agentic AI: Threats and Mitigations"
[8]: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals "OpenAI — Guardrails and human review"
[9]: https://docs.temporal.io/ai/cookbook/human-in-the-loop-python "Temporal — Human-in-the-loop AI agent"
[10]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills "Anthropic — Equipping agents for the real world with Agent Skills"
[11]: https://modelcontextprotocol.io/specification/2026-07-28 "Model Context Protocol — Specification"
[12]: https://arxiv.org/html/2604.18394v1 "OpenGame: Open Agentic Coding for Games"
[13]: https://arxiv.org/html/2602.12670v1 "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks"
[14]: https://www.anthropic.com/claude/fable "Claude Fable — public product page"
[16]: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf "Claude Fable 5 & Claude Mythos 5 System Card"
[17]: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents "Anthropic — Effective harnesses for long-running agents"
[18]: https://www.anthropic.com/engineering/harness-design-long-running-apps "Anthropic — Harness design for long-running application development"
[19]: https://code.claude.com/docs/en/agent-sdk/agent-loop "Claude Code Docs — How the agent loop works"
[20]: https://code.claude.com/docs/en/agent-teams "Claude Code Docs — Orchestrate teams of Claude Code sessions"
[21]: https://claude.com/product/cowork "Claude Cowork — public product page"
[15]: https://developers.openai.com/api/docs/guides/agents "OpenAI — Agents SDK"
