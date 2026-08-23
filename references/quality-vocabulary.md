# Calibrated Quality Vocabulary

Use this reference whenever a user uses an intensity word such as **good**, **best**, **maximum**, **perfect**, or **go to your limit**. These words describe a target and effort policy; they do not grant permissions, imply unlimited resources, or prove success.

## Translation contract

Convert every intensity word into:

> **target → scope → constraints → evidence → budget → stopping rule**

If the user’s wording is ambiguous, preserve the strongest explicit goal and make reversible assumptions visible. Ask one focused question when the interpretation would change architecture, cost, privacy, safety, authority, or likely value.

| Term | Operational meaning | Evidence needed | Stop when |
|---|---|---|---|
| **Basic** | The simplest valid path satisfies the explicit core requirement | Direct artifact check or focused test | The core path works |
| **Good** | Correct, usable, understandable, and complete for the stated main outcome | Must-have acceptance checks and one key failure check | Must-haves pass and no material omission remains |
| **Strong** | Good quality plus robust edge handling, clear structure, and appropriate accessibility | Main path, high-risk edge states, and targeted critique | High-risk defects are resolved |
| **Excellent** | Strong quality plus refined details, low unnecessary effort, and evidence-backed polish | Independent review and relevant live or rendered checks | Additional polish has diminishing value |
| **Best** | The strongest tested option for the task-specific objective and constraints | Same-condition comparison, trade-offs, and evidence | The option wins the defined objective or the trade-off is accepted |
| **Very best** | Best across the agreed dimensions without material safety, cost, accessibility, or user-effort regression | Multi-metric comparison, regression checks, and appropriate human/domain review | The measured Pareto frontier is reached |
| **Top tier** | Verified correctness, reliability, craft, human value, and trustworthy evidence for the task class | Contract gates, live verification, independent critique, and uncertainty report | Critical gates pass and residual issues are disclosed |
| **Maximum** | Highest reasonable rigor within explicit time, cost, compute, permission, and risk limits | Budget ledger, risk review, and proportional verification | Authorized ceiling or diminishing returns is reached |
| **Go to your limit** | Maximum safe, authorized effort that can materially improve the outcome | Checkpoints, budget tracking, and unresolved-unknowns report | Expected value falls, the budget ends, or an authority boundary is reached |
| **Perfect / pixel-perfect** | Exact only against a defined tolerance and observable acceptance condition | Same-condition comparison with explicit tolerance | Tolerance is met; otherwise report measured closeness |
| **Quick / simple** | Smallest sufficient workflow with focused verification | Smoke check and explicit omissions | The requested outcome is reliably achieved |

## Non-equivalences

**Beautiful** is not automatically professional. **Professional** is not automatically usable. **Minimal** is not automatically clear. **Premium** is not automatically valuable. **Pixel-perfect** is not evidence of accessibility or functionality. **Longer** is not automatically more intelligent. **More Skills** are not automatically better.

## Safety and honesty constraints

Do not interpret “maximum,” “full power,” or “go to your limit” as permission to bypass approvals, access private data, perform external side effects, spend money, use unlimited credits, retry forever, or expose private reasoning. Do not call a first render perfect. Do not claim an unmeasured quality improvement. If evidence is missing, label the result `unverified`, `partial`, `needs_review`, or `blocked` as appropriate.

## Examples

| Request | Correct interpretation |
|---|---|
| “Make this the best.” | Define what “best” means for this artifact, compare reasonable options, and verify the chosen option. |
| “Go to your limit.” | Use the highest safe and authorized effort that materially improves the user’s outcome, with a budget and stopping rule. |
| “Make it perfect.” | Ask or define the tolerance and test condition; otherwise report the closest measured result and remaining differences. |
| “Do it quickly.” | Use the smallest sufficient route, preserve must-haves, run a focused check, and disclose what was not tested. |
| “Make it top tier for people.” | Evaluate outcome, effort, clarity, agency, trust, accessibility, emotional ease, dignity, and future usefulness—not praise or engagement alone. |
