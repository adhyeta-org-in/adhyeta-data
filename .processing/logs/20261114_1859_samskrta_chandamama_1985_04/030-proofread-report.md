# Proofread report: 1985_04 p030 (START=30, RUN 20261114_1859_samskrta_chandamama_1985_04)

## Summary

Range 30..32 (3 scans) transcribed in Phase A and proofread here with images closed; extract gate and proofread gate both pass with exit 0. Four findings: two applied STY verdicts (stray print singles before double-opens, the same defect at two sites) and two held word candidates (unverified). The systematic issue is a stray single quote stroke printed immediately before a double-open at three sites (deleted twice by verdict, kept once where it nests). The Sanskrit orth scanner reported no hits on deblocked text, and the word-level pass found case, voice, gerund and agreement all sound, with the edition's mixed open/joined sandhi kept as house style throughout. No passage was left unchecked; glyph questions were settled in Phase A and travel here only as blocks.

## Findings

Loc is `pNN:Pm` (NN = scan sequence 30 + `{pgb}`-span ordinal, Pm = lint chunk number within that span) plus the first two words as anchor.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p031:P11 पत्नी पुनः | stray `'` before `"कीदृशः` | delete (applied `{del:'}`) | STY | style | high | lone single jammed before a double-open breaks SQ/DQ nesting and no boundary pins an SQ open here |
| F2 | p032:P4 पतिपत्न्योः सम्भाषणं | stray `'` before `"गृहस्य` | delete (applied `{del:'}`) | STY | style | high | same stray-single-before-double defect inside a thought-quote; deletion leaves a balanced `"..."` pair |
| F3 | p032:P3 `"एवं वा?"'` | `पत्नी तूष्ण्या निद्राम्` | `पत्नी तूष्णीं निद्राम्` | SPL | likely | medium* | `तूष्ण्या` has no stem and instrumental fits nothing with `आलिङ्गितवती`; the same story writes adverbial `तूष्णीं` at p030:P8 |
| F4 | p032:P9 कुप्रसिद्धचोरस्य ग्रहण | `ग्रहण साहाय्यं कृतवते` | `ग्रहणे साहाय्यं कृतवते` | OCR | likely | medium* | dropped `e`-mātrā is the smallest change and `ग्रहणे` + noun matches this story's own `ग्रहणे कृतम् उपायं` at p032:P8 |

## Patterns

Stray single printed immediately before a double-open (`'‘`): 3 sites. Deleted by verdict at p031:P11 `कीदृशः` (F1) and p032:P4 `गृहस्य` (F2). Kept as printed at p032:P3 `'"एवं वा?"'` (balanced SQ(DQ) nest, no gate residual, no verdict).

## Unverified

F3* `तूष्ण्या` vs `तूष्णीं`: held as `{sug-del:तूष्ण्या}{sug-ins:तूष्णीं}`. Would be settled by a 400 DPI+ glyph re-check (्या vs ीं + anusvāra) or a second print witness; dictionary attestation of `तूष्ण्या` as an instrumental adverb would instead clear the print. F4* `ग्रहण` vs `ग्रहणे`: held as `{sug-del:ग्रहण}{sug-ins:ग्रहणे}`. Would be settled by a glyph re-check for an `e`-mātrā trace on `ण`; the parallel `ग्रहणे कृतम् उपायं` one line above supports `ग्रहणे`.

## Coverage

p030:P1 `{x-com:layout:` : skip layout-only chunk
p030:P2 `# कौमुदी-सोपानम्` : skip title heading
p030:P3 श्रीकृष्णदेवरायः विजयनगरं : clean
p030:P4 कृष्णदेवरायस्य आस्थाने : clean
p030:P5 इति। एवं : clean
p030:P6 'सम्पत्तिविषयं श्रुत्वा : clean
p030:P7 यथानिरीक्षितं सः : clean
p030:P8 अनन्तरं सः : clean
p030:P9 `{note:` : skip footer metadata chunk
p031:P1 `{x-com:layout:` : skip layout-only chunk
p031:P2 शयनं करोतु : clean
p031:P3 तदा पत्नी : clean
p031:P4 "चोरः आगच्छतु : clean
p031:P5 'एतद्विषये प्रष्टव्यम् : clean
p031:P6 "अये उच्चैः : clean
p031:P7 "चौर्येण वा : clean
p031:P8 "भवान् सर्वं : clean
p031:P9 करोमि। अन्यथा : clean
p031:P10 "स्वयं ब्रह्मा : clean
p031:P11 पत्नी पुनः : F1
p032:P1 `{x-com:layout:` : skip layout-only chunk
p032:P2 तावत् प्रतीक्षां : clean
p032:P3 '"एवं वा?"' : F3
p032:P4 पतिपत्न्योः सम्भाषणं : F2
p032:P5 अनन्तरदिने एषः : clean
p032:P6 गवाक्षः तेन : clean
p032:P7 तत्र वायुं : clean
p032:P8 एतदनन्तरं रामकृष्णः : clean
p032:P9 कुप्रसिद्धचोरस्य ग्रहण : F4
J1 p030:P4 -> p030:P5 : ok (column turn, `...क्षीणम्'` → `{pc}इति।` closes the speech)
J2 p030:P8 -> p031:P2 : ok (page turn, `...तूष्णीं` → `{pc}शयनं...` adverb-verb join)
J3 p031:P8 -> p031:P9 : ok (column turn, `...निद्रां` → `{pc}करोमि।` object-verb join)
J4 p031:P11 -> p032:P2 : ok (page turn, `...न प्रसरति` → `{pc}तावत्...` यावत्-तावत् correlative)
J5 p032:P5 -> p032:P6 : ok (column turn, `...उक्तः` → `{pc}गवाक्षः...` participle-noun join)
J6 p032:P9 -> END : ok (clean break, story ends)
