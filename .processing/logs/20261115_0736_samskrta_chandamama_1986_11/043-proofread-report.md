# Proofread report: 1986_11 p043 (अदृष्टं दुरदृष्टं च, p043 span)

## Summary

2 findings (both STY/error, high confidence), each a single-stroke close mark where the era standard and the opening mark require a double; both sit at an `इति`-closure pinning the position, so each is routed as a verified `{del:'}{ins:"}` verdict in the story file. No repeats, so no Patterns section. Print conventions kept as house style throughout: open sandhi at word boundaries (तस्य क्षेत्रे, मम अपि), mixed `अधिकम् अधिकं`, commas after `पश्यतु`, `दृश्यते`, `आसीत्`, `आलिङ्ग्य`, `गृहं`, balanced print doubles on all speeches, and print singles kept as seen for the epithet `'श्वेतवस्त्रधारिणी'` (p044:P13) and the thought `'दरिद्रदेवतां ... समीपम्'` (p045:P6-P7). Orth scanner (`scan.py orth` on deblocked text) reports no findings; word, sandhi, morphology, syntax, quote, and flow passes done sentence by sentence from text alone with images closed. The story opens on p043 and closes terminal on p045, so flow is verified for the whole tale; the text is direct transcription from scans, not OCR output. Loc below uses file page `p043`-`p045` + lint chunk `P` + word counted on the chunk from 1, with the chunk's first two words as anchor.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p043:P8:7 (नष्टानि न) | `योजयन्ती अस्मि'` | `योजयन्ती अस्मि"` | STY | error | high | speech opened with `"` closes with one stroke where the era standard expects two (dropped second stroke); `इति` pins the position, applied as `{del:'}{ins:"}` |
| 2 | p043:P10:11 ("तत्र पश्यतु,) | `सा अस्ति'` | `सा अस्ति"` | STY | error | high | speech opened with `"` closes with one stroke where the era standard expects two (dropped second stroke); `इति` pins the position, applied as `{del:'}{ins:"}` |

## Unverified

None. Both inherited Phase A candidates (single closes on p043:P8 and p043:P10) are promoted to verified verdicts (F1, F2); no candidate is held for the user. Keeping either single would leave a `"` opened span closed by a thought-sort mark with no grammatical role, so supply stands.

## Coverage

p043:P1 {x-com:layout:} : skip x-com-only
p043:P2 # अदृष्टं : skip title
p043:P3 कस्मिंश्चित् ग्रामे : clean
p043:P4 एकस्मिन् वर्षे : clean
p043:P5 तदा सः : clean
p043:P6 यदा सा : clean
p043:P7 "अहं भवतः : clean
p043:P8 नष्टानि न : F1
p043:P9 "एवं वा? : clean
p043:P10 "तत्र पश्यतु, : F2
p043:P11 अदृष्टदेवताम् अन्विष्यन् : clean
p043:P12 तदा चुल्याः : clean
p043:P13 उच्चैः रोदनं : clean
p043:P14 "बहुदूरं गन्तव्यम्। : clean
p043:P15 {category:} : skip metadata
p044:P1 {x-com:layout:} : skip x-com-only
p044:P2 बालिका। चलितुं : clean
p044:P3 अनन्तरम् अनुजः : clean
p044:P4 तत्क्षणमेव दरिद्रदेवता : clean
p044:P5 मार्गे एकत्र : clean
p044:P6 सः दक्षिणदिशि : clean
p044:P7 "मया एकः : clean
p044:P8 अनुजः एतत् : clean
p044:P9 यत् लभ्यते : clean
p044:P10 एवमेव अधिकम् : clean
p044:P11 ततः कश्चन : clean
p044:P12 अनुजः तस्याः : clean
p044:P13 तस्मात् 'श्वेतवस्त्रधारिणी' : clean
p044:P14 "भवती का?" : clean
p045:P1 {x-com:layout:} : skip x-com-only
p045:P2 अद्य आरभ्य : clean
p045:P3 अनुजः खननसमये : clean
p045:P4 इदानीम् अनुजः : clean
p045:P5 एकस्मिन् दिने : clean
p045:P6 अनुजस्य ऐश्वर्यं : clean
p045:P7 समीपम्' इति : clean
p045:P8 अतः सः : clean
p045:P9 तत्क्षणे एव : clean
p045:P10 एतां पुनः : clean
p045:P11 यदा सः : clean
J1 p043:P7 {pb} -> p043:P8 {pc} : ok (column turn; वृथा + नष्टानि forms valid spaced join)
J2 p043:P14 {pb} -> p044:P2 {pc} : ok (page turn; इतोऽपि + बालिका continuous, close-plus-इति on p044)
J3 p044:P9 {pb} -> p044:P10 fresh : ok (clean column break; terminal । then new indented para)
J4 p044:P14 {pb} -> p045:P2 {pc} : ok (page turn; same speech, close-plus-इति on p045)
J5 p045:P6 {pb} -> p045:P7 {pc} : ok (column turn; तस्य + समीपम् forms valid spaced join, SQ pair closes)
J6 p045:P11 {pb} -> END : ok (clean break; story ends terminal before bottom art)
