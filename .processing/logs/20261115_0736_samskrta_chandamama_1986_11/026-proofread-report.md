# Proofread report: 1986_11 p026 (scans 26–29, कविसम्माननम्)

## Summary

Range p026 (4 spans, scans 26–29) transcribes a complete court episode: the poet चान्द्रायण seeks patronage from विशाखदत्त, the minister मञ्जुनाथ first offers him a stable-groom post and then slanders him, and the poet's defence of कवित्व converts the minister and wins the आस्थानकविपदवी. Two findings: one certain quote-sort verdict (F1) and one held proper-noun candidate (F2). No systematic problem, no unchecked passage (every chunk read sentence by sentence for continuity), and the text is hand transcription, not OCR. Orth scan (`scan.py orth` on deblocked text) is clean; `lint --phase proofread` exits 0. `Loc` is `pNN:Pm` plus the chunk's first two words, words counted on the chunk from 1 with block tokens excluded.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p029:P7 देशस्य गौरवस्य w36 | `तिष्ठति" इति` | `तिष्ठति{ins:'}" इति` | STY | style | high | Print opens the maxim with SQ but closes with DQ, breaking era nesting DQ SQ ... SQ DQ; the inner close is missing at a pinned position |
| 2 | p027:P5 विशालदेशस्य सचिवस्य w1 | `विशालदेशस्य सचिवस्य` | `{sug-del:विशालदेशस्य}{sug-ins:वत्सदेशस्य}` | CNS | likely | medium* | The heard words are मञ्जुनाथ's, minister of विशाखदत्त of वत्सदेश (p026:P3), so विशालदेशस्य fits neither person nor realm |

## Unverified

F2 held: `विशालदेशस्य` is a clear print reading (verified in Phase A) but a story inconsistency, not a glyph doubt; the minimal repair is `वत्सदेशस्य` (keeps `देशस्य`), with `विशाखदत्तस्य` as the alternative. Tested readings: (a) minister of another realm fails, because सचिवस्य owns the just-heard words spoken by मञ्जुनाथ; (b) epithet reading fails, since देशस्य forces a realm name. What would settle it: a later issue page naming the realm, or editorial records; images stay closed so the glyph cannot be re-settled, and per house style the candidate is held for the user.

## Coverage

p026:P1 layout-only : skip x-com-only
p026:P2 title : skip title
p026:P3 पूर्व वत्सदेशं : clean
p026:P4 'अलसाः कवयः : clean
p026:P5 "कविजनानां पोषणं : clean
p026:P6 वस्तुतः विशाखदत्तः : clean
p026:P7 किन्तु सचिवः : clean
p026:P8 करोति। एतस्य : clean
p026:P9 एवं हि : clean
p026:P10 स्वीयपितामहस्य काले : clean
p026:P11 author-only : skip metadata
p027:P1 layout-only : skip x-com-only
p027:P2 विशाखदत्तः अतीव : clean
p027:P3 विशाखदत्तराजः चान्द्रायणम् : clean
p027:P4 यापयतु" इति : clean
p027:P5 विशालदेशस्य सचिवस्य : F2
p027:P6 विशाखदत्तः चान्द्रायणस्य : clean
p027:P7 सचिवः मञ्जुनाथः : clean
p027:P8 एकस्य कवेः : clean
p028:P1 layout-only : skip x-com-only
p028:P2 किन्तु चान्द्रायणः : clean
p028:P3 चान्द्रायणस्य वचनं : clean
p028:P4 भवेत्" इति : clean
p028:P5 एतत् वचनं : clean
p028:P6 एतेन अतीव : clean
p029:P1 layout-only : skip x-com-only
p029:P2 भवतः आस्थाने : clean
p029:P3 "कः सः : clean
p029:P4 "विशाखदत्तमहाराजस्य राज्ये : clean
p029:P5 सचिवः किमपि : clean
p029:P6 तदा चान्द्रायणः : clean
p029:P7 देशस्य गौरवस्य : F1
p029:P8 तस्य वचनानि : clean
p029:P9 सचिवे जातं : clean
J1 p026:P7 {pb} -> p026:P8 {pc} continues : ok
J2 p026:P10 {pb} -> p027:P2 {pc} continues : ok
J3 p027:P3 {pb} -> p027:P4 {pc} continues : ok
J4 p027:P8 {pb} -> p028:P2 fresh : ok
J5 p028:P3 {pb} -> p028:P4 {pc} continues : ok
J6 p028:P6 {pb} -> p029:P2 {pc} continues : ok
J7 p029:P6 {pb} -> p029:P7 {pc} continues : ok
J8 p029:P9 {pb} -> END : ok
