# Proofread report: samskrta_chandamama 1985_06, p029 (scan pages 29–31)

## Summary

Story `कस्य दोषः?` transcribed from pages 29–31 and proofread with images closed. Three findings, all `STY` readability insertions supplying quote mates the print dropped or left to span edges; no word changes. Systematic issue: the print marks the rajaguru's long speech only at its extremes, dropping the close after `तावत्` (p030) and leaving middle paragraphs unmarked. `scan.py orth` on deblocked text reports zero hits; the text is human transcription, not OCR output. Proper nouns (`मिहिरदेवः`, `निर्मलानन्दः`, `राजगुरुः`, `यमराजः`) spell consistently throughout. Print quirks kept as seen per fidelity: `वहु` for `बहु` (p031, probable typesetting slip), `धाष्ट्येन` (p029), open sandhi `जानन् अपि` (p030), `तदीयः शिष्याः` agreement as printed. Loc below is `pNN:Pm:word` (words counted on the chunk from 1) with the anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P4:40 `ध्यानपूर्वकं शृणोतु तावत्।` | `...शृणोतु तावत्।` (open `"` at `भवतः`, no close) | `...शृणोतु तावत्।{ins:"}` | STY | style | high | reporting verb `उक्तवान्` plus complete utterance pins the close |
| 2 | p031:P3:6 `'वलम् एव न्यायम् इति` | `'वलम्{sug-ins:'} एव न्यायम् इति वादः` (single open, no mate) | `'वलम् एव न्यायम्{ins:'} इति वादः` (drop doubling candidate, supply single close) | STY | style | high | `इति वादः` pins the maxim span; single is correct nested sort inside unmarked outer speech |
| 3 | p031:P5:1 `भवतः पूजया कापि` | merged span P5→P6 closes at `आरोपयेयुः"` with no open | `{ins:"}भवतः पूजया...` | STY | style | high | printed close needs its mate in-span; span start is the structurally forced position |

## Patterns

No repeats. The three findings are three different edge-drop shapes (missing close, single without mate, close without open), each once.

## Unverified

None held. The inherited `{sug-ins:'}` was ruled out (F2) rather than held: the single open is correct nesting, not a dropped second stroke.

## Coverage

- p029:P1 `{x-com:layout:` : skip layout declaration
- p029:P2 `# कस्य` : skip title heading
- p029:P3 `पूर्वं लक्ष्मणपुरे` : clean
- p029:P4 `राजा मिहिरदेवः` : clean
- p029:P5 `राजा निर्मलानन्दम्` : clean
- p029:P6 `{pc}वक्तुम् आरब्धवान्` : clean
- p029:P7 `तथापि निर्मलानन्दः` : clean
- p029:P8 `"किन्तु भवान्` : clean
- p029:P9 `"महाराज! अत्र` : clean (open pairs across page turn via J3, residual verified)
- p029:P10 `{author: श्रीमाता}` : skip footer metadata
- p030:P1 `{x-com:layout:` : skip layout declaration
- p030:P2 `{pc}मम आश्रयः` : clean (close pairs with p029:P9 open via J3)
- p030:P3 `राजा निर्मलानन्दस्य` : clean
- p030:P4 `निर्मलानन्दस्य वचनेषु` : F1
- p030:P5 `पूर्वं कस्याश्चित्` : clean (unmarked middle of long speech, vacuous balance, kept as print)
- p030:P6 `माता चिन्तितवती` : clean (same as above)
- p030:P7 `नरकलोके यमराजः` : clean (open pairs across page turn via J5, residual verified)
- p031:P1 `{x-com:layout:` : skip layout declaration
- p031:P2 `{pc}भवती तेषां` : clean (close pairs with p030:P7 open via J5)
- p031:P3 `एतया कथया` : F2
- p031:P4 `अये निर्मलानन्द!` : clean (unmarked middle of long speech, vacuous balance, kept as print)
- p031:P5 `भवतः पूजया` : F3
- p031:P6 `{pc}स्यात्। किन्तु` : F3 (printed close, mated by F3 open)
- p031:P7 `राजगुरोः वचनेन` : clean
- p031:P8 `तदा राजगुरुः` : clean
- p031:P9 `राजा मिहिरदेवः` : clean
- J1 p029:P3 {pb} -> p029:P4 fresh : ok (complete sentence, clean column break)
- J2 p029:P5 {pb} -> p029:P6 {pc} : ok (`एकैकशः वक्तुम् आरब्धवान्` joins across columns)
- J3 p029:P9 {pb} -> p030:P2 {pc} : ok (`अपेक्षया मम आश्रयः...चिन्तयन्ति` joins across pages)
- J4 p030:P3 {pb} -> p030:P4 fresh : ok (complete sentence, clean column break)
- J5 p030:P7 {pb} -> p031:P2 {pc} : ok (`अकृत्वा भवती...समर्थनं कृतवती` joins across pages)
- J6 p031:P4 {pb} -> p031:P5 fresh : ok (complete sentence, clean column break)
- J7 p031:P5 {pb} -> p031:P6 {pc} : ok (`अल्पप्रमाणेन स्यात्` joins across columns)
- J8 p031:P9 {pb} -> END : ok (story closes complete, no folio printed)
