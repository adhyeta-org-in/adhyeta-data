# Proofread report: 1984_07 p033 अधिकारः (scans 33–38)

## Summary

Seven findings: four `STY` `error` verdicts (all `high`: three speech opens corrected `'` → `"` and one missing speech open supplied via `{ins:"}`) and three held `low*` candidates (one `OCR`, one `MRP`, one `SPL`). The systematic issue is print punctuation: balanced single-stroke speech quotes are kept as seen, and only unbalanced spans were re-sorted to doubles. One joint re-routed on textual evidence (J6 fresh → continues: `इति` + `सुहासिनी उक्तवती` split across the page turn). All 53 joints verified text-continuous against the asserted layouts; orth scanner clean; text is human transcription, not OCR. Loc is `pNN:Pm w<word>` (scan-sequence page, lint chunk number, 1-based story-word index on the chunk) plus a two-word anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p034:P3 w1 (किन्तु तादृशपरिस्थितिः) | `'किन्तु तादृशपरिस्थितिः … प्रार्थयतु" --- प्रतापः उक्तवान्` | `"किन्तु … प्रार्थयतु"` | STY | error | high | direct speech with reporting verb missorted open; balance forces `"` to match print close |
| 2 | p034:P4 w1 (महाराजः इव) | `'महाराजः … वा?"` | `"महाराजः … वा?"` | STY | error | high | outer speech missorted open; balance forces `"` to match print close, inner `'यतिकमपि …'` stays |
| 3 | p034:P4 w3 (इव यतिकमपि) | `यतिकमपि` | `यत्किमपि` | OCR | likely | low* | `यतिकमपि` is no word; minimal conjunct fix `ति` → `त्कि` gives the `यत् किमपि` used elsewhere |
| 4 | p035:P4 w10 (उक्तवन्तः भोः) | `ते उक्तवन्तः --- भोः युवराज! … एव"` | `--- {ins:"}भोः …` | STY | error | high | ministers' speech opens with no mark and closes with `"`; open supplied at sentence boundary |
| 5 | p036:P7 w18 (कृपया क्षाम्यतु) | `क्षाम्यतु` | `क्षम्यताम्` | MRP | likely | low* | `क्षाम्` stem gives no "forgive" imperative; `क्षम्` passive-imperative fits `कृपया` + 3rd-person address |
| 6 | p036:P11 w13 (तु राज्याः) | `राज्याः हस्ते` | `राज्ञ्याः हस्ते` | SPL | likely | low* | `राज्याः` (of the kingdom) breaks sense; `राज्ञ्याः` (of the queen) fits "she must become queen" |
| 7 | p038:P4 w1 (महाप्रभो, प्रजानां) | `'महाप्रभो, … व्यवहारम् … आरब्धवन्तः" इति` | `"महाप्रभो, … आरब्धवन्तः"` | STY | error | high | outer speech spans the page joint and missorts open; `"` matches print close in P5, inner `'भवतां …'` stays |

## Patterns

| # | Pattern | Count | Examples |
|---|---|---|---|
| 1 | speech opens printed `'` or dropped where `"` balances the span; corrected only where unbalanced | 4 | F1 p034:P3, F2 p034:P4, F4 p035:P4, F7 p038:P4 |

## Unverified

- F3 `यतिकमपि` (p034:P4): tried clause re-segmentation (`यत् इकम् अपि` has no parse; `यत् कम् अपि` needs unattested stem); `यत्किमपि` ("whatever") is the only sense fit and matches p036:P7 usage. Settles with: coordinator print check whether the conjunct is `त्कि` or `तिक`.
- F5 `क्षाम्यतु` (p036:P7): tried `क्षमताम्` (active) and `क्षम्यताम्` (passive) for "please forgive"; honorific 3rd-person address supports either, length of `क्षाम्` vs `क्षम्` undecidable from text. Settles with: print check of the vowel length plus house imperative usage.
- F6 `राज्याः` (p036:P11): tried `राज्यस्य` ("of the kingdom") and `राज्ञः` ("of the king"); `राज्ञ्याः` ("of the queen") wins on the next clause (`एषा राज्ञी भवेत् एव`). Settles with: print check for `ज्ञ्य` vs `ज्य`.

