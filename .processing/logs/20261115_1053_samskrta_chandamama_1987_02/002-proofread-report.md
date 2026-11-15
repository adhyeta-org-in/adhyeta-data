## Summary

Proofread of `p002.md` (1987_02, scan pages 2–7; complete story `संन्यासव्रतम्`): 7 findings — 4 quote-sort/supply verdicts on print-mismatched speech and label quotes (F1–F4), 1 stray-mark deletion on the byline (F5), 1 print-misprint word correction (F6), and 1 balanced print quote-pair kept as seen with no block (F7). Sanskrit orth scanner reported zero hits on the deblocked text. No image reopened in Phase B; all glyph questions were settled in Phase A at 3–5x (footer `माणवकः"`, the `"? 'इति` cluster, `मियांव्`, `प्रत्यर्पयत' 'इति`, `'शङ्करः`, `चनलवलनादयः`). `Loc` below is `pNN:Pm` (scan page : lint chunk) plus the first two words as anchor.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p003:P2 संन्यासी आशीर्वादं | `"भवान् कः? किम् आवश्यकम्"? 'इति` | `"भवान् कः? किम् आवश्यकम्?" इति` | STY | error | high | close doubles before `?`, drop stray single before `इति`: `{del:"}{del:'}{ins:"}` |
| F2 | p004:P2 'शङ्करं सर्वेऽपि | `शिष्यसंन्यासी इति आह्वयन्त` | `शिष्यसंन्यासी' इति आह्वयन्त` | STY | error | high | `इति`-closure pins the missing single close of the `'शङ्करं … इति` label-quote: `{ins:'}` |
| F3 | p006:P2 किञ्चित् स्थापयित्वा | `विक्रीतवान् 'शङ्करः।` | `विक्रीतवान् 'शङ्करः'।` | STY | error | medium | lone single opens a name-label with no mate; close after the name completes it parallel to F2: `{ins:'}` |
| F4 | p006:P8 किञ्चित्कालानन्तरं वृद्धः | `प्रत्यर्पयत' 'इति` | `प्रत्यर्पयत" इति` | STY | error | high | two-stroke double close printed with a gap, era standard wants `"` for speech: `{del:'}{del:'}{ins:"}` |
| F5 | p002:P9 {author: माणवकः} | `माणवकः"` | `माणवकः` | STY | error | high | lone closing double on a byline with no opener and no speech frame; stray print mark: `{del:"}` |
| F6 | p006:P4 राजशेखरस्य पुत्र्याः | `तस्याः चनलवलनादयः` | `तस्याः चलनवलनादयः` | OCR | error | high | `चनल` is a non-word; `चलनवलनादयः` fits the विनय-विधेयता/चातुर्य/हावभाव series: `{del:चनलवलनादयः}{ins:चलनवलनादयः}` |
| F7 | p006:P5 'तद्दिनादारभ्य सर्वेऽपि | `'तद्दिनादारभ्य सर्वेऽपि तं 'शङ्कर इत्येव आह्वयन्ति स्म।` | `?` (keep as seen) | STY | style | high | balanced SQ…SQ print pair with a genuinely uncertain pairing (stray open vs dropped close); kept, never relitigated |

## Patterns

- Print quote-mark disorder (F1, F4, F5): the compositor drops, doubles, or mis-sorts closing strokes (`"? '`, `' '`, lone `"` on the byline); all normalized to era-standard doubles for speech with `{del:}`/`{ins:}` verdicts. The kept singles (F2/F3 label-quotes, `मियांव्` DQ pair, F7) and all balanced speech doubles are untouched.
- No repeated word-level defect: F6 is a single न/ल misprint; the orth scanner was silent and proper nouns (`शिवस्वामी`, `शङ्करः`, `भूस्वामिन्`, `राजशेखरः`) spell consistently across all six pages.

## Unverified

- None. Every Phase A residual was promoted to a verdict (F1–F6) or kept with reason (F7); no `{sug-…}` candidate remains in the file.

## Coverage

- p002:P1 `{x-com:layout:` : skip layout-only chunk
- p002:P2 `# संन्यासव्रतम्` : skip title chunk
- p002:P3 गोदावरीनद्याः तीरे : clean (speech `"अहं … अस्मि"` opens P6 closes P6)
- p002:P4 एव क्रमः : clean
- p002:P5 तस्य ग्रामस्य : clean (speech `"स्वामिन् … भवेत्"` balanced)
- p002:P6 तदा संन्यासी : clean
- p002:P7 संन्यासी सर्वसङ्गपरित्यागी : clean
- p002:P8 तस्मिन् समये : clean (ends `{pb}`, page turn)
- p002:P9 `{author: माणवकः}` : F5
- p003:P1 `{x-com:layout:` : skip layout-only chunk
- p003:P2 संन्यासी आशीर्वादं : F1
- p003:P3 तदा बालकः : clean (speech `"श्रीमन् … दातव्या"` balanced)
- p003:P4 "अस्तु, भवान् : clean
- p003:P5 शङ्करः श्रद्धया : clean
- p003:P6 कदाचित् संन्यासी : clean (speech `"श्रीमन् … आगच्छामि"` balanced)
- p003:P7 संन्यासी शिवस्वामी : clean (speech `"शङ्कर … जीवतु"` balanced)
- p003:P8 तदा शङ्करस्य : clean (speech `"श्रीमन्! … यापयामि"` balanced)
- p003:P9 संन्यासी किमपि : clean
- p003:P10 यद्दिने संन्यासी : clean (ends mid-sentence `{pb}`, mate in p004:P2)
- p004:P1 `{x-com:layout:` : skip layout-only chunk
- p004:P2 'शङ्करं सर्वेऽपि : F2 (with `{ins:'}`, joins p003:P10 into `शिष्यं 'शङ्करं … शिष्यसंन्यासी' इति`)
- p004:P3 कस्याञ्चित् रात्रौ : clean
- p004:P4 तदा ग्रामस्थः : clean (speech `"भवता … समीचीनम्"` balanced)
- p004:P5 मार्जालः पालनीयः : clean (speech `"एकस्य … आपतेत्"` balanced; `पालयतः` is gen. sg. participle, grammatical)
- p004:P6 तस्य वचनेन : clean (speech `"श्रीमन्! … भवति?"` balanced)
- p004:P7 शङ्करः किमपि : clean
- p004:P8 सः मार्जालशिशुः : clean (`"मियांव् मियांव्"` DQ pair balanced)
- p004:P9 शङ्करः मार्जालस्य : clean (speech `"भोः … दास्यति"` balanced; ends `{pb}`, page turn)
- p005:P1 `{x-com:layout:` : skip layout-only chunk
- p005:P2 एतदेव उचितम् : clean
- p005:P3 एकः सप्ताहः : clean (long speech `"मार्जालशिशोः …` opens here, closes p005:P4 — page-internal multi-column span carried by `{pb}`/`{pc}`)
- p005:P4 भूस्वामिनः एव। : clean (`{pc}` joins `ऊषरभूमिः`; speech `… क्षेत्रे"` closes here)
- p005:P5 एतत् उत्तमं : clean (speech `"एतस्याः … अस्मि"` balanced)
- p005:P6 एतेन शङ्करः : clean
- p005:P7 एतां अभिवृद्धिं : clean
- p005:P8 अनन्तरवर्षे तस्य : clean (ends mid-phrase `व्ययार्थ{pb}`, mate in p006:P2)
- p006:P1 `{x-com:layout:` : skip layout-only chunk
- p006:P2 किञ्चित् स्थापयित्वा : F3 (with `{ins:'}`, joins p005:P8 into `व्ययार्थ … 'शङ्करः'।`)
- p006:P3 राजशेखरः कदाचित् : clean (speech `"कालः … किल?"` balanced)
- p006:P4 राजशेखरस्य पुत्र्याः : F6
- p006:P5 'तद्दिनादारभ्य सर्वेऽपि : F7 (ends mid-quote `{pb}`, mate in p006:P6)
- p006:P6 आह्वयन्ति स्म। : F7 (`{pc}` joins P5; pair kept as seen)
- p006:P7 एवमेव कानिचन : clean
- p006:P8 किञ्चित्कालानन्तरं वृद्धः : F4 (both speeches balanced after verdicts)
- p007:P1 `{x-com:layout:` : skip layout-only chunk
- p007:P2 एवं पक्षद्वयं, : clean
- p007:P3 सर्वे तं : clean
- p007:P4 शिवस्वामी तान् : clean (speech `"पञ्च … जातम्?"` balanced)
- p007:P5 तं प्रश्नं : clean
- p007:P6 शिवस्वामी तस्याः : clean (ends mid-sentence `समस्याम्{pb}`, mate in p007:P7)
- p007:P7 उचितरीत्या परिहृतवान्। : clean (`{pc}` joins P6)
- p007:P8 तस्मिन् दिने : clean (speech `"श्रीमन् … तत्!"` balanced)
- p007:P9 शिवस्वामी हसन् : clean (speech `"इतःपरम् … शक्नोमि"` balanced)
- p007:P10 शिवस्वामी तस्मै : clean (speech `"संसार … पालयतः"` balanced)
- p007:P11 दिनद्वयानन्तरं शङ्करः : clean (story ends complete, departure with vow taken)
- J1 p002:P5 `{pb}` -> p002:P6 fresh (clean break) : ok
- J2 p002:P8 `{pb}` -> p003:P2 fresh (clean break) : ok
- J3 p003:P5 `{pb}` -> p003:P6 fresh (clean break, time jump) : ok
- J4 p003:P7 `{pb}` -> p003:P8 fresh (clean break) : ok
- J5 p003:P10 `{pb}` -> p004:P2 `{pc}` (continues, F2) : ok
- J6 p004:P6 `{pb}` -> p004:P7 fresh (clean break) : ok
- J7 p004:P9 `{pb}` -> p005:P2 fresh (clean break) : ok
- J8 p005:P3 `{pb}` -> p005:P4 `{pc}` (continues; `ऊषरभूमिः भूस्वामिनः एव`) : ok
- J9 p005:P8 `{pb}` -> p006:P2 `{pc}` (continues; `व्ययार्थ किञ्चित् स्थापयित्वा`, F3) : ok
- J10 p006:P5 `{pb}` -> p006:P6 `{pc}` (continues; F7 kept pair) : ok
- J11 p006:P8 `{pb}` -> p007:P2 fresh (clean break) : ok
- J12 p007:P6 `{pb}` -> p007:P7 `{pc}` (continues; `समस्याम् उचितरीत्या परिहृतवान्`) : ok
- J13 p007:P11 `{pb}` -> END (clean break, story complete) : ok
