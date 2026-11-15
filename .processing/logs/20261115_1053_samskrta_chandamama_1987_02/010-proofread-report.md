# Proofread report: 1987_02 p010 (scan pages 10-16, ज्वालाद्वीपः --- द)

## Summary

10 findings: 6 error (all STY/SPL verdicts already landed as blocks), 4 likely held as `{sug-}` candidates. The systematic issues are dropped second quote-strokes at three speech boundaries (F4/F5/F9) and print's house spellings (`शिबिका` for `शिविका`, `पाश्वर्त-`/`पाश्व-` stem for `पार्श्व`, kept as print). The orth scanner reported zero hits on deblocked text, so this is clean letterpress, not OCR output. Every body chunk was read sentence by sentence for continuity; all 14 joints verified grammatical with the asserted left-then-right column order. Loc below is story coordinates `pNN:Pm` plus word index on the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p010:P6 w2 | `इतरपाश्वर्भ्यां सैनिकाः` | `इतरपार्श्वाभ्यां सैनिकाः` | SPL | likely | low* | print keeps a पाश्वर्त- stem throughout, but the dual -भ्यां on it is unparalleled; classical needs पार्श्वाभ्याम् |
| F2 | p011:P5 w9 | `पाश्वें पतितस्य` | `पार्श्वे पतितस्य` | SPL | likely | low* | locative of 'side' is needed; print's पाश्व- stem is consistent but the anusvara is unexplained |
| F3 | p012:P2 w32 | `चिन्तितवान् उग्राक्षः` | `चिन्तितवान् चित्रसेनः` | LEX | likely | medium* | sentence 1 names Chitrasena as angered, the thought is the slighted man's, his abrupt departure proposal follows, and Ugraaksha then fails to grasp his intent |
| F4 | p012:P3 w14 | `तावत्' इति` | `तावत्" इति` | STY | error | high | speech opened with doubles (two-stroke open verified at 3x); single close is a dropped second stroke |
| F5 | p013:P4 w1 | `'राजकुमार्याः विश्वासपूर्णवचनेन` | `"राजकुमार्याः विश्वासपूर्णवचनेन` | STY | error | high | speech (इति वदन्); single open where doubles are expected |
| F6 | p013:P8 w7 | `इदमिदानीम् उक्तवान्` | `इदम् इदानीम् उक्तवान्` | CMP | likely | medium* | no such word exists; missing space fusing इदम् + इदानीम् |
| F7 | p014:P6 w13 | `पलायनं 'न कृतवान्` | `पलायनं न कृतवान्` (stray mark deleted) | STY | error | medium | stray single inside a doubles span; no sentence boundary pins an inner mate |
| F8 | p014:P3 w41 | `पूरस्करोति` | `पुरस्करोति` | SPL | error | high | प्रार्थनां पुरस्करोति ('honour a prayer') is the only verb fitting; पूर- is no root |
| F9 | p015:P6 w36 | `अपि' इति` | `अपि" इति` | STY | error | high | speech opened with doubles; single close is a dropped second stroke |
| F10 | p016:P10 w4 | `इत आश्वर्येण` | `इति आश्चर्येण` | SPL | error | high | इति + instrumental of manner is the fixed idiom; आश्चर्य is the only word fitting |

## Patterns

- Dropped/mismatched quote strokes at speech boundaries (3x: F4, F5, F9), all repaired with `{del:}`/`{ins:}` verdicts. One long Chitrasena speech is printed throughout in singles (p012:P6-P7 `'किम् ... प्रयोजनम्?'`); it is balanced and uniform, so it is kept as the compositor's choice per the p01 precedent, not normalised.
- House spellings kept as print: `शिबिका` (12x, never `शिविका`), `पाश्वर्त-`/`पाश्व-` stem (4x), open sandhi (`तत् श्रुत्वा`, `यत् कठोरम्`) matching the 1984 reference behaviour. No finding.
- Tense mixing in narration (presents `पश्यति` amid pasts, p016:P5) is STY at most per the prose guide; no finding.

## Unverified

- F1 (`इतरपाश्वर्भ्यां`): settled by comparing other 1987 issues' spelling of the पार्श्वतः/पार्श्वाभ्याम् adverbs; if the पाश्वर्त- stem recurs, drop the candidate and log a house variant.
- F2 (`पाश्वें`): settled by checking whether the anusvara recurs on this stem elsewhere in the run; single occurrence favours the `पार्श्वे` fix.
- F3 (thinker `उग्राक्षः`/`चित्रसेनः`): settled by the coordinator reading p012:P2 against the story sense; both agents' anger is conceivable, so this stays a user call.
- F6 (`इदमिदानीम्`): settled by checking inter-word spacing habits of this compositor; a clear इदम् + इदानीम् split applies.

## Coverage

