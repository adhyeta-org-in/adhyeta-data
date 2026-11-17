# Proofread report — 1987_07, पृष्ठ 1 — भृगुमहर्षिः (story start p001)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p001.md` (scan page 1, images closed). 4 findings: 1 error fixed as a `{del:}/{ins:}` verdict (`पादाचिह्नं`→`पादचिह्नं`), 3 held candidates kept as `{sug-del:}`/`{sug-ins:}` (`भक्तावरपायणः`, `आदागनतगम्य`, `राराजते`→`विराजते`). `scan.py orth` on deblocked text: 0 hits. Quote pass: singles mark Bhrigu's thought (P6), doubles mark Viṣṇu's and Bhrigu's speech (P7, P10); all pairs balanced, no para ships unbalanced. The single `{pb}` joint closes the page on a clean sentence end (`उक्तवान्।`), so the story's continuation on p002 (outside this range) has no continuation dependency. Loc below is `pNN:Pm` + word number within the chunk (lint P numbering, counting all chunks of the page); anchor = first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p001:P8 w12 (भृगुः लज्जाम्) | `भवतः पादाचिह्नं` | `भवतः पादचिह्नं` | SPL | error | high | `पादाचिह्नं` is not a word; "may your footprint stay on my chest in Śrīvatsa-mark form" admits only `पादचिह्नं`; fixed as `{del:पादाचिह्नं}{ins:पादचिह्नं}` per Phase A `{x-com:}` on file |
| 2 | p001:P9 w1 (भक्तावरपायणः आदागनतगम्य) | `भक्तावरपायणः` | `?` | SPL | likely | low* | No Sanskrit parse in this clause; clause-level re-segmentations tested, none fits; possible print corruption; held for human review |
| 3 | p001:P9 w2 (भक्तावरपायणः आदागनतगम्य) | `आदागनतगम्य` | `?` | SPL | likely | low* | No Sanskrit parse; fused/split re-segmentations tested, none fits; possible print corruption; held for human review |
| 4 | p001:P9 w7 (श्रीवत्सचिह्नं राराजते) | `राराजते` | `विराजते` | OCR | likely | medium* | Intensive of √राज् is dubious in this register; print likely dropped `वि` (smallest change, same class as `वधते`→`वर्धते` in p008); held since the sorts verify as `राराजते` |

## Patterns

None — no defect repeats.

## Unverified

- `भक्तावरपायणः` (F2): what would settle it — a dictionary/Heritage check for the compound as a Viṣṇu epithet, or another occurrence of the word in the issue. Kept as a held `{sug-del:}` candidate for human review; not an open task.
- `आदागनतगम्य` (F3): what would settle it — a dictionary/Heritage check for a `गम्य`-final compound fitting "प्रतीकरूपेण", or another occurrence in the issue. Kept as a held `{sug-del:}` candidate for human review; not an open task.
- `विराजते` (F4): what would settle it — confirmation that no intensive `राराजते` reading is intended here (grammar reference or editor judgment). Kept as a held `{sug-del:}/{sug-ins:}` candidate for human review; not an open task.

## Dispositions of Phase A carried candidates

- `पादाचिह्नं` (p001:P8): **ruled** — fixed via `{del:पादाचिह्नं}{ins:पादचिह्नं}`; see F1.
- `भक्तावरपायणः`, `आदागनतगम्य` (p001:P9): **held** — see F2, F3. Every glyph was crop-verified in Phase A (4–6x), so the corruption, if any, is in the print itself, not the transcription.
- `राराजते` (p001:P9): **held** — see F4. Sorts verified (no `वि`) in Phase A.
- Comma after `सर्वोत्तमः` (p001:P10: `सर्वोत्तमः, सः कल्पवृक्षः`): **kept as printed.** Print punctuation, sense-neutral; no block.
- `श्रीवत्सचिह्नरूपेण` (P8, one compound, no anusvara) vs `श्रीवत्सचिह्नं` (P9, separate word with anusvara): **both kept as printed.** Each spelling crop-verified in its place; noted for the compiler, no block.
- Grammar corroboration of contested Phase A readings (no blocks): dual optative `स्यातां` agrees with dual subject `पादौ`; dual `नृत्यमग्नौ`/`ज्ञातवन्तौ` agree with `शिवः पार्वती`; `तिष्ठतु` reads as the blessing imperative; `कठिनस्य`, `योगनिद्रामग्नः`, `सन्तृप्तः`, `कैलासे`/`कैलासं`, `वैकुण्ठे`/`वैकुण्ठं` all parse cleanly in context.

## Coverage appendix

Chunks (lint P numbers include layout/title chunks):

- p001:P1 (layout x-com) : skip layout-declaration chunk
- p001:P2 (भृगुमहर्षिः) : skip title
- p001:P3 कदाचित् मुनीनां : clean
- p001:P4 प्रथमं सः : clean
- p001:P5 कैलासे नृत्यमग्नौ : clean
- p001:P6 वैकुण्ठे विष्णुः : clean (single-quote thought as printed, house style)
- p001:P7 विष्णुः तत्क्षणे : clean (double-quote speech as printed, house style)
- p001:P8 भृगुः लज्जाम् : F1
- p001:P9 भक्तावरपायणः आदागनतगम्य : F2, F3, F4
- p001:P10 सन्तृप्तः भृगुमुनिः : clean (double-quote speech as printed, house style)
- p001:P11 (category) : skip metadata chunk

Joints (from in-file `## Joints` index):

- J1 p001:P10 {pb} -> END (clean break) : ok (ends `उक्तवान्।`; no continuation dependency on p002)
