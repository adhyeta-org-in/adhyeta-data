## Summary

Range p041 (scans 41–44: स्नुषायाः शक्तिः complete in 4 pages): 3 findings — 1 direct-speech sort normalization singles-to-doubles (F1), 2 held candidates (F2, F3). Systematic issue: one direct speech printed in singles where Era house style uses doubles, normalized via verdict. Orth scanner (`scan.py orth`) on 50 deblocked lines: 0 hits. No joint ruptures, so no Moves. Two items held for the user (F2, F3); nothing else unverified. Loc below is `pNN:Pm` (scan sequence + chunk per lint `P` numbers) plus the first two words as anchor, with 1-based word counts excluding blocks.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p043:P2 सा आनीतं w7,w13 | `'हे…नयत्'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with vocative, imperatives, reporting verb and इति takes doubles (print singles verified at 3x in Phase A) |
| F2 | p044:P6 इदानीम् अपि w6 | `त्रिवाम् अपि` | `{sug-del:त्रिवाम्}{sug-ins:त्रिवारम्}` | OCR | likely | medium* | त्रिवाम् is not a word; त्रिवारम् fits the three just-narrated incidents (त्रिवारं two lines above) with one dropped र; print read verified at 3x so held |
| F3 | p043:P2 सा आनीतं w13 | `एतत् नयत्` | `{sug-del:नयत्}{sug-ins:नयतु}` | OCR | likely | medium* | parallel honorific उत्तिष्ठतु to the same addressee requires नयतु; print lacks ु at 3x so held |

## Unverified

F2 (`त्रिवाम्` → `त्रिवारम्`, p044:P6 w6): held as `{sug-del:}{sug-ins:}`. Print reads त्रिवाम् at 3x (Phase A crop-verified), so the dropped-र is a print slip if the sense hypothesis is right. Would settle it: re-examine scan 44 left column (`इदानीम् अपि…` line) for a faint र, or dictionary check that त्रिवाम् has no stem. Sense strongly favors त्रिवारम् (three incidents narrated, lines drawn त्रिवारं).

F3 (`नयत्` → `नयतु`, p043:P2 w13): held as `{sug-del:}{sug-ins:}`. Print reads नयत् with no ु at 3x (Phase A crop-verified against उत्तिष्ठतु which shows ु). Would settle it: re-examine scan 43 left column (`एतत् नयत्` line) for a lost ु, or editorial decision for the honorific imperative. Sense strongly favors नयतु (parallel उत्तिष्ठतु, same addressee, command context).

## Coverage

p041:P1 {x-com:layout: : skip (layout chunk)
p041:P2 स्नुषायाः शक्तिः : skip (title)
p041:P3 पूर्वं चीनादेशे : clean
p041:P4 एकदा सः : clean
p041:P5 केषाञ्चित् दिनानाम् : clean (thought singles kept as seen)
p041:P6 तस्मिन् ग्रामे : clean (J1 trailing)
p041:P7 पुरतः अश्वं : clean (J1)
p041:P8 तत्र एका : clean
p041:P9 मातः, अहं : clean
p041:P10 स्थलदानं मम : clean
p041:P11 गृहस्वामी कुत्र : clean
p041:P12 अहम् एका : clean (J2 trailing; edge-spanning open)
p041:P13 {category: : skip (footer + page close)
p042:P1 {x-com:layout: : skip (layout chunk)
p042:P2 पुत्रः। सः : clean (J2; edge-spanning close)
p042:P3 तर्हि भवत्याः : clean
p042:P4 किमर्थं पृच्छति : clean (J3 trailing)
p042:P5 उक्तवती वृद्धा। : clean (J3)
p042:P6 एतं वृत्तान्तं : clean
p042:P7 कीदृशं विचित्रम्? : clean
p042:P8 अनाथाम् एतां : clean
p042:P9 एतत् भवता : clean
p042:P10 वृद्धायाः एतत् : clean
p042:P11 दुष्टपीडाभ्यः पीडितानां : clean (nested singles kept)
p042:P12 किञ्चित्कालानन्तरं स्नुषा : clean (J4 trailing)
p043:P1 {x-com:layout: : skip (layout chunk)
p043:P2 सा आनीतं : F1, F3
p043:P3 वृद्धा दीपम् : clean
p043:P4 एषः अश्वः : clean
p043:P5 तदा योधः : clean
p043:P6 अतिथिः गृहम् : clean
p043:P7 भवती तथा : clean
p043:P8 तस्य दृष्ट्या : clean
p043:P9 सा शीघ्रं : clean (J5 trailing)
p043:P10 परिवेषितवती। : clean (J5)
p043:P11 अस्माकं भोजनं : clean
p043:P12 तथा नास्ति। : clean
p043:P13 भोजनानन्तरं योधः : clean
p043:P14 एतत् वचनं : clean (J6 trailing)
p044:P1 {x-com:layout: : skip (layout chunk)
p044:P2 त्वरा मास्तु : clean
p044:P3 सा एकस्याः : clean
p044:P4 सा त्रिवारं : clean
p044:P5 एतत् दृष्टवतः : clean
p044:P6 इदानीम् अपि : F2 (J7 trailing; edge-spanning pair)
p044:P7 इति उक्तवान् : clean (J7)
p044:P8 समीचीनम्, अहम् : clean
p044:P9 विना आयुधं : clean (thought singles kept)
p044:P10 असहायानां रक्षणं : clean
p044:P11 अनन्तरदिने उषःकाले : clean (J8 trailing; story END)
J1 p041:P6 -> p041:P7 : ok (continues)
J2 p041:P12 -> p042:P2 : ok (continues; edge-spanning speech pair)
J3 p042:P4 -> p042:P5 : ok (continues)
J4 p042:P12 -> p043:P2 : ok (clean break)
J5 p043:P9 -> p043:P10 : ok (continues)
J6 p043:P14 -> p044:P2 : ok (clean break)
J7 p044:P6 -> p044:P7 : ok (continues; edge-spanning इति pair)
J8 p044:P11 -> END : ok (clean break)
