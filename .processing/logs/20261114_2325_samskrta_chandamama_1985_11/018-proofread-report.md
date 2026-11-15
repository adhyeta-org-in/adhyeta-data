# Proofread report: 1985_11 p018 (मालविका)

## Summary

Four findings (F1--F4, all STY/style, high confidence): four supplied `"` marks (`{ins:"}` blocks already in the file) so each paragraph of the Swami's multi-paragraph उपन्यास speech opens and closes its own double pair, with nested singles (`'अम्ब!...'`, `'कलाकाराणाम्...'`) correctly enclosed. No `{sug-ins:}`/`{sug-del:}` queue survives from Phase A and none was created; the orth scan reports no hits, the proofread gate is green, and the text was eye-transcribed from print, not OCR output. `Loc` below uses story coordinates `pNN:Pm` with the chunk's first two words as anchor and word counts on the deblocked chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p020:P5 (स्वभावतः प्रेमस्वरूपिणी।) w15 | `सर्वेषु वितरति।` | `सर्वेषु वितरति।{ins:"}` | STY | style | high | first quoted para of the speech needs its own close; reporting verb plus इति-span pins the paragraph |
| 2 | p020:P6 (पुत्रः कदाचित्) w1 | `पुत्रः कदाचित्` | `{ins:"}पुत्रः कदाचित्` | STY | style | high | middle quoted para needs its own open; its four single pairs are nested speech examples requiring enclosing doubles |
| 3 | p020:P6 (पुत्रः कदाचित्) w48 | `तस्याः स्वभावः।` | `तस्याः स्वभावः।{ins:"}` | STY | style | high | middle quoted para needs its own close at its terminal danda |
| 4 | p020:P7 (किन्तु कदाचित्) w1 | `किन्तु कदाचित्` | `{ins:"}किन्तु कदाचित्` | STY | style | high | final quoted para opens here; its close is the print `"` after आगतवान् in p021:P2 across the page turn, which is never forced closed |

## Patterns

Multi-para quotation pairing in the Swami's speech (4 insertions across 3 quoted paragraphs, F1--F4): the print carries one opening `"` (before प्रेम्णः in p020:P4) and one closing `"` (after स्वीकुर्वन्ति ... in p021:P2) for the whole speech, so each paragraph gets its own pair per the stand-alone rule. Page-turn quotation spans verified as print-faithful pairs needing no supply: King's `"जनेभ्यः...अस्ति।` (p019:P9) closing with `...कुर्वन्तु।"` (p020:P2), and F4's paragraph closing across `{pgb}` into p021:P2.

## Unverified

None held; print-consistent spellings (सङ्ग्रह-/सङ्ग्रहः, रूप्यकाणि in both amounts, समित्या/समितेः, आगामिनि, तद्देशस्य) stand as seen with no block, and no new glyph claim is invented from text alone.

## Coverage

p018:P1 ({x-com:layout:) : skip layout note
p018:P2 (मालविका) : skip title
p018:P3 (मन्दाकिनीनद्याः तीरे) : clean
p018:P4 (मरकतपुरे विजयपर्वनामकः) : clean
p018:P5 (एवं स्थिते) : clean
p018:P6 (मालविकायाः समीपम्) : clean
p018:P7 (आत्मनः नृत्यप्रदर्शनस्य) : clean
p018:P8 (एकं वर्षम्) : clean
p018:P9 (मालविका एतां) : clean
p019:P1 ({x-com:layout:) : skip layout note
p019:P2 (तान् न) : clean
p019:P3 (मालविका व्यवस्थापकान्) : clean
p019:P4 (एतत् श्रुत्वा) : clean
p019:P5 (कृत्वा निर्णयं) : clean
p019:P6 (व्यवस्थापकानां मुखं) : clean
p019:P7 (व्यवस्थापकाः मालविकायाः) : clean
p019:P8 (अतः उत्सवव्यवस्थापकाः) : clean
p019:P9 (महाराजः कृष्णदेवः) : clean
p020:P1 ({x-com:layout:) : skip layout note
p020:P2 (विजयपर्वसन्दर्भे मरकतपुरे) : clean
p020:P3 (महाराजस्य कृष्णदेवस्य) : clean
p020:P4 (निश्चिते समये) : clean
p020:P5 (स्वभावतः प्रेमस्वरूपिणी।) : F1
p020:P6 (पुत्रः कदाचित्) : F2, F3
p020:P7 (किन्तु कदाचित्) : F4
p021:P1 ({x-com:layout:) : skip layout note
p021:P2 (लाभार्थं जनानां) : clean
p021:P3 (एवम् एव) : clean
p021:P4 (प्रवचनसमाप्यनन्तरं मालविका) : clean
p021:P5 (चन्द्रशेखरस्वामी न) : clean
p021:P6 (आह्वातुं चिन्तयन्) : clean
p021:P7 (पुरतः स्थितः) : clean
p021:P8 (इदानीं मालविका) : clean
J1 p018:P5 {pb} -> p018:P6 {pc} (continues) : ok
J2 p018:P9 {pb} -> p019:P2 {pc} (continues) : ok
J3 p019:P4 {pb} -> p019:P5 {pc} (continues) : ok
J4 p019:P9 {pb} -> p020:P2 {pc} (continues) : ok
J5 p020:P4 {pb} -> p020:P5 {pc} (continues) : ok
J6 p020:P7 {wb} -> p021:P2 {pc} (continues) : ok
J7 p021:P5 {pb} -> p021:P6 {pc} (continues) : ok
J8 p021:P8 {pb} -> END (clean break) : ok
