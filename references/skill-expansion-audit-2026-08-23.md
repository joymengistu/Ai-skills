# Skill catalog expansion audit

## Audit snapshot

The repository contains **61 Skills**. Their current `SKILL.md` files range from **12 to 64 lines**, with an average of **19.5 lines** and an average of approximately **246.7 words**. The shortest group is concentrated in foundational and frequently triggered Skills such as communication, data analysis, coding, creative work, task framing, interaction design, research, memory, planning, self-improvement, accessibility, tool use, multimodal reasoning, safety governance, and tool evaluation.

This confirms the user’s observation that many Skills are intentionally compact. Compactness is not automatically a defect: the Skill Creator guidance treats the context window as a shared resource and recommends progressive disclosure. However, several short Skills can become more useful with operational detail that is specific to their trigger, procedure, evidence, failure modes, examples, and composition boundaries.

## Expansion decision

Use a **deepening protocol**, not blind padding. Each Skill may gain a tailored operational section when the added content provides non-obvious execution value. The expansion must add at least one of: a preflight, decision rule, workflow, failure mode, verifier, example/counterexample, composition contract, stopping rule, or human-value/accessibility boundary. Generic prose copied into every Skill does not count as improvement.

The target is not a uniform line count. Foundational Skills and high-risk Skills deserve more operational detail; narrow utility Skills should remain smaller when additional text would duplicate existing references or increase routing noise. Every expansion must stay under the Skill body limit, preserve progressive disclosure, and be validated with the repository Skill validator.

## Quality rubric

| Dimension | Question |
|---|---|
| Trigger precision | Does the Skill clearly say when to load it and when not to load it? |
| Actionability | Could another agent execute the procedure without inventing the important steps? |
| Requirement preservation | Does it protect the user’s intent and distinguish explicit requirements from assumptions? |
| Evidence | Does it say what counts as proof and what remains unknown? |
| Failure handling | Does it identify common failure modes and the smallest repair? |
| Examples | Does it include useful good, bad, borderline, exception, or transformation examples where relevant? |
| Composition | Are inputs, outputs, dependencies, conflicts, permissions, and handoffs clear? |
| Human value | Does it reduce user effort while preserving agency, accessibility, trust, and recovery? |
| Restraint | Does each paragraph justify its context cost, or is it duplication/decoration? |

## Evidence boundary

| Label | Claim |
|---|---|
| **FACT** | The catalog has 61 Skills and the measured size distribution above. |
| **EVIDENCE** | The Skill Creator guidance explicitly recommends concise Skills, progressive disclosure, and avoiding duplication. |
| **INFERENCE** | The best response to short Skills is selective operational deepening with shared references, not uniform padding. |
| **HYPOTHESIS** | Tailored operational sections will improve first-pass execution and reduce requirement loss more than repeated generic explanation. |
| **UNKNOWN** | Whether expanded Skills improve real hosted-agent outcomes without displacing task context; this requires paired evaluation. |

## Execution strategy

Expand in domain batches: capability framing and completeness; evaluation, evidence, and self-improvement; research, memory, and communication; safety, tools, and hosted execution; UI and human value; then narrow utility Skills. After each batch, run the Skill validators and relevant benchmark cases. Stop expanding a Skill when the rubric is covered, the body would become duplicative, or added text has no new testable behavior.
