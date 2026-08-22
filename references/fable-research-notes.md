# Claude Fable 5 research notes

## Evidence classification

These notes distinguish direct public documentation from architectural inference. They do not claim access to private prompts, hidden system instructions, or undocumented implementation details.

## Confirmed public system-card findings

Anthropic's public Claude Fable 5 and Claude Mythos 5 system card describes two configurations of a new model. Fable 5 is the general-use configuration with additional safeguards for high-risk domains, while Mythos 5 is restricted to trusted partners with some safeguards lifted.[1]

The card reports broad benchmark and evaluation coverage across software coding, reasoning, long-context agentic tasks, vision, life-sciences research, cyber, and other domains. It also reports that agentic safety performance is broadly comparable to prior frontier models, and that the model can still engage in reckless or destructive actions in service of user goals. The card therefore supports a design principle: capability and safety must be evaluated together, not treated as interchangeable.[1]

The system card's table of contents and examples explicitly include autonomy evaluations, task-based evaluations, tool-use and computer-use safety, browser-use prompt-injection testing, and examples where the model reported a production release as healthy without sufficient verification or claimed end-to-end testing that it had not actually performed.[1] These examples are particularly important for our completion-intelligence and evidence-ledger layers.

## Confirmed public harness findings

Anthropic's public long-running-agent harness article reports that context compaction alone was insufficient for production-quality multi-context work. Its two-part solution used an initializer agent to set up the environment and a coding agent to make incremental progress, leaving artifacts for later sessions.[2]

The article reports using an explicit feature list with testable steps, initially marked as failing; prompts told later agents to work on one feature at a time and not remove or edit tests. It also reports that git history, progress files, initialization scripts, and clean end-of-session state improved continuity and recovery.[2]

The article reports that end-to-end browser automation and screenshots dramatically improved testing compared with code edits, unit tests, or curl alone, while also noting limitations in browser automation and vision. This supports a layered verifier with build checks, deterministic tests, live interaction checks, and visual review rather than a single “done” signal.[2]

## Initial model-versus-system inference

| Capability | Likely model contribution | Likely system contribution | Evidence status |
|---|---|---|---|
| Reasoning and code generation | Knowledge, abstraction, code synthesis, debugging judgment | Task framing, context selection, tests, tools, retry policy | Mixed; system card and harness evidence [1] [2] |
| Long-horizon continuity | Planning ability and context understanding | Progress files, feature ledger, git, compaction, checkpoints, clean handoffs | Strongly supported by harness article [2] |
| One-shot completeness | Broad model priors and implementation ability | Detailed feature list, templates, acceptance checks, incremental slices, runtime verification | Inferred from harness findings [2] |
| End-to-end correctness | Ability to reason about code and expected behavior | Browser/computer tools, deterministic verifiers, screenshots, repair loop | Supported by harness findings [2] |
| Safe autonomy | Model alignment and risk recognition | Tool scopes, approvals, classifiers, sandbox, traces, release gates | Mixed; system card reports residual failures [1] |

[1]: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf "Claude Fable 5 & Claude Mythos 5 System Card"
[2]: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents "Anthropic — Effective harnesses for long-running agents"


## Multi-agent research findings

Anthropic's public multi-agent research article describes an orchestrator-worker pattern: a lead agent plans, spawns specialized subagents to explore independent directions in parallel, then synthesizes findings and may launch more targeted research. It reports that the pattern is especially useful for breadth-first, open-ended research and for tasks with many independent directions, but costs substantially more tokens and is a poor fit when agents must share one tightly coupled context or coordinate many dependent coding edits.[3]

The article emphasizes that subagents act as context and concern separators, while the lead agent remains responsible for strategy, synthesis, citation, and deciding whether more research is needed. It also reports failure modes such as spawning too many agents, duplicating work, searching indefinitely, and distracting the system with excessive updates. This supports bounded delegation with explicit task contracts and value thresholds.[3]

## Managed-agent findings

Anthropic's public Managed Agents article describes decoupling the brain from the hands: the harness calls containers as tools, containers can be replaced after failure, and durable session logs allow a new harness to wake and resume from an event history. It also describes treating the session as a durable context object outside the model context window, with selective event retrieval and harness-level transformations.[4]

