# Proofread report: 1987_01 p029 (range 29–35, उत्तररामायणम्)

## Summary

Phase B (images closed) on `.processing/samskrta_chandamama/1987_01/p029.md`, 7 page spans p029–p035 (Kubera's defeat through Anaranya's curse and Narada's arrival). 12 findings, all high confidence: 11 error (one stray open quote, one stray dot, eight print-misprint corrections, one agreement fix, one lexicon fix) and 1 style (quote-sort correction for speech in singles). 4 candidates held as Unverified (two void words with no emendation, two with competing emendations); a sharper scan would settle all four. The orth scanner (`scan.py orth` on deblocked text) returned a single low hit, the `मम.` full stop, ruled a stray mark (F2). The text is eye transcription, not OCR output. One detached single stroke (p034, `वशीकृतवान् ' अस्मि`) was omitted as print noise with an `{x-com:}` on file. `Loc` is `pNN:Pm wN` with the first-two-words anchor, words counted on the deblocked chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p029:P3 w1 (शुक्रः प्रोष्ठपदः) | `"शुक्रः` | `शुक्रः` | STY | error | high | Para opens narration, not speech; the outer `"` has no mate while `"रे...एव"` is complete. |
| F2 | p029:P3 w14 (शुक्रः प्रोष्ठपदः) | `मम. हितवचनानि` | `मम हितवचनानि` | STY | error | high | Stray baseline dot with no grammatical role; orth scanner flags the full stop. |
| F3 | p030:P4 w17 (एतत् दृष्ट्वा) | `साचवान्` | `सचिवान्` | SPL | error | high | Same lexeme spelled सचिवः on p034 (सचिवः शुकः); Ravana questions his ministers. |
| F4 | p030:P5 w3 (अत्रान्तरे ईश्वरस्य) | `पार्श्वधरः` | `पार्श्वचरः` | SPL | error | high | Nandi is Shiva's attendant (पार्श्वचर); पार्श्वधरः is void. |
| F5 | p030:P2 w8 (गतवान् इत्थं) | `एतादृशगार्वितेन` | `एतादृशगर्वितेन` | SPL | error | high | गर्वित (proud) required; Kubera falls silent to avoid dispute with the arrogant Ravana. |
| F6 | p031:P4 w17 (तेन रावणस्य) | `साचवाः` | `सचिवाः` | SPL | error | high | Same damaged sort as F3; सचिवः is correct on p034. |
| F7 | p031:P6 w7 (तदा रावणः) | `मर्द्वपये` | `मद्विषये` | SPL | error | high | मद्विषये (towards me) required by प्रीतः; मर्द्वपये is void. |
| F8 | p032:P3 w14 (इत्थं दिग्विजयपरायणः) | `ऋषयः इव` | `ऋषिः इव` | AGR | error | high | सा (f.sg) needs ऋषिः, not m.pl ऋषयः. |
| F9 | p032:P6 w8 (सा नेत्रे) | `साविस्तरं` | `सविस्तरं` | SPL | error | high | सविस्तर (in detail) is the standard form. |
| F10 | p033:P9 w24 (रावणस्य दर्शनसमनन्तरम्) | `अश्वरूपं` | `हंसरूपं` | LEX | error | high | Gods favor those whose forms they took (p034) and Varuna favors हंसाः (p035); epic Varuna takes हंस-form. |
| F11 | p034:P4 w19 (रावणः स्वीयमहाध्वनिना) | `परिचयग्रहतः` | `परिचयरहितः` | SPL | error | high | तादृशः भवान् लब्धः irony requires "ignorant of"; ग्रहतः is void. |
| F12 | p032:P2 w33 (पुष्पकविमानम् आरुह्य) | `'भवदुक्तम् अनुसरामः'` | `"भवदुक्तम् अनुसरामः"` | STY | style | high | Reported speech takes doubles in this era's print; singles mark thought or nested speech. |

## Patterns

सचिव misprinted twice with displaced vowel marks (F3 साचवान्, F6 साचवाः) against correct सचिवः on p034. Joined open-spellings kept as house variants, not findings: युक्तेकाले (= युक्ते काले, p030), एवंगत्या (= एवं गत्या, p031), तत्क्षणएव (= तत्क्षण एव, p033). मरुत्त stem throughout (मरुत्तमहाराजः, मरुत्तराजं, मरुत्तः) against epic मरुत्त, and विमान in both genders (एषः विमानः beside विमानम्, epic usage), kept as variants. शुक्रध्वजः (epic कुशध्वज) and सुरटः occur once each and stand as printed.

## Unverified

H1 p030:P5 w4 (अत्रान्तरे ईश्वरस्य) `महावार्लप्तः` Conf low* : void epithet of Nandi with no confident reading at 4x; tried महाबलयुक्तः, महावरिष्ठः, महावलिप्तः, none fit the glyphs; a sharper image or a lexicon hit would settle it.
H2 p030:P7 w15 (तत्र शिवः) `शूड्गमोहितं` Conf low* : void face-word, no confident reading at 4x; tried शृङ्गमण्डितं, शुण्डामण्डितं and ape-face words, none fit; a sharper image or the parallel Uttara Kanda Nandi-episode wording would settle it.
H3 p031:P2 w2 (वराकाः अज्ञत्याः) `अज्ञत्याः` Conf low* : competing emendations अत्रत्याः (one-akshara change, deictic "those here") vs अज्ञतया ("through ignorance"); a sharper image (ज्ञ/त्र, याः/या) would settle it.
H4 p034:P6 w1 (तप्तमानः पितृसदृशम्) `तप्तमानः` Conf low* : तप्तमानसः (one dropped स, standard मानस-compound) vs तप्तमनाः (ā-shift) vs as-is तप्तमान (hot-pride); a sharper image (मा/म, नः/नाः/नसः) would settle it.

## Coverage

p029:P1 {x-com:layout: : skip x-com-only layout chunk.
p029:P2 # उत्तररामायणम् : skip title heading.
p029:P3 शुक्रः प्रोष्ठपदः : F1, F2.
p029:P4 कुबेरस्य वचनानि : clean.
p029:P5 पूर्वापेक्षया उग्रतरः : clean.
p029:P6 एवंरीत्या रावणः : clean.
p029:P7 {category: वेदवतीप्रतिज्ञा : skip metadata footer chunk.
p030:P1 {x-com:layout: : skip x-com-only layout chunk.
p030:P2 गतवान् इत्थं : F5.
p030:P3 पुष्पकविमानारूढः रावणः : clean.
p030:P4 एतत् दृष्ट्वा : F3.
p030:P5 अत्रान्तरे ईश्वरस्य : F4, H1.
p030:P6 तानि वचनानि : clean.
p030:P7 तत्र शिवः : H2.
p030:P8 साक्षात् शङ्करसदृशः : clean.
p030:P9 रावणः महान्तम् : clean.
p030:P10 {pgb: : skip page-close chunk.
p031:P1 {x-com:layout: : skip x-com-only layout chunk.
p031:P2 वराकाः अज्ञत्याः : H3.
p031:P3 एतत्सर्वं पश्यन् : clean.
p031:P4 तेन रावणस्य : F6.
p031:P5 रावणः वेदनया : clean.
p031:P6 तदा रावणः : F7.
p031:P7 माम् अनुगृह्णातु : clean.
p031:P8 शिवः रावणाय : clean.
p031:P9 एवंगत्या शिवेन : clean.
p031:P10 {pgb: : skip page-close chunk.
p032:P1 {x-com:layout: : skip x-com-only layout chunk.
p032:P2 पुष्पकविमानम् आरुह्य : F12.
p032:P3 इत्थं दिग्विजयपरायणः : F8.
p032:P4 रावणः तां : clean.
p032:P5 भूत्वा तस्याः : clean.
p032:P6 सा नेत्रे : F9.
p032:P7 तस्याः वचनानि : clean.
p032:P8 {pgb: : skip page-close chunk.
p033:P1 {x-com:layout: : skip x-com-only layout chunk.
p033:P2 दीर्घसुमङ्गली भवतु : clean.
p033:P3 रे गर्वोन्मत्त : clean.
p033:P4 तत्क्षणएव रावणः : clean.
p033:P5 सा अग्निं : clean.
p033:P6 एषा वेदवती : clean.
p033:P7 एवंरीत्या वेदवत्याः : clean.
p033:P8 महायज्ञं दृष्टवान् : clean.
p033:P9 रावणस्य दर्शनसमनन्तरम् : F10.
p033:P10 रावणः निःशङ्कं : clean.
p033:P11 {pgb: : skip page-close chunk.
p034:P1 {x-com:layout: : skip x-com-only layout chunk.
p034:P2 शरणम् आगच्छति : clean.
p034:P3 भवान् कीदृशः : clean.
p034:P4 रावणः स्वीयमहाध्वनिना : F11.
p034:P5 तस्य वचनं : clean.
p034:P6 तप्तमानः पितृसदृशम् : H4.
p034:P7 तदा संवर्तः : clean.
p034:P8 गुरोः वचनं : clean.
p034:P9 रावणः यज्ञवाटिकायाम् : clean.
p034:P10 अनन्तरं दिक्पालकाः : clean.
p034:P11 {pgb: : skip page-close chunk.
p035:P1 {x-com:layout: : skip x-com-only layout chunk.
p035:P2 ततः पूर्वं : clean.
p035:P3 तथैव यमस्य : clean.
p035:P4 वरुणस्य अनुग्रहेण : clean.
p035:P5 रावणः लोके : clean.
p035:P6 तदा प्रवृत्ते : clean.
p035:P7 एवंरीत्या रावणः : clean.
p035:P8 {pgb: : skip page-close chunk.
J1 p029:P4 {pb} -> p029:P5 {pc} (continues) : ok.
J2 p029:P6 {pb} -> p030:P2 {pc} (continues) : ok.
J3 p030:P4 {pb} -> p030:P5 fresh (clean break) : ok.
J4 p030:P9 {pb} -> p031:P2 {pc} (continues) : ok-text with held H3.
J5 p031:P6 {pb} -> p031:P7 {pc} (continues) : ok.
J6 p031:P9 {pb} -> p032:P2 {pc} (continues) : ok.
J7 p032:P4 {pb} -> p032:P5 {pc} (continues) : ok.
J8 p032:P7 {pb} -> p033:P2 {pc} (continues) : ok.
J9 p033:P7 {pb} -> p033:P8 {pc} (continues) : ok.
J10 p033:P10 {pb} -> p034:P2 {pc} (continues) : ok.
J11 p034:P5 {pb} -> p034:P6 {pc} (continues) : ok-text with held H4.
J12 p034:P10 {pb} -> p035:P2 fresh (clean break) : ok.
J13 p035:P5 {pb} -> p035:P6 fresh (clean break) : ok.
J14 p035:P7 {pb} -> END (clean break, range end) : ok.
