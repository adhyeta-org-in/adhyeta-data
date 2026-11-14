# Proofread report: samskrta_chandamama 1984_12, story p032 (pp. 32–36, "युक्तिमान्")

## Summary

Loc below is `pNN:Pm:wN` (page span, lint chunk number, word number on the chunk counting print words from 1); anchors are the first two print words of the chunk. 10 findings: 4 errors with high confidence (print misprints fixed via `{del:}`/`{ins:}`), 3 held candidates (`{sug-del:}`/`{sug-ins:}`, unverified), 3 style findings (top-level spoken utterances set in single quotes, normalized to doubles). One pattern (quote-sort normalization, 3 cases). Sanskrit `scan.py orth` on deblocked text reported zero hits; both extract and proofread lint gates are green. One furniture note: p32 prints a centered `"भगिनी"` below the story frame (next-story teaser); stripped per furniture rules, not transcribed.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p32:P3:w33 [मः स्वयमेव] | `प्रभवामि" इति मः स्वयमेव` | `सः` | OCR | error | high | `मः` is not a Sanskrit word; the clause needs masc.nom.sg subject for `कुर्वन् आसीत्` |
| F2 | p32:P5:w24 [कृतः तदर्थं] | `यदि साधारं साधयति` | `सप्रमाणं` | OCR | likely | low* | `साधारं` has no dictionary standing here; `सप्रमाणं` ("with evidence") fits `साधयति`, but the glyph distance is large so this is held |
| F3 | p33:P6:w4 ["अस्तु गच्छावः] | `इति उभावतपि मान्त्रिकस्य` | `उभावपि` | OCR | error | high | dual subject `गतवन्तौ` requires `उभौ + अपि = उभावपि` |
| F4 | p34:P3:w13 [मान्त्रिकः नेत्रे] | `यच्छन्ति तदेन देवी` | `तदेव` | OCR | likely | low* | `तदेन` is not a word; minimal change (`न`/`व`, cf. `त`/`न` confusion) gives `तदेव` "that itself", though correlative `तत्तत्` to `यद्यत्` is also conceivable |
| F5 | p34:P4:w8 ["दशदिनेभ्यः पूर्वं] | `केनचित् अपहृतनि।` | `अपहृतानि` | OCR | error | high | `रूप्यकाणि` (neut.pl) needs neut.pl participle; dropped `आ` matra |
| F6 | p34:P5:w8 [वस्त्रे बन्धयित्वा] | `स्थापितवान् आसम्।` | `अस्मि` | MRP | likely | low* | `अहं` subject needs 1st person, but the story elsewhere uses bare `क्तवतु` for 1st person (`अहं न कथितवान्` p36:P4), so `आसम्` may instead be intrusive; held |
| F7 | p36:P2:w10 [आगतवान् तदा] | `अतः भवनः समीपे` | `भवतः` | OCR | error | high | `समीपे` takes genitive (cf. `भवतः समीपे` p34:P5, p35:P13); `न`/`त` confusion |
| F8 | p35:P9:w5 [तत्र कनकराजः] | `'मान्त्रिकस्य ... नास्ति' इति।` (spoken, `उक्तवान्`) | `"मान्त्रिकस्य ... नास्ति"` | STY | style | high | top-level spoken utterance with reporting verb takes era double marks, not singles |
| F9 | p35:P11:w1 ['मम धनं] | `'मम ... भवेत्' इति उक्तवान्` (spoken) | `"मम ... भवेत्"` | STY | style | high | same as F8: spoken utterance with `उक्तवान्` takes doubles |
| F10 | p35:P6:w2 [कनकराजः 'अस्तु'] | `'अस्तु' इति अङ्गीकृत्य` (spoken assent) | `"अस्तु"` | STY | style | medium | spoken assent is speech, but single-word assents may be a print economy; normalized to doubles for consistency |

## Patterns

- Quote-sort normalization (3 cases: F8 p35:P9, F9 p35:P11, F10 p35:P6): top-level spoken utterances printed in single quotes corrected to era double marks; all other top-level speeches in the story already use doubles and all nested/thought singles are correct as seen.

## Unverified

- F2 `साधारं`: no dictionary attestation found for an adverbial `स` + `आधार` formation here; settling needs either a lexicon attestation or a parallel-text witness. Held as `{sug-del:साधारं}{sug-ins:सप्रमाणं}`.
- F4 `तदेन`: `तदेव` vs correlative `तत्तत्` cannot be decided from text alone; settling needs the source-language (likely Telugu/Hindi Chandamama) sentence. Held as `{sug-del:तदेन}{sug-ins:तदेव}`.
- F6 `आसम्`: periphrastic `स्थापितवान् अस्मि` vs bare `स्थापितवान्` (story's own 1st-person idiom) cannot be decided from text alone; settling needs corpus evidence from other Chandamama issues. Held as `{sug-del:आसम्}{sug-ins:अस्मि}`.

## Checked print-faithful (no change)

- `ससन्तोषं` (p32:P3, P5): regular `स` + `सन्तोष` adverbial formation (cf. `सस्मितं`); kept.
- `कञ्चन` (p32:P3): valid classical variant of `कश्चन`; kept.
- `चिन्तयति स्म` (p32:P3): Epic `स्म` for `स्म`; kept as variant.
- `दीयन्ते` (p32:P5): print spaces its akṣaras loosely (`दी य न्ते`); one word, joined.
- Open sandhi throughout (`सः मान्त्रिकः`, `अतः एव`, `तं ग्रामं प्रति`) and open/joined mix (`तदर्थं`, `एतत्सर्वं`) match Chandamama house style; not flagged.
- House commas (`'मान्त्रिकस्य, प्रभावेण`, `निश्चितवान्, दत्तवान्`, `अस्थिद्वयम्, एकं`) are consistent print punctuation; kept.
- `'अस्तु, गच्छावः'` stays double; lone-word `'अस्तु'` normalized per F10; all thought/inner singles kept as seen.

## Coverage

- p32:P1 {x-com:layout:} : skip layout-only chunk
- p32:P2 # युक्तिमान् : skip title
- p32:P3 सीतापुरम् इति : F1
- p32:P4 एकस्मिन् दिने : clean
- p32:P5 कृतः तदर्थं : F2
- p32:P6 कनकराजः किञ्चित् : clean
- p32:P7 कमलनाथः एकम् : clean
- p33:P1 {x-com:layout:} : skip layout-only chunk
- p33:P2 स्वीकृतवान् किल? : clean
- p33:P3 "यदि मान्त्रिकः : clean
- p33:P4 "तदा भवता : clean
- p33:P5 कमलनाथस्य चातुर्यपूर्णं : clean
- p33:P6 "अस्तु गच्छावः : F3
- p33:P7 कनकराजः तं : clean
- p34:P1 {x-com:layout:} : skip layout-only chunk
- p34:P2 "स्वामिन् मम : clean
- p34:P3 मान्त्रिकः नेत्रे : F4
- p34:P4 "दशदिनेभ्यः पूर्वं : F5
- p34:P5 वस्त्रे बन्धयित्वा : F6
- p34:P6 मान्त्रिकः पुनः : clean
- p35:P1 {x-com:layout:} : skip layout-only chunk
- p35:P2 केनापि उपायेन : clean
- p35:P3 मान्त्रिकः एवम् : clean
- p35:P4 कनकराजः विनयेन : clean
- p35:P5 "चोरः भवतः : clean
- p35:P6 कनकराजः 'अस्तु' : F10
- p35:P7 अतः सः : clean
- p35:P8 एतत्सर्वं दृष्ट्वा : clean
- p35:P9 तत्र कनकराजः : F8
- p35:P10 तदा कमलनाथः : clean
- p35:P11 'मम धनं : F9
- p35:P12 "अये भवान् : clean
- p35:P13 "अहं यदा : clean
- p36:P1 {x-com:layout:} : skip layout-only chunk
- p36:P2 आगतवान् तदा : F7
- p36:P3 "एतत् सर्वं : clean
- p36:P4 "ग्रामे सर्वेऽपि : clean
- p36:P5 इति कनकराजः : clean
- p36:P6 "भवता सत्यं : clean
- p36:P7 "एतत् बहु : clean
- p36:P8 तदा कमलनाथः : clean
- J1 p32:P4 {pb} -> p32:P5 {pc} : ok (उपकारः + कृतः spaced join, column turn inside open speech)
- J2 p32:P7 {pb} -> p33:P2 {pc} : ok (ऋणत्वेन + स्वीकृतवान् spaced join, page turn inside open speech)
- J3 p33:P4 {pb} -> p33:P5 fresh : ok (कमलनाथः। terminal, clean column break)
- J4 p33:P7 {pb} -> p34:P2 {pc} : ok (उक्त्वा + "स्वामिन् continuation, page turn)
- J5 p34:P4 {pb} -> p34:P5 {pc} : ok (एकस्मिन् + वस्त्रे spaced join, column turn)
- J6 p34:P6 {pb} -> p35:P2 {pc} : ok (अतः + केनापि spaced join, page turn inside open thought)
- J7 p35:P5 {pb} -> p35:P6 fresh : ok (उक्तवान्। terminal, left-column to right-column break)
- J8 p35:P13 {pb} -> p36:P2 {pc} : ok (याचितुम् + आगतवान् spaced join, page turn inside open speech)
- J9 p36:P4 {pb} -> p36:P5 {pc} : ok (कथितवान्" + इति continuation across columns, quote mate follows)
- J10 p36:P8 {pb} -> END : ok (गतवान्। story closes, no folio on print)