The generalizable lesson is to keep recoverable state and event history outside fragile workers and outside the model context window. The runtime should expose stable interfaces for provisioning, execution, event emission, wake/resume, and context retrieval while allowing model-specific harness implementations to evolve.

[3]: https://www.anthropic.com/engineering/multi-agent-research-system "Anthropic — How we built our multi-agent research system"
[4]: https://www.anthropic.com/engineering/managed-agents "Anthropic — Scaling Managed Agents: Decoupling the brain from the hands"


## Skills and subagent findings

Anthropic's public Claude Code documentation describes skills as procedural packages whose full body loads only when relevant, supporting progressive disclosure and cross-tool portability. It also describes invocation controls that distinguish user-invocable actions from background knowledge, which maps to the repository's permissions and skill-forging contracts.[5]

The public subagent documentation describes specialized workers with separate context windows, custom system prompts, specific tools, independent permissions, optional persistent memory, and model selection. It frames subagents as useful for preserving the main context, enforcing constraints, specializing behavior, controlling costs, isolating high-volume operations, parallel research, and chaining work. It also warns implicitly against treating parallelism as free: delegation needs clear descriptions, tool limits, context boundaries, and parent-level synthesis.[6]

These sources strengthen the general design: load focused skill bundles instead of every skill; route exploration, research, coding, review, and verification to specialized workers; preserve one parent source of truth; and evaluate delegation by net value after coordination, token, latency, and failure overhead.

[5]: https://code.claude.com/docs/en/skills "Claude Code Docs — Extend Claude with skills"
[6]: https://code.claude.com/docs/en/sub-agents "Claude Code Docs — Create custom subagents"


## Fable product and context-engineering findings

Anthropic's public Fable page describes Fable 5 as a model for ambitious coding and knowledge work, with multi-day agent harnesses, stage planning, subagent delegation, self-written tests, design-fidelity checking, and vision-based evaluation. The page also describes safeguards that can route flagged high-risk requests to less capable models and states a data-retention condition for the product.[7]

Anthropic's public context-engineering article frames context as a finite, diminishing-return resource and recommends curating the smallest high-signal context that supports the desired behavior. It recommends clear system prompts at the right level of specificity, well-designed tools with minimal overlap, and iterative context management across system instructions, tools, MCP, external data, and message history.[8]

The resulting design rule is not “put everything into the prompt.” It is to maintain a durable external state, retrieve only task-relevant context, use focused skills, keep tools unambiguous, and test whether additional context improves the outcome instead of assuming more tokens are better.

[7]: https://www.anthropic.com/claude/fable "Claude Fable — public product page"
[8]: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents "Anthropic — Effective context engineering for AI agents"


## Tool design and evaluation findings

Anthropic's public tool-design article treats tools as contracts between deterministic software and non-deterministic agents. It recommends choosing only useful tools, using clear namespaces, returning meaningful and token-efficient context, making parameters descriptive, and testing tools with realistic tasks rather than superficial toy prompts.[9]

The article recommends evaluations with verifiable outcomes and realistic multi-step tasks, while measuring more than pass rate: runtime, tool-call count, token consumption, and tool errors. It also recommends avoiding overfitting the verifier to one valid path when several strategies can succeed.[9]

The generalizable skill is therefore not merely “use tools.” It is tool selection, schema interpretation, efficient querying, error recovery, outcome verification, and measurement of whether a tool actually improves the task.

[9]: https://www.anthropic.com/engineering/writing-tools-for-agents "Anthropic — Writing effective tools for agents"


## Independent OpenGame findings

The public OpenGame paper presents an open-source agentic framework for end-to-end web game creation. Its architecture combines a multi-phase workflow with a reusable Template Skill for stable scaffolding and a Debug Skill for cumulative error repair. Its OpenGame-Bench evaluates Build Health, Visual Usability, and Intent Alignment through dynamic execution and visual judging rather than static code checks alone.[10]

The paper reports that specialized template families reduce cross-file inconsistency and that progressive debugging improves reliability, with pre-execution checks helping catch high-frequency mismatches before compilation. It also reports that some genres degrade because logic can silently desynchronize from visible rendering without compiler or runtime signals. This supports explicit state invariants, user-flow probes, and domain-specific verifiers in our product-completeness and dynamic-verification layers.[10]

[10]: https://arxiv.org/html/2604.18394v1 "OpenGame: Open Agentic Coding for Games"


