# Proofread report — 1986_01 p002 (scan pages 2–5, `चोरस्य उपकारः`)

## Summary

Story file (4 page spans, 27 body chunks) passes `lint --phase proofread` with 0 errors. Three verified verdicts landed as blocks: one glued-word split promoted from the Phase A candidate (F1) and two supplied double-quote marks restoring balance (F2, F3). Three low/medium-confidence grammar forms are held as `{sug-…}` candidates for the user (F4–F6). The recurring stray tick before three `p003` speech opens was verified at 3x and read as print noise, keeping print's doubles with an `{x-com:}` on file. Print spelling/sandhi variants (`नाम्नाः`, `यदिने`-adjacent `तद्दिने`, `अज्ञात्वा`, `निषद्योगी`, `फल्गुम्फ`/`गुम्फ` beside `कदलीगुम्फ`, `कनकाम्बा च`) are kept as house variants with no blocks. One red tick after `अटन्` (p005:P4) was ignored as a proofreader mark. Text was transcribed directly from scans, not OCR output; no passages unchecked.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p003:P3 (कनकाम्बा यानि) :24 | `दिने पतिम्उक्तवती` | `दिने पतिम् उक्तवती` | STY | error | high | print glues two words at 3x; accusative object plus absolutive need the break |
| F2 | p003:P2 (अस्माभिः जागरूकैः) :1 | `अस्माभिः जागरूकैः ... अन्वेषयिष्यामि" इति।` | `{ins:"}` before `अस्माभिः` | STY | error | high | closing `"` plus `इति` pins a speech open at the paragraph start |
| F3 | p003:P6 (तत् श्रुत्वा) :30 | `"वयं तूष्णीं ... वर्धते एव।` | `{ins:"}` after `एव।` | STY | error | high | speech opens with `"` and never closes; next paragraph is a new speaker |
| F4 | p005:P5 (इति ज्ञातवान्) :4 | `अतः सर्वां सम्पत्तिः मया गृहीता` | `सर्वा सम्पत्तिः` | AGR | likely | medium* | accusative `सर्वां` mismatches nominative subject `सम्पत्तिः` of passive `गृहीता` |
| F5 | p005:P5 (इति ज्ञातवान्) :26 | `क्षाम्यतु माम्` | `क्षम्यताम्` | MRP | likely | low* | `क्षाम्यतु` is no standard imperative of `क्षम्`; sense is "forgive me" |
| F6 | p002:P7 (यदिने नूतनगृहं) :1 | `यदिने नूतनगृहं प्रविष्टं` | `यस्मिन् दिने` | MRP | likely | low* | `यदिने` is not a word; sense is "on the day (they) entered" |

## Unverified

F4 held: `सर्वां` could be a print slip for `सर्वा`, or a frozen adverbial accusative kept by the compositor; another copy of the issue or an editor ruling would settle it. F5 held: `क्षम्यताम्` fits best, but `क्षमस्व` or a dialectal `क्षाम्यतु` cannot be excluded; a dictionary check of attestations or an editor ruling would settle it. F6 held: `यस्मिन् दिने` fits the sense, but a deliberate contraction or a slip for `तद्दिने`-style brevity cannot be excluded; another copy or an editor ruling would settle it.

## Coverage

p002:P1 : skip layout
p002:P2 # चोरस्य : skip title
p002:P3 पूर्वम् एकस्मिन् : clean
p002:P4 विवाहसमनन्तरं एकदा : clean
p002:P5 एवमेव कालः : clean
p002:P6 तौ पलायनं : clean
p002:P7 यदिने नूतनगृहं : F6
p002:P8 एवमेव एकवारं : clean
p002:P9 {author} : skip metadata
p003:P1 : skip layout
p003:P2 अस्माभिः जागरूकैः : F2
p003:P3 कनकाम्बा यानि : F1
p003:P4 कनकाम्बा अपि : clean
p003:P5 वार्तालापमध्ये अवकाशं : clean
p003:P6 तत् श्रुत्वा : F3
p003:P7 "भवत्याः कथनस्य : clean
p003:P8 तदा कनकाम्बा : clean
p003:P9 "एवं वा? : clean
p003:P10 तस्मिन् दिने : clean
p004:P1 : skip layout
p004:P2 पुनः भित्तिम् : clean
p004:P3 कनकाम्बा तं : clean
p004:P4 प्रातःकाले कनकराजस्य : clean
p004:P5 कण्ठहारः अपि : clean
p004:P6 निश्चय "अहो! : clean
p004:P7 एतावति काले : clean
p004:P8 तयोः सान्त्वनार्थम् : clean
p005:P1 : skip layout
p005:P2 स्थितं कदलीगुम्फं : clean
p005:P3 कनकाम्बा-कनकराजयोः अपि : clean
p005:P4 तस्मिन् कदलीगुम्फे : clean
p005:P5 इति ज्ञातवान् : F4, F5
p005:P6 कनकराजः कनकाम्बा : clean
p005:P7 'अनामिकः चोरः : clean
J1 p002:P5 -> p002:P6 {pc} (continues) : ok
J2 p002:P8 -> p003:P2 fresh (clean break) : ok
J3 p003:P3 -> p003:P4 fresh (clean break) : ok
J4 p003:P6 -> p003:P7 fresh (clean break) : ok
J5 p003:P10 -> p004:P2 fresh (clean break) : ok
J6 p004:P5 -> p004:P6 {pc} (continues) : ok
J7 p004:P8 -> p005:P2 {pc} (continues) : ok
J8 p005:P4 -> p005:P5 {pc} (continues) : ok
J9 p005:P7 -> END (clean break) : ok
