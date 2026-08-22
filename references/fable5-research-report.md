# Claude Fable 5: capability extraction and independent agent architecture

**Status:** Public-source research synthesis. **Purpose:** Understand why Fable 5 can appear to take a short request much further with fewer corrections, then translate the underlying mechanisms into reusable, independent Ai-skills capabilities. This report does not reproduce leaked, private, or access-controlled prompts.

## Executive summary

The strongest public explanation for the “one-shot magic” is not one hidden prompt. It is a compound system: a capable model, a tool-using agent loop, focused skills, durable state, context management, staged planning, domain templates, parallel or delegated work when useful, skeptical evaluation, dynamic execution, and repair. Anthropic publicly describes Fable 5 as suited to ambitious coding, multi-day agent harnesses, self-written tests, vision-based checking, and subagent delegation; its public system card also documents important failures, including insufficient verification and reckless or destructive actions.[1] [2]

The independent design conclusion is therefore **model + harness + tools + state + verification + human control**, not Fable imitation. Skills should make procedures explicit and composable, while the runtime should enforce permissions, persist state, expose progress, and verify outcomes.

## 1. Capability map

| Capability family | What an agent needs to do | Independent skill or contract |
|---|---|---|
| Intelligence | Reason, abstract, prioritize, judge, and decompose | Task framing, superlative analysis, requirement compiler |
| Intent | Infer the outcome behind short language without silently inventing risky scope | Intent preservation, requirement traceability, assumption management |
| Planning | Turn goals into stages, dependencies, budgets, and acceptance tests | Ultra planning, staged execution, build recipes |
| Tools | Select, call, interpret, and recover from tools | Tool use, hosted-tool bridge, capability discovery |
| State | Maintain goals, decisions, progress, evidence, and artifacts across sessions | Durable execution, memory, trace schema, progress state |
| Delegation | Split independent work, specialize workers, synthesize results | Agent collaboration, online orchestration, model routing |
| Verification | Test code, runtime behavior, visuals, requirements, safety, and readiness | Dynamic verification, evidence ledger, product completeness |
| Repair | Diagnose, patch, retest, and prevent recurrence | Repair loop, incident response, self-improvement |
| Human experience | Minimize unnecessary effort while preserving clarity, trust, agency, and delight | Human satisfaction, optimal assistance, UI Vision, accessibility |
| Completion | Know whether the requested outcome is genuinely done | Outcome completion, release gates |

## 2. Public evidence and evidence status

| Finding | Status | Evidence and implication |
|---|---|---|
| Fable 5 is positioned for ambitious coding and long-running work | Confirmed public claim | Anthropic's product page and system card describe broad coding, agentic, vision, and long-context capabilities.[1] [2] |
| Fable 5 can operate inside an agent harness with stage planning, subagents, self-testing, and visual checking | Confirmed public claim | Anthropic publicly names Claude Code and Managed Agents as harnesses and describes planning, delegation, tests, and vision.[2] |
| Harness design materially changes long-horizon results | Confirmed public engineering report | Anthropic reports initializer/coding agents, feature lists, progress files, git, incremental work, browser automation, and clean handoffs.[3] |
| Multi-agent work helps breadth-first research but costs more and is not ideal for tightly coupled coding | Confirmed public engineering report | Anthropic reports orchestrator-worker research, parallel exploration, synthesis, and substantial token overhead.[4] |
| Durable state should live outside fragile workers and context windows | Confirmed public engineering report | Managed Agents describes external session logs, event retrieval, wake/resume, and replaceable containers.[5] |
| Focused skills can improve performance; loading everything is not necessarily better | Supported by independent benchmark | SkillsBench reports benefits from curated skills, domain variance, negative deltas on some tasks, and stronger results for focused 2–3 module bundles.[6] |
| Generated work needs dynamic evaluation, not static source inspection | Supported by independent research and Anthropic reports | OpenGame-Bench uses build health, visual usability, and intent alignment through execution; Anthropic reports browser-based testing catching bugs code inspection missed.[7] [3] |
| A stronger model alone guarantees completion | Unsupported | Anthropic's own system card documents examples of insufficient verification and destructive behavior; the claim should not be made.[1] |
| A short prompt alone caused a complete project | Unknown | Public demonstrations may omit the exact harness, tools, template, model settings, retries, or edits. Treat anecdotal “one-shot” reports as demonstrations, not causal proof. |

## 3. Model intelligence versus agent intelligence

