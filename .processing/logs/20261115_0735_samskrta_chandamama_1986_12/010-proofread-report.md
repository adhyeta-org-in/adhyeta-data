# Proofread report — 1986_12, story p010 (ज्वालाद्वीपः, scans 10–16)

## Summary

Range 1986_12 p010–p016 (7 page spans, "ज्वालाद्वीपः" serial with (अनुवर्तते) to be continued) proofread with images closed. Extract gate and proofread gate both pass with 0 errors; `scan.py orth` on deblocked text reports 0 hits. No `{del:}`/`{ins:}` verdicts and no new `{sug-…}` candidate blocks were added, so the story file is byte-identical to its Phase A state apart from the tool-generated `## Joints` index. Findings table is empty; 3 low-confidence holds sit in Unverified (report-only, no story blocks, since Phase A left no `{x-com:}`/`{sug-…}` flag on file and Phase B invents no new glyph claims). Word-level `Loc` below counts words on the chunk from 1. Proper nouns (चित्रसेन/उग्राक्ष/अमरपाल/नागवर्मन्/कपिलपुर/ज्वालाद्वीप/धवलगिरि/महावट) spell consistently throughout.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — | — |

## Patterns

Open sandhi kept as house style throughout (e.g. `अश्रुतवान् इव`, `अवतीर्य स्थितवान्`, `गताः न`, `गताः एव`, `उक्तवान् इति`); never normalized per print-fidelity doctrine. Consistent print spellings stood as seen: `भीकरं` (p015:P8, p015:P10), `एतत्क्षणतः` (p012:P2), `सहनया तिष्ठतु` (p011:P6), `इतः आरभ्यः` (p012:P2), interjection `आं चित्रसेन` (p014:P3).

## Unverified

| # | Loc | Original | Suggestion | Conf | Why | What would settle it |
|---|---|---|---|---|---|---|
| U1 | p013:P7 राक्षसाः अपि | `गताः न। अति तु गोप्यतया` | `अपि तु` for `अति तु` | low* | `अति तु` is unidiomatic as an adversative; `अपि तु` fits "but secretly" | Phase A re-check of the second akṣara at 3x (`ति` vs `पि`) — images closed, so held |
| U2 | p016:P5 उग्राक्षः निरुत्साहेन | `एते पातकिनः अस्माक राज्यतः` | `अस्माकं राज्यतः` | low* | bare `अस्माक` against `अस्माकम्`/`अस्माकं` everywhere else (p013:P9, p015:P10) | Phase A re-check for a dropped visarga at 3x — held |
| U3 | p016:P10 "किमर्थं वा | `मया सह पञ्चषान् सैनिकान्` | `?` (e.g. `पञ्चाशतं`?) | low* | `पञ्चषान्` is not a standard numeral; troop-count sense is clear but the form is not | Dictionary/grammar check plus Phase A glyph re-check — held |

## Coverage

