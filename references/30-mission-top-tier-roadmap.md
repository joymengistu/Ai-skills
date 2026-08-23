# Ai-skills: 30-Mission Top-Tier Roadmap

**Status:** Planning baseline, 23 August 2026  
**Scope:** The private `joymengistu/Ai-skills` repository  
**Purpose:** Improve capability quality through measurable, composable, human-centered infrastructure rather than by adding Skills for their own sake.

> “Top tier” is not a permanent ranking. It is a task-relative standard: the system should produce the best verified outcome it can reasonably achieve under the user’s constraints, authority, time, cost, safety, privacy, and evidence limits.

## 1. Audit baseline

The repository currently contains **63 Skills**, **111 evaluation cases**, a model-agnostic core prompt, a reference runtime, evidence and risk contracts, human-lovability guidance, a screenshot-reconstruction capability, and the universal Agent Max entry Skill. Existing strengths include requirement preservation, progressive Skill loading, governed tool boundaries, durable-execution references, visual reconstruction workflows, evidence ledgers, held-out evaluation structure, and explicit limits on unsupported claims. The current intelligence benchmark is structurally valid but correctly reports `not_run` when measured baseline and candidate model results are absent; therefore this roadmap must not claim that the system is already better than another agent.

The highest-leverage gaps are not simply missing domain Skills. They are **semantic calibration**, consistent cross-Skill composition, measurable research quality, real host integration for one-touch entry, stronger human-value measurement, and repeated baseline-versus-candidate experiments. The repository also contains some historical fixed-count tests, which should be replaced by contract-based or manifest-derived checks as the catalog evolves.

| Audit area | Current position | Top-tier target |
|---|---|---|
| Capability catalog | Broad and progressively disclosed | Discoverable, deduplicated, versioned, and retired when redundant or harmful |
| Routing | Core router plus Agent Max presets | One universal entry with deterministic route previews and conflict resolution |
| Research | Public-source research packages and evidence boundaries | Freshness, source hierarchy, contradiction handling, and claim-level provenance by default |
| Runtime | Reference-grade controls and traces | Portable host adapters with stronger artifact, recovery, privacy, and approval coverage |
| Evaluation | 106 cases, held-out family, hard gates | Measured paired trials, calibrated graders, human review, and regression-aware promotion |
| Human value | Lovability and satisfaction principles | Observable effort, clarity, agency, trust, accessibility, and future-usefulness measures |
| Quality language | Mostly natural-language intensifiers | Explicit operational scale that never converts adjectives into unsafe permission or unlimited work |

## 2. Calibrated quality language

Intensity words must describe **quality targets and effort policies**, not authority. They never authorize external actions, bypass safety controls, assume unlimited credits, or justify endless planning. Every request should translate the word into an objective, evidence requirement, budget, and stopping rule.

| Word or phrase | Operational definition | Minimum evidence | Default stopping rule |
|---|---|---|---|
| **Basic** | Satisfies the explicit core requirement on the simplest valid path | Direct artifact check or focused test | Stop after the core path works |
| **Good** | Correct, usable, understandable, and complete for the stated main outcome | Acceptance checks for must-haves and main failure state | Stop when must-haves pass and no material omission remains |
| **Strong** | Good quality with robust edge handling, clear structure, and appropriate accessibility | Main path, key edge states, and targeted critique | Stop when high-risk defects are resolved |
| **Excellent** | Strong quality with refined details, low unnecessary effort, and evidence-backed polish | Independent review plus relevant live or rendered checks | Stop when additional polish has diminishing value |
| **Best** | The strongest verified option among the tested alternatives for this task and constraints | Same-condition comparison and explicit trade-offs | Stop when the chosen option wins the defined objective or trade-off is accepted |
| **Very best** | Best under multiple relevant dimensions, with no hidden material regression in safety, cost, accessibility, or user effort | Multi-metric comparison, regression checks, and human or domain review where needed | Stop at a measured Pareto frontier; do not claim universal superiority |
| **Top tier** | A quality bar combining outcome correctness, reliability, craft, human value, and trustworthy evidence | Contract gates, live verification, independent critique, and uncertainty report | Stop when all critical gates pass and remaining defects are non-material or disclosed |
| **Maximum** | Use the highest reasonable rigor available within explicit budgets, time, permissions, and risk limits | Budget ledger, risk review, and proportional verification | Stop at the authorized ceiling or when expected value declines |
| **Ultimate / full mode** | A high-rigor workflow with complete planning, implementation, verification, repair, and reporting for a difficult task | Full route trace and completion gate | Stop at completion, block, authority boundary, or diminishing returns |
| **Go to your limit** | Spend the maximum safe and authorized effort that materially improves the requested outcome | Checkpointed evidence, budget tracking, and unresolved-unknowns report | Never interpret it as unlimited time, money, compute, permissions, or retries |
| **Perfect / pixel-perfect** | Exact only if the defined tolerance and all required states are demonstrably met | Same-viewport or same-condition comparison with explicit tolerance | Otherwise report measured closeness and remaining differences |
| **Quick / simple** | Use the smallest sufficient route and avoid unnecessary breadth | Focused smoke check | Stop as soon as the stated outcome is reliably achieved |

