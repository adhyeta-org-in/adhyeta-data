# Proofread report: 1984_08 p029 (अति सर्वत्र वर्जयेत्)

## Summary

4 findings, all STY quote-mark rulings (3 single-open speeches corrected to doubles, 1 missing close supplied); no word-level verdicts, since print is grammatical throughout and Phase A left no word flags on file. The systematic issue is the compositor dropping one stroke of double-low open quotes on four speeches (three verified lone singles, plus a recurring detached speck before several genuine double opens that was omitted as print noise in Phase A). One mechanical spacing fix applied directly (भवतीअन्यत्र to भवती अन्यत्र, matching the edition's spaced usage in the same column). Loc is story coordinates pNN:Pm with the word counted on the chunk from 1, blocks ignored. No passages left unchecked; the text is a print transcription, not OCR output (orth scan clean, 0 hits).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p030:P6 [एकस्मिन् दिने] w11 | `'भवती सत्यं` | `"भवती सत्यं` | STY | style | high | reported speech takes doubles; हसित्वा plus उक्तवती and iti-closure pin speech |
| 2 | p030:P8 [साधुः गृहम्] w38 | `'पत्युः स्वभावे` | `"पत्युः स्वभावे` | STY | style | high | spoken question by the sadhu; same speech closes with a double on p031:P2 |
| 3 | p032:P7 [यावत् पर्यन्तं] w13 | `'अहं गृहे` | `"अहं गृहे` | STY | style | high | direct spoken retort in an alternating dialogue; doubles match every neighbouring speech |
| 4 | p032:P7 [यावत् पर्यन्तं] w20 | `हानिः?` (no close) | `हानिः?"` | STY | style | high | speech ends at a speaker-change column edge; iti-less dialogue still needs its close |

## Patterns

Print singles-for-speech corrected to doubles: 4 blocks across 3 speeches (neighbour's teasing F1, sadhu's question F2, Sadananda's retort open F3 plus its supplied close F4); all other singles kept as correct thought/inner marks ('तदा अहम्', 'गृहे', 'तर्हि', 'सदानन्द', 'अस्याः'). Detached pre-quote specks omitted as print noise in Phase A before the double-low opens of भवत्याः (p029), मम, बाले, तत्र, and अहं परगृहं; verified at 3x-plus as clearly detached from the mark. One stray comma-like mark after शक्यते।'' (p032:P6) omitted as print noise with an on-file x-com.

## Unverified

गृहीयाणां (p029:P8, Sadananda's स्वामी speech): odd formation for the expected household-care word; no dictionary check done and images closed, so no block laid — settles with a lexicon lookup of गृहीय. माम् असमर्थः (p029:P8, same speech): nominative complement after accusative माम् inside an इति-quote reads colloquial; kept as printed dialogue — settles with a style ruling on quoted-speech agreement.

## Coverage

p029:P1 {x-com:layout} : skip layout
p029:P2 अति सर्वत्र : skip title
p029:P3 {x-com:title-trim} : skip print-note
p029:P4 एकस्मिन् ग्रामे : clean
p029:P5 पत्तने सदानन्दस्य : clean
p029:P6 दशद्वादश दिनानि : clean
p029:P7 एवम् एव : clean
p029:P8 पत्युः वचनं : clean
p029:P9 {category:भगिनी} : skip metadata
p030:P1 {x-com:layout} : skip layout
p030:P2 क्षालनं वस्त्रक्षालनं : clean
p030:P3 अन्यस्मिन् दिने : clean
p030:P4 सदानन्दः तत् : clean
p030:P5 वान्। सदानन्दस्य : clean
p030:P6 एकस्मिन् दिने : F1
p030:P7 एवमेव कानिचन : clean
p030:P8 साधुः गृहम् : F2
p031:P1 {x-com:layout} : skip layout
p031:P2 किं परिवर्तनम् : clean
p031:P3 अरुणा पत्युः : clean
p031:P4 विना कारणं : clean
p031:P5 अस्तु। भवत्याः : clean
p031:P6 अस्तु, अवश्यं : clean
p031:P7 अनन्तरं साधुः : clean
p031:P8 अहमपि तस्याः : clean
p031:P9 तर्हि भवतः : clean
p031:P10 भाग्यशाली!" : clean
p031:P11 अस्याः कारणेन : clean
p031:P12 अरुणा किंकर्तव्यमूढा : clean
p031:P13 कुत्र गतवती? : clean
p032:P1 {x-com:layout} : skip layout
p032:P2 तत्र गत्वा : clean
p032:P3 दारिद्र्यम् किमपि : clean
p032:P4 भवती अन्यत्र : clean
p032:P5 भवतः योग्यतयाः : clean
p032:P6 यत्किमपि भवतु : clean
p032:P7 यावत् पर्यन्तं : F3, F4
p032:P8 अहं परगृहं : clean
p032:P9 अनन्तरं सदानन्दः : clean
p032:P10 अरुणे! मां : clean
p032:P11 हन्त! अद्य : clean
p032:P12 एकमासपर्यन्तं व्रताचरणेन : clean
J1 p029:P6 {pb} -> p029:P7 fresh : ok (clean column break, new episode)
J2 p029:P8 {wb} -> p030:P2 {pc} : ok (पात्र-क्षालनं solid join, category follows)
J3 p030:P4 {wb} -> p030:P5 {pc} : ok (प्रेषित-वान् solid join across columns)
J4 p030:P8 {pb} -> p031:P2 {pc} : ok (sadhu question continues, F2 open ruled)
J5 p031:P9 {pb} -> p031:P10 {pc} : ok (speech continues across columns)
J6 p031:P13 {pb} -> p032:P2 fresh : ok (speaker change to Sadananda, clean break)
J7 p032:P7 {pb} -> p032:P8 fresh : ok (speaker change to Aruna, clean break, F4 close supplied)
J8 p032:P12 {pb} -> END : ok (story-end clean break)
