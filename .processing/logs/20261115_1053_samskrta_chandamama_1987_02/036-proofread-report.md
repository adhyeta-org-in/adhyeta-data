# Proofread report: 1987_02 p036 (scan pages 36-40, story उद्देशपूर्वकं व्यवहारः)

## Summary

4 verdict blocks (`{del:}`/`{ins:}`, F1-F4) and 1 held candidate (`{sug-del:}`/`{sug-ins:}`, H1) across 5 page spans (45 body chunks, 10 joints); orth scanner gave 1 hit, the baseline period that confirms print defect F3. Systematic issue: failing print sorts and dropped combining signs (reph in F1, i-matra in F2, visarga rendered as period in F3, intrusive visarga in F4), each verified enlarged in Phase A. Held H1 is a letter-order suspicion (`करो` vs `क्रो`) with no enlarged Phase A crop on file, so it stays a candidate despite a unique fix. Images stayed closed throughout Phase B; every chunk ruled from text, house style, and story sense.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p036:P8:9 (रामपुरस्य नागवर्मा) | `क्रीत्वा धियन्ते चेत्` | `क्रीत्वा ध्रियन्ते चेत्` | OCR | error | high | passive "when worn" needs the धृ-passive ध्रियन्ते; धियन्ते is no word (dropped reph) |
| F2 | p036:P9:11 (अन्यस्मिन् समये) | `तु यथाशक्त` | `तु यथाशक्ति` | OCR | error | high | adverb "according to ability" needs यथाशक्ति; यथाशक्त is a non-word (dropped i-matra) |
| F3 | p036:P11:4 (स्नेहितस्य सीतारामस्य) | `पुत्रः गणपति.` | `पुत्रः गणपतिः` | ENC | error | high | nominative subject of प्रेषणीयः needs गणपतिः; baseline period is a failing visarga sort (orth fullstop hit, verified 5x in Phase A) |
| F4 | p038:P6:8 (रजतस्थालिकाः आसन्) | `भूमौः कदलीपत्रं` | `भूमौ कदलीपत्रं` | ENC | error | high | locative "on the ground" needs भूमौ; visarga cannot stand after the औ-locative (verified 5x in Phase A) |

## Patterns

- Failing print sorts and dropped combining signs (4x): dropped reph (F1) and dropped i-matra (F2) both yield non-words fixed by restoring the sign; visarga printed as a baseline period (F3, orth-confirmed) and visarga intruding on a locative (F4), both fixed by restoring the grammatical ending.

## Unverified

- H1 `अङ्गीक्रोति` -> `अङ्गीकरोति` (SPL, likely, M*): p036:P9:8 (एतत् न). The printed sequence `करो` vs `क्रो` decides a non-word against the unique fix अङ्गीकरोति, with the same root printed अङ्गीकृतवान् three times later in the story; no enlarged Phase A crop of this word sits on file, so Phase B adds no verdict. Settles by: inspecting a second copy of this issue printing; if `क्रो` is confirmed, promote the on-file `{sug-del:}`/`{sug-ins:}` to `{del:}`/`{ins:}`.

## Coverage

