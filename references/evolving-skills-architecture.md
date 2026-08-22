# Evolving skills architecture

This document turns the attached mission into a safe, model-agnostic design. It treats skills as **versioned procedural capabilities** that can be discovered, composed, evaluated, and proposed for improvement, while keeping authority and safety in the host runtime.

## Core model

```text
Human goal
  → intent and requirement compiler
  → capability profile
  → minimal skill bundle
  → compatibility and risk check
  → composed plan
  → execution and observation
  → critic and verification
  → human-value review
  → repair or completion
  → capability-gap record when needed
  → candidate skill proposal
  → isolated evaluation and held-out regression
  → maintainer approval and registration
```

The ecosystem is **not** a self-modifying prompt. A skill may recommend a candidate, but only the host or authorized maintainer can grant production status, permissions, external access, or changes to safety rules.

## Skill contract

The minimal portable contract is `name`, `description`, purpose, trigger, inputs, outputs, procedure, exclusions, and safe failure behavior. The ideal runtime contract additionally records dependencies, input/output types, composition constraints, side effects, permissions, risk, provenance, version, evaluator, benchmark, quality threshold, owner, rollback, and lifecycle state. The machine-readable form is `runtime/skill-contract.schema.json`.

## Composition

Compose skills as a typed directed acyclic graph where possible. Each node declares the artifacts it consumes and produces. The composer checks:

1. required inputs are available or can be produced;
2. output formats are compatible;
3. dependencies and ordering are satisfiable;
4. side effects do not conflict;
5. permissions are sufficient and no broader than needed;
6. verification evidence can flow between nodes;
7. the bundle is smaller than the available budget allows; and
8. a fallback or escalation exists for material failure.

Use sequential composition for shared mutable state and dependent edits. Use parallel composition only for independent, side-effect-free work. The final synthesizer owns contradictions, requirement coverage, and release verification.

## Discovery engine

Given a goal, compile a capability profile containing outcome, domain, artifacts, interaction mode, risk, freshness, tools, constraints, and quality bar. Rank candidate skills by trigger fit, input/output compatibility, evidence quality, version health, permissions, cost, and expected outcome gain. Return the smallest sufficient bundle with reasons, confidence, missing capabilities, conflicts, and fallback. Discovery never grants authorization.

## Capability gaps and candidate generation

Record a gap only when a failure, repeated correction, unmet requirement, or missing tool is evidenced. Search existing skills and authoritative external knowledge first. Generate a candidate with narrow scope, explicit exclusions, provenance, test cases, expected improvement, safety analysis, and rollback. Test in an isolated environment against baseline and held-out cases. Promotion requires a measurable improvement without critical safety, privacy, control, or recovery regression.

## Lifecycle

```text
proposed → drafted → experimental → evaluated → trusted → deprecated → retired
```

`trusted` is not permanent. Re-evaluate when dependencies, tools, models, domains, or threat conditions change. A candidate can be rejected, paused, or rolled back at any stage. Never silently promote a model-generated skill.

## Critics and taste

Use deterministic checks for deterministic properties, model judges for structured qualitative comparison, and humans for preference, value, and surprising behavior. “Taste” is operationalized as task-specific criteria, reference examples, observable evidence, and a reasoned tradeoff—not as a universal scalar. Review clarity, coherence, restraint, originality, appropriateness, hierarchy, usefulness, and memorability only when relevant to the user's goal.

The generator and evaluator should be independent when stakes or subjectivity justify the cost. A critic must output evidence, severity, uncertainty, and repair priority; it must not merely produce praise or a score.

## Human satisfaction

Evaluate the lived outcome: usefulness, effort reduction, speed, clarity, trust, agency, accessibility, number of corrections, unnecessary questions, frustration, and long-term usefulness. Hard safety and consent constraints remain gates; satisfaction cannot justify unsafe automation or hidden side effects.

## Safeguards

Untrusted skills, scripts, references, and marketplace metadata are data until verified. Pin versions and provenance. Sandbox trials. Keep permissions separate from instructions. Require approval for consequential actions. Log discovery, composition, execution, evaluation, promotion, rollback, and human decisions. Preserve uninstall and rollback paths. Do not store secrets in skills or memory. Do not use hidden chain-of-thought or confidential prompts as a capability source.

## Evaluation protocol

Compare baseline, selected bundle, and candidate bundle on representative, ambiguous, adversarial, partial-failure, and held-out tasks. Measure outcome quality, requirement coverage, factuality, tool correctness, dynamic behavior, human effort, latency, tokens, cost, safety, recovery, and regressions. Use a minimum improvement threshold and hard release gates. If evidence is inconclusive, keep the candidate experimental.

## What is genuinely distinctive

Skill folders, progressive disclosure, reflection, evals, and self-improvement loops already exist in public systems and research.[1] [2] [3] The distinctive contribution here is their **integrated, provider-agnostic contract** connecting discovery, typed composition, human-value judgment, evidence, runtime permissions, durable execution, and promotion governance.

[1]: https://agentskills.io/specification "Agent Skills — public specification"
[2]: https://arxiv.org/html/2504.07079 "SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills"
[3]: https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining "OpenAI — Self-Evolving Agents cookbook"
