# Proofread report: 1987_04 p010 (START=10 END=16, scans 10--15)

## Summary

Range p010 covers six scans (10, 11, 12, 13, 14, 15; magazine folios bare, २०, २१, २२, २३, २४) of the serial ज्वालाद्वीपः (part १०). Extract gate and proofread gate both pass with 0 error paras. No verdict blocks were needed: every inherited quote pairs cleanly across its column or page joint, and all glyph readings were settled in Phase A. Findings: 0 error, 0 likely, 4 variant, 0 style. Two low-confidence glyph suspicions are held in Unverified. The text is a print transcription, not OCR output. No passages were left unchecked; Phase B worked text-only with images closed throughout. Loc below is `pNN:Pm` (scan-sequence page, chunk in span) plus the anchor words.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p012:P5 उग्राक्षः उच्चैः | `दुर्गभित्तिः दृढः` | `दुर्गभित्तिः दृढा` | AGR | variant | high | feminine भित्तिः takes दृढा by classical agreement; print kept as-is, no block |
| F2 | p015:P3 आं महाराज! | `तौ राक्षसपक्षिणौ साहसिनः मदनुचराः` | `साहसिनौ मदनुचरौ` or keep | AGR | variant | high | dual तौ/पक्षिणौ with plural साहसिनः/अनुचराः; print kept as-is, no block |
| F3 | p011:P11 'तत् यथाकथम् | `सद्याकालीनं` | `सद्यकालीनं` | SPL | variant | medium* | सद्या- looks like a slip for सद्य-; glyphs verified at 3x in Phase A, form unchecked in dictionary |
| F4 | p015:P8 नागवर्मा करवीरः | `भीकरं श्मशानमौनं` | `?` | SPL | variant | medium* | भीकरं is nonstandard for the dreadful-silence sense; glyphs read clearly in Phase A, lexicon unchecked |

## Patterns

Print-spelling and agreement variants kept as seen (4 instances across 2 patterns, no blocks per print-fidelity doctrine): gender/number slips (F1, F2: दृढः with भित्तिः, plural adjectives with dual nouns); nonstandard spellings (F3, F4: सद्याकालीनं, भीकरं). Open sandhi throughout (तत् इति, यत् तौ, एतत् दुर्गम्) is consistent house style, never flagged. One `scan.py orth` hit (`तत्र!` p015:P8, latin-for-danda) was rejected: the line-final `!` is a certain print exclamation closing the range. Proper nouns are consistent throughout (चित्रसेनः, उग्राक्षः, वीरसिंहः, नागवर्मणः/नागवर्मा, कान्तिमती, अमरपालः, करवीरः, तारकेश्वरेण twice, कपिलपुरदुर्गं, धवलगिरिं): no CNS findings.

## Unverified

| # | Loc | Form | What would settle it |
|---|---|---|---|
| U1 | p012:P5 उग्राक्षः उच्चैः | `दुर्गभत्तेः` (vs भित्तिः/भित्तिं 3x in the same speech) | scan re-check whether the conjunct is त्त or त्ति; Phase A carried no flag so no block was issued |
| U2 | p013:P5 नागवर्मा अनुचरैः | `सर्वदिक्कृतः` | scan re-check of the compound akṣaras; sense and lexicon otherwise unclear from text alone |

## Coverage

