# Evolving skills ecosystem: gap analysis

**Source:** User-provided mission preserved at `contributions/Fable-research-mission-original.txt`.

The mission asks Ai-skills to become more than a static prompt library: a general-purpose ecosystem that discovers, composes, evaluates, verifies, and safely improves capabilities. The current repository already implements much of the operating contract, hosted execution, human value, Fable-derived completion controls, and skill-forging lifecycle. The opportunity is to make the lifecycle more explicit and machine-readable without turning the project into an uncontrolled self-modifying agent.

| Mission area | Current coverage | Gap or improvement |
|---|---|---|
| Rigorous skill definition | Manifest, skill-forging, capability manifests, concise SKILL.md format | Add an explicit skill contract with interfaces, quality threshold, evaluation method, lifecycle state, provenance, and composition metadata. |
| Skill composition | Agent collaboration, orchestration, staged execution, routing | Add compatibility checks for inputs/outputs, ordering, conflicts, side effects, and evidence handoff. |
| Skill discovery | Capability discovery, routing, requirement compiler | Add a discovery procedure that returns a minimal bundle with reasons, confidence, missing capabilities, and fallback behavior. |
| Capability gap detection | Capability discovery, self-improvement, incident response | Add a bounded gap record and research-to-candidate workflow; candidate creation must not auto-register trust. |
| Skill generation | Skill-forging | Add draft → experimental → evaluated → trusted/deprecated state transitions and held-out evaluation requirements. |
| Critics and evaluators | Evaluation, evidence ledger, evaluator-critic, dynamic verification | Add critic selection by artifact type and a required separation between generator evidence and evaluator evidence. |
| Taste and qualitative quality | Human satisfaction, UI Vision, interaction design, optimal assistance | Add a portable quality-judgment framework that operationalizes taste as criteria plus examples and evidence, not as one universal score. |
| Human satisfaction | Human-satisfaction and human-feedback skills | Connect satisfaction measures to task success, effort, corrections, trust, agency, and accessibility; never optimize a score through manipulation. |
| Optimal action | Optimal assistance, orchestration, safety governance | Add explicit action-choice records: ask, assume, research, proceed, delegate, verify, recover, stop, or request approval. |
| Universal verification | Dynamic verification, evidence ledger, completion intelligence | Add verification profiles and hard release gates for build health, usability, intent alignment, operational readiness, and safety. |
| Continuous improvement | Self-improvement, repair loop, skill-forging, evaluation | Add a bounded improvement proposal record, regression protection, rollback, provenance, and human or maintainer approval before production promotion. |
| Online-first operation | Online orchestration, hosted-tool bridge, cost-aware execution | Preserve hosted priority; new capability lifecycle must work with remote model/tool workers and explicit budgets. |
| Future local compatibility | Documented future track | Do not implement local AI now; require future adapters to honor the same contracts and controls. |

## High-leverage design decision

Do not add thousands of static skills or a giant universal prompt. Use a small number of composable contracts:

> **Discover → compose → execute → observe → critique → verify → repair → evaluate → propose improvement → approve → register.**

The host runtime should enforce registration, permissions, versioning, rollback, and release gates. Skills may propose changes; they must not silently alter their own authority, safety boundaries, or production status.

## Proposed focused additions

1. **Skill contract and composition:** a machine-readable schema plus a concise skill that validates interfaces, dependencies, side effects, and evidence requirements.
2. **Capability discovery and gap response:** extend current discovery with a minimal-bundle algorithm and a bounded candidate-skill pipeline.
3. **Evaluation and promotion:** extend current evaluation with lifecycle states, held-out tests, quality thresholds, regression cases, and promotion/rollback rules.
4. **Quality and taste:** add a task-specific qualitative evaluator that uses observable criteria, reference examples, and human review rather than pretending taste is fully objective.
5. **Action selection:** add an explicit next-action framework that balances outcome value, uncertainty, risk, reversibility, cost, and human effort.

## Non-goals

This improvement does not seek confidential prompts, hidden reasoning, proprietary assets, universal superiority claims, unrestricted self-modification, autonomous permission escalation, or local-model deployment. It also does not treat agent self-critique as sufficient evidence for high-stakes outcomes.


## Public research update

Anthropic's public Agent Skills guidance confirms a lightweight directory format with a required `SKILL.md`, metadata loaded at startup, optional scripts/resources, and progressive disclosure. It also emphasizes using deterministic code for operations where traditional execution is more reliable or efficient than token generation.[1]