### Translation rule

When an intensifier appears, convert it into: **target → scope → constraints → evidence → budget → stop rule**. For example, “make it the very best” becomes “maximize the specified outcome across the agreed dimensions, compare reasonable alternatives, preserve safety and agency, measure regressions, and stop when the evidence supports the choice.” It does not become permission to load every Skill, expose hidden reasoning, make unapproved changes, or invent confidence.

## 3. Thirty missions in six components

Each component contains five missions. Each mission has an objective, concrete repository work, and a promotion gate. Missions should be executed sequentially only when their dependencies and evidence justify the next one.

### Component A — Intent, quality semantics, and task framing

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **1. Audit baseline** | Maintain a machine-readable inventory of Skills, routes, schemas, tests, known gaps, duplicated concepts, unsupported claims, and unresolved questions. Link every proposed change to an observed gap. | Audit is reproducible; no roadmap claim is presented as a measured performance result. |
| **2. Quality vocabulary** | Add the calibrated scale in this document to the core prompt, Agent Max, Ultra Plan, and relevant quality Skills. Make intensity words produce scope, budget, evidence, and stopping semantics. | Adversarial cases show that “maximum” does not bypass safety, imply unlimited resources, or force unnecessary work. |
| **3. Intent compiler** | Strengthen requirement compilation to preserve outcomes, non-goals, constraints, references, user preferences, and authority boundaries, with explicit conflict resolution. | Paired cases show fewer silent omissions and no unauthorized interpretation of unknowns. |
| **4. Difficulty and risk classifier** | Classify requests by ambiguity, consequence, reversibility, dependency depth, artifact complexity, evidence burden, and user effort. Map classes to planning and verification depth. | The classifier chooses proportional routes on small, complex, high-impact, and ambiguous cases without systematic over-planning. |
| **5. Acceptance contract** | Standardize typed definitions of done, evidence requirements, failure states, stopping rules, and completion statuses across Skills and runtime traces. | Every major route can state what success means, how it will be checked, and what would block completion. |

### Component B — Research, evidence, and memory

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **6. Source hierarchy** | Define source classes by authority, proximity, recency, reproducibility, independence, and conflict risk. Add freshness policies by domain. | Research cases choose stronger sources when available and disclose stale or weak evidence. |
| **7. Claim provenance** | Extend evidence ledgers so every material claim records source, quote or extracted fact, scope, date, confidence, transformation, and verifier. | Claims can be traced from output to evidence without relying on hidden reasoning. |
| **8. Contradiction handling** | Add workflows for conflicting sources, version drift, missing evidence, and unresolved disputes. Prevent silent averaging of incompatible claims. | Contradiction cases produce explicit alternatives, uncertainty, and a justified conclusion or deferral. |
| **9. Research and lesson memory** | Unify reusable research records, failed-experiment lessons, examples, counterexamples, consent, provenance, expiry, retrieval scope, and deletion rules. | Memory retrieval improves a matched task without contaminating unrelated tasks or preserving unauthorized sensitive data. |
| **10. Uncertainty discipline** | Formalize `FACT`, `EVIDENCE`, `INFERENCE`, `HYPOTHESIS`, and `UNKNOWN` across research, planning, UI inference, and completion reports. | Evaluation catches fabricated certainty and rewards calibrated unknowns when evidence is insufficient. |

