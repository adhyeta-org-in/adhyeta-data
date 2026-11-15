## Summary

Story जागरणम् (p26--p29) proofread images-closed: 5 findings — 1 verified quote-sort verdict (F1, error/high) and 4 held `{sug-}` candidates for the user (F2--F5, unverified). Systematic issues: era print mixes single/double quote strokes (`'` opened vs `"` closed in minister's speech) and two print spelling inconsistencies (`मध्यवयस्कः`/`मध्यमवयस्कः`). `scan.py orth` on deblocked text: no hits. No inherited Phase A `{sug-}` queue existed. All joints verified both sides in Phase A; print's quote marks kept where sense does not decide (crowd's `'युक्तम् एतत्'` singles; footer `‘‘माणवकः’’` recorded quote-free as `{category: माणवकः}` per existing category-node convention). Text is manual transcription, not OCR. Loc is `pNN:Pm` + anchor words, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p28:P4 एवं स्थिते w36 | `'महाराज! ... अभिप्रायः"` | `{del:'}{ins:"}महाराज!` (open doubles) | STY | error | high | direct speech after `उक्तवान् ---` takes doubles; thought in same para already uses singles correctly |
| F2 | p27:P3 कुमारवर्मा आगमनकारणं w6 | `मध्यमवयस्कः` | `मध्यवयस्कः` | CNS | likely | low* | same man called `मध्यवयस्कः` two sentences earlier; `मध्यमवयस्कः` nonstandard |
| F3 | p27:P5 तद्दिने रात्रौ w6 | `चिन्तितवात्` | `चिन्तितवान्` | OCR | likely | medium* | active past needs `क्तवतु` `-वान्`; `त`/`न` one-stroke confusion, glyph unverified images-closed |
| F4 | p26:P6 कुमारवर्मा पितुः w36 | `निष्प्रयोजिनः` | `निष्प्रयोजनाः` | SPL | likely | low* | `निष्प्रयोजिन्` stem unattested; expected `निष्प्रयोजनाः` agreeing the idle ones, but authorial formation possible |
| F5 | p29:P4 तदा पार्श्वग्रामीणः w21 | `एतात्पर्यन्तं` | `एतत्पर्यन्तं` or `एतावत्पर्यन्तं` | OCR | likely | low* | extra `आ` or dropped `व`; sense "who was a vassal until now" fits either fix |

## Unverified

- F2 `मध्यमवयस्कः` vs `मध्यवयस्कः`: settle by checking whether the 1985 print font distinguishes `मध्यम` here or the compositor doubled the sense; kept `{sug-}` held.
- F3 `चिन्तितवात्`: settle by re-examining the glyph at 3x in a future images-open pass; grammar pins `-वान्` but the print stroke is unverified.
- F4 `निष्प्रयोजिनः`: settle by dictionary check for a `निष्प्रयोजिन्` stem; if attested, drop the candidate and log a house variant.
- F5 `एतात्पर्यन्तं`: settle by re-examining print at 3x (`तत्प` vs `तावत्प`); two single-sign hypotheses, neither fits better from text alone.

## Coverage

p26:P2 जागरणम् : skip title
p26:P3 पूर्वं सिंहपुरमहाराजः : clean
p26:P4 एकदा सः : clean
p26:P5 पिता एवं : clean
p26:P6 कुमारवर्मा पितुः : F4
p26:P7 एवम् एव : clean
p26:P8 माणवकः : skip metadata
p27:P2 एकदा राजसभा : clean
p27:P3 कुमारवर्मा आगमनकारणं : F2
p27:P4 एतेभ्यः यत् : clean
p27:P5 तद्दिने रात्रौ : F3
p27:P6 अपरस्मिन् दिने : clean
p27:P7 महाराजः एतावता : clean
p28:P2 एवमेव कवयः : clean
p28:P3 एतादृशविचित्रव्यवहारेण राज्ये : clean
p28:P4 एवं स्थिते : F1
p28:P5 राजा एतत् : clean
p28:P6 वटवृक्षस्य अधः : clean
p28:P7 पार्श्वे अन्ये : clean
p28:P8 ग्रामप्रमुखेषु एकः : clean
p28:P9 तदा पार्श्वग्रामीणः : clean
p29:P2 आस्थानतः निष्कासितवान्। : clean
p29:P3 एतत् श्रुत्वा : clean
p29:P4 तदा पार्श्वग्रामीणः : F5
p29:P5 तदा अपरः : clean
p29:P6 नूतनं योग्यं : clean
p29:P7 एतत् श्रुत्वा : clean
p29:P8 अनन्तरं मन्त्रिणा : clean
p29:P9 एवं च : clean
J1 p026:P4 {pb} -> p026:P5 {pc} : ok (father's scolding continues across columns)
J2 p026:P7 {pb} -> p027:P2 fresh : ok (clean break)
J3 p027:P3 {pb} -> p027:P4 {pc} : ok (complaint speech continues across columns)
J4 p027:P7 {pb} -> p028:P2 fresh : ok (clean break)
J5 p028:P6 {pb} -> p028:P7 {pc} : ok (तेषां पार्श्वे spaced join across columns)
J6 p028:P9 {pb} -> p029:P2 {pc} : ok (speech continues across pages)
J7 p029:P5 {pb} -> p029:P6 {pc} : ok (speech continues across columns)
J8 p029:P9 {pb} -> END : ok (story ends clean; next story p030 untouched)
