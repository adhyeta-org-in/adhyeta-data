## Summary

One finding (F1: gender mismatch `इत्येतां विषयं`, held as an unverified candidate with no inline block since Phase A filed no glyph flag for it). No other defects: the orth scan is clean, proper names are consistent, all quote marks map to an open/close/inner role, and every `{pb}`/`{wb}` joint plus the straight read show continuous grammar and event order. Loc uses story coordinates `pNN:Pm` with the chunk's first two words as anchor and the word index counted on the chunk from 1. The print keeps open sandhi before voiced sounds (`कश्चित् धर्मज्ञानी`, `कदाचित् अपि`, `गुरुः इव`, `लोपः आचरितः`) as a house-style variant throughout; per doctrine these are never flagged. The text is a clean transcription, not OCR output; no passage went unchecked.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p019:P8 ('धनमूलम् इदं), w4 | `इत्येतां विषयं` | `इत्येतं विषयं` | AGR | error | medium* | `विषयः` is masculine but `एताम्` is feminine accusative |

## Patterns

None (single isolated finding; open-sandhi spellings are a deliberate print convention, not a recurring defect).

## Unverified

F1 `इत्येतां विषयं` (p019:P8): the printed `एतां` is certain as transcribed, but the masculine `विषयम्` requires `एतम्`; the one-stroke `तां`/`तम्` difference points to a typesetter slip, yet with no Phase A `{x-com:}` or `{sug-…}` on file no verdict block may be emitted, so the correction `एतम्` is held for the user rather than applied. Settled by accepting `एतम्` (then emit `{del:एतां}{ins:एतं}` at `इत्येतां`) or by keeping the print with a documented reason.

## Coverage

p018:P3 पूर्वं भद्रशीलः : clean
p018:P4 भद्रशीलस्य द्वौ : clean
p018:P5 कथयति स्म। : clean
p018:P6 एकदा लोहकः : clean
p018:P7 भद्रशीलः मन्दं : clean
p018:P1 layout : skip x-com-only chunk
p018:P2 title : skip title heading
p018:P8 author : skip footer metadata chunk
p019:P2 यावत् जानाति : clean
p019:P3 गुर्वर्यस्य एतद्वचनेन : clean
p019:P4 तदा लोहकः : clean
p019:P5 एतत् मम : clean
p019:P6 भद्रशीलः किञ्चित् : clean
p019:P7 आचार्यस्य वचनेन : clean
p019:P8 'धनमूलम् इदं : F1
p019:P1 layout : skip x-com-only chunk
p020:P2 "सुखपूर्वकजीवने धनं : clean
p020:P3 अनन्तरं लोहकः : clean
p020:P4 एतत् अविगणयन् : clean
p020:P5 बालकः 'किं : clean
p020:P6 एतत् श्रुत्वा : clean
p020:P7 तदा भद्रशीलः : clean
p020:P8 लोहकः शिरः : clean
p020:P1 layout : skip x-com-only chunk
J1 p018 col1-col2 : ok (`लघुकथाः अपि` + `कथयति स्म।` one sentence)
J2 p018-p019 page : ok (`भवान्` + `यावत् ... तावत्` correlative complete)
J3 p019 col1-col2 : ok (same speech `आचार्य! ... भवान्?` + `एतत् ... दौर्भाग्यम्`, margin-start `{pc}`)
J4 p019-p020 page : ok (clean break `कृतवान्।` to new-scene narration)
J5 p020 col1-col2 : ok (narration continuous `इति।` to `बालकः ...`, margin-start `{pc}`)
J6 p020 END : ok (story closes `प्रसिद्धः जातः।`)
