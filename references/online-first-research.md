# Online-first agent research

## Public findings

OpenAI's public Agents SDK documentation describes agents as applications that plan, call tools, collaborate across specialists, and keep enough state to complete multi-step work. Its public navigation includes runners, streaming, continuation, sandbox agents, orchestration and handoffs, guardrails and human review, results and state, MCP, agents as tools, sessions and resumable run state, resumable approval flows, built-in traces, and evaluation.[1]

Anthropic's public Claude Fable page describes multi-day autonomous coding, self-written tests, vision-based checking, document understanding, design fidelity, fewer turns, and complex multi-agent workflows.[2] These are public product claims, not a guarantee for every task. The reusable lesson is an online host that keeps the model supplied with tools, state, feedback, specialized procedures, and verification.

## Online-first design implications

1. The current priority is hosted models and online tools. Local model execution is documented as a future compatibility track, not the active resource assumption.
2. A thin client can run on a modest laptop while hosted workers perform model calls, browser sessions, builds, visual checks, and long-running queues.
3. The user should see a fast first usable result while the online agent continues verification and refinement through resumable state.
4. Model routing should choose cheap/fast models for classification, extraction, and routine edits; stronger models for architecture, ambiguous requirements, difficult debugging, and final review; and never bypass safety or approval gates.
5. Online orchestration needs explicit session identity, state checkpoints, event traces, cancellations, approval records, usage budgets, tool scopes, and cleanup/expiry policies.

[1]: https://developers.openai.com/api/docs/guides/agents "OpenAI — Agents SDK"
[2]: https://www.anthropic.com/claude/fable "Claude Fable — public product page"