### Component C — Routing, runtime, and controlled action

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **11. Agent Max router** | Make Agent Max the single universal entry: normalize button, slash-command, and natural-language invocations; select minimal Skills; show route previews; resolve conflicts; and preserve host authority. | Routing cases show correct minimal bundles, no catalog scrambling, clear fallback, and no permission escalation. |
| **12. Adaptive planning** | Connect difficulty, risk, budget, and evidence burden to focused, standard, deep, or ultra planning. Record why depth changed. | Same tasks do not receive expensive planning without measurable expected benefit. |
| **13. Tool and approval contract** | Strengthen typed tool intents, least privilege, destination boundaries, approvals, sensitive-data handling, idempotency, and human confirmation semantics. | Safety and authority gates block unsafe or unapproved side effects in adversarial tests. |
| **14. Durable execution** | Expand restart, timeout, cancellation, partial completion, approval wait, retry, reconciliation, and handoff behavior with resumable state. | Crash and interruption tests neither lose user work nor duplicate consequential effects. |
| **15. Grounded artifact verification** | Verify actual files, URLs, builds, rendered outputs, traces, and environment state against the expected artifact contract. | Completion is blocked when evidence is absent, stale, mismatched, or supplied by an untrusted source. |

### Component D — Professional output and multimodal craft

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **16. Complete deliverable recipes** | Create domain recipes for apps, games, research reports, documents, data work, media, and automations with thin vertical slices and state coverage. | Representative artifacts work end to end, not merely look plausible or compile. |
| **17. Professional quality system** | Convert professional taste into observable criteria for hierarchy, typography, spacing, density, interaction clarity, restraint, consistency, and task fit while preserving user intent. | Blind review and live checks distinguish professional quality from generic beautification. |
| **18. Multimodal fidelity** | Extend screenshot reconstruction, image understanding, diagrams, documents, audio, and video workflows with provenance, measurement, same-condition comparison, and correction loops. | Multimodal cases report measured fidelity and limits instead of claiming exactness from a first pass. |
| **19. Engineering quality gates** | Add reusable checks for code correctness, security, performance, responsive behavior, accessibility, observability, data integrity, and deployment readiness. | A visually polished artifact cannot pass if critical runtime, security, accessibility, or data gates fail. |
| **20. Completion and repair loop** | Unify defect classification, minimal repair, regression testing, plateau detection, final evidence, and honest statuses across all production routes. | Every failure produces a useful lesson or clear unresolved limitation, and “done” is never used to hide missing evidence. |

### Component E — Human lovability and agency

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **21. Lovability model** | Operationalize human value across outcome quality, effort saved, clarity, agency, calibrated trust, emotional ease, accessibility, dignity, and future usefulness. | Human review and task metrics are kept separate from engagement or praise metrics. |
| **22. Communication calibration** | Adapt explanation depth, status frequency, tone, uncertainty, error messages, and next steps to user context without condescension or noise. | Users can understand what happened, what matters, and what they can control with lower unnecessary effort. |
| **23. Initiative and memory** | Define when to anticipate needs, when to ask, how to remember preferences, how to forget, and how to make personalization visible and reversible. | Initiative improves outcomes without making authority decisions or creating dependence. |
| **24. Trustworthy disagreement and repair** | Add respectful challenge, correction acceptance, apology without performance, transparent error recovery, and escalation to human review. | The agent can disagree usefully, correct itself, and preserve user dignity under failure or uncertainty. |
| **25. Feedback learning** | Convert explicit user corrections and outcome signals into scoped, consent-aware lessons with rollback and non-authoritative personalization. | Feedback improves future matched tasks without overgeneralizing one user’s preference or retaining unnecessary data. |

