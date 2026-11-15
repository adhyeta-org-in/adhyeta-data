# Proofread report: 1986_11 p030 (उत्तररामायणम् --- रावणजन्म, p30--37 span)

## Summary

3 findings (3 error severity: 1 OCR/high routed as a verified `{del:}`/`{ins:}` verdict in the story file, 1 OCR/medium* routed as verified `{del:}` with a held `{sug-ins:}` replacement, 1 AGR/low* held as `{x-com:}` commentary with no verdict for lack of Phase A grounding); no repeats, so no Patterns section. Print conventions kept as house style throughout: open sandhi at word boundaries, `-तस्` ablatives (लङ्कातः, बलात्, बाल्यतः), house spellings (पारङ्गताः, सङ्कल्पितवान्), and double quotes for all spoken dialogue with cross-page pairs left intact. Orth scanner (`scan.py orth` on deblocked text) reports no findings; word, sandhi, participle, quote, flow and straight-through continuity passes done sentence by sentence from text alone, images closed for the whole phase. Not checked: the story continues before p30 and past p37 (outside the assigned range), so flow is verified only within this span; the text is direct transcription from scans, not OCR output. Loc below is keyed on story coordinates `pNN:Pm` (NN = scan sequence, Pm = lint chunk number within the span) plus the chunk's first two words as anchor, counting words on the chunk from 1 with a `{...}` block occupying its span's word slot.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p034:P8:4 (सत्यं सर्वम्) | `मन्तः पुत्रान्` | `मत्तः पुत्रान्` | OCR | error | high | मन्तः is not a Sanskrit word; the sentence needs the ablative "from me" (कैकसी came to obtain sons from विश्रवस्), and न्त/त्त ligatures confuse in print; applied as `{del:मन्तः}{ins:मत्तः}` |
| 2 | p036:P8:5 (एवं तर्हि) | `अन्यप्राणितः भयं` | `अन्यप्राणिनः भयं` | OCR | error | medium* | अन्यप्राणितः has no grammatical parse (a -तस् adverb cannot sit on a consonant-stem compound); भयम् with नास्ति takes genitive or ablative, and the genitive is the minimal त→न fix, though ablative अन्यप्राणिभ्यः is also possible; removal applied as `{del:}`, replacement held as `{sug-ins:}` |
| 3 | p036:P4:20 (रावणः निराहारः) | `नवमस्तकानि अग्नौ आहुतीभूताः` | `आहुतीभूतानि` | AGR | error | low* | feminine plural predicate with a neuter plural subject; no `{del:}`/`{ins:}` placed because no Phase A flag is on file, so an `{x-com:}` marks the spot for the compiler |

## Unverified

F2 replacement: `अन्यप्राणिनः` (genitive, minimal fix) vs `अन्यप्राणिभ्यः` (ablative, idiomatic with भयम्); a 3x print re-check of त vs न/भ्य would settle the glyph, otherwise the compiler picks on sense. F3: `आहुतीभूतानि` for printed `आहुतीभूताः`; nothing in print supports a feminine subject here, but without a Phase A flag this phase may not verdict it, so it is held for the compiler as filed. The inherited Phase A candidates are both dispositioned in the file (F1 promoted to verified verdict, F2 to verified deletion with held replacement); no candidate is left unexamined.

## Coverage

