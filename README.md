# Ai skills

**Ai skills** is a model-agnostic capability and governance layer for building AI agents that are more reliable, useful, safe, and satisfying to work with. It is not a magic prompt and it does not make an unsupported claim to universally outperform Claude, Fable, or any other model. Its purpose is to make improvement measurable on the tasks that matter to you.

> Better AI is not only a smarter answer. It is a better outcome: correct when correctness matters, grounded in evidence, efficient with attention and tools, safe under pressure, transparent about uncertainty, and genuinely easier for a person to use.

## What is included

The repository contains a self-directing core prompt, an operating contract, a bounded execution loop, an explicit action protocol, forty-one modular skills, adapters for the user's Joy and CLAI repositories, a human-satisfaction framework, a security and governance layer, evaluation cases, and validation scripts.

| Area | Included capability |
|---|---|
| Reasoning and execution | Task framing, planning, orchestration, context engineering |
| Continuity | Scoped memory, compaction, provenance, deletion |
| Action | Tool design, permissions, approvals, verification, recovery |
| Domains | Research, coding, data analysis, creative work, communication |
| Human value | Human satisfaction, interaction design, agency, accessibility |
| Trust | Safety governance, threat modeling, privacy, auditability |
| Planning depth | Focused, Deep, and Ultra Plan modes with budgets, checkpoints, and resumability |
| Bestness and frontier | Superlative analysis, frontier research, evidence, alternatives, and stopping criteria |
| Assistance and product | Optimal assistance, product strategy, magic moments, quality bar, and outcome completion |
| Improvement | Traces, graders, regression cases, bounded self-improvement |
| Peak runtime | Durable execution, event traces, resumable approvals, idempotency, and progress states |
| Quality gates | Capability-risk matrix, evidence ledger, human feedback, and release criteria |
| Capability extension | Skill forging, capability discovery, model routing, agent collaboration, and progressive disclosure |
| Universal access | Multimodal reasoning, accessibility, and incident response |
| Build completeness | Intent preservation, requirement traceability, product completeness, and dynamic verification |
| Fable-like acceleration | Requirement compiler, build recipes, staged execution, repair loops, and runtime host |
| User contributions | CLAI memory/project/tool patterns and Joy interaction patterns |

## Quick start

Read `core/self-directing-prompt.md` and combine it with `core/operating-contract.md` and `core/execution-loop.md`. For a specific task, load only the relevant specialist skills. A coding task might use task framing, planning, context engineering, coding, tool use, safety governance, evaluation, and communication. A research task might use task framing, research, context engineering, evaluation, and communication.

Run the structural checks from the repository root:

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

The “one-shot” effect is treated as a system, not a magic prompt: a strong model plus structured requirement compilation, reusable recipes, a thin vertical slice, staged execution, dynamic verification, targeted repair, persistent state, and a host runtime. The pipeline is **brief compiler → architecture pass → vertical slice → staged expansion → dynamic verification → repair loop → release gate**. See `references/fable-like-runtime-blueprint.md` and the skills `requirement-compiler`, `build-recipes`, `staged-execution`, `repair-loop`, and `runtime-host`.

## Absolute Best standard

“Absolute best” is defined operationally as the agent that maximizes verified human outcome value across the dimensions that matter for the current task, subject to safety, privacy, time, cost, capability, and user-control constraints, while minimizing unnecessary effort and preventing silent omission of important requirements. It is not a context-free claim that one model wins every task.

## Ultra Ultra Mode

Ultra Ultra Mode is the highest-rigor route for complex interactive builds and ambitious briefs. It preserves every explicit requirement, labels reasonable inferences, expands necessary system details, builds a thin end-to-end vertical slice, and verifies the running artifact. It checks interface, interactions, state, data, backend, persistence, errors, accessibility, security, deployment, documentation, and acceptance criteria. For games it also checks controls, camera, collisions, progression, feedback, pause, restart, win/lose behavior, performance, and playability. It does not mean infinite text or permission to act without approval.

See `core/layered-system-prompts.md`, `core/ultra-ultra-mode.md`, `skills/intent-preservation/SKILL.md`, `skills/product-completeness/SKILL.md`, `skills/dynamic-verification/SKILL.md`, and `skills/requirement-traceability/SKILL.md`.

## Full-mode expansion

The full-mode release adds a skill-forging lifecycle: **discover gap → frame outcome → define trigger and scope → choose progressive disclosure → write → add resources → define permissions → test → validate → package/version → observe → improve or retire**. It also adds model routing, structured agent collaboration, multimodal reasoning, accessibility, incident response, and portable capability discovery. The goal is not to cover everything in one skill; it is to make future capabilities easier to create, discover, evaluate, control, and retire.

See `references/full-mode-capability-map.md` and `runtime/capability-manifest.schema.json`.

## Peak review

The current improvement focuses on the highest-leverage gap: converting excellent instructions into observable runtime behavior. `runtime/trace-schema.json` defines auditable events; `runtime/progress-state-machine.md` defines resumable states; `skills/durable-execution` protects retries and side effects; `skills/evidence-ledger` protects claims and provenance; `skills/human-feedback` turns corrections into scoped learning; and `governance/capability-risk-matrix.md` prevents capability gains from compensating for failed safety, privacy, control, or recovery gates.

## Human satisfaction

The included human-satisfaction skill defines satisfaction as actual outcome quality plus lived experience: effort saved, clarity, agency, calibrated trust, emotional ease, accessibility, and future usefulness. It includes a starting weighted score, but the weights are hypotheses to validate—not a target to manipulate. Measure both task outcomes and user feedback.

## Research basis

The design is grounded in public guidance from Anthropic on effective agents, context engineering, tool design, and reusable Agent Skills [1] [2] [3] [10]; OpenAI on trace-based agent evaluation and human review [4] [8]; NIST on AI risk management and human-centered AI [5] [6]; OWASP on agentic-AI threats and mitigations [7]; Temporal on durable human-in-the-loop execution [9]; MCP on portable resources, prompts, tools, progress, cancellation, tasks, and consent [11]; and OpenGame-Bench on dynamic build health, visual usability, and intent alignment [12]. See `references/research-and-sources.md` and `references/absolute-best-research.md` for the synthesis.

## Public Fable analysis

`references/public-fable-analysis.md` summarizes only publicly documented Fable 5 capabilities and turns them into original design lessons. No leaked or confidential prompts are included. The reviewed official material did not verify a current public Claude Fable 3 release, so the repository does not invent one; provide a product URL if “Fable 3” means something else.

The latest user-authored additions are preserved in `contributions/ULTRIA-original.txt` and `contributions/FORK-original.txt`. Their implementation map is in `references/ultria-fork-integration-map.md`; the source documents are treated as design requirements while safety, privacy, user authority, and evidence standards remain non-negotiable.

## Reuse of Joy and CLAI

`contributions/CLAI-patterns.md` translates CLAI's memory, project mapping, approval, menu, export, and compaction patterns into model-agnostic capabilities. `contributions/Joy-patterns.md` translates Joy's search, responsive layout, hierarchy, and low-friction interaction ideas into human-centered interaction guidance. These are adapters and design notes, not copied runtime code.

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
