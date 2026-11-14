---
name: chandamama-issue
description: Coordinate a full Sanskrit Chandamama issue run from PDF to gated story files and proofread reports. Use when given an issue PDF (or a whole issue directory) to transcribe and proofread.
---

# Chandamama issue (coordinator)

The coordinator owns the issue run and talks to the user. It never transcribes or proofreads story text itself — it splits the issue into story ranges, dispatches one story-agent per range (≤8 at a time), collects reports, propagates house style, and compiles only on user nod. Leaf work lives in chandamama-extract (Phase A, images open) and chandamama-proofread (Phase B, images closed), both operating on a single story file per range.

## Input and output

- Issue source: `.processing/samskrta_chandamama/<ISSUE>.pdf`. Render with the tool (300 DPI; `--dpi 400` only if print is illegible at 300 DPI):
  `python3 .agents/tools/chandamama/render.py <ISSUE> [--dpi N]`
  This writes `.processing/samskrta_chandamama/<ISSUE>/<NN>.jpg` (`<NN>` = scan sequence, 1-based, no zero-pad), skips pages already rendered, and verifies the count against the PDF. Never hand-roll pdftoppm loops; every agent renders through this script so output is identical every time. and the range index `.processing/samskrta_chandamama/<ISSUE>.story_index` — one story start page per line, `#` comments allowed. Each story runs from its start page to the page before the next start; the last runs to the last scan JPG. (Count JPGs for the issue end; never trust memory.)
- Run log: `.processing/logs/<RUN>/` created once per issue run, `<RUN>` = `<YYYYMMDD_HHMM>_samskrta_chandamama_<issue>` (e.g. `.processing/logs/20261114_0930_samskrta_chandamama_1985_04/`). Pass this path to every story-agent. Create it before dispatching; workers create it if absent (same path — harmless).
- Per story: `.processing/samskrta_chandamama/<ISSUE>/p<START>.md` (story file) + `.processing/logs/<RUN>/<START>-proofread-report.md` (`<START>` = start page zero-padded to 3 digits — story_index `5` → `p005.md`; `000` for prelude). Finished stories persist on disk even if other ranges fail, and a retry redoes only missing ranges.
- Pages before the first start go out as one prelude batch (`p000.md`): transcribe story text if any, else one `{x-com:non-story-page: <what>}` section per page, each closed with bare `{pgb}`.
- Reference pair: `.agents/refs/chandamama/1984_04/p01.extract.md` (what a story file looks like leaving Phase A) and `p01.proofread.md` (what it looks like leaving Phase B), with scans `01.jpg`–`04.jpg`.

## Dispatch

- Orchestration is already decided by this skill: coordination runs in this session, story execution always runs in subagents. Do not ask the generic inline / subagent / fork question — it does not apply here. If the user says "inline," it means coordination-inline; workers are still dispatched.
- Dispatch via the `subagent` tool with the `worker` agent, cwd = repo root, in order. Brief each worker with: issue, range START/END, story-file path, RUN report path, and the instruction to read `chandamama-extract` then `chandamama-proofread` in order (Phase A images-open → gate → Phase B images-closed), write the report directly to the given path, and return only a summary.
- The coordinator's first action after render + RUN setup is dispatch. The coordinator never opens `*.jpg`, never transcribes, never edits story text. Opening a scan is a role violation — if you catch yourself reading a JPG, stop and dispatch instead.
- One story-agent per story range, each writing only its own disjoint files. A story-agent does both phases back-to-back on its range: Phase A (chandamama-extract) until the story file passes the extract gate, then Phase B (chandamama-proofread) on the same file. The boundary is one-way — an agent that finished Phase B never reopens images; leftovers travel as held candidates in the report, never as rework.
- Forward each transcriber's uncertainties in context (same-agent runs carry them automatically); across agents, propagate the issue's established house style (quote sorts, recurring corrections like `घुटिका→गुटिका`), so each mark is decided once per issue, not once per agent. After collecting, sweep the reports for recurring correction pairs across ranges (parallel dispatch can't propagate live) and note conflicts for the user.
- Collect every report. A coordinator that only dispatches and never collects has not finished.

## Gates (story files only, never scattered sidecars)

- Extract gate: `python3 .agents/tools/chandamama/lint.py --phase extract --story .processing/samskrta_chandamama/<ISSUE>/p<START>.md` — verdicts rejected; the only legitimate residuals are notes-only (paired-continuation notes, unbalanced print quotes kept as seen).
- Proofread gate: `python3 .agents/tools/chandamama/lint.py --phase proofread --story .processing/samskrta_chandamama/<ISSUE>/p<START>.md` — re-run after Phase B amends; every error fixed, every note dispositioned in the report.
- After Phase B, only the proofread gate must pass. The extract gate necessarily fails once `{del:}`/`{ins:}` verdicts land and is not re-run as a gate.
- Re-run with `--json` when feeding findings to another tool.
- Run gates exactly as documented here, flags included; never improvise or normalize the command line (a dropped flag can turn a red gate green or crash the tool — test verbatim).

## User nod and compile

- Proofreading reports go to the user; on acceptance of a story's report, the coordinator compiles that range to its final story MD: apply accepted `{del:X}{ins:Y}` verdicts to `Y` (lone `{ins:Y}` → `Y`, lone `{del:X}` → drop), keep held `{sug-…}` candidates as print for a human, keep user-facing `{x-com:}` notes, and keep `{pb}`/`{pc}`/`{wb}`/`{pgb}` markers as the audit trail (compile never strips joins). Then re-run both gates green and append `## Applied` to the story's report file with gate results.
- Route nothing back to transcription. A held candidate the user rejects is dropped with reason in the `## Applied` entry, not re-investigated.

## Finalize

- Verify counts: every story_index start has one `p<START>.md`; every story file passes `--phase proofread --story`; every story has its `<START>-proofread-report.md` with `## Applied` where accepted.
- Spot-read one mid-issue page and report file count, total bytes, and residual uncertainties as transcribed-as-seen with the block used.
- Every linter note across the issue needs a disposition in the final report: accepted print-faithful (with reason) or fixed via block. A green gate with unreviewed notes is not done. A failed batch leaves no partial page sections behind (agents write only complete sections); re-run the same range to continue after the last complete `{pgb}`.
