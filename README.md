# Ai skills

**Ai skills** is a model-agnostic capability and governance layer for building AI agents that are more reliable, useful, safe, and satisfying to work with. It is not a magic prompt and it does not make an unsupported claim to universally outperform Claude, Fable, or any other model. Its purpose is to make improvement measurable on the tasks that matter to you.

> Better AI is not only a smarter answer. It is a better outcome: correct when correctness matters, grounded in evidence, efficient with attention and tools, safe under pressure, transparent about uncertainty, and genuinely easier for a person to use.

## What is included

The repository contains a self-directing core prompt, an operating contract, a bounded execution loop, an explicit action protocol, sixteen modular skills, adapters for the user's Joy and CLAI repositories, a human-satisfaction framework, a security and governance layer, evaluation cases, and validation scripts.

| Area | Included capability |
|---|---|
| Reasoning and execution | Task framing, planning, orchestration, context engineering |
| Continuity | Scoped memory, compaction, provenance, deletion |
| Action | Tool design, permissions, approvals, verification, recovery |
| Domains | Research, coding, data analysis, creative work, communication |
| Human value | Human satisfaction, interaction design, agency, accessibility |
| Trust | Safety governance, threat modeling, privacy, auditability |
| Improvement | Traces, graders, regression cases, bounded self-improvement |
| User contributions | CLAI memory/project/tool patterns and Joy interaction patterns |

## Quick start

Read `core/self-directing-prompt.md` and combine it with `core/operating-contract.md` and `core/execution-loop.md`. For a specific task, load only the relevant specialist skills. A coding task might use task framing, planning, context engineering, coding, tool use, safety governance, evaluation, and communication. A research task might use task framing, research, context engineering, evaluation, and communication.

Run the structural checks from the repository root:

```bash
python3 scripts/validate_repo.py
```

The skill files follow the progressive-disclosure format: each has YAML metadata, a concise body, and optional references can be added later. The host agent still needs actual model APIs, tools, permission enforcement, memory storage, tracing, and evaluators.

## Architecture

The layers are: identity and contract; request understanding; strategy; context; memory; capability routing; tools; domain execution; human experience; safety and governance; evaluation; and bounded improvement. The system is deliberately modular so a failure can be diagnosed and fixed at the right layer instead of making the prompt longer by default.

## Human satisfaction

The included human-satisfaction skill defines satisfaction as actual outcome quality plus lived experience: effort saved, clarity, agency, calibrated trust, emotional ease, accessibility, and future usefulness. It includes a starting weighted score, but the weights are hypotheses to validate—not a target to manipulate. Measure both task outcomes and user feedback.

## Research basis

The design is grounded in public guidance from Anthropic on effective agents, context engineering, and tool design [1] [2] [3]; OpenAI on trace-based agent evaluation [4]; NIST on AI risk management and human-centered AI [5] [6]; and OWASP on agentic-AI threats and mitigations [7]. See `references/research-and-sources.md` for the synthesis and links.

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