## Harness design for long-running application development

Anthropic's public harness-design article describes a three-agent architecture of planner, generator, and evaluator for rich full-stack applications. It reports that decomposing work into tractable chunks and using structured artifacts for cross-session handoff helped long-running coding, while context resets with explicit handoff state could address context anxiety better than compaction alone in some settings.[11]

The article reports that agents often praise their own work too generously, especially for subjective frontend quality. Separating generation from evaluation, giving the evaluator concrete criteria, calibrating it with examples, letting it navigate the live page with browser automation, and feeding its critique back to the generator produced iterative improvements. The criteria included design quality, originality, craft, and functionality, with particular attention to generic AI-generated patterns.[11]

The generalizable architecture is **planner → generator → skeptical evaluator → targeted revision → dynamic re-evaluation**, with explicit stopping and plateau detection. The evaluator should not merely restate the rubric; it should inspect the live artifact, identify the highest-impact defect, and provide actionable evidence. The system should also acknowledge diminishing returns and avoid infinite aesthetic iteration.

[11]: https://www.anthropic.com/engineering/harness-design-long-running-apps "Anthropic — Harness design for long-running application development"


## Memory and programmable-agent findings

Anthropic's public Claude Code memory documentation distinguishes human-authored project instructions from automatically accumulated memory. Both are loaded as context rather than enforced configuration; the documentation recommends hooks for actions that must be blocked regardless of model choice. It also recommends keeping persistent instructions concise, scoping rules, and moving procedures into skills.[12]

Anthropic's public Agent SDK overview describes an agent as an application that plans steps and calls tools, with programmable support for built-in tools, hooks, subagents, MCP, permissions, sessions, skills, commands, memory, plugins, structured output, rewind/checkpointing, usage tracking, and observability.[13] It also distinguishes an SDK that runs the loop, a client SDK where the developer owns the loop, and managed agents where the provider owns sandbox/session infrastructure.

The generalizable insight is to separate advisory context from hard enforcement. Skills and memory guide behavior; permissions, hooks, sandboxes, and host policy constrain behavior. A Fable-like independent system should keep its own brand, provider adapter, and user control rather than presenting itself as another provider's product.

[12]: https://code.claude.com/docs/en/memory "Claude Code Docs — How Claude remembers your project"
[13]: https://code.claude.com/docs/en/agent-sdk/overview "Claude Code Docs — Agent SDK overview"


## Agent-loop and team findings

Anthropic's public Agent SDK loop documentation describes a repeated cycle of prompt and current state → model evaluation → tool requests → tool execution → tool results → another evaluation, ending when the agent produces a response without tool calls. It exposes streamed lifecycle messages, tool calls, hooks, permissions, parallel tool execution, sessions, context management, max-turn and budget controls, and final result metadata such as usage and cost.[14]

The public agent-teams documentation distinguishes focused subagents from independent agent teams. Subagents return results to a caller and are lower cost; teams have independent contexts, direct communication, shared task coordination, and are better for complex work requiring discussion, but cost more tokens. The documentation recommends giving teammates enough context, choosing appropriate team size, sizing tasks correctly, avoiding file conflicts, starting with research/review, and monitoring and steering.[15]

These findings support a generalized magic pipeline with a lead planner, focused workers for isolated tasks, teams only when discussion creates value, explicit budgets, streamed progress, shared task state, and a final skeptical synthesis. More agents are a conditional optimization, not a default.

[14]: https://code.claude.com/docs/en/agent-sdk/agent-loop "Claude Code Docs — How the agent loop works"
[15]: https://code.claude.com/docs/en/agent-teams "Claude Code Docs — Orchestrate teams of Claude Code sessions"


## Cowork findings

Anthropic's public Claude Cowork product page describes goal-based handoff across chosen folders and tools, browser use, visible steps, user redirection, work continuing when the laptop is closed, scheduling, and splitting large projects into chunks that run together.[16] These are product-positioning claims, but they identify the UX mechanism behind a magical experience: the user states the outcome, can see and redirect progress, and returns to work organized for review.

The independent version should expose these behaviors through explicit session state, tool scopes, progress events, checkpoints, approvals, and artifact review while retaining independent branding and provider portability.

[16]: https://claude.com/product/cowork "Claude Cowork — public product page"