- p036:P1 `{x-com:layout:` : skip layout declaration
- p036:P2 `उद्देशपूर्वकं व्यवहारः` : skip title
- p036:P3 `सीतापुरे नारायणः` : clean
- p036:P4 `दशवर्षानन्तरं कस्याश्चित्` : clean (open sandhi फलम् इव kept as house variant)
- p036:P5 `एकस्मिन् दिने` : clean (speech pair opens and closes in-chunk)
- p036:P6 `कमला आतङ्केन` : clean (mid-sentence column turn into J1; speech pair spans the turn)
- p036:P7 `{pc}इति न` : clean ({pc} closes J1 speech with ज्ञायते")
- p036:P8 `रामपुरस्य नागवर्मा` : F1
- p036:P9 `अन्यस्मिन् समये` : F2, H1
- p036:P10 `भवान् समीपे` : clean (speech pair opens and closes in-chunk)
- p036:P11 `स्नेहितस्य सीतारामस्य` : F3 (mid-sentence page turn into J2)
- p036:P12 `{category:` : skip footer metadata (print centers it in quotes; quotes kept inside the block)
- p037:P1 `{x-com:layout:` : skip layout declaration
- p037:P2 `{pc}रामपुरं प्रति` : clean ({pc} continues पुत्रः गणपतिः across page turn)
- p037:P3 `गणपतिः विंशतिवर्षीयः` : clean (stray midline dot in कोऽपि न omitted as print noise per on-file x-com; father's reasoning kept in print's singles)
- p037:P4 `अतः नारायणः` : clean (mid-sentence column turn into J3; speech opens here)
- p037:P5 `{pc}मम बन्धुः` : clean ({pc} closes J3 speech with ददामि")
- p037:P6 `एतत् सर्वं` : clean
- p037:P7 `रामपुरं गन्तुं` : clean
- p037:P8 `सिद्धराजः अभिमानेन` : clean (speech pair opens and closes in-chunk)
- p037:P9 `सिद्धराजस्य पुत्रः` : clean
- p037:P10 `तावति काले` : clean (mid-word-page turn बृहत् into J4)
- p038:P1 `{x-com:layout:` : skip layout declaration
- p038:P2 `{pc}उदभाण्डम् आनीय` : clean ({pc} completes बृहत् उदभाण्डम्)
- p038:P3 `सः गणपतिम्` : clean (speech pair and thought-singles each open and close in-chunk)
- p038:P4 `गणपतिः स्नानसमये` : clean (suspicion kept in print's singles)
- p038:P5 `सिद्धराजस्य सर्वेऽपि` : clean (mid-sentence column turn into J5)
- p038:P6 `{pc}रजतस्थालिकाः आसन्` : F4
- p038:P7 `भोजनानन्तरं गणपतेः` : clean
- p038:P8 `परेद्युः प्रातः` : clean (wife's speech pair opens and closes in-chunk; range continues)
- p039:P1 `{x-com:layout:` : skip layout declaration
- p039:P2 `तस्मिन् समये` : clean (open sandhi तेन एव kept as house variant)
- p039:P3 `गणपतिः किमपि` : clean (speech pair opens and closes in-chunk)
- p039:P4 `अहम् अपि` : clean (speech pair opens and closes in-chunk)
- p039:P5 `गमनसमये सिद्धराजस्य` : clean (mid-sentence column turn into J7)
- p039:P6 `{pc}यच्छन् सः` : clean ({pc} continues हस्ते across column turn; speech opens here)
- p039:P7 `तं कूष्माण्डस्यूतं` : clean
- p039:P8 `कूष्माण्डफलानि तस्मै` : clean
- p039:P9 `नागवर्मन् नारायणः` : clean (speech pair opens and closes in-chunk; परतया kept as translator's idiom)
- p039:P10 `नागवर्मा एतत्` : clean
- p039:P11 `दिनचतुष्टयम् अपि` : clean
- p039:P12 `हारः यदा` : clean (mid-sentence page turn into J8; family speech opens with " and stays open)
- p040:P1 `{x-com:layout:` : skip layout declaration
- p040:P2 `{pc}चेत् अस्माकं` : clean ({pc} closes J8 speech with भवता")
- p040:P3 `गणपतिः सीतापुरम्` : clean
- p040:P4 `गणपतिः प्रथमं` : clean (speech pair opens and closes in-chunk)
- p040:P5 `प्रवृत्तं वृत्तान्तं` : clean (speech pair opens and closes in-chunk)
- p040:P6 `कार्पण्यम् अपि` : clean (mid-sentence column turn into J9; speech opens here)
- p040:P7 `{pc}तावत् कार्पण्यं` : clean ({pc} closes J9 speech with स्युः")
- p040:P8 `वस्तुस्थितिं न` : clean (speech pair opens and closes in-chunk; षण्मासेभ्यः kept as printed ष)
- p040:P9 `इदानीं गणपतिः` : clean
- p040:P10 `इतःपरम् एतादृशैः` : clean (resolve kept in print's singles; story concludes with the moral)
- J1 p036:P6 {pb} -> p036:P7 {pc} (continues) : ok (उत्पन्ना | इति, speech spans column turn)
- J2 p036:P11 {pb} -> p037:P2 {pc} (continues) : ok (गणपतिः | रामपुरं, spaced join across page turn)
- J3 p037:P4 {pb} -> p037:P5 {pc} (continues) : ok (रामपुरे | मम, speech spans column turn)
- J4 p037:P10 {pb} -> p038:P2 {pc} (continues) : ok (बृहत् | उदभाण्डम्, spaced join across page turn)
- J5 p038:P5 {pb} -> p038:P6 {pc} (continues) : ok (पुरतः | रजतस्थालिकाः, spaced join across column turn)
- J6 p038:P8 {pb} -> p039:P2 fresh (clean break) : ok (terminal ।; next-morning scene opens)
- J7 p039:P5 {pb} -> p039:P6 {pc} (continues) : ok (हस्ते | यच्छन्, spaced join across column turn)
- J8 p039:P12 {pb} -> p040:P2 {pc} (continues) : ok (आगच्छति | चेत्, family speech spans page turn)
- J9 p040:P6 {pb} -> p040:P7 {pc} (continues) : ok (गृहे | तावत्, speech spans column turn)
- J10 p040:P10 {pb} -> END (clean break) : ok (terminal ।; story concludes, next scan starts a new story)
