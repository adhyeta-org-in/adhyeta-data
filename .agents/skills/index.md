# Skills index

## Skills (`.agents/skills`)

- `chandamama-issue` — run a full Sanskrit Chandamama issue from PDF to gated story files and proofread reports: dispatch one story-agent per range (Phase A transcription then Phase B proofreading), collect reports, verify counts, compile on user nod.
- `chandamama-extract` — transcribe one Sanskrit Chandamama story range from scan images into a single print-faithful story file. Phase A, images open.
- `chandamama-proofread` — proofread one transcribed story file: rule on every candidate from text, house style, and story sense. Phase B, images closed.
- `chandamama-compile` — apply accepted verdicts to final story files and re-gate. Depends on `chandamama-issue`: run only after its proofread reports are accepted (user supplies ISSUE, RUN, accepted START list).
- `sanskrit-proofreading` — generic Sanskrit proofreading: report errors with location, suggested fix, category and confidence, without silently rewriting. Runs `sanskrit/scan.py` on story text.

## Refs (`.agents/refs`)

Reference material, not skills: read by path whenever a skill points at it, never invoked.

- `chandamama-blocks.md` — the closed `{...}` block vocabulary (form and meaning) shared by the Chandamama skills.
- `chandamama/1984_04/` — example story: scan JPGs plus the Phase A (`p01.extract.md`) and Phase B (`p01.proofread.md`) story files, versioned with the skills.
- `sanskrit/` — generic Sanskrit proofreading references (`error-taxonomy`, `prose-checks`, `ocr-and-orthography`, `report-format`, `verse`) shared by `sanskrit-proofreading` and `chandamama-proofread`.

## Tools (`.agents/tools`)

Shared scripts, invoked by path from any skill — never reach into another skill's directory. Grouped by domain, mirroring Refs:

- `chandamama/lint.py` — story-file linter: `lint.py [--json] [--phase extract|proofread] <story.md>`, plus `lint.py --refresh-joints <story.md>` to regenerate the `## Joints` index.
- `sanskrit/scan.py` — orthography/meter scanner (`orth`, `meter`); stdlib only.
