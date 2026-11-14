# Proofread report: samskrta_chandamama 1985_06, p048 (scan pages 48–51)

## Summary

Story `दासस्य रहस्यम्` transcribed from pages 48–51 and proofread with images closed. Seven findings: two `error` (F1 dittography of `इति` across the p048–p049 page turn, F2 भ/म print confusion `मगवान्` for `भगवान्`) and five `STY` style readability deletions of a stray single quote sort beside doubles in spoken speeches (F3–F7, one systematic print quirk in five places). `scan.py orth` on deblocked text reports zero hits; the text is human transcription, not OCR output. Proper nouns (`बस्तरनगरम्`, `दासवणिक्`/`दासवणिजः`/`वणिक्`/`वणिजः`) spell consistently throughout. Print quirks kept as seen per fidelity: open sandhi (`यः आकाशः`, `सः तदीय`, `यः आनन्दः`), thought content in doubles (p048:P4), `?` outside the close (p050:P3), missing `इति` after the दास's `भवामि` speech (p051:P6). Loc below is `pNN:Pm:word` (words counted on the chunk from 1, `{...}` blocks excluded) with anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p048:P9:25 `मयि स्निह्यति इति` | `स्निह्यति इति{pb} / {pc}इति अहं` | delete the first `इति` (`{del:इति}` on p048:P9) | KRK | error | high | dittography across the page turn; `जानामि` needs exactly one `इति` |
| 2 | p049:P5:12 `मगवान् भवति` | `मगवान्` | `{del:मगवान्}{ins:भगवान्}` | OCR | error | high | भ/म print confusion verified at 5x; `मगवान्` is a non-word and sense plus `भगवतः` on p051 require `भगवान्` |
| 3 | p050:P3:23 `अस्ति वा` | `वा'"?` | `वा"` (`{del:'}` on the stray single) | STY | style | high | top-level spoken question (`पृष्टवन्तः` + `इति`) takes doubles; the single has no inner-speech role; `?` outside the close kept as print |
| 4 | p051:P6:6 `अहं उपकृतः भवामि` | `भवामि'"` | `भवामि"` (`{del:'}` on the stray single) | STY | style | high | close of the दास's spoken `उक्तवान्` speech takes doubles; the single has no role; absent `इति` kept as print |
| 5 | p051:P7:9 `भवन्तम् अनुसरामः` | `अनुसरामः'"` | `अनुसरामः"` (`{del:'}` on the stray single) | STY | style | high | close of the भक्ताः's spoken chorus (`उक्तवन्तः` + `इति`) takes doubles; the single has no role |
| 6 | p051:P8:10 `प्रार्थितवान् --- "भगवन्!` | `"'भगवन्!` | `"भगवन्!` (`{del:'}` on the stray single) | STY | style | high | open of the दास's spoken final prayer (`प्रार्थितवान्` + `इति`) takes doubles; the extra single has no role |
| 7 | p051:P8:54 `सन्निधौ नयतु` | `नयतु'"` | `नयतु"` (`{del:'}` on the stray single) | STY | style | high | close of the same spoken prayer takes doubles; the single has no role |

## Patterns

Stray single sort beside doubles in spoken speeches: 5x (F3 p050:P3 close, F4 p051:P6 close, F5 p051:P7 close, F6 p051:P8 open, F7 p051:P8 close). Each sits in a top-level `उक्तवान्`/`पृष्टवन्तः`/`प्रार्थितवान्` utterance that otherwise uses era doubles; the lone single never opens or closes an inner thought or nested speech, so it deletes. Thought singles where print uses them (`'एषः अत्र किं कुर्यात्?'` p048:P8) are kept as print.

## Unverified

None held. The inherited `{sug-del:'}` queue (4 closings + 1 opening) is fully promoted to `{del:'}` above; the inherited `{x-com:}` on `मगवान्` is resolved by F2. No new glyph claims were invented in Phase B.

## Coverage

- p048:P1 `{x-com:layout:` : skip layout declaration
- p048:P2 `# दासस्य` : skip title heading
- p048:P3 `पूर्वं कदाचित्` : clean
- p048:P4 `जनाः चिन्तितवन्तः` : clean (collective-thought content in print doubles kept as seen)
- p048:P5 `अस्यां परिस्थितौ` : clean (open pairs across columns via J1)
- p048:P6 `सस्यानि सर्वाणि` : clean (close pairs with p048:P5 open via J1)
- p048:P7 `अर्धरात्रपर्यन्तम्` : clean
- p048:P8 `तेषु भक्तेषु` : clean (thought singles kept as print)
- p048:P9 `सः युवकः` : F1
- p048:P10 `{category: अरेबिया` : skip footer metadata
- p049:P1 `{x-com:layout:` : skip layout declaration
- p049:P2 `इति अहं` : F1 (second `इति` kept; first deleted by F1)
- p049:P3 `प्रार्थनां परिसमाप्य` : clean
- p049:P4 `अहं कश्चन` : clean
- p049:P5 `युवकस्य एतानि` : F2 (open pairs across columns via J3)
- p049:P6 `जानाति महाभक्तानां` : clean (close pairs with p049:P5 open via J3)
- p049:P7 `युवकः क्षणकालं` : clean
- p049:P8 `एवम् उक्त्वा` : clean
- p049:P9 `भक्तः आश्चर्येण` : clean
- p049:P10 `भक्तः तं` : clean
- p049:P11 `प्रातःकालपर्यन्तं` : clean (open pairs across pages via J4)
- p050:P1 `{x-com:layout:` : skip layout declaration
- p050:P2 `जलेन पूर्णाः` : clean (close joins solid via J4)
- p050:P3 `तद्दिने रात्रौ` : F3
- p050:P4 `एकः किं` : clean
- p050:P5 `वणिजः अधीने` : clean (open pairs across columns via J5)
- p050:P6 `द्वारस्य पृष्ठतः` : clean (close pairs with p050:P5 open via J5)
- p050:P7 `भक्तः यदा` : clean
- p050:P8 `वयम् एतं` : clean
- p050:P9 `वयम् एतम्` : clean (open pairs across pages via J6)
- p051:P1 `{x-com:layout:` : skip layout declaration
- p051:P2 `आत्मना सह` : clean (close joins via J6)
- p051:P3 `भवता एव` : clean
- p051:P4 `एतत् श्रुत्वा` : clean
- p051:P5 `ओह् एवं` : clean (open `रात्रौ` pairs across columns via J7)
- p051:P6 `अवकाशं कल्पयन्ति` : F4
- p051:P7 `प्रार्थना अवश्यं` : F5
- p051:P8 `सः दासः` : F6, F7
- p051:P9 `एतदनन्तरं सः` : clean
- J1 p048:P5 {pb} -> p048:P6 {pc} : ok (`क्षामकारणतः सस्यानि` joins across columns)
- J2 p048:P9 {pb} -> p049:P2 {pc} : F1 (`इति इति` dittography across pages)
- J3 p049:P5 {pb} -> p049:P6 {pc} : ok (`कथं जानाति` joins across columns)
- J4 p049:P11 {pb} -> p050:P2 {pc} : ok (`इदानीं जलेन पूर्णाः` joins across pages)
- J5 p050:P5 {pb} -> p050:P6 {pc} : ok (`कोणे द्वारस्य` joins across columns)
- J6 p050:P9 {pb} -> p051:P2 {pc} : ok (`तं आत्मना` joins across pages)
- J7 p051:P5 {pb} -> p051:P6 {pc} : ok (`कर्तुम् अवकाशं` joins across columns)
- J8 p051:P9 {pb} -> END : ok (complete sentence, clean story end)