| Capability | Likely model contribution | Likely system contribution | Best improvement lever |
|---|---|---|---|
| Code synthesis and abstraction | Learned programming and reasoning priors | Relevant context, tools, examples, tests, and repair feedback | Model plus skills and verification |
| Intent understanding | Semantic interpretation and world knowledge | Requirement compiler, assumptions, examples, user feedback | Skills and evaluator; model-dependent ceiling |
| Long-horizon coherence | Planning and self-monitoring ability | Progress files, event logs, checkpoints, clean resets, artifact handoffs | Harness and state |
| Product completeness | Knowledge of common product patterns | Explicit feature ledger, domain recipes, completeness map, acceptance tests | Harness and skills |
| Tool choice | Tool-use capability and judgment | Small ergonomic tool set, schemas, permissions, routing, feedback | Tools and harness |
| Delegation | Ability to describe subtasks and synthesize | Worker contracts, concurrency limits, shared task state, conflict control | Orchestration |
| Visual taste | Perception and learned aesthetic priors | Criteria, references, evaluator separation, browser screenshots, iteration | Model plus evaluator/harness |
| Safe autonomy | Alignment and risk recognition | Hard gates, hooks, approvals, sandbox, audit, rollback, classifiers | Mostly system enforcement |
| Completion | Judgment about whether the goal is satisfied | Requirement traceability, dynamic tests, independent evaluator, release gate | System plus model |

The distinction is mandatory. The host must never treat a skill, memory note, or model statement as proof of authorization or completion. Hard safety and side-effect restrictions belong in enforceable runtime policy.

## 4. Reconstructed agent loop

A general loop is:

> **Understand → expand requirements → plan → select skills → select tools → act → observe → evaluate → delegate if useful → revise → verify → complete → present.**

This is an adaptive loop, not a fixed chain. Every tool result can change the plan. The host should persist the loop state, expose useful progress, and stop on completion, budget exhaustion, unresolved risk, cancellation, or non-convergence.

Anthropic's public Agent SDK describes a repeated cycle in which the model evaluates current state, requests tools, receives results, and continues until it produces a response without tool calls. It also describes turn and budget limits, streamed lifecycle messages, permissions, hooks, sessions, compaction, and final usage/cost information.[8]

## 5. The “one-shot magic” mechanism

The perceived magic is best understood as ranked factors:

| Rank | Factor | Evidence level | Why it matters |
|---:|---|---|---|
| 1 | Better intent expansion and defaults | Supported/inferred | The agent builds what the user meant, not only the literal noun phrase. |
| 2 | Tool access plus dynamic execution | Confirmed/supported | Running the artifact reveals failures that code inspection misses.[3] [7] |
| 3 | Structured decomposition and incremental progress | Confirmed | Feature ledgers, vertical slices, and clean handoffs prevent half-built work.[3] |
| 4 | Model capability and efficient reasoning | Confirmed but model-dependent | A strong model can design and repair more effectively, but remains fallible.[1] |
| 5 | Reusable skills and domain templates | Supported | Stable scaffolds reduce repeated design and cross-file inconsistency.[6] [7] |
| 6 | Skeptical independent evaluation | Supported | Separating generator and evaluator reduces self-praise and creates actionable feedback.[9] |
| 7 | Persistent state and context engineering | Confirmed | External progress and high-signal context preserve continuity across long work.[5] [8] |
| 8 | Delegation and parallelism | Supported but conditional | Parallel independent work increases breadth but adds coordination and token cost.[4] [15] |
| 9 | Hidden complexity and calm UX | Product inference | Users experience a simple goal-based handoff while the system manages the machinery.[16] |

A “Minecraft in 20 minutes” demonstration can therefore be a fast first slice, a strong model with extensive tool use, a prepared environment, a template or common-pattern prior, asynchronous work, or a result judged visually rather than by production completeness. The responsible benchmark is to reproduce the exact task under controlled conditions and inspect the full trajectory.

## 6. Intent understanding

A weak system maps “professional” to colors, “car game” to a canvas, or “flower-pot shop” to a scroll page. A stronger system compiles the request into the user's job, primary journey, entities, state, interactions, content, quality bar, platform, backend, persistence, errors, accessibility, security, deployment, and acceptance tests. Necessary inferences are labeled; unknowns that change architecture, risk, cost, or experience become questions or conservative defaults.

The test is requirement conservation: every explicit requirement must be implemented, deliberately deferred, rejected with a reason, or called out as an unverified limitation.

## 7. Assumption framework