p030:P1 {x-com:layout:} : skip x-com-only
p030:P2 # उत्तररामायणम् : skip title
p030:P3 तपोधनैः महामुनिभिः : clean (ब्रह्मदेवतः kept as print-faithful -तस् formation, variant at most)
p030:P4 राक्षसानां सकाशात् : clean
p030:P5 कृते कुत्रापि : clean
p030:P6 किन्तु महेश्वरः : clean
p030:P7 {category:} : skip metadata
p031:P1 {x-com:layout:} : skip x-com-only
p031:P2 गच्छन्तु सः : clean
p031:P3 देवताः ऋषयः : clean
p031:P4 विष्णुमूर्तिः तेभ्यः : clean
p031:P5 व्यवहारान् अपि : clean
p031:P6 तानि वचनानि : clean
p031:P7 एषा वार्ता : clean
p032:P1 {x-com:layout:} : skip x-com-only
p032:P2 इदानीम् आलोचनां : clean
p032:P3 मालिः सुमालिः : clean (सधैर्यं parses as adverbial accusative and stands)
p032:P4 एवंरीत्या आलोचनां : clean
p032:P5 राक्षसाः महद्युद्धार्थं : clean
p032:P6 धनुर्बाण-शङ्ख-चक्र-गदा-खड्गादिकं : clean
p032:P7 विष्णुमूर्तिः स्वीयबाणैः : clean
p033:P1 {x-com:layout:} : skip x-com-only
p033:P2 कृतवान् : clean
p033:P3 मालेः मरणं : clean
p033:P4 एतत् दृष्ट्वा : clean
p033:P5 वचनपालनम् एव : clean
p033:P6 द्वौ अपि : clean
p033:P7 विष्णुमूर्तिः तूष्णीं : clean
p033:P8 एवंरीत्या सर्वे : clean
p033:P9 सर्वे राक्षसाः : clean
p034:P1 {x-com:layout:} : skip x-com-only
p034:P2 कुबेरः इति : clean
p034:P3 एवं स्थिते : clean
p034:P4 तदा सुमालेः : clean
p034:P5 रूपेण अपरलक्ष्मीः : clean
p034:P6 जनकस्य विषये : clean
p034:P7 कैकसी अञ्जलिबद्धा : clean
p034:P8 सत्यं सर्वम् : F1
p034:P9 तपोधनस्य भवतः : clean
p035:P1 {x-com:layout:} : skip x-com-only
p035:P2 साधुगुणयुतान् कुमारान् : clean
p035:P3 एवंरीत्या बहुधा : clean
p035:P4 किञ्चित्कालानन्तरं कैकसी : clean
p035:P5 रावणानन्तरं जातः : clean
p035:P6 महाबलशाली तस्य : clean
p035:P7 चतुर्षु अपि : clean
p035:P8 विभीषणः एव : clean
p035:P9 रावणकुम्भकर्णौ अरण्ये : clean
p035:P10 कदाचित् ते : clean
p036:P1 {x-com:layout:} : skip x-com-only
p036:P2 दृष्ट्वा हे : clean
p036:P3 महान् क्रोधनः : clean
p036:P4 रावणः निराहारः : F3
p036:P5 पुरतः प्रत्यक्षीभूय : clean
p036:P6 रावणः परमानन्दभरितः : clean
p036:P7 वत्स तादृशवरः : clean
p036:P8 एवं तर्हि : F2
p037:P1 {x-com:layout:} : skip x-com-only
p037:P2 अल्पप्राणिनां विचारे : clean
p037:P3 ब्रह्मा रावणस्य : clean
p037:P4 अनन्तरं ब्रह्मा : clean
p037:P5 मम मनः : clean
p037:P6 इदानीं वरप्रार्थनायाः : clean
p037:P7 तदा देवाः : clean
p037:P8 विहरन्तीः सप्त : clean
p037:P9 तदा सरस्वत्याः : clean
p037:P10 सद्यः एव : clean
p037:P11 एवंरीत्या रावणः : clean
J1 p030:P4 {pb} -> p030:P5 {pc} : ok (साधुसज्जनानां → कृते, spaced continuation across columns)
J2 p030:P6 {pb} -> p031:P2 {pc} : ok (समीपं → गच्छन्तु, spaced continuation across pages)
J3 p031:P4 {pb} -> p031:P5 {pc} : ok (तेषां → व्यवहारान्, spaced continuation across columns)
J4 p031:P7 {pb} -> p032:P2 {pc} : ok (वयम् → इदानीम्; speech closes, spaced continuation across pages)
J5 p032:P5 {pb} -> p032:P6 {pc} : ok (धृत्वा → धनुर्बाण, spaced continuation across columns)
J6 p032:P7 {pb} -> p033:P2 {pc} : ok (कर्तनं → कृतवान्, spaced continuation across pages)
J7 p033:P4 {pb} -> p033:P5 fresh : ok (clean break; माल्यवान्'s challenge ends, विष्णु replies)
J8 p033:P9 {pb} -> p034:P2 {pc} : ok (सः → कुबेरः, spaced continuation across pages)
J9 p034:P6 {pb} -> p034:P7 fresh : ok (clean break; विश्रवस्'s question ends, कैकसी answers)
J10 p034:P9 {pb} -> p035:P2 {pc} : ok (कृपया → साधुगुणयुतान्, speech continues across pages)
J11 p035:P5 {pb} -> p035:P6 {pc} : ok (कुम्भकर्णः → महाबलशाली, spaced continuation across columns)
J12 p035:P10 {pb} -> p036:P2 {pc} : ok (रावणं → दृष्ट्वा, spaced continuation across pages)
J13 p036:P4 {pb} -> p036:P5 {pc} : ok (तस्य → पुरतः, spaced continuation across columns)
J14 p036:P8 {pb} -> p037:P2 {pc} : ok (मनुष्यादीनाम् → अल्पप्राणिनां, speech continues across pages)
J15 p037:P7 {pb} -> p037:P8 {pc} : ok (नन्दनवने → विहरन्तीः, spaced continuation across columns)
J16 p037:P11 {pb} -> END : ok (clean break; sentence and range end together)
