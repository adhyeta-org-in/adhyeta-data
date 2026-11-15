# Proofread report: 1986_11 p001 (कल्याणऋषिः, p01 span)

## Summary

1 finding (1 STY/style, high confidence), routed as a verified `{del:}` verdict in the story file; no repeats, so no Patterns section. Print conventions kept as house style throughout: open sandhi at word boundaries (मार्गस्य अन्वेषणं, यदि एतं) and single quotes for all four quoted speeches, matching the 1984_04 precedent where print singles stand. Orth scanner (`scan.py orth` on deblocked text) reports no findings; grammar, sandhi, participle and quote passes done sentence by sentence from text alone. Not checked: the story continues past this one-page span (out of assigned range), so flow is verified only within p001; the text is direct transcription from scans, not OCR output. Loc below uses file page `p001` + lint chunk `P` + word counted on the chunk from 1, with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p001:P5:11 (कल्याणः स्वर्गमार्गस्य) | `तेन: मिलितवान्` | `तेन मिलितवान्` | STY | style | high | stray colon after तेन has no grammatical role (verified in print at 6x); minimal fix is deletion, already applied as `{del::}` |

## Unverified

None. The single inherited Phase A candidate (`{sug-del::}` on the तेन colon) is promoted to verified `{del::}` (F1); no candidate is held for the user. Widest alternative considered (visarga reading तेनः) is ungrammatical, and supplying सह would invent a word, so deletion stands.

## Coverage

p001:P1 {x-com:layout:} : skip x-com-only
p001:P2 {category:} : skip metadata
p001:P3 # कल्याणऋषिः : skip title
p001:P4 पूर्वं कदाचित् : clean
p001:P5 कल्याणः स्वर्गमार्गस्य : F1
p001:P6 कल्याणः सन्तोषेण : clean
p001:P7 कल्याणम् अनुसरन्तः : clean
p001:P8 उपकारं कृतवतः : clean
J1 p001:P8-{pb}->END : ok (clean break; sentence ends with । before bottom art, no continuation)
