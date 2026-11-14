# Proofread report: 1984_07 p052 (चिन्तारहस्यम्, 52.jpg only, last page of issue)

## Summary

Range p052 is a single complete page (1col, art bottom full-width) holding one short story, transcribed in Phase A and ruled here with images closed. 3 findings: 2 style/high verdicts already landed as blocks (F1 quote-nesting sort at the speech open, F2 wrap-hyphen split) and 1 held SPL/likely/medium* candidate (F3 बन्धवेषु) awaiting a dictionary/tool check. No repeats, so no Patterns section. Orth scan on deblocked text returned 0 hits; this is direct transcription, not OCR output, and the whole range was read sentence by sentence with no unchecked passages.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p52:P5:6 (जगन्नाथः दीर्घं) | `--- 'भवन्तं` | `--- "'भवन्तं` | STY | style | high | outer उक्तवान्-speech takes DQ while the inner इति-चिन्तितवान् thought keeps SQ (DQ SQ...SQ DQ nesting) |
| F2 | p52:P5:21 (जगन्नाथः दीर्घं) | `अतः काऽपि-चिन्ता न` | `अतः काऽपि चिन्ता न` | STY | style | high | line-end hyphen splits two words that form no compound; wrap artifact kept in print, split in reading |
| F3 | p52:P6:26 (तदा सोमनाथः) | `मम बन्धवेषु` | `मम बान्धवेषु` | SPL | likely | medium* | बन्धव- is no standard stem for kinsman; held for check (see Unverified) |

Loc is `p52:Pm` (scan 52, file chunk m) with the whitespace-token index on that chunk; anchor words are the chunk's first two words.

## Unverified

- F3 `बन्धवेषु` (held as `{sug-del:बन्धवेषु}{sug-ins:बान्धवेषु}`, never applied): tried बान्धवेषु (loc pl of बान्धवः, kinsman; one-mātrā change ब→बा) against बन्धुषु (loc pl of बन्धुः; larger change); बान्धवेषु fits the punchline sense (no childless kinsman left to inherit from) but बन्धव is not verifiable from text alone. Settles with: Heritage Platform / dictionary lookup of बन्धव vs बान्धव, then promote the sug pair to `{del:}/{ins:}` or drop it.

## Coverage

p52:P1 {x-com:layout: 1col, : skip x-com-only
p52:P2 # चिन्तारहस्यम् : skip title
p52:P3 जगन्नाथः एकः : clean
p52:P4 एतत् दृष्ट्वा : clean
p52:P5 जगन्नाथः दीर्घं : F1, F2
p52:P6 तदा सोमनाथः : F3
J1 p52:P6 {pb} -> END : ok (clean break; punchline इति। closes the story at issue end)
