# Proofread report: 1984_04_sansar p001 (scans 1–4)

## Summary

Loc is `pNN:Pm:wN` (page span NN = scan order, chunk Pm = lint chunk number, word N counted on the chunk from 1); the anchor after Loc is the chunk's first two words.
3 findings (1 STY/style, 2 SPL/error, one SPL/error folded as a 6-instance pattern) plus 1 held KRK candidate (F4, low*); the systematic press problem is a घ-for-ग sort error in घुटिका- (6x) beside a उ-for-ऊ slip in पुर्ववत् (1x).
Every Devanagari body chunk was read for continuity and every joint fit-tested; no passage left unchecked, and the file is print transcription from scans (sansar torch drafts used as keystrokes only, every word verified against the scan in Phase A), not OCR output.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p001:P5:w60 (क्रोशयुगं धावनं) | `आसन्। मम धावनं द्रष्टुम्` | `आसन्। "मम धावनं द्रष्टुम्` | STY | style | high | closing `"` stands without an opener; mate supplied at the certain position before मम |
| F2 | p002:P4:w35 (वैद्येन यथा) | `शरीरं पुर्ववत् स्थूलम्` | `शरीरं पूर्ववत् स्थूलम्` | SPL | error | high | पुर्ववत् is not a word, उ for ऊ; पूर्ववत् confirmed by in-story यथापूर्वं |
| F3 | p002:P8:w16; p003:P2:w3; p003:P3:w5,w27,w42,w58 ("मम समीपे; "प्रतिदिनम् एकैकां; परस्मिन् दिने) | `घुटिका-` (6x: दश घुटिकाः; एकैकां घुटिकां; एकां घुटिकां; घुटिका आहारगुणयुक्ता; घुटिका स्वीकृता; घुटिकाः स्वीकरणीयाः) | `गुटिका-` in all 6 spans | SPL | error | high | घुटिका is not a word, press घ for ग; गुटिका (pill) fits the vaidya's घुटिका/gुटिका dosage in all 6 |
| F4 | p001:P3:w96+1 (कश्चित् ग्रामः) | `परिहसति। उपहासवचनानि शृणोति तदा` | `?` (candidate यदा सोमः held) | KRK | likely | low* | तदा without यदा and with no subject; अन्यः-as-subject tried (wrong sense, the mocker turns sad), सोमः-carried-from-context tried (तदा still dangles); held for the user |

## Patterns

PAT1 press-sort substitution घ for ग: `घुटिका-` for `गुटिका-`, 6 instances (F3: p002:P8:w16, p003:P2:w3, p003:P3:w5,w27,w42,w58); print is consistent (Phase A crops plus draft agreement), so this is one press error repeated, not six independent ones.

## Unverified

U1 (= F4) `यदा सोमः` before उपहासवचनानि (p001:P3): what would settle it is an editorial call, not more text work — Phase A crops verify the print jumps from परिहसति। to उपहासवचनानि with no room for two words, so the print either drops यदा सोमः (press/author ellipsis) or intends the loose reading; supplying two unseen words as a verdict is too invasive, hence held.

## Coverage

p001:P1 {x-com:layout: : skip x-com-only
p001:P2 # स्थूलः : skip title
p001:P3 कश्चित् ग्रामः : F4
p001:P4 अनन्तरं सोमः : clean
p001:P5 क्रोशयुगं धावनं : F1
p001:P6 अतः लज्जितः : clean
J1 p001:P3 {pb} -> p001:P4 fresh : ok
J2 p001:P6 {wb} -> p002:P2 {pc} : ok
p002:P1 {x-com:layout: : skip x-com-only
p002:P2 {pc}दयतः पूर्वमेव : clean
p002:P3 अतः पुनः : clean
p002:P4 वैद्येन यथा : F2
p002:P5 पुनः वैद्यस्य : clean
p002:P6 "मिताहारः कति : clean
p002:P7 "यावज्जीवं मिताहारः : clean
p002:P8 "मम समीपे : F3
J3 p002:P3 {pb} -> p002:P4 fresh : ok
J4 p002:P8 {pb} -> p003:P2 {pc} : ok
p003:P1 {x-com:layout: : skip x-com-only
p003:P2 {pc}"प्रतिदिनम् एकैकां : F3
p003:P3 परस्मिन् दिने : F3
p003:P4 तस्मिन् दिने : clean
p003:P5 एतत् श्रुत्वा : clean
p003:P6 {pc}पश्यतु। माम् : clean
p003:P7 एतत् श्रुत्वा : clean
p003:P8 "यद्यपि भवान् : clean
J5 p003:P5 {pb} -> p003:P6 {pc} : ok
J6 p003:P8 {pb} -> p004:P2 {pc} : ok
p004:P1 {x-com:layout: : skip x-com-only
p004:P2 {pc}दृष्ट्वा हसतां : clean
p004:P3 "श्रीमन्! अहम् : clean
p004:P4 सोमः तु : clean
p004:P5 "तदपि सत्यमेव। : clean
p004:P6 "अत्रैव यथार्थः : clean
p004:P7 {pc}कोऽपि भवन्तं : clean
p004:P8 "वामनस्य वचने : clean
p004:P9 अनन्तरं वामनं : clean
p004:P10 अनन्तरं यद्यपि : clean
J7 p004:P6 {pb} -> p004:P7 {pc} : ok
J8 p004:P10 {pb} -> END : ok
