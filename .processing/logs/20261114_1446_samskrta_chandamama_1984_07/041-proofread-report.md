# Proofread report: 1984_07 p041 विष्णुकथा (scans 41–47)

## Summary

Fifteen findings: six `error` (all `STY` quote defects: four mismatched open/close sorts, two missing opens), one `likely` (`MRP` non-word held as candidate), three `variant` (odd word-forms kept as print), five `style` (balanced single-quoted speech normalized to doubles). The systematic issue is print punctuation: most dialogue opens with a single stroke and several closes carry a double, so `'…"` pairs are genuinely mismatched; balanced `'…'` speech is normalized to `"…"` wherever a reporting verb plus `इति` pins speech, against in-text doubles precedent (Narada p043:P5). Orth scanner ran on deblocked text with two hits, both confirmed in context as print exclamations (`जातः!` p042:P6, `पश्यन्ति!` p047:P2), not dandas. Every Devanagari chunk was read sentence by sentence; all 14 joints verified text-continuous against the asserted layouts. Loc is `pNN:Pm w<word>` (scan-sequence page, lint chunk number, 1-based word index on the deblocked chunk) plus a two-word anchor. The text is human transcription, not OCR.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p041:P4 w1 ("देवि! किञ्चित्) | `'देवि!` | `{del:'}{ins:"}देवि!` | STY | style | high | Vishnu's assurance (उक्तवान् + इति) is speech; doubles mark speech here (Narada p043:P5) |
| 2 | p042:P2 w3 (आसीत्। तदा) | `'एतस्याः` | `{del:'}{ins:"}एतस्याः` | STY | style | high | bodiless-voice proclamation + इति is speech; doubles |
| 3 | p042:P3 w13 (एतत् श्रुत्वा) | `--- 'देवक्याः` | `--- "देवक्याः` via `{del:'}{ins:"}` | STY | style | high | Vasudeva's plea (प्रार्थितवान्) + इति is speech; doubles |
| 4 | p042:P7 w4 (विष्णुः योगमायां) | `'भवती` | `{del:'}{ins:"}भवती` | STY | error | high | command + इति is speech; print's open-single/close-double is mismatched |
| 5 | p042:P7 w10 (प्रविशतु" इति) | `इति आज्ञसवान् ।` | `इति {del:आज्ञसवान्}{sug-ins:आज्ञप्तवान्} ।` | MRP | likely | medium* | print form is no Sanskrit word; sense (order + तथैव आचरितवती) needs ज्ञप्तवान्; alternative आज्ञापितवान्, so held |
| 6 | p042:P8 w15 (देवकी अष्टमवारं) | `नाशनीयः"` | `नाशनीयः{del:"}{ins:'}` | STY | error | high | resolve with चिन्तयित्वा is thought; singles mark thought |
| 7 | p043:P3 w26 (कंसः धावन्) | `'अये` | `{del:'}{ins:"}अये` | STY | error | high | goddess's utterance (उक्तम्) + इति is speech; print's open-single/close-double is mismatched |
| 8 | p044:P5 w1 ("कृष्णेन मृत्तिका) | `'कृष्णेन` | `{del:'}{ins:"}कृष्णेन` | STY | style | high | reported speech (श्रुत्वा + इति); doubles |
| 9 | p044:P9 w11 ('कृष्णबलरामौ एव) | `'धनुर्यागव्याजेन` | `{del:'}{ins:"}धनुर्यागव्याजेन` | STY | style | high | Kamsa's spoken order (उक्त्वा) + इति is speech; doubles (the resolve itself stays singles as thought) |
| 10 | p045:P9 w20 (मुचुकुन्दः देवासुरसङ्ग्रामे) | `'द्वापरयुगे` | `{del:'}{ins:"}द्वापरयुगे` | STY | error | high | gods' speech (उक्तवन्तः) + इति; print's open-single/close-double is mismatched |
| 11 | p045:P13 w7 (अनन्तरं कृष्णः) | `जातः। भवान्` | `जातः। {ins:"}भवान्` | STY | error | high | Krishna's spoken order + इति has a close but no open; boundary pinned at भवान् |
| 12 | p046:P3 w1 (येन उन्नीतं) | `येन उन्नीतं` | `{ins:"}येन उन्नीतं` | STY | error | high | bodiless-voice utterance + इति has a close but no open; relative-clause start pins it |
| 13 | p043:P4 w3 (गोकुले कृष्णस्य) | `कृष्णस्य जननना` | `?` keep print | MRP | variant | medium* | analogical -न- ktavatu for जन् (standard जात); kept as print variant |
| 14 | p043:P4 w10 (गोकुले कृष्णस्य) | `जन्मोत्सवं आंचरितवन्तः` | `?` keep print | SPL | variant | low* | non-standard nasal in आचरित; kept as print; settles with dictionary/print check |
| 15 | p047:P3 w8 (क्रुद्धः शिशुपालः) | `अग्नेः आहुतित्वेन समर्पितवान्` | `?` keep print | KRK | variant | low* | odd instrumental of purpose (sense = as an offering, clear); kept as print idiom |

## Patterns

- Single-stroke speech opens normalized to doubles (F1, F2, F3, F4, F7, F8, F9, F10: 8 instances): the compositor prints dialogue opens with one stroke and often closes with two; every instance pinned by reporting verb plus इति-closure and backed by in-text doubles for speech (F12-style supplied opens and Narada/Muchukunda/Satvati passages). Thought-singles (चिन्तयित्वा, निश्चितवान्) deliberately untouched.

## Unverified

- F5 `आज्ञसवान्` (p042:P7): removal certain (no such word), replacement held between `आज्ञप्तवान्` (one-ligature change प्त for स) and `आज्ञापितवान्` (same sense). Settles with: coordinator print check at 5x+ whether the second-line onset is स, प्त, or पि.
- F13 `जननना`, F14 `आंचरितवन्तः`, F15 `आहुतित्वेन` (all `?` keep-print): settle with a dictionary/grammar check (F13/F14) and a parallel-text or print check (F15); upgrade to verdicts only if confirmed.
- U1 agreement mismatch p041:P7 (देवासुराणां युद्धे): `जरासन्धः महाक्रूरी अतीव बलशाली च` pairs feminine adjectives with masculine जरासन्धः. No file block emitted: Phase B invents no new glyph claims and Phase A left no flag on these words, so the print stands pending a coordinator print check (ूरी/शाली vs ूरः/शालः); if print confirms, leave for the compiler as a print misprint.

## Coverage

p041:P1 {x-com:layout: : skip layout-only chunk
p041:P2 # विष्णुकथा : skip title
p041:P3 कृतत्रेतायुगयोः अनन्तरं : clean
p041:P4 "देवि! किञ्चित् : F1
p041:P5 कालनेमिः नाम : clean
p041:P6 नगरस्य महाराजः : clean
p041:P7 देवासुराणां युद्धे : clean (agreement note U1, no block)
p041:P8 उग्रसेनस्य अनुजस्य : clean
p041:P9 {category: कृष्णावतारः} : skip footer metadata
p042:P1 {x-com:layout: : skip layout-only chunk
p042:P2 आसीत्। तदा : F2
p042:P3 एतत् श्रुत्वा : F3
p042:P4 कंसः एतत् : clean
p042:P5 विष्णोः आज्ञानुसारं : clean
p042:P6 गर्भे स्वकीयम् : clean (scanner `जातः!` confirmed print exclamation)
p042:P7 विष्णुः योगमायां : F4, F5
p042:P8 देवकी अष्टमवारं : F6
p042:P9 श्रावणमासे कृष्णपक्षे : clean
p042:P10 एषः पुत्रः : clean
p042:P11 महाविष्णोः प्रेरणानुसारं : clean
p042:P12 तस्मिन् काले : clean
p043:P1 {x-com:layout: : skip layout-only chunk
p043:P2 एव एकां : clean
p043:P3 कंसः धावन् : F7
p043:P4 गोकुले कृष्णस्य : F13, F14
p043:P5 एकदा नारदः : clean
p043:P6 एतेन कंसः : clean
p043:P7 निरङ्कुशः कंसः : clean
p043:P8 आहूय, तान् : clean
p043:P9 अनन्तरं कंसेन : clean
p044:P1 {x-com:layout: : skip layout-only chunk
p044:P2 बालः कृष्णः : clean
p044:P3 कृष्णस्य लीलाविनोदाः : clean
p044:P4 कृष्णस्य पीडा : clean
p044:P5 "कृष्णेन मृत्तिका : F8
p044:P6 कालियसर्पस्य फणानां : clean
p044:P7 कदाचित् गोकुलनिवासिनः : clean
p044:P8 कृष्णः वेणुगोपालः : clean
p044:P9 'कृष्णबलरामौ एव : F9
p044:P10 बालः कृष्णः : clean
p045:P1 {x-com:layout: : skip layout-only chunk
p045:P2 शिखाग्रहणपूर्वकम् आकृष्य : clean
p045:P3 अनन्तरं कृष्णः : clean
p045:P4 जरासन्धः कृष्णस्य : clean
p045:P5 दुष्टः जरासन्धः : clean
p045:P6 आक्रमणं कृतवान्। : clean
p045:P7 कृष्णः ततः : clean
p045:P8 मुचुकुन्दः इक्ष्वाकुवंशीयस्य : clean
p045:P9 मुचुकुन्दः देवासुरसङ्ग्रामे : F10
p045:P10 तदा मुचुकुन्दः : clean
p045:P11 देवाः तथैव : clean
p045:P12 कृष्णम् अनुधावन् : clean
p045:P13 अनन्तरं कृष्णः : F11
p045:P14 शापग्रस्तौ जयविजयौ : clean
p046:P1 {x-com:layout: : skip layout-only chunk
p046:P2 वन्तौ। चेदिदेशस्य : clean
p046:P3 येन उन्नीतं : F12
p046:P4 एतत् दृष्ट्वा : clean
p046:P5 कालान्तरे जरासन्धः : clean
p046:P6 कृष्णः समुद्रं : clean
p046:P7 जरासन्धः अन्तिमतया : clean
p046:P8 पुनरपि आक्रमणं : clean
p046:P9 इतः पूर्वम् : clean
p046:P10 एतत् दृष्ट्वा : clean
p046:P11 जरासन्धादयः "कृष्णबलरामौ : clean
p047:P1 {x-com:layout: : skip layout-only chunk
p047:P2 पश्यन्ति! : clean (scanner `पश्यन्ति!` confirmed print exclamation)
p047:P3 क्रुद्धः शिशुपालः : F15
p047:P4 जरासन्धः द्वारकां : clean
p047:P5 विदर्भराजस्य भीष्मकस्य : clean
p047:P6 रुक्मिण्याः अग्रजः : clean
p047:P7 रुक्मिणी कृष्णं : clean
p047:P8 कृष्णम् अवरोद्धुं : clean
p047:P9 कृष्णः रुक्मिराजस्य : clean
p047:P10 द्वारकायां कृष्णरुक्मिण्योः : clean
J1 p041:P5 {wb} -> p041:P6 {pc} (continues) : ok (मधुरा+नगरस्य)
J2 p041:P8 {pb} -> p042:P2 {pc} (continues) : ok (गच्छन् आसीत्)
J3 p042:P5 {pb} -> p042:P6 {pc} (continues) : ok (देवक्याः गर्भे)
J4 p042:P12 {pb} -> p043:P2 {pc} (continues) : ok (निद्रायाम् एव)
J5 p043:P7 {pb} -> p043:P8 {pc} (continues) : ok (राक्षसान् आहूय)
J6 p043:P9 {pb} -> p044:P2 fresh (clean break) : ok (वर्धमानः आसीत्। then new episode)
J7 p044:P4 {pb} -> p044:P5 fresh (clean break) : ok (शापविमोचनं कृतवान्। then मृत्तिका episode)
J8 p044:P10 {pb} -> p045:P2 {pc} (continues) : ok (कंसं शिखाग्रहणपूर्वकम्)
J9 p045:P5 {pb} -> p045:P6 {pc} (continues) : ok (उपरि आक्रमणं)
J10 p045:P14 {wb} -> p046:P2 {pc} (continues) : ok (प्राप्तवन्तौ)
J11 p046:P7 {pb} -> p046:P8 {pc} (continues) : ok (सह पुनरपि)
J12 p046:P11 {pb} -> p047:P2 {pc} (continues) : ok (मुखं पश्यन्ति)
J13 p047:P5 {pb} -> p047:P6 fresh (clean break) : ok (विवाहः सम्पन्न rubric then Rukmini topic)
J14 p047:P10 {pb} -> END (clean break) : ok (story ends; next story p048)
