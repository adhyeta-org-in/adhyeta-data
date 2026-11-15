# Proofread report: 1986_09 p36 (उत्तमः कर्मकरः)

## Summary

Single-page story, 8 body paragraphs, fully continuous text with art bottom full-width. Three findings, all print misprints corrected as verdict blocks: twice a final `तु` imperative printed as `त्` (F1, F2) and once `आवश्यकम्` printed as `आवश्यकञ्` (F3). Orth scanner run on deblocked text returned zero hits, so all three findings come from the grammar pass. Loc below is `p036:Pm:W` (page span 36, chunk number matching lint `P` numbers, whitespace-token index within the chunk); the Original column opens with the chunk's first two words as anchor. No text was beyond checking; the file is a faithful transcription with no OCR layer involved.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p036:P4:14 | `भूस्वामी एतत् ... नियोजयत्` | `नियोजयतु` | OCR | error | high | quoted order needs the लोट् 3rd sg; print drops the उ-mātrā |
| 2 | p036:P6:13 | `वीरेश्वरः तान् ... आगच्छत्` | `आगच्छतु` | OCR | error | high | quoted command अपसार्य आगच्छ needs the लोट् 2nd sg; print drops the उ-mātrā |
| 3 | p036:P8:12 | `तृतीयः तु ... आवश्यकञ्` | `आवश्यकम्` | OCR | error | high | neuter predicate adjective agreeing with एकं खनित्रम् needs -म्; print sets कञ् |

## Patterns

- Final-`तु` printed as `त्` (2x): F1 (p036:P4 नियोजयत्), F2 (p036:P6 आगच्छत्). Both sit in quoted imperatives where लोट् is required by sense; the print font renders तु with a hook (cf. वस्तुतः) versus a straight halant tick here, so the glyphs are genuinely त्, i.e. a repeated dropped-mātrā slip rather than a reading doubt.

## Unverified

None. All findings are high confidence; no candidate is held for the user.

## Coverage

- p036:P1 {x-com:layout:} : skip layout-only chunk (1col, art bottom full-width, verified against scan in Phase A)
- p036:P2 उत्तमः कर्मकरः : skip title chunk
- p036:P3 वीरेश्वरः कस्यचित् : clean (thought quote in singles, एतं विषयं agrees, सञ्जातः/अङ्गीकृत्य-type nasals as printed)
- p036:P4 भूस्वामी एतत् : F1
- p036:P5 वीरेश्वरः स्वपरिचितान् : clean (त्रयः/आगतवन्तः plural agreement)
- p036:P6 वीरेश्वरः तान् : F2 (भवत्सु अन्यतमः construction correct)
- p036:P7 आगतेषु द्वौ : clean (dual उक्तवन्तौ/निर्गतवन्तौ, आवां/शक्नुवः dual, एतावद्बृहती sandhi correct)
- p036:P8 तृतीयः तु : F3 (अपसारयिष्यामि future, ल्यप् स्वीकृत्य, शानच् परीक्षमाणः, आगता agrees with शिला — all correct)
- p036:P9 तदा आश्चर्यकरं : clean (किञ्चिद्दूरं sandhi, क्त्वा same-subject, दृश्यते स्म idiom)
- p036:P10 वीरेश्वरः तृप्तिभावेन : clean (श्रीमन् vocative, अर्हति + infinitive, speech quotes balanced doubles throughout)
- J1 p036:P10 {pb} -> END (clean break) : ok (final sentence terminal, page-turn break asserted and closed by bare {pgb}, no folio in print)