For each ambiguity choose among **ask, assume, research, test, proceed, or stop**. Proceed without asking when the assumption is reversible, low-risk, and does not change the product's core outcome. Ask when it changes architecture, permissions, cost, privacy, safety, legal exposure, or the user's intended experience. Research when public facts can resolve it. Test when the question can be answered cheaply through the artifact. Stop when the action would be irreversible or unsafe without authority.

## 8. Long-horizon work and memory

The minimum continuity set is a versioned requirement ledger, progress log, task graph, decision record, evidence ledger, artifact index, test status, next-step pointer, and clean source-control state. Context should be retrieved by need rather than dumped wholesale. Memory is useful context, not permission. User corrections should become scoped, consent-aware improvements instead of uncontrolled permanent profiles.[3] [5] [12]

## 9. Delegation and subagents

Delegate when subtasks are independent, high-volume, context-heavy, or naturally specialized. Keep one agent sequential when changes share fragile state, dependencies are tight, or coordination costs exceed parallel value. Give each worker objective, inputs, exclusions, output schema, tool limits, evidence requirements, and time/budget bound. The parent owns synthesis, contradiction resolution, requirement coverage, and final verification.

Teams are not automatically better. Public guidance distinguishes lower-cost focused subagents from higher-cost teams with direct communication and shared coordination; the choice depends on whether discussion creates more value than overhead.[4] [15]

## 10. Self-improvement and visual verification

A safe loop is:

> **Generate → inspect → critique → revise → verify → finalize.**

The generator should not be the sole judge. For visual work use:

> **Build → render → see → compare with goals → identify defects → fix → render again.**

Use deterministic checks for build health and interactions, visual checks for hierarchy and appearance, and human review for taste, value, and surprising behavior. Keep a plateau rule to stop when improvements are negligible or begin damaging clarity, accessibility, or intent.

## 11. Completion intelligence

“Output generated” means the system produced files or text. “Task complete” means the result satisfies the requirement ledger, passes relevant tests, works through the real user journey, handles important edge states, meets safety and accessibility gates, is recoverable, and is honestly communicated. The final answer must report verified, unverified, deferred, and blocked items separately.

## 12. Failure recovery

The default recovery loop is:

> **Fail → diagnose → adapt → retry → verify.**

Do not retry uncertain side effects blindly. Reconcile external state first. Classify failures as requirement, architecture, context, implementation, dependency, tool, environment, permission, or verification failures. Patch the smallest cause, rerun focused and regression tests, record the failure signature, and escalate when repeated repair indicates a wrong architecture or missing host capability.

## 13. Model orchestration

Use a fast/cheap model for classification, extraction, formatting, routine edits, and test summarization. Use a stronger model for architecture, ambiguity, complex debugging, multimodal judgment, difficult research, and final review. Use parallel workers for independent exploration or isolated artifacts; do not parallelize shared-file edits by default. Evaluate routing by verified outcome quality, latency, cost, privacy exposure, tool errors, retries, and human effort—not by model prestige.

## 14. Meta-skills

The highest-leverage skills are not hundreds of isolated tricks but a controlled lifecycle:

1. **Skill discovery:** identify the missing procedural capability.
2. **Skill selection:** choose the smallest relevant bundle.
3. **Skill composition:** order skills around a shared requirement and evidence ledger.
4. **Skill evaluation:** compare no-skill, curated-skill, and alternative-skill conditions.
5. **Skill critique:** find omissions, ambiguity, brittleness, and unsafe assumptions.
6. **Skill optimization:** improve the skill against held-out tasks without overfitting.
7. **Skill generation:** create a focused package with triggers, dependencies, tools, risks, tests, and rollback.
8. **Skill routing:** select skills, models, tools, and workers by task fit and risk.

## 15. Replicable, model-dependent, and unknown

| Category | Capabilities |
|---|---|
| Replicable through skills/harness/tools | Requirement compilation; feature ledgers; templates; staged work; progress; state persistence; routing; delegation contracts; tool schemas; approvals; dynamic tests; screenshot comparison; repair; evidence; completion gates; calm UX; cost measurement |
| Model-dependent | Deep abstraction; broad domain knowledge; code synthesis quality; subtle visual taste; difficult debugging; ambiguous intent judgment; novel strategy; sustained reasoning efficiency |
| Unknown from public information | Exact Fable 5 system prompts; hidden training or post-training data; internal routing thresholds; proprietary evaluator prompts; full harness configuration; exact tool availability for viral demos; causal contribution of any one component |

## 16. Existing repository gap analysis

