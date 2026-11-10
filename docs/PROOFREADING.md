# Proofreading

## Sanskrit Chandamama (data/www/sa/k/samskrta-chandamama)

- Produce proofreading input with the installed `adhyeta md` CLI (`adhyeta md --root . --out <dir>`), then proofread per the Sanskrit Proofreading skill (see skills index).
- Chandamama print does NOT apply sandhi consistently (open and joined forms mix, e.g. तद् दिने vs तद्दिने). Match the print; do not flag open junctions as errors. Record them as house-style variants.
- Report verdicts for this corpus are against print fidelity, not classical perfection.
- Write log to <project-root>/.logs
- Each `.logs` entry proves full coverage with a per-paragraph appendix built during the pass, never reconstructed afterwards: one line per story paragraph in order, `P<n> <first two words> : clean`, `P<n> <first two words> : F<k>[, F<j>...]` naming touching findings, or `P<n> <first two words> : skip <reason>` for non-story lines. Worker briefs must demand it. Verify before filing: the `P` line count equals the story's paragraph count, anchors match the source in order, every finding number appears on at least one line. A report without a passing appendix is incomplete and its verdicts are unverified.
- Crash safety: each worker writes its own `.logs` entry directly (one distinct file per story, never shared paths), including the coverage appendix. The coordinator never funnels work product through its own context: it verifies the entries exist, spot-checks appendices mechanically, and only then summarizes. A coordinator crash must never lose worker output.
