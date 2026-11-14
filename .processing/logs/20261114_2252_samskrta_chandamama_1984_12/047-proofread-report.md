# Proofread report: 1984_12, story p047 (हस्तसामुद्रिकम्, scans 47-49)

## Summary

4 findings, all high confidence: 2 morphology/agreement errors (F1, F2) and 2 spelling errors (F1-region excluded; F3, F4). No systematic problem; each finding is a one-off typesetting slip. One Phase A suggestion dropped (राजास्थानम् kept as print-faithful). Orth scanner (`scan.py orth`) on deblocked text: 0 hits. No passages left unchecked; the text is composed print, not OCR output. Loc below is story coordinates `pNN:Pm` (NN = scan sequence, Pm = chunk number in that page span) plus word index in the chunk.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p047:P4 w2 (`कृष्णशास्त्रिणः पत्न्यैः`) | `पत्न्यैः` | `पत्न्यै` | MRP | error | high | रुच् takes the dative of the person pleased; dat.sg of पत्नी is पत्न्यै, the visarga form is no case here |
| 2 | p047:P4 w6 (`एतत् न रोचसे`) | `रोचसे` | `रोचते` | AGR | error | high | 2sg verb with 3rd-person subject सा/पत्नी; sense needs 3sg रोचते |
| 3 | p048:P7 w14 (`सः उद्दारं प्रकटितवान्`) | `उद्दारं` | `उद्गारं` | SPL | error | high | उद्दारं is no word here; उद्गारं (exclamation) is the idiom with प्रकटितवान्, द्द/द्ग one-stroke difference |
| 4 | p049:P4 w22 (`भवतः माग्ये राजपदप्राप्तेः`) | `माग्ये` | `भाग्ये` | OCR | error | high | माग्ये is no word; भ/म confusion, भाग्ये राजपदप्राप्तेः योगः is the idiom |

## Patterns

None; each finding is unique.

## Unverified

None. All five Phase A `{sug-…}` candidates were routed: four promoted to verdicts above, one dropped. Dropped: `{sug-del:राजास्थानम्}{sug-ins:राजस्थानम्}` (p048:P3) --- राजास्थानम् stands as print-faithful, defensible as राजा+स्थानम् (the king's place) for the soldiers' summons, so the suggestion was removed and the print kept. Kept without blocks: भावदीय (house spelling for भवदीय, variant at most); क्षाम्यतु (correct दिवादि imperative of क्षम्, verified against grammar, not a misprint); म हा रा जः (print spaces the word for emphasis, kept as seen); quote sorts kept exactly as print --- spoken turns in doubles, brief formulae, thoughts and the वार्ता line in singles --- since press practice here is mixed (चिन्त् verbs take doubles twice, प्रार्थना/आदेश take singles twice, cf. accepted 1984_04 p01), sense does not pin a change, so all marks were ratified as print-faithful for the compiler.

## Coverage

p047:P1 {x-com:layout : skip layout-only chunk
p047:P2 हस्तसामुद्रिकम् : skip title
p047:P3 राजपुरे कृष्णशास्त्री : clean
p047:P4 कृष्णशास्त्रिणः पत्न्यैः : F1, F2
p047:P5 तदा कृष्णशास्त्री : clean
p047:P6 श्रद्धां भक्तिं : clean
p047:P7 तदा पत्नी : clean
p047:P8 'कृष्णशास्त्री श्रेष्ठः : clean
p047:P9 "कृष्णशास्त्री आस्थानपण्डितरूपेण : clean
p047:P10 {author : skip metadata
p048:P1 {x-com:layout : skip layout-only chunk
p048:P2 निर्णयस्वीकरणतः पूर्वं : clean
p048:P3 मन्त्री तद्दिने : clean
p048:P4 किन्तु कृष्णशास्त्री : clean
p048:P5 चण्डी जाता : clean
p048:P6 "कृष्णशास्त्री राजाज्ञां : clean
p048:P7 कृष्णशास्त्रिणः उत्तरं : F3
p048:P8 एकसप्ताहानन्तरं राजा : clean
p048:P9 किन्तु कृष्णशास्त्री : clean
p049:P1 {x-com:layout : skip layout-only chunk
p049:P2 गौरवपूर्वकं स्वागतम् : clean
p049:P3 महाराजस्य इच्छानुसारं : clean
p049:P4 पुनरपि किञ्चित् : F4
p049:P5 एवम् उक्त्वा : clean
p049:P6 अग्निम् आनेतुम् : clean
p049:P7 तयोः एकः : clean
p049:P8 एतदनन्तरम् एकसप्ताहाभ्यन्तरे : clean
J1 p047:P5 -> p047:P6 : ok
J2 p047:P9 -> p048:P2 : ok
J3 p048:P4 -> p048:P5 : ok
J4 p048:P9 -> p049:P2 : ok
J5 p049:P5 -> p049:P6 : ok
J6 p049:P8 -> END : ok
