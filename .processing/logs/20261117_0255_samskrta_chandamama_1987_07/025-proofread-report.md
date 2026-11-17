# Proofread report: 1987_07 p025 (pages 25-28, वृद्धस्य विवाहः)

## Summary

Phase B on `.processing/samskrta_chandamama/1987_07/p025.md` (4 page spans, 25-28): 3 findings, all `STY`/style quote-punctuation verdicts (1 supplied thought-open, 1 supplied speech-open across the p25-p26 page turn, 1 dropped stray mark); 0 word-form verdicts, 0 held candidates. Print-faithful quirks kept as seen (all 3x/4x crop-verified in Phase A, no Phase A flag on file so no Phase B glyph block per step 5): `पितः` (p025:P9, sense `पितुः`), `माता त` (p026:P2, sense `तु`), `वधः` (p026:P3, sense `वधूः`), `दशादिनानाम्` (p026:P3, sense `दशदिनानाम्`), `मौनं स्थितिः` (p026:P2, syntax), `आसम्` (p027:P5, sense `अस्मि`), `एषा वार्तां` (p028:P4, sense `वार्ता`). The p25-p26 speech keeps print's single-open/double-close (`'माता ... वरम्'"`) with the DQ open supplied at the pinned `---` boundary (F2); sort deviation documented, not rewritten. Proper nouns consistent throughout (`मुनिरामः` x8, `रत्ना`, `सर्वसिद्धि` in both compounds, `कृष्णशर्मन्`/`रामानुज`/`जयलक्ष्मी`/`वेङ्कटरमण`/`स्नुषा` stems). `scan.py orth` on deblocked text: 0 hits. Proofread gate: exit 0, all pages clean. `Loc` below is `pNN:Pm` (lint chunk number within the span) plus anchor words, counting words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p025:P6 w11 `{pc}आश्चर्यचकितः। यतः` | `आसीत्। एतादृशस्य` | `आसीत्। {ins:'}एतादृशस्य` | STY | style | medium | print drops the thought-open; `इति आलोचितवान्` pins a thought span, opening placed at the wondering's sentence boundary (alternative before `यतः` kept as narrator ground) |
| F2 | p025:P9 w15 `सायङ्काले जयलक्ष्म्याः` | `उक्तवान् --- {pb}` | `उक्तवान् --- {ins:"} {pb}` | STY | style | medium | speech reporting verb plus `---` pins the DQ open; print's p26 `'...'"` pair stands as seen inside it, mate across the `{pb}`/`{pc}` page turn |
| F3 | p027:P3 w9 `मुनिरामः अतिथीन्` | `च।' रत्ना` | `च।{del:'} रत्ना` | STY | style | high | narrator sentence with no speech, thought, or reporting verb; lone single is a print stray |

## Unverified

None. No `{sug-del:}`/`{sug-ins:}` candidates were inherited from Phase A and none are kept; every residual was ruled with a block (F1-F3) or kept as print-faithful with reason above.

## Coverage

p025:P1 `{x-com:layout: ...}` : skip layout
p025:P2 `# वृद्धस्य` : skip title
p025:P3 `सरसपुरग्रामे रामानुजः` : clean
p025:P4 `एकदा रामानुजः` : clean
p025:P5 `रामानुजस्य अपेक्षां` : clean
p025:P6 `{pc}आश्चर्यचकितः। यतः` : F1
p025:P7 `"तथैव भवतु` : clean
p025:P8 `एषः वार्तालापः` : clean
p025:P9 `सायङ्काले जयलक्ष्म्याः` : F2
p025:P10 `{misc: "माणवकः"}` : skip footer metadata
p026:P1 `{x-com:layout: ...}` : skip layout
p026:P2 `{pc}'माता त` : clean (print `'...'"` mismatch kept as seen, mate of F2 supply, documented in Summary)
p026:P3 `दशादिनानाम् अनन्तरं` : clean (`दशादिनानाम्`, `वधः` kept as printed, documented in Summary)
p026:P4 `"मम वयः` : clean
p026:P5 `"भवदीयान् सर्वान्` : clean
p026:P6 `"अस्तु तावत्,` : clean
p026:P7 `कृष्णशर्मा पञ्चाङ्गम्` : clean
p026:P8 `एषा वार्ता` : clean
p026:P9 `पुत्रः वेङ्कटरमणः` : clean
p026:P10 `पूर्वनिश्चयानुसारं कृष्णशर्मा` : clean
p027:P1 `{x-com:layout: ...}` : skip layout
p027:P2 `{pc}हस्तेन एकं` : clean
p027:P3 `मुनिरामः अतिथीन्` : F3
p027:P4 `रामानुजः तां` : clean
p027:P5 `एतत् वचनं` : clean (`आसम्` kept as printed, documented in Summary)
p027:P6 `कृष्णशर्मा तु` : clean
p027:P7 `रामानुजः शान्तस्वरेण` : clean
p028:P1 `{x-com:layout: ...}` : skip layout
p028:P2 `{pc}धनग्रन्थिं निष्क्रम्य` : clean
p028:P3 `रामानुजस्य वचनं` : clean
p028:P4 `तदा रामानुजः` : clean (`एषा वार्तां` kept as printed, documented in Summary)
p028:P5 `"आं श्रीमन्!` : clean
p028:P6 `"श्रीमन्! सत्यं` : clean
p028:P7 `{pc}विक्रीय प्राप्तं` : clean
p028:P8 `रामानुजस्य उदारतां` : clean
p028:P9 `"योग्यं वरम्` : clean
p028:P10 `"रामानुजार्य! भवतः` : clean
p028:P11 `एतावत्पर्यन्तं द्वारस्य` : clean
J1 p025:P5 {pb} -> p025:P6 {pc} (continues) : ok
J2 p025:P9 {pb} -> p026:P2 {pc} (continues) : ok
J3 p026:P3 {pb} -> p026:P4 fresh (clean break) : ok
J4 p026:P10 {pb} -> p027:P2 {pc} (continues) : ok
J5 p027:P4 {pb} -> p027:P5 fresh (clean break) : ok
J6 p027:P7 {pb} -> p028:P2 {pc} (continues) : ok
J7 p028:P6 {pb} -> p028:P7 {pc} (continues) : ok
J8 p028:P11 {pb} -> END (clean break) : ok