### Component F — Evaluation, curation, safety, and evolution

| Mission | Objective and repository work | Promotion gate |
|---|---|---|
| **26. Measured benchmark arms** | Expand representative, regression, held-out, and safety cases with baseline, candidate, and ablation arms under matched model and budget conditions. | Results contain measured per-case outcomes; absent measurements remain `not_run`. |
| **27. Graders and human review** | Improve rubric graders, trace metrics, artifact verifiers, inter-rater guidance, calibration sets, and human review for taste, lovability, and accessibility. | Graders are tested for consistency, blind spots, and susceptibility to superficial polish. |
| **28. Red-team resilience** | Exercise prompt injection, hostile files and websites, data exfiltration, unsafe tool requests, authority confusion, memory poisoning, and misleading evidence. | Hard safety, privacy, authority, and recovery gates pass before capability promotion. |
| **29. Skill curation lifecycle** | Add catalog search, trigger quality, duplication detection, composition conflicts, dependency graphs, deprecation, retirement, ownership, and version migration. | A new Skill must close a demonstrated gap and beat or complement existing routes without redundant context cost. |
| **30. Governed continuous improvement** | Establish release packets containing before/after diffs, evidence, regressions, lessons, user feedback, unresolved questions, rollback data, and next priorities. | No change is promoted from enthusiasm alone; authorized review, measurable benefit, safety gates, and rollback readiness are present. |

## 4. Recommended execution order

Begin with Missions **1–5** because semantic quality and proportionality prevent later infrastructure from optimizing the wrong target. Continue through **6–10** to make research and uncertainty trustworthy. Then improve routing and runtime in **11–15**, followed by artifact quality in **16–20**. Human lovability in **21–25** should be evaluated alongside—not after—technical quality. Finish with **26–30**, because measurement, red-teaming, curation, and governed release determine whether improvements are real and durable.

Each mission should produce four artifacts: a concise implementation change, a before-versus-after evaluation plan, a failure or uncertainty record, and a release decision. A mission may be merged with another only when the combined change has one clear acceptance contract and separate evidence for each outcome.

## 5. Top-tier definition of done

The repository should be considered **top-tier for a given task class** only when it can demonstrate all of the following:

1. It understands and preserves the user’s intended outcome, constraints, non-goals, and authority.
2. It selects a proportional route rather than confusing more Skills, more text, or more agents with better quality.
3. It distinguishes evidence from inference and uncertainty from failure.
4. It produces a useful artifact and verifies the real result under the relevant conditions.
5. It repairs important defects and reports what remains unresolved.
6. It protects safety, privacy, accessibility, user control, and reversibility.
7. It improves human experience through clarity, low effort, respect, calibrated trust, and agency.
8. It demonstrates improvement against a matched baseline without hiding regressions behind aggregate scores.
9. It can explain why a Skill was loaded, what it contributed, and when it should not be used.
10. It can retire or roll back a capability when evidence no longer supports it.

## 6. Immediate next action

The next concrete repository increment should be **Mission 2: Quality vocabulary**, implemented as a small shared reference and routed through Agent Max, the umbrella router, Ultra Plan, Superlative Analysis, Outcome Completion, and Human Satisfaction. Add adversarial evaluation cases for “best,” “maximum,” “go to your limit,” “perfect,” and “quick.” Do not alter safety or authority boundaries while adding the scale.

## References

[1]: ../README.md "Ai-skills repository overview and current capability map"
[2]: ../manifest.yaml "Ai-skills registry and version manifest"
[3]: ./screenshot-reconstruction-architecture.md "Screenshot reconstruction architecture and evidence boundaries"
[4]: ./lovability-benchmark-plan.md "Human lovability benchmark plan"
[5]: ./modern-prompt-architecture-2026-08-23.md "Modern prompt architecture research and implementation guidance"
[6]: ./intelligence-infrastructure-architecture.md "Intelligence infrastructure architecture"
[7]: ../evals/intelligence-benchmark.json "Benchmark arms, metrics, and promotion gates"
[8]: ../skills/agent-max/SKILL.md "Universal Agent Max routing Skill"