## Coverage

p033:P1 {x-com:layout: ...} : skip layout-only chunk
p033:P2 # अधिकारः : skip title
p033:P3 चन्दनदेशस्य राजकुमारः : clean
p033:P4 सुहासिनी इति : clean
p033:P5 कृतज्ञतापूर्वकं प्रतापवर्मा : clean
p033:P6 "प्रथमं 'लग्नः : clean
p033:P7 'तस्य कः : clean
p033:P8 "यः स्वकीयं : clean
p033:P9 {author: विवेकः}{pgb} : skip footer metadata
p034:P1 {x-com:layout: ...} : skip layout-only chunk
p034:P2 सुहासिनी उक्तवती। : clean
p034:P3 किन्तु तादृशपरिस्थितिः : F1
p034:P4 महाराजः इव : F2, F3
p034:P5 सुहासिन्याः स्निग्धसौन्दर्येण : clean
p034:P6 अहं देशाटनं : clean
p034:P7 "अहं जानामि, : clean
p034:P8 प्रतापवर्मा पृष्टवान् : clean
p034:P9 'भवता एतत् : clean
p034:P10 आश्चर्यचकितः प्रतापवर्मा : clean
p034:P11 'किमर्थं न : clean
p034:P12 किञ्चित्कालं चिन्तयित्वा : clean
p035:P1 {x-com:layout: ...} : skip layout-only chunk
p035:P2 'अस्तु, पश्यामि : clean
p035:P3 प्रतापवर्मा स्वराजधानीं : clean
p035:P4 एतत् श्रुत्वा : F4
p035:P5 इति। : clean
p035:P6 "यदि एतत् : clean
p035:P7 महाराजः एतं : clean
p035:P8 तदा तु : clean
p036:P1 {x-com:layout: ...} : skip layout-only chunk
p036:P2 सर्वम् अपि : clean
p036:P3 सर्वं श्रुत्वा : clean
p036:P4 'परन्तु सा : clean
p036:P5 'एवं वा? : clean
p036:P6 यदा प्रतापवर्मा : clean
p036:P7 इति ज्ञातम्, : F5
p036:P8 प्रतापवर्मा उक्तवान् : clean
p036:P9 सुहासिनी धैर्यम् : clean
p036:P10 'तथा अधिकारं : clean
p036:P11 इदानीं महाराजः : F6
p036:P12 अन्ते एकः : clean
p037:P1 {x-com:layout: ...} : skip layout-only chunk
p037:P2 कारी भविष्यति। : clean
p037:P3 सुहासिनी तत् : clean
p037:P4 राज्यव्यवहारे बहु-स्थलेषु, : clean
p037:P5 एवम् एव : clean
p037:P6 त्रयः अपि : clean
p037:P7 दिक्?' इति। : clean
p037:P8 सः उक्तवान् : clean
p037:P9 महाराजस्य प्रतापवर्मणः : clean
p037:P10 अनन्तरम् ते : clean
p037:P11 सः उत्तरम् : clean
p037:P12 इदानीं सुहासिनी : clean
p038:P1 {x-com:layout: ...} : skip layout-only chunk
p038:P2 उक्तवती --- : clean
p038:P3 "एतत् तु : clean
p038:P4 महाप्रभो, प्रजानां : F7
p038:P5 आरब्धवन्तः" इति : clean
p038:P6 प्रतापवर्मा आश्चर्येण : clean
p038:P7 महाराजः गम्भीरः : clean
p038:P8 अनन्तरम् अल्पे : clean
J1 p033:P3 {pb} -> p033:P4 fresh (clean break) : ok
J2 p033:P4 {pb} -> p033:P5 fresh (clean break) : ok
J3 p033:P5 {pb} -> p033:P6 fresh (clean break) : ok
J4 p033:P6 {pb} -> p033:P7 fresh (clean break) : ok
J5 p033:P7 {pb} -> p033:P8 fresh (clean break) : ok
J6 p033:P8 {pb} -> p034:P2 {pc} (continues) : ok
J7 p034:P2 {pb} -> p034:P3 fresh (clean break) : ok
J8 p034:P3 {pb} -> p034:P4 fresh (clean break) : ok
J9 p034:P4 {pb} -> p034:P5 fresh (clean break) : ok
J10 p034:P5 {pb} -> p034:P6 {pc} (continues) : ok
J11 p034:P6 {pb} -> p034:P7 fresh (clean break) : ok
J12 p034:P7 {pb} -> p034:P8 fresh (clean break) : ok
J13 p034:P8 {pb} -> p034:P9 fresh (clean break) : ok
J14 p034:P9 {pb} -> p034:P10 fresh (clean break) : ok
J15 p034:P10 {pb} -> p034:P11 fresh (clean break) : ok
J16 p034:P11 {pb} -> p034:P12 fresh (clean break) : ok
J17 p034:P12 {pb} -> p035:P2 fresh (clean break) : ok
J18 p035:P2 {pb} -> p035:P3 fresh (clean break) : ok
J19 p035:P3 {pb} -> p035:P4 fresh (clean break) : ok
J20 p035:P4 {pb} -> p035:P5 {pc} (continues) : ok
J21 p035:P5 {pb} -> p035:P6 fresh (clean break) : ok
J22 p035:P6 {pb} -> p035:P7 fresh (clean break) : ok
J23 p035:P7 {pb} -> p035:P8 fresh (clean break) : ok
J24 p035:P8 {pb} -> p036:P2 {pc} (continues) : ok
J25 p036:P2 {pb} -> p036:P3 fresh (clean break) : ok
J26 p036:P3 {pb} -> p036:P4 fresh (clean break) : ok
J27 p036:P4 {pb} -> p036:P5 fresh (clean break) : ok
J28 p036:P5 {pb} -> p036:P6 fresh (clean break) : ok
J29 p036:P6 {pb} -> p036:P7 {pc} (continues) : ok
J30 p036:P7 {pb} -> p036:P8 fresh (clean break) : ok
J31 p036:P8 {pb} -> p036:P9 fresh (clean break) : ok
J32 p036:P9 {pb} -> p036:P10 fresh (clean break) : ok
J33 p036:P10 {pb} -> p036:P11 fresh (clean break) : ok
J34 p036:P11 {pb} -> p036:P12 fresh (clean break) : ok
J35 p036:P12 {wb} -> p037:P2 {pc} (continues) : ok
J36 p037:P2 {pb} -> p037:P3 fresh (clean break) : ok
J37 p037:P3 {pb} -> p037:P4 fresh (clean break) : ok
J38 p037:P4 {pb} -> p037:P5 fresh (clean break) : ok
J39 p037:P5 {pb} -> p037:P6 fresh (clean break) : ok
J40 p037:P6 {pb} -> p037:P7 {pc} (continues) : ok
J41 p037:P7 {pb} -> p037:P8 fresh (clean break) : ok
J42 p037:P8 {pb} -> p037:P9 fresh (clean break) : ok
J43 p037:P9 {pb} -> p037:P10 fresh (clean break) : ok
J44 p037:P10 {pb} -> p037:P11 fresh (clean break) : ok
J45 p037:P11 {pb} -> p037:P12 fresh (clean break) : ok
J46 p037:P12 {pb} -> p038:P2 {pc} (continues) : ok
J47 p038:P2 {pb} -> p038:P3 fresh (clean break) : ok
J48 p038:P3 {pb} -> p038:P4 fresh (clean break) : ok
J49 p038:P4 {pb} -> p038:P5 {pc} (continues) : ok
J50 p038:P5 {pb} -> p038:P6 fresh (clean break) : ok
J51 p038:P6 {pb} -> p038:P7 fresh (clean break) : ok
J52 p038:P7 {pb} -> p038:P8 fresh (clean break) : ok
J53 p038:P8 {pb} -> END (clean break) : ok
