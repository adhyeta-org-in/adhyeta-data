# Proofread report: 1984_07 p048 धर्मो रक्षति रक्षितः (scans 48-51)

## Summary

Two findings, both `STY` `error` at `high` confidence: the outer/inner reported-speech pair in the final recognition scene is sorted `"` outside / `'` inside (two blocks: open and close of one outer speech). The systematic point is print punctuation: single-stroke speech quotes are kept as seen throughout as the house variant, with only this nested passage re-sorted for readability. All eight `{pb}`/`{pc}` joints are text-continuous against the asserted 2col layouts, and the orth scanner is clean; the text is human transcription, not OCR. Loc is `pNN:Pm w<word>` (scan-sequence page, lint chunk number, 1-based whitespace-token index on the chunk) plus a two-word anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p051:P7 w7 (युवराजः मुबारकं) | `उक्तवान् --- 'राजन्!` | `उक्तवान् --- "राजन्!` | STY | error | high | outer reported speech quoting inner reported speech takes " outside and ' inside; reporting verbs plus iti-closures pin both levels |
| 2 | p051:P8 w60 (प्रविष्टवान्। तत्र) | `आगतवान्' इति।` | `आगतवान्" इति।` | STY | error | high | closing sort of the outer reported speech, matching the corrected open in F1 |

## Patterns

- Nested-quote sort (2 blocks, 1 passage): outer speech re-sorted to `"` at p051:P7 open and p051:P8 close; inner spies' speech keeps print `'` (e.g. `'युवराज!` at p051:P8 w32).

## Unverified

- None held. No word was left as a low-confidence candidate; apparent print oddities (`समाश्वसिहतु`, `प्रति प्रेषितवान्` spacing, `सानानगरं` end-spelling) are kept print-faithful with no new glyph claim, since Phase B invents no glyph readings from text alone.

## Coverage

p048:P1 {x-com:layout: ...} : skip layout-only chunk
p048:P2 # धर्मो : skip title
p048:P3 यमन् देशे : clean
p048:P4 एकदा राजा : clean
p048:P5 क्रुद्धः राजा : clean
p048:P6 हरिणं दृष्ट्वा : clean
p048:P7 'एतस्य शिरः : clean
p048:P8 सलीमः राज्ञः : clean
p048:P9 एतया प्रार्थनया : clean
p048:P10 {category: अरेबिया : skip footer metadata
p049:P1 {x-com:layout: ...} : skip layout-only chunk
p049:P2 अभवत्। अतः : clean
p049:P3 वर्षद्वयम् अतीतम्। : clean
p049:P4 जले पतितः : clean
p049:P5 द्विरात्रं समुद्रे : clean
p049:P6 शनैः शनैः : clean
p049:P7 अज्ञाते एतस्मिन् : clean
p049:P8 'एषः किमर्थं : clean
p049:P9 राजा मुबारकः : clean
p050:P1 {x-com:layout: ...} : skip layout-only chunk
p050:P2 'एतत् सर्वं : clean
p050:P3 'श्वः एतस्य : clean
p050:P4 मुबारकः चिन्तितवान् : clean
p050:P5 कारागृहे एकः : clean
p050:P6 'हन्त! शीघ्रकोपतः : clean
p050:P7 द्वित्राः निमेषाः : clean
p050:P8 क्षिप्तः मुबारकः : clean
p050:P9 युवराजः मुबारकं : clean
p050:P10 भूमौ पतितं : clean
p050:P11 मुबारकः युवराजं : clean
p051:P1 {x-com:layout: ...} : skip layout-only chunk
p051:P2 बृहत् रन्ध्रम् : clean
p051:P3 'सः तरुणः : clean
p051:P4 'सः तरुणः : clean
p051:P5 'अहम् अपि : clean
p051:P6 युवराजेन उक्तं : clean
p051:P7 युवराजः मुबारकं : F1
p051:P8 प्रविष्टवान्। तत्र : F2
p051:P9 राजा मुबारकः : clean
J1 p048:P5 {pb} -> p048:P6 {pc} (continues) : ok
J2 p048:P9 {pb} -> p049:P2 {pc} (continues) : ok
J3 p049:P4 {pb} -> p049:P5 {pc} (continues) : ok
J4 p049:P9 {pb} -> p050:P2 fresh (clean break) : ok
J5 p050:P8 {pb} -> p050:P9 fresh (clean break) : ok
J6 p050:P11 {pb} -> p051:P2 {pc} (continues) : ok
J7 p051:P7 {pb} -> p051:P8 {pc} (continues) : ok
J8 p051:P9 {pb} -> END (clean break) : ok
