# Intent-Resolution Contract

Use this contract before choosing an interpretation when a request is ambiguous, compressed, typo-heavy, or carries several plausible outcomes. The goal is to reduce unnecessary questions without silently choosing an architecture, cost, privacy, safety, external-action, or high-value decision for the user.

## Required record

```yaml
intent_record:
  literal_request: "What the user actually said"
  desired_outcome: "The real-world result being sought"
  context: "Relevant project, artifact, or conversation state"
  explicit_requirements: []
  non_goals: []
  candidate_intents:
    - interpretation: "Candidate meaning A"
      evidence: []
      confidence: 0.0
      impact_if_wrong: low|medium|high
      reversibility: easy|moderate|hard
  selected_interpretation: "A candidate or unresolved"
  decision: continue|ask_one_question|offer_options|defer|refuse_unsafe_part
  assumption: "Only if the selected interpretation is reversible"
  correction_path: "How the user can change the interpretation"
  expiry: "conversation|task|project|explicitly_saved"
```

Do not expose internal hidden reasoning. Provide a concise decision summary, meaningful assumption, alternatives when useful, and one focused question when needed.

## Decision policy

| Situation | Action |
|---|---|
| One interpretation is strongly supported, low-risk, reversible, and easy to correct | Continue with the assumption and state it briefly |
| Several interpretations are plausible but the result is cheap to revise | Offer the smallest useful draft or two concise options |
| The choice changes architecture, cost, privacy, safety, external effects, or likely value | Ask one focused clarification before committing |
| The user’s current correction conflicts with memory or an earlier guess | Prefer the correction, update only scoped conversation state, and do not defend the old guess |
| The request contains an unsafe or unauthorized part | Refuse that part and offer the safest useful alternative |
| Evidence is weak and no reversible default exists | Mark the intent unresolved and defer the consequential choice |

## Required separations

Keep these distinct:

- **Intent:** what the user means.
- **Output preference:** what form or level of detail may help.
- **Next step:** an optional action that may be useful.
- **Correction:** a possible misunderstanding to test.
- **Preference:** a scoped, user-provided collaboration choice.

A predicted next step is not permission. A remembered preference is not a current requirement. A fluent interpretation is not evidence of confidence.

## Quality checks

Before acting, confirm that explicit requirements survived, unknowns are visible, assumptions are reversible where possible, the user can correct the route, and no prediction authorizes a side effect. After correction, record the error cause and update only the relevant scope. Do not turn one typo, reaction, or successful guess into a universal rule.

## Compact examples

| Request | Good resolution | Failure to avoid |
|---|---|---|
| “Make it like the last one” | Identify the referenced artifact; ask if multiple candidates exist | Guessing from an unrelated memory |
| “Use the skill thing” | Treat as likely Agent Max or Skill curation; offer the two interpretations if the difference matters | Loading every Skill or pretending certainty |
| “Do whatever is needed” | Use reasonable reversible implementation choices; still ask before consequential external actions | Treating it as unlimited authority |
| “Make this professional” | Ask or infer the product context, audience, device, and quality dimensions; preserve explicit style constraints | Replacing the user’s intent with generic beautification |