p010:P1 {x-com:layout: 2col, : skip x-com-layout
p010:P2 ज्वालाद्वीपः --- : skip title
p010:P3 चित्रसेनः उग्राक्षः : clean
p010:P4 चित्रसेनस्य वचनं : clean
p010:P5 एव नागवर्मणः : clean
p010:P6 "अत्र आश्चर्यस्य : clean
p011:P1 {x-com:layout: 2col, : skip x-com-layout
p011:P2 तस्याः संशयः : clean
p011:P3 एतत् वचनं : clean
p011:P4 उग्राक्षः तु : clean
p011:P5 वीरसिंहः क्षणकालं : clean
p011:P6 उग्राक्षः शिरः : clean
p011:P7 निरीक्षमाणाः स्मः : clean
p011:P8 तदा लज्जया : clean
p011:P9 नागवर्मणः नाम्नः : clean
p011:P10 'नागवर्मा धवलगिरिं : clean
p011:P11 'तत् यथाकथम् : F3
p011:P12 एवं चिन्तयन् : clean
p012:P1 {x-com:layout: 2col, : skip x-com-layout
p012:P2 अयं कालः। : clean
p012:P3 "गुप्तचराणां वचनं : clean
p012:P4 "अस्तु तावत्, : clean
p012:P5 उग्राक्षः उच्चैः : F1, U1
p012:P6 "एवं वा!" : clean
p012:P7 अत्रान्तरे अमरपालः : clean
p012:P8 अमरपालस्य वचनं : clean
p012:P9 सः अमरपालं : clean
p013:P1 {x-com:layout: 2col, : skip x-com-layout
p013:P2 प्रत्युत्पन्नमतिः प्रशंसार्हा : clean
p013:P3 "महाराज! मम : clean
p013:P4 "विलम्बः किमर्थम्? : clean
p013:P5 "नागवर्मा अनुचरैः : U2
p013:P6 सूचितवान् उग्राक्षः। : clean
p013:P7 "आम्। एषः : clean
p013:P8 "एतत् तु : clean
p013:P9 "तत् यथा : clean
p013:P10 "उग्राक्ष! युक्तम् : clean
p014:P1 {x-com:layout: 2col, : skip x-com-layout
p014:P2 इति स्वसन्तोषं : clean
p014:P3 "अर्धं राज्यं : clean
p014:P4 "आं पुत्रि! : clean
p014:P5 "अस्तु तावत्, : clean
p014:P6 "आं महाराज! : clean
p014:P7 --- "हुँ, : clean
p014:P8 अमरपालस्य उग्राक्षस्य : clean
p014:P9 एतस्मिन् एव : clean
p015:P1 {x-com:layout: 2col, : skip x-com-layout
p015:P2 सः करवीरः : clean
p015:P3 "आं महाराज! : F2
p015:P4 करवीरः। : clean
p015:P5 "मां तु : clean
p015:P6 अनन्तरं नागवर्मा : clean
p015:P7 नागवर्मा करवीरः : clean
p015:P8 नागवर्मा करवीरः : F4
J1 p010:P4 -> p010:P5 : ok
J2 p010:P6 -> p011:P2 : ok
J3 p011:P6 -> p011:P7 : ok
J4 p011:P12 -> p012:P2 : ok
J5 p012:P6 -> p012:P7 : ok
J6 p012:P9 -> p013:P2 : ok
J7 p013:P5 -> p013:P6 : ok
J8 p013:P10 -> p014:P2 : ok
J9 p014:P6 -> p014:P7 : ok
J10 p014:P9 -> p015:P2 : ok
J11 p015:P3 -> p015:P4 : ok
J12 p015:P8 -> END : ok

## Continuation (scan 16)

Scan 16.jpg transcribed and proofread as a new page span p016 appended after the
`{pgb: २४}` seam (existing p010--p015 text untouched). Layout
`{x-com:layout: 2col, art bottom-full-width}`: left column (Nagavarma--Karavira
exchange, Ugraksa-fright, the whispering-horse paragraph) then right column
(the overheard aside, Karavira's long counsel) then `{category: (अनुवर्तते)}`
as the page footer (same convention as p042). No folio numeral is printed or
visible on the scan, so the page closes with bare `{pgb}` per the no-invention
rule (folio २५ expected by sequence but not asserted). The serial continues
past this page (`अनुवर्तते`), so the range END moves from p015:P8 to p016.
Proofread gate passes with 0 error paras; `scan.py orth` on deblocked story
text reports only the pre-existing `तत्र!` hit (p015:P8, already dispositioned
above as certain print exclamation) and zero hits from the new span.
One verdict block (F5) was issued on the new text; everything else is kept
as printed. Loc below is `pNN:Pm` plus anchor words, continuing F-numbering.

### Findings (new span only)

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F5 | p016:P9 तदा करवीरः | `अस्माकम्'` + `इति सूचितवान्।` (outer `"` never closes) | `अस्माकम्{del:'}{ins:"}` | STY | style | high | outer speech opens `"अत्र` with reporting `इति सूचितवान्` pinning a double close at paragraph end; print sets `'` in that slot which would otherwise cross the two complete inner `'...'` pairs (`'ते ... वा'`, `'कोऽपि ... नास्ति'`) |

Quote map for p016:P9: `"` opens before अत्र and (after F5) closes after
अस्माकम्; inner SQ pair 1 `'ते ... स्युः वा'`, inner SQ pair 2
`'कोऽपि ... नास्ति'`; the `एव --- 'ते` and `मास्तु`-clause sit inside the
outer DQ, so no crossing remains. All other new-span marks pair as printed:
P2/P3/P4 speeches each open and close `"` in-paragraph; P6 opens `"` before
नागवर्म- and closes it after भाति in the same chunk; P8 opens `"` before अत्र
of the short aside and closes after भोः. S-glyph allographs read as avagraha
ऽ (कोऽपि twice, m2 crop at 4x), matching established house style.
`नागवर्म-महाराज!` is a line-wrap hyphenation joined silently
(नागवर्ममहाराज!) with the preceding dash-plus-quote read as `---` per the
mdash rule. Print-noise omissions (verified at 4--5x as clearly detached
specks, omitted per the speck rule): a dot before the first शवाः (P4; the
second शवाः in the same sentence is clean), a tick before श्मशानमौनं (P9),
a tick before शक्यते (P9), and two high dots around किमपि (P7, above the
headline). None pairs quotationally; positions logged here for re-check.

### Coverage (new span only)

p016:P1 {x-com:layout: : skip x-com-layout
p016:P2 "अत्र कापि : clean
p016:P3 "वञ्चनायाः प्रसक्तिः : clean
p016:P4 "अस्माकं सैनिकेषु : clean
p016:P5 उग्राक्षस्य नामश्रवणेन : clean
p016:P6 सः कम्पमानेन : clean (opens column-turn speech, J13)
p016:P7 {pc}समीपं नीतवान्। : clean (closes J13 join)
p016:P8 तत् श्रोतुम् : clean
p016:P9 तदा करवीरः : F5
p016:P10 {category: (अनुवर्तते)} : skip metadata
J12 p015:P8 -> p016:P2 : ok (prev ends तत्र! terminal, fresh break)
J13 p016:P6 {pb} -> p016:P7 {pc} : ok (नागवर्मणः | समीपं, spaced join)
J14 p016:P9 {pb} -> END : ok (speech closed via F5, serial continues next issue)
