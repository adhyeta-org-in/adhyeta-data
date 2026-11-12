---
name: chandamama-compile
description: Compile accepted chandamama-issue proofread ranges into final story files. Depends on chandamama-issue: use only after its proofread reports are accepted, when the user supplies ISSUE, RUN, and the accepted START list.
depends_on: chandamama-issue
---

# Chandamama compile

Post-nod step of the chandamama-issue workflow (depends on chandamama-issue: its proofread reports must already be accepted). Applies accepted verdicts to the story files, keeps held candidates as print for a human, re-gates, and records the result. Images never open here; no linguistic judgment happens here — anything the reports left held stays held unless the user lists an explicit override.

## Input (all supplied by the user)

- `ISSUE`, `RUN` (`.logs/<RUN>/`).
- Accepted START list (3-digit, zero-padded: `001`, not `1`). The user edits the list when rejecting any range.
- Optional rejection overrides: specific held items to drop with reason, or cross-range conflict rulings (e.g. `p002-F5 A vs p018-F5 B → keep B`).

## Method (per accepted START, in order)

- Story: `.sources/data/<ISSUE>/p<START>.md`. Report: `.logs/<RUN>/<START>-proofread-report.md`.
- Read the Finalize / User nod and compile section of `.agents/skills/chandamama-issue/SKILL.md` and follow it; the rules below are that section made mechanical.
- Apply: `{del:X}{ins:Y}` → `Y`, lone `{ins:Y}` → `Y`, lone `{del:X}` → drop.
- Never half-apply confidence: any span containing `sug-` stays fully untouched (held in whole) unless the user lists it as an explicit override.
- Keep: held `{sug-…}` as print, user-facing `{x-com:}`, and all `{pb}`/`{pc}`/`{wb}`/`{pgb}` markers (never strip joins).
- Rejections: drop with reason in `## Applied`, do not re-investigate.
- Then, verbatim in this order:
  1. `python3 .agents/tools/chandamama/lint.py --refresh-joints .sources/data/<ISSUE>/p<START>.md` — abort the range if the `## Joints` content changes (verdict application never moves markers across chunks).
  2. `python3 .agents/tools/chandamama/lint.py --phase proofread --story .sources/data/<ISSUE>/p<START>.md` — must be green (final).
  3. `python3 .agents/tools/chandamama/lint.py --phase extract --story .sources/data/<ISSUE>/p<START>.md` — must be green (all verdicts consumed; held `{sug-…}` is extract-legal).
- Append `## Applied` to the report (once — skip if already present): accepted list, dropped holds + reasons, and both gate outputs.

## Do not

- Do not open scan images; do not re-rule held items; do not touch other ranges, JPGs, or logs.
- Write only the accepted story files + their reports. Return a gate table (START × extract/proofread exit codes).
