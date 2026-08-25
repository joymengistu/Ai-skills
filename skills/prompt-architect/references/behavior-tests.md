# Bounded Prompt-Quality Behavior Tests

These manual contract tests show that Prompt Architect changes vague prompts into clearer, bounded, testable task instructions. They do not prove universal model performance, tool access, or that one wording is always best across providers.

| Case | Starting request | Prompt Architect behavior | Evidence limit |
|---|---|---|---|
| Website build | “Make me a really cool flower shop website.” | Adds audience, primary conversion goal, required pages/states, responsive and accessibility checks, output format, and a rule to label assumptions. | No website was built or visually compared. |
| Research | “Research how AI agents work and make it good.” | Narrows the research question, asks for source quality, fact/inference separation, citations, and unresolved questions. | No external research run was performed. |
| Agent workflow | “Make an agent that finishes my work by itself.” | Preserves the desired outcome but adds authority boundaries, evidence/approval requirements, stop conditions, and honest partial/block labels. | No agent runtime was created or tested. |

## Result

Across all three cases, the Skill replaces generic intensifiers and ambiguous output requests with an outcome, inputs, constraints, output contract, and uncertainty policy. This demonstrates a process change; future tests should compare actual model runs under fixed contexts and evaluate requirement coverage, ambiguity handling, output utility, and hallucinated-action rate.
