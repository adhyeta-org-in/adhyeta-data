# Proofread report — 1984_04, START=001 (scan pages 1–4, story `स्थूलः वामनः च`, complete story)

## Summary

9 findings: 8 error (1 quote-supply, 7 spelling verdicts) and 1 likely held unverified. One systematic problem: `घुटिका` for `गुटिका` throughout (6 spans, F3–F8). One print gap held as `{sug-ins:यदा सोमः}` (F9). `scan.py orth` on deblocked text reports 0 hits. Text is fresh human transcription from scans (not OCR output). Loc below is `pNN:Pm` (scan span + lint chunk) with the first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p001:P5 `मम धावनं` | `आसन्। मम धावनं ... स्थितवन्तः" इति सोमः भावितवान्।` | `{ins:"}` before `मम` | STY | error | high | each para opens and closes its own pair; print keeps the close but drops the open and `इति` + `भावितवान्` pins the speech |
| 2 | p002:P4 `पुर्ववत् स्थूलम्` | `शरीरं पुर्ववत् स्थूलम्` | `{del:पुर्ववत्}{ins:पूर्ववत्}` | SPL | error | high | `पूर्ववत्` is the only Sanskrit form, confirmed by `यथापूर्वं` in p002:P6 |
| 3 | p002:P8 `दश घुटिकाः` | `वैद्यः दश घुटिकाः दत्तवान्।` | `{del:घुटिकाः}{ins:गुटिकाः}` | SPL | error | high | the वैद्य gives pills; `गुटिका` is the pill word and `घुटिका` is not a word |
| 4 | p003:P2 `एकैकां घुटिकां` | `प्रतिदिनम् एकैकां घुटिकां स्वीकरोतु` | `{del:घुटिकां}{ins:गुटिकां}` | SPL | error | high | same as F3; daily one-pill instruction |
| 5 | p003:P3 `एकां घुटिकां` | `सोमः एकां घुटिकां सेवितवान्।` | `{del:घुटिकां}{ins:गुटिकां}` | SPL | error | high | same as F3 |
| 6 | p003:P3 `घुटिका आहारगुणयुक्ता` | `यतः घुटिका आहारगुणयुक्ता आसीत्।` | `{del:घुटिका}{ins:गुटिका}` | SPL | error | high | same as F3 |
| 7 | p003:P3 `यदा घुटिका` | `यदा घुटिका स्वीकृता` | `{del:घुटिका}{ins:गुटिका}` | SPL | error | high | same as F3 |
| 8 | p003:P3 `सर्वाः घुटिकाः` | `सर्वाः घुटिकाः स्वीकरणीयाः` | `{del:घुटिकाः}{ins:गुटिकाः}` | SPL | error | high | same as F3 |
| 9 | p001:P3 `उपहासवचनानि शृणोति` | `{sug-ins:यदा सोमः} उपहासवचनानि शृणोति तदा` | `{sug-ins:यदा सोमः}` kept | KRK | likely | low* | `तदा` with no `यदा` and no overt subject; ellipsis is possible so the insertion stays a candidate |

## Patterns

Pattern A — `घुटिका` for `गुटिका` (6x: F3, F4, F5, F6, F7, F8). Print spells the pill word with `घ` in every occurrence across two page spans; all six are verdict-converted because `घुटिका` is not a Sanskrit word and the medical context pins `गुटिका`.
Patterns B — house variants kept as seen, no findings: open vs joined sandhi side by side (`तद् दिने` in p003:P3 beside `तद्दिने` in the same chunk), doubled consonant (`जीवम्मा` in p001:P3), short mock-exclamations kept in print singles (`'आह, गजराजविराजितमन्दगतिः'` and `'अये कथं ... चलति'` in p001:P3), thought singles balanced across the page turn (`'सूर्यो` + `{wb}{pc}` + `दयतः ... कर्तव्यम्'` in p001:P6–p002:P2).

## Unverified

F9: settle from Chandamama house style for bare `तदा` without `यदा` elsewhere in the issue; the images stay closed in this phase so no glyph re-check applies, and dropping the candidate (reading the subject from the verb ending) is also defensible.

## Coverage

p001:P1 skip layout-only chunk
p001:P2 skip title chunk
p001:P3 कश्चित् ग्रामः : F9
p001:P4 अनन्तरं सोमः : clean
p001:P5 क्रोशयुगं धावनं : F1
p001:P6 अतः लज्जितः : clean
p001:P7 skip author metadata chunk
p002:P1 skip layout-only chunk
p002:P2 दयतः पूर्वमेव : clean
p002:P3 अतः पुनः : clean
p002:P4 वैद्येन यथा : F2
p002:P5 पुनः वैद्यस्य : clean
p002:P6 मिताहारः कति : clean
p002:P7 यावज्जीवं मिताहारः : clean
p002:P8 मम समीपे : F3
p003:P1 skip layout-only chunk
p003:P2 प्रतिदिनम् एकैकां : F4
p003:P3 परस्मिन् दिने : F5, F6, F7, F8
p003:P4 तस्मिन् दिने : clean
p003:P5 एतत् श्रुत्वा : clean
p003:P6 एतत् श्रुत्वा : clean
p003:P7 यद्यपि भवान् : clean
p004:P1 skip layout-only chunk
p004:P2 दृष्ट्वा हसतां : clean
p004:P3 श्रीमन् अहम् : clean
p004:P4 सोमः तु : clean
p004:P5 तदपि सत्यमेव : clean
p004:P6 अत्रैव यथार्थः : clean
p004:P7 वामनस्य वचने : clean
p004:P8 अनन्तरं वामनं : clean
p004:P9 अनन्तरं यद्यपि : clean
J1 p001:P3 {pb} -> p001:P4 fresh : ok (clean break, अनन्तरं opens a new para)
J2 p001:P6 {wb} -> p002:P2 {pc} : ok (सूर्यो + दयतः forms सूर्योदयतः, thought singles balanced across the turn)
J3 p002:P8 {pb} -> p003:P2 {pc} : ok (दत्तवान्। closes the pill-giving speech, प्रतिदिनम् continues it via इत्यपि)
J4 p003:P7 {pb} -> p004:P2 {pc} : ok (भवन्तं + दृष्ट्वा spaced join, speech continues)
J5 p004:P9 {pb} -> END : ok (clean story close)