p010:P2 # ज्वालाद्वीपः : skip title
p010:P3 (चित्रसेनः स्वकीयैः : clean
p010:P4 कथनं मध्ये : clean
p010:P5 दूरीकरोमि वा?" : clean
p010:P6 अमरपालः तस्य : clean
p011:P2 नागवर्माणं स्मरति : clean
p011:P3 'मम व्रणान् : clean
p011:P4 अत्रान्तरे चित्रसेनः : clean
p011:P5 "अल्पः एषः : clean
p011:P6 "उग्राक्ष! युक्तायुक्तविवेकं : clean
p011:P7 चित्रसेनस्य वचनं : clean
p011:P8 "भवतः प्राणापायस्य : clean
p012:P2 "क्षाम्यतु महाराज! : clean
p012:P3 "एवं तर्हि : clean
p012:P4 "ते अपि : clean
p012:P5 "एतेषां भयङ्करपक्षिणां : clean
p012:P6 कोपावेशेन अङ्गचालनं : clean
p012:P7 शिथिलाः आसन्। : clean
p012:P8 "किमर्थं न : clean
p012:P9 "हो हो : clean
p013:P2 उक्त्वा भुजास्फालनं : clean
p013:P3 अत्रान्तरे केचन : clean
p013:P4 प्राणभीत्या हाहाकारं : clean
p013:P5 "महाराज! अनतिदूरे : clean
p013:P6 पशून् च : clean
p013:P7 राक्षसाः अपि : clean
p013:P8 "चित्रसेन! इदानीम् : clean
p013:P9 "गमनं विना : clean
p013:P10 अनन्तरं चित्रसेनः : clean
p013:P11 वृक्षाणां मध्ये : clean
p014:P2 यदि ते : clean
p014:P3 उग्राक्षः एतत् : clean
p014:P4 अमरपालस्य उग्राक्षस्य : clean
p014:P5 'अविवेकेन पौरान् : clean
p014:P6 किन्तु तन्मध्ये : clean
p014:P7 एवं चित्रसेनः : clean
p014:P8 उक्तवान् --- : clean
p014:P9 "तत्र शतशः : clean
p015:P2 "तेषां पक्षिणां : clean
p015:P3 "कः सः : clean
p015:P4 तदा अमरपालः : clean
p015:P5 "विचारः तु : clean
p015:P6 "तदर्थं मया : clean
p015:P7 अस्ति अपि" : clean
p015:P8 चित्रसेनः उग्राक्षः : clean
p015:P9 केचन भयङ्करपक्षिणः : clean
p015:P10 एतत् भीकरं : clean
p016:P2 चित्रसेनस्य वचनसमनन्तरम् : clean
p016:P3 तदा चित्रसेनः : clean
p016:P4 ज्वालाद्वीपवासिनः दृष्टिपथात् : clean
p016:P5 उग्राक्षः निरुत्साहेन : clean
p016:P6 "आम् आम्। : clean
p016:P7 चिन्तनीयः एव" : clean
p016:P8 "यदा ते : clean
p016:P9 "तत् कथं : clean
p016:P10 "किमर्थं वा : clean
p016:P11 (अनुवर्तते) : skip continuation marker

J1 p010:P4 -> p010:P5 {pc} : ok (पित्तविकारं दूरीकरोमि, same speech, spaced join)
J2 p010:P6 -> p011:P2 {pc} : ok (वशीकृतवन्तं नागवर्माणं, accusative completes, unique fit)
J3 p011:P4 -> p011:P5 fresh : ok (stop order -> angry reply, clean break)
J4 p011:P8 -> p012:P2 fresh : ok (rebuke complete -> submission क्षाम्यतु, clean break)
J5 p012:P6 -> p012:P7 {pc} : ok (बन्धाः शिथिलाः आसन्, mid-sentence)
J6 p012:P9 -> p013:P2 {pc} : ok (इति उक्त्वा भुजास्फालनं, narration continues)
J7 p013:P5 -> p013:P6 {pc} : ok (जनान् पशून् च नयन्तः, mid-sentence)
J8 p013:P11 -> p014:P2 {pc} : ok (speech spans page turn, closes तावदेव" इति)
J9 p014:P7 -> p014:P8 {pc} : ok (तदा अमरपालः उक्तवान्, subject-verb split)
J10 p014:P9 -> p015:P2 fresh : ok (doubt -> new offer सुलभोपायः, clean break)
J11 p015:P6 -> p015:P7 {pc} : ok (चिन्तितः अस्ति अपि, speech spans column)
J12 p015:P10 -> p016:P2 fresh : ok (first aid done -> वचनसमनन्तरम् narrative, clean break)
J13 p016:P6 -> p016:P7 {pc} : ok (यावच्छीघ्रं चिन्तनीयः एव, mid-sentence)
J14 p016:P11 -> END : ok ((अनुवर्तते) closes range, clean)
