## Summary

Story 1985_10 pp. 21-25 (वैराग्यम्, जातककथा, to be continued): 5 findings — 2 press-slip verdicts (F1, F2) and 3 quote-sort verdicts promoting print singles to era-standard doubles for unambiguous spoken utterances (F3-F5). One systematic problem: singles used for spoken lines in three places. Orth scanner (sanskrit/scan.py orth on deblocked text, 41 lines): 0 hits; text reads as clean print, not OCR output. Three further observations held without file blocks (U1-U3, no Phase A glyph flag on file, so no verdict per images-closed rule). Loc below is story coordinates pNN:Pm plus the first two words of the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p022:P2 किञ्चित्कालानन्तरम् कश्चित् | `राज्याः प्रश्नं` | `राज्ञ्याः प्रश्नं` | SPL | error | high | queen's question needs feminine genitive राज्ञ्याः; print ज्य mis-sets ज्ञ |
| 2 | p022:P5 "आर्य अहं | `परिचितः कोडपि` | `परिचितः कोऽपि` | SPL | error | high | कोडपि is no word; को + अपि voices कोऽपि |
| 3 | p022:P7 तस्य वचनम् | `'किम् एतत्? किं जातम्?'` | `"किम् एतत्? किं जातम्?"` | STY | style | high | पृष्टवन्तः plus इति closes a spoken question; era standard is doubles for speech |
| 4 | p023:P5 {pc}अनादरं प्रदर्शयन्ति | `'एषः विधवापुत्रः अस्मान् ताडयति'` | `"एषः विधवापुत्रः अस्मान् ताडयति"` | STY | style | high | आक्रोश and निन्दन्ति pin shouted mockery as spoken; era standard is doubles |
| 5 | p024:P7 राजपुरोहितः महाजनकस्य | `'कृपया अनाथस्य विदेहराज्यस्य राजा भवान् एव भवतु'` | `"कृपया अनाथस्य विदेहराज्यस्य राजा भवान् एव भवतु"` | STY | style | high | प्रार्थितवान् with second-person address pins a spoken request; era standard is doubles |

## Patterns

Singles for spoken utterances (3x: F3, F4, F5). Print keeps singles for the disciples' question, the boys' taunt, and the purohit's request; all three are vocalized exchanges with reporting verbs (पृष्टवन्तः, निन्दन्ति, प्रार्थितवान्) and iti-closures, so all three take doubles. Interior lines kept as printed: brahmin's scheme (p022:P6 doubles, print), resolve (p023:P7 singles, print), mother's resolve (p024:P2 doubles, print), garden resolve with मनसि (p025:P7 doubles, print, cf. मनसि-doubles kept in this issue).

## Unverified

U1: कालानन्तरे (p021:P4 अग्रजस्य एवं) vs कालान्तरे (p025:P3 कालः गच्छति) — isolated extra न in an otherwise consistent story; किञ्चित्कालानन्तरम् (with अनन्तरम्) is correct elsewhere, so the locative कालानन्तरे looks like a slip for कालान्तरे. No Phase A flag on file, so no block; would settle with a print re-check or a lexicon search for कालानन्तर. Conf low*.
U2: एषा जन्म प्राप्स्यति (p023:P2 {pc}एषा जन्म) — mother as the obtainer of birth; classical idiom wants प्रसविष्यति for the mother. Likely translationese; rewriting author wording is out of scope and there is no Phase A flag, so no block. Conf low*.
U3: मार्गेण गच्छतः (p021:P9 किन्तु वराकी) — participle agrees with nothing (सा is feminine nominative, wants गच्छन्ती; पथिकान् wants गच्छताम्). No Phase A flag on file, so no block; a print re-check for a damaged न्ती ligature would settle it. Conf medium*.

## Coverage

p021:P1 {x-com:layout: 2col, : skip layout chunk
p021:P2 # वैराग्यम् : skip title
p021:P3 काशीराज्ये ब्रह्मदत्तस्य : clean
p021:P4 वृद्धस्य महाजनकस्य : clean (कालानन्तरे noted in U1, no block)
p021:P5 अग्रजस्य एवं : clean
p021:P6 अनन्तरं केनचित् : clean
p021:P7 {pc}आक्रम्य तं : clean
p021:P8 अनिष्टजनकस्य मरणसमये : clean
p021:P9 किन्तु वराकी : clean (गच्छतः noted in U3, no block)
p021:P10 {category: जातककथा} : skip footer metadata
p022:P1 {x-com:layout: 2col, : skip layout chunk
p022:P2 किञ्चित्कालानन्तरम् कश्चित् : F1
p022:P3 राज्ञी स्वीयकण्डोलं : clean
p022:P4 किञ्चित्कालानन्तरम् कश्चन : clean (detached speck after पतिता omitted as print noise at 5x)
p022:P5 "आर्य अहं : F2
p022:P6 "एवं तर्हि : clean
p022:P7 तस्य वचनम् : F3
p022:P8 तदा ब्राह्मणः : clean
p023:P1 {x-com:layout: 2col, : skip layout chunk
p023:P2 {pc}एषा जन्म : clean (जन्म प्राप्स्यति noted in U2, no block)
p023:P3 ब्राह्मणस्य वचनेषु : clean
p023:P4 महाजनकः तत्र : clean
p023:P5 {pc}अनादरं प्रदर्शयन्ति : F4
p023:P6 स्वीयमाता विधवा : clean
p023:P7 स्वीयपितृव्यः अधर्ममार्गेण : clean
p024:P1 {x-com:layout: 2col, : skip layout chunk
p024:P2 {pc}एव’ इति : clean
p024:P3 यदा कुमारः : clean
p024:P4 अपुत्रस्य पोलजनकस्य : clean
p024:P5 {pc}रथं सज्जीकृतवान्। : clean
p024:P6 रथः किञ्चिद्दूरं : clean
p024:P7 राजपुरोहितः महाजनकस्य : F5
p024:P8 महाजनकः एव : clean
p025:P1 {x-com:layout: 2col, : skip layout chunk
p025:P2 {pc}देवी तस्य : clean
p025:P3 कालः गच्छति : clean
p025:P4 महाजनकः यदा : clean
p025:P5 {pc}तदा तस्य : clean
p025:P6 महाजनकः सम्पूर्णम् : clean
p025:P7 "एतेन एकः : clean
p025:P8 {note: आगामिसञ्चिकायां समाप्ता : skip footer metadata
J1 p021:P6 {pb} -> p021:P7 {pc} (continues) : ok
J2 p021:P9 {pb} -> p022:P2 fresh (clean break) : ok
J3 p022:P5 {pb} -> p022:P6 fresh (clean break) : ok
J4 p022:P8 {pb} -> p023:P2 {pc} (continues) : ok
J5 p023:P4 {pb} -> p023:P5 {pc} (continues) : ok
J6 p023:P7 {pb} -> p024:P2 {pc} (continues) : ok
J7 p024:P4 {pb} -> p024:P5 {pc} (continues) : ok
J8 p024:P8 {wb} -> p025:P2 {pc} (continues) : ok
J9 p025:P4 {pb} -> p025:P5 {pc} (continues) : ok
J10 p025:P7 {pb} -> END (clean break) : ok
