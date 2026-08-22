# Absolute Best and complete-build research

## What “absolute best” can mean

There is no context-free absolute best agent. The strongest defensible definition is:

> **The agent that maximizes verified human outcome value across the dimensions that matter for the current task, subject to safety, privacy, time, cost, capability, and user-control constraints, while minimizing unnecessary effort and preventing silent omission of important requirements.**

This definition has three layers:

| Layer | Question |
|---|---|
| Objective | What outcome does the person actually want? |
| Quality vector | How will success be judged: correctness, completeness, intent alignment, usability, reliability, safety, speed, cost, accessibility, trust, control, maintainability, and delight? |
| Constraints | What may the agent access, change, spend, expose, delay, or decide? |

“Absolute” therefore describes the quality of the decision and verification process, not a universal leaderboard position. A system can be best for a flower-pot storefront, a game prototype, or a privacy-sensitive local workflow under different constraints.

## Public complex-build lesson

The public OpenGame paper introduces OpenGame-Bench, which evaluates generated games dynamically through headless browser execution and VLM judging rather than static code checks alone. It separates **Build Health**, **Visual Usability**, and **Intent Alignment**, and notes that baseline language models often default to single-file vanilla HTML/JavaScript even when a richer framework is requested.[1]

The design lesson is directly relevant to the user's car-game and flower-pot-shop examples: a complete agent must compile the natural-language brief into a structured requirement specification, preserve each requirement through implementation, and test the running artifact. A page that scrolls is not a shop if the intended outcome requires product data, cart behavior, checkout or inquiry flow, persistence, error handling, and responsive interaction. A car-game mockup is not the requested game if controls, camera, collisions, progression, feedback, audio, menus, restart, and playability were implied by the user's goal.

## Ultra Ultra principles

1. **Requirement conservation:** Every user requirement becomes a tracked item with source, interpretation, implementation location, verification method, and status.
2. **Detail expansion without invention:** Expand likely necessary details and edge cases, but label inferred requirements and ask when ambiguity changes architecture, cost, safety, or user experience.
3. **Vertical-slice first:** Build one thin end-to-end path before broadening. For a shop, that could be browse → product detail → add to cart → persisted cart → checkout/inquiry result.
4. **Product completeness:** Inspect frontend, backend, data model, state, interaction, errors, loading, empty states, accessibility, security, deployment, and documentation—not just visuals.
5. **Dynamic verification:** Run the artifact. Test key flows with browser or domain-specific execution. Static syntax success is insufficient.
6. **Intent alignment:** Judge each explicit and inferred requirement against the running result; report omissions instead of silently simplifying.
7. **Progressive depth:** Ultra Ultra can plan deeply internally, but it must stop redundant analysis, respect budgets, and show the user only useful progress.
8. **Human control:** Keep inferred details editable, preview consequential work, preserve cancellation and rollback, and never turn “full mode” into permission to act without approval.

## References

[1]: https://arxiv.org/html/2604.18394v1 "OpenGame: Open Agentic Coding for Games"


## Skills and rapid complex work

SkillsBench reports a public benchmark of 84 tasks across 11 domains, evaluated with and without curated or self-generated skills. Its reported findings are that curated skills improve average pass rate but vary by domain, self-generated skills do not reliably help, focused 2–3 skill combinations outperform comprehensive documentation, and smaller models with good skills can sometimes match larger models without them.[2] These findings support a selective router and focused skill bundles rather than loading every skill at once.

## Public Fable capability claims

Anthropic's public Fable page describes multi-day autonomous coding sessions, self-written tests, design fidelity, vision-based checking, document understanding, code review, fewer turns, and complex multi-agent workflows.[3] These are product claims, not proof of universal superiority. The engineering lesson is that speed comes from a strong model plus tool access, persistent context, reusable procedures, effective task decomposition, self-testing, and a host runtime that can keep work moving. A prompt wrapper alone cannot reproduce the complete system.

[2]: https://arxiv.org/html/2602.12670v1 "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks"

[3]: https://www.anthropic.com/claude/fable "Claude Fable — public product page"
