# Research and sources

This repository translates external guidance into implementation heuristics. It does not claim that a prompt can universally outperform a named model. Capability must be measured on a defined task distribution.

## Evidence summary

Anthropic distinguishes workflows, where code orchestrates LLMs and tools through predefined paths, from agents, where the LLM dynamically directs process and tool use. It recommends environmental ground truth, human checkpoints, stopping conditions, simple composable loops, and thoughtful tool documentation.[1]

Anthropic's context-engineering guidance treats context as finite, recommends the smallest high-signal context, progressive disclosure, clear prompts at the right altitude, minimal non-overlapping tools, and iteration based on observed failure modes.[2]

Anthropic's tool-design guidance treats tools as contracts between deterministic software and non-deterministic agents. It recommends realistic evaluations, meaningful and token-efficient tool responses, clear specifications, verifiable outcomes, and metrics such as task accuracy, runtime, call count, token use, and tool errors.[3]

OpenAI's agent-evaluation guidance recommends traces, graders, datasets, and evaluation runs. Traces capture model calls, tool calls, guardrails, and handoffs; trace grading helps locate wrong tool choice, bad handoffs, policy violations, and regressions before moving to repeatable datasets and runs.[4]

NIST's AI Risk Management Framework organizes trustworthy AI risk work around Govern, Map, Measure, and Manage and encourages trustworthiness considerations throughout design, development, use, and evaluation.[5]

NIST's human-centered AI work emphasizes keeping humans at the core, respect for autonomy, beneficence, justice, subjective experience, and measurement of trust in human-AI interaction.[6]

OWASP's Agentic AI guidance provides a threat-model-based reference for emerging agentic threats and mitigations, supporting least privilege, input and output validation, prompt-injection resistance, approval boundaries, and auditability.[7]

## References

[1]: https://www.anthropic.com/engineering/building-effective-agents "Anthropic — Building Effective AI Agents"

[2]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents "Anthropic — Effective context engineering for AI agents"

[3]: https://www.anthropic.com/engineering/writing-tools-for-agents "Anthropic — Writing effective tools for agents"

[4]: https://developers.openai.com/api/docs/guides/agent-evals "OpenAI — Evaluate agent workflows"

[5]: https://www.nist.gov/itl/ai-risk-management-framework "NIST — AI Risk Management Framework"

[6]: https://www.nist.gov/programs-projects/human-centered-ai "NIST — Human-Centered AI"

[7]: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ "OWASP GenAI Security Project — Agentic AI: Threats and Mitigations"


The peak review identified an operational gap between good instructions and durable runtime behavior. Temporal's public AI cookbook describes resource-efficient waiting for approvals, durable timers that survive disruptions, asynchronous approval signals, configurable timeouts, and audit trails.[8] OpenAI's public guardrails guidance describes automatic checks plus human review, resumable approval interruptions, validation of target/action/arguments/identity/scope, denial of out-of-scope or destructive actions, decision logging, and fail-closed behavior when review is unavailable.[9] These findings motivate the runtime trace schema, progress state machine, durable-execution skill, idempotency rules, and capability-risk release gates.

## Additional references

[8]: https://docs.temporal.io/ai/cookbook/human-in-the-loop-python "Temporal — Human-in-the-loop AI agent"

[9]: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals "OpenAI — Guardrails and human review"


Anthropic's public Agent Skills guidance describes modular directories with `SKILL.md`, optional resources, scripts, and templates, and recommends progressive disclosure so the agent loads only scenario-relevant detail.[10] The Model Context Protocol specification separates resources, prompts, and tools; supports capability negotiation, progress, cancellation, error reporting, and asynchronous tasks; and emphasizes explicit consent, privacy, clear authorization, and caution with untrusted tool descriptions.[11] These findings inform `skills/skill-forging`, `skills/capability-discovery`, the capability-manifest schema, and the full-mode routing rules.

[10]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills "Anthropic — Equipping agents for the real world with Agent Skills"

[11]: https://modelcontextprotocol.io/specification/2026-07-28 "Model Context Protocol — Specification"
