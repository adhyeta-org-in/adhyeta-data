# Proofread report: 1987_06 p001 (pages 1-1)

## Summary

Zero findings: no verdict (`{del:}`/`{ins:}`) or candidate (`{sug-}`) blocks were added, and the story file is byte-identical apart from blocks (none added). Loc below is keyed on story coordinates `p001:Pm` plus the first two words as anchor, counting words on the chunk from 1. The `orth` scanner reported no hits, and the proofread gate is green with no notes. Variants kept as print: `एकदां` (anusvāra, verified in print), the house spelling `जाजालिः` (consistent across all five nominative occurrences; vocative `जाजले`), and the edition's open-sandhi style (`तस्य शीर्षम्`, `ते शावकाः`). One item is held as unverified (title display spelling vs body spelling); the images stayed closed throughout Phase B.

## Findings

No findings.

## Patterns

None.

## Unverified

| # | Loc | Original | Suggestion | Cat | Conf | Why | What would settle it |
|---|---|---|---|---|---|---|---|
| U1 | p001:P3 `# जा जि.लिः` | `जि.` (middle akshara with i-mātrā plus a distinct dot) vs body `जाजालिः` | `?` | CNS | low* | Title display type reads `जा जि.लिः`, differing from the consistent body spelling `जाजालिः`; letter-spaced display sorts can mimic mātrās and dots, so the print intent is uncertain. | Reopening the title crop to rule whether the hook and dot belong to the display sort or spell `जाजिलिः`; out of scope with images closed, so print is kept as seen and no block is emitted. |

## Coverage

- p001:P1 `{x-com:layout:` : skip layout-only chunk
- p001:P2 `{category: पुराणगाथावली` : skip metadata chunk (node content proofread: series label with printed separator, matches sibling-issue convention)
- p001:P3 `# जा जि.लिः` : skip title chunk (see U1)
- p001:P4 पूर्वसमुद्रतीरे अरण्ये : clean
- p001:P5 एकदां सः : clean
- p001:P6 दिनानि अतीतानि। : clean
- p001:P7 समुद्रस्नानसमये चटकयोः : clean
- p001:P8 राक्षसस्य आदेशानुसारं : clean
- J1 p001:P8 {pb} -> END (clean break) : ok