OpenAI's public self-evolving-agent cookbook documents a concrete improvement loop: establish a baseline, collect human or LLM-judge feedback, run evals against predefined criteria, aggregate scores, iterate up to a bounded retry limit, and promote the improved baseline only after it meets a threshold. It also presents manual escalation when automated improvement plateaus.[2]

These sources support the mission's architecture but also narrow its novelty. The distinctive repository contribution should be the integration of portable skill contracts, discovery, composition, human-value evaluation, safety gates, durable evidence, and hosted-first runtime controls—not the generic idea of reflection or prompt optimization alone.

[1]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills "Anthropic — Equipping agents for the real world with Agent Skills"
[2]: https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining "OpenAI — Self-Evolving Agents cookbook"


## Additional public evidence

The public Agent Skills specification defines a portable directory with `SKILL.md`, optional scripts/references/assets, metadata fields, and progressive disclosure from startup metadata to instructions to on-demand resources. It does not by itself define a complete capability registry, interface type system, benchmark protocol, promotion policy, or trust model; those remain repository/runtime responsibilities.[3]

SkillWeaver is a research prototype for web agents that proposes reusable skills, practices them in an environment, synthesizes browser APIs, and hones them with testing and debugging. Its paper reports gains on WebArena and real-world websites, but the scope is website interaction and short-horizon reusable APIs, not a general-purpose self-improving operating system. It also documents failure modes such as API invocation and parameter errors and a ceiling tied to base-agent capability.[4]

The design implication is to separate **skill packaging** from **skill trust**. A skill may be discoverable and composable while still experimental; promotion requires reproducible tests, provenance, permission review, regression protection, and a rollback path.

[3]: https://agentskills.io/specification "Agent Skills — public specification"
[4]: https://arxiv.org/html/2504.07079 "SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills"


## Lovability and personalization evidence

OpenAI's public personalization guidance frames custom instructions as stable working-style preferences and memory as recurring context that can improve relevance and consistency. Its public Memory FAQ describes user controls to inspect, edit, delete, disable, and use temporary conversations; it also warns that deleting one chat may not remove separately stored memory and that sensitive information can appear if shared.[5] [6]

The portable design implication is not “make the agent more human.” It is **make the collaboration more useful, continuous, honest, and controllable**. Separate stable preferences, project state, short-term context, and inferred hypotheses. Give the user visibility, correction, deletion, temporary mode, and a reason when recalled context materially changes a response. Personalization should reduce effort without becoming overfamiliar or surprising.

[5]: https://openai.com/academy/personalization/ "OpenAI Academy — Personalizing ChatGPT"
[6]: https://help.openai.com/en/articles/8590148-memory-faq "OpenAI Help Center — Memory FAQ"


## Honesty, agency, rapport, and trust evidence

OpenAI's public Model Spec describes intended behavior including interpreting underlying intent and context, asking clarifying questions when appropriate, controlling and communicating side effects, expressing uncertainty, avoiding an independent agenda, and respecting user agency.[7] These principles reinforce that initiative must remain bounded and that a lovable assistant should help the user's goals rather than create goals of its own.

A 2024 Frontiers in Psychology review discusses socio-emotional attributes in human-AI collaboration, including rapport, effective communication, empathy, active listening, familiarity, and trust. The review is useful for identifying candidate interaction variables, but it is a literature review with heterogeneous underlying evidence; its percentages and examples should not be treated as universal product targets.[8] The repository should therefore evaluate emotional appropriateness and trust calibration, not maximize anthropomorphism or engagement.

[7]: https://model-spec.openai.com/2026-08-18.html "OpenAI Model Spec, 2026-08-18"
[8]: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1369957/full "The role of socio-emotional attributes in enhancing human-AI collaboration"


## Public constitutional guidance

Anthropic's public constitution presents a model-behavior vision organized around broad safety, broad ethics, compliance with guidelines, and genuine helpfulness. It emphasizes honesty, thoughtfulness, care, correction, and the need to be transparent about the gap between intended and observed behavior.[9] This is a public statement of intended behavior, not evidence that every model response meets it. The repository can translate the principle into observable contracts: helpfulness must be substantive, honesty must include uncertainty, care must preserve agency, and correction must remain possible.

[9]: https://www.anthropic.com/constitution "Anthropic — Claude's Constitution"