The repository already contains strong prompt layers, 47 validated skills, runtime schemas, governance, online-first routing, product completeness, dynamic verification, UI Vision, and user-contributed ULTRIA/FORK/CLAI/Joy patterns. Before this research, the remaining gap was a single evidence-ledger research report and stronger separation between confirmed Fable claims, architectural inference, and unknowns. This report closes that documentation gap and identifies runtime implementation as the next major frontier.

## 17. Proposed next-generation architecture

```text
Human brief
   ↓
Intent + requirement compiler
   ↓
Quality objective + assumption policy
   ↓
Focused skill/model/tool router
   ↓
Planner and task graph
   ↓
Vertical-slice generator
   ↓
Durable online orchestrator
   ├─ specialist workers / subagents
   ├─ browser, code, data, vision, and deployment tools
   ├─ session state, artifacts, traces, and approvals
   └─ budget, privacy, and risk gates
   ↓
Independent evaluator
   ├─ deterministic tests
   ├─ live interaction tests
   ├─ visual and UX review
   ├─ requirement coverage
   └─ safety and operational checks
   ↓
Repair controller
   ↓
Completion gate
   ↓
Human-ready result + evidence + next options
```

## 18. Recommended implementation order

| Order | Build next | Reason |
|---:|---|---|
| 1 | Requirement compiler and immutable feature ledger | Prevents short prompts from collapsing into shallow outputs |
| 2 | Real host runtime with sessions, traces, tools, and approvals | Turns documented contracts into behavior |
| 3 | Vertical-slice generator and reusable domain recipes | Produces an early usable result quickly |
| 4 | Dynamic verifier with browser/runtime execution | Finds integration and interaction defects |
| 5 | Repair controller with failure signatures and regression tests | Converts failures into progress |
| 6 | Independent evaluator for design, usability, and intent | Reduces self-evaluation bias |
| 7 | Online model/tool router and cost telemetry | Improves quality per unit of cost and latency |
| 8 | Bounded delegation and specialist workers | Adds breadth only where the task benefits |
| 9 | Benchmark harness and held-out task suite | Proves which layers actually help |
| 10 | Future local-AI adapters | Adds offline/privacy execution without changing contracts |

## 19. What still needs to be measured

The repository should eventually run controlled comparisons across the same tasks: baseline model, core prompt only, focused skills, full skills, staged harness, dynamic verifier, evaluator/repair loop, and multi-agent route. Measure requirement coverage, intent alignment, build health, visual usability, factuality, safety, tool errors, turns, runtime, usage, cost, repair convergence, user effort, and satisfaction. Do not infer causal improvement from a single impressive demo.

## 20. Final answer to the research mission

If this repository were given to a capable agent tomorrow, it would improve behavior where the improvement is procedural: preserving intent, choosing context, using tools, planning stages, maintaining state, testing the real artifact, handling failures, and communicating honestly. It cannot erase the underlying model's limitations, grant tools or permissions the host does not provide, or guarantee a perfect complex build from one sentence. Its strongest path to being better than a competitor on a chosen task is to define the task, build a better measured harness around available models, and improve the system from evidence.

## References

[1]: https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf "Claude Fable 5 & Claude Mythos 5 System Card"
[2]: https://www.anthropic.com/claude/fable "Claude Fable — public product page"
[3]: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents "Anthropic — Effective harnesses for long-running agents"
[4]: https://www.anthropic.com/engineering/multi-agent-research-system "Anthropic — How we built our multi-agent research system"
[5]: https://www.anthropic.com/engineering/managed-agents "Anthropic — Scaling Managed Agents: Decoupling the brain from the hands"
[6]: https://arxiv.org/html/2602.12670v1 "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks"
[7]: https://arxiv.org/html/2604.18394v1 "OpenGame: Open Agentic Coding for Games"
[8]: https://code.claude.com/docs/en/agent-sdk/agent-loop "Claude Code Docs — How the agent loop works"
[9]: https://www.anthropic.com/engineering/harness-design-long-running-apps "Anthropic — Harness design for long-running application development"
[10]: https://www.anthropic.com/engineering/writing-tools-for-agents "Anthropic — Writing effective tools for agents"
[11]: https://code.claude.com/docs/en/skills "Claude Code Docs — Extend Claude with skills"
[12]: https://code.claude.com/docs/en/memory "Claude Code Docs — How Claude remembers your project"
[13]: https://code.claude.com/docs/en/agent-sdk/overview "Claude Code Docs — Agent SDK overview"
[14]: https://code.claude.com/docs/en/agent-teams "Claude Code Docs — Orchestrate teams of Claude Code sessions"
[15]: https://claude.com/product/cowork "Claude Cowork — public product page"
