# Report format

The report is Markdown. Write each paragraph as a single line (no hard wrapping). Quote and suggest in Devanagari.

## Structure

1. **Summary** (three to five lines): the number of findings by severity, the one or two systematic problems (for example, "`ब`/`व` swapped throughout"), the passages you could not check, and whether the text appears to be OCR output.
2. **Findings**: a table, sorted by position in the text.
3. **Patterns** (only if there are repeats): one entry per recurring problem, with a count and two or three example locations.
4. **Unverified**: forms you flagged below high confidence without checking a tool or dictionary, each with what would settle it.
5. **Corrected text**: only if the user asked for it. Apply `high` and `medium` findings only, and list in a closing line what you left unchanged and why.
6. **Coverage** (appendix, required): one disposition line per story paragraph, built during the pass — see Coverage appendix below. A report without it is incomplete.

## Findings table

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | 3:14 | `राम:` | `रामः` | ENC | error | high | ASCII colon used for visarga |
| 2 | 5:2 | `वनं गच्छति तत` | `तत्` | OCR | likely | medium | final halant probably dropped; `तत` is not a Sanskrit word |
| 3 | 9:20 | `रामः फलं खादितम्` | `रामेण फलं खादितम्` or `रामः फलं खादितवान्` | KRK | error | high | nominative agent with a passive `kta` participle |

- **Loc** is `line:column` for a character-level finding and `line:word` (counting words on that line from 1) for a word-level finding. Say which you use in the summary.
- **Original** quotes enough context to find the place (the word and a neighbour), nothing more.
- **Suggestion** is the minimal change. When two fixes are possible, give both separated by "or". When no suggestion is possible, write `?` and say why in **Why**.
- **Cat**, **Sev**, **Conf** follow `error-taxonomy.md`. Append `*` to **Conf** for `unverified`.
- **Why** is one short sentence naming the rule or the OCR hypothesis. Do not teach grammar in this column.

## Coverage appendix

One line per story paragraph, in order, written as you finish that paragraph during the pass — never reconstructed from memory afterwards. Format: `P<n> <first two words> : clean`, or `P<n> <first two words> : F<k>[, F<j>...]` naming the findings that touch it, or `P<n> <first two words> : skip <reason>` for non-story lines such as headers and English summaries. Verify before filing: the `P` line count equals the story's paragraph count, the anchors match the source paragraphs in order, and every finding number appears on at least one line. A finding that cites a paragraph with no corresponding line, or a line whose anchor does not match the source, fails verification.

## Rules

- Never put a finding in the table that you would not stand behind in a code review. A hunch goes in **Unverified**.
- Do not praise the text, and do not explain Sanskrit grammar beyond the rule you cite. The user wants a list of defects.
- For scanner output, merge duplicates: several JSON findings at the same place are one row.
- If the text looks clean, say so in the summary and list only the `variant` and `style` notes, if any.

## Optional machine-readable form

If the user wants the findings in a file for another tool, emit JSON with the same fields as the table (`loc`, `original`, `suggestion`, `category`, `severity`, `confidence`, `unverified`, `why`), one object per finding.

## Worked mini-example

Input (`Loc` below is `line:column`):

```
1: राम: वनं गच्छति |
2: सोपी वन गच्छति ।
3: रामः फलं खादितम् ।
```

Scanner hits on line 1 (`colon-for-visarga` on `:` and `pipe-for-danda` on `|`) confirm directly. Lines 2-3 need the word-level pass: `सोपी` and bare `वन` are not scanner hits but grammar shows dropped signs; line 3 is a syntax error, not OCR.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | 1:4 | `राम:` | `रामः` | ENC | error | high | ASCII colon used for visarga |
| 2 | 1:17 | `गच्छति \|` | `गच्छति ।` | ENC | error | high | pipe used for danda |
| 3 | 2:1 | `सोपी` | `सोऽपि` | OCR | likely | medium | avagraha probably dropped; confirm `सः + अपि` reading from context |
| 4 | 2:6 | `वन गच्छति` | `वनं गच्छति` | OCR | likely | medium | final anusvāra probably dropped; accusative destination needs `वनम्` / `वनं` |
| 5 | 3:1 | `रामः फलं खादितम्` | `रामेण फलं खादितम्` or `रामः फलं खादितवान्` | KRK | error | high | nominative agent with a passive `kta` participle |