- p010:P1 `{x-com:layout:` : skip layout-only chunk
- p010:P2 `# ज्वालाद्वीपः` : skip title chunk
- p010:P3 `(अमरपालस्य नायकत्वे` : clean
- p010:P4 `व्याघ्रचर्मधारिणां नायकः` : clean
- p010:P5 `एकपाश्वर्तः चित्रसेनः,` : clean
- p010:P6 `उग्राक्षः, इतरपाश्वर्भ्यां` : F1
- p011:P1 `{x-com:layout:` : skip layout-only chunk
- p011:P2 `इति ज्ञात्वा` : clean
- p011:P3 `'कान्तिमत्याः रक्षणे` : clean
- p011:P4 `चित्रसेनः कोपावेशेन` : clean
- p011:P5 `तदा अकस्मात्` : F2
- p011:P6 `तत् दृष्ट्वा` : clean
- p011:P7 `"एषः चित्रपुरराज्यस्य` : clean
- p011:P8 `कान्तिमती उग्राक्षं` : clean
- p012:P1 `{x-com:layout:` : skip layout-only chunk
- p012:P2 `राजकुमार्याः कान्तिमत्याः` : F3
- p012:P3 `"उग्राक्ष! अस्माकं` : F4
- p012:P4 `चित्रसेनस्य आन्तर्यं` : clean
- p012:P5 `"चित्रसेन! कपिलपुरस्य` : clean
- p012:P6 `'किम् अस्माभिः` : clean
- p012:P7 `{pc}कपिलपुरं वशीकृत्य` : clean
- p012:P8 `चित्रसेनस्य वचनं` : clean
- p013:P1 `{x-com:layout:` : skip layout-only chunk
- p013:P2 `"सः कपिलपुरीयः` : clean
- p013:P3 `"असत्यम् एतत्।` : clean
- p013:P4 `'राजकुमार्याः विश्वासपूर्णवचनेन` : F5
- p013:P5 `{pc}प्रदर्शितवान् उग्राक्षः।` : clean
- p013:P6 `"भोः जडमते!` : clean
- p013:P7 `"साहाय्यम् आवश्यकम्` : clean
- p013:P8 `तदा कान्तिमती` : F6
- p013:P9 `चित्रसेनः उग्राक्षं` : clean
- p013:P10 `क्षणकालानन्तरं मन्दस्वरेण` : clean
- p014:P1 `{x-com:layout:` : skip layout-only chunk
- p014:P2 `{pc}अधिकारी सः` : clean
- p014:P3 `"एवं वा?` : F8
- p014:P4 `एतत् श्रुतवतः` : clean
- p014:P5 `"आम्, भवतः` : clean
- p014:P6 `कान्तिमती मन्दहासं` : F7
- p014:P7 `कान्तिमती तत्` : clean
- p014:P8 `"युक्तं महाराज!` : clean
- p015:P1 `{x-com:layout:` : skip layout-only chunk
- p015:P2 `{pc}व्याघ्रचर्मधारिणः यत्` : clean
- p015:P3 `"इतःपरं राजकुमार्या` : clean
- p015:P4 `एकघण्टां यावत्` : clean
- p015:P5 `{pc}उपरि दुर्गरक्षणार्थं` : clean
- p015:P6 `तौ भयङ्करपक्षिणौ` : F9
- p015:P7 `अमरपालस्य जीवितविषये` : clean
- p015:P8 `वस्तुतः चित्रसेनस्य` : clean
- p016:P1 `{x-com:layout:` : skip layout-only chunk
- p016:P2 `{pc}दुर्गे पक्षिणौ` : clean
- p016:P3 `"युक्तं निर्णयं` : clean
- p016:P4 `अनन्तरं सः` : clean
- p016:P5 `उग्राक्षः तु` : clean
- p016:P6 `उग्राक्षस्य मनोभावं` : clean
- p016:P7 `{pc}मदीयं नायकत्वम्` : clean
- p016:P8 `"बलम् अस्ति` : clean
- p016:P9 `"पक्षिणोः विषये` : clean
- p016:P10 `"तत् कथं` : F10
- p016:P11 `"अद्य प्रातः` : clean
- J1 p010:P5 -> p010:P6 : ok (अपरपाश्वर्तः -> उग्राक्षः, spaced continuation)
- J2 p010:P6 -> p011:P2 : ok (page turn, clean break)
- J3 p011:P3 -> p011:P4 : ok (column turn, clean break)
- J4 p011:P8 -> p012:P2 : ok (page turn; p012 reacts to the reboarding)
- J5 p012:P6 -> p012:P7 : ok (प्रयत्नेन -> कपिलपुरं, spaced continuation)
- J6 p012:P8 -> p013:P2 : ok (page turn; answers her question)
- J7 p013:P4 -> p013:P5 : ok (गमनत्वरां -> प्रदर्शितवान्, spaced continuation)
- J8 p013:P10 -> p014:P2 : ok (एतस्य -> अधिकारी, speech continues)
- J9 p014:P5 -> p014:P6 : ok (column turn, clean break)
- J10 p014:P8 -> p015:P2 : ok (दुष्टान् -> व्याघ्रचर्मधारिणः, spaced continuation)
- J11 p015:P4 -> p015:P5 : ok (दुर्गस्य -> उपरि, spaced continuation)
- J12 p015:P8 -> p016:P2 : ok (अस्मि --- -> दुर्गे, speech continues)
- J13 p016:P6 -> p016:P7 : ok (भवान् -> मदीयं, speech continues)
- J14 p016:P11 -> END : ok (clean end at अनुवर्तते)
