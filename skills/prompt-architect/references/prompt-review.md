# Prompt Review

## Review rubric

| Check | Pass condition | Repair if it fails |
|---|---|---|
| Intent conservation | Every explicit user requirement appears or is visibly deferred. | Restore missing requirement or explain the deferral. |
| Outcome clarity | A reader can tell what artifact, decision, or state is required. | Replace vague verbs with an observable end state. |
| Input sufficiency | The prompt contains the information needed for the next decision. | Add only relevant context; ask one material question if needed. |
| Constraint clarity | Scope, format, authority, and key limits are explicit. | Separate musts, non-goals, and unknowns. |
| Instruction coherence | No contradictory priorities or duplicated directives. | Resolve conflict and remove repetition. |
| Output utility | The requested format can be used immediately by the person or next agent. | Specify sections, schema, or file type. |
| Verification honesty | Claims have an appropriate evidence path and failure state. | Add evidence/uncertainty language; do not simulate proof. |
| Economy | Every line changes behavior or output. | Remove role-play, filler, and decorative adjectives. |

## Common repairs

| Weak wording | Better wording |
|---|---|
| “Make the best website ever.” | “Build a responsive landing page for [audience] that makes [primary action] clear in the first screen; include [sections] and verify desktop/mobile rendering.” |
| “Use all skills and make it perfect.” | “Select the smallest relevant Skill route, state the route, preserve [requirements], verify [checks], and label unverified work.” |
| “Research this deeply.” | “Use primary sources where possible; distinguish facts, inference, and unknowns; return [answer structure] with citations.” |

## Stop rule

Stop after one material critique pass when the prompt preserves intent, has no contradiction, requests an observable output, and names how uncertainty is handled. More prompt length is not automatically more control.
