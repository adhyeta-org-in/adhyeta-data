## Summary

Phase A extract gate and Phase B proofread gate both pass clean (`lint.py --phase extract` and `--phase proofread`: 4 pages, 0 error paras, 0 story findings); `scan.py orth` on deblocked text reports 0 hits across 35 lines. Findings table: none — no `{del:}`/`{ins:}` verdicts and no `{sug-del:}`/`{sug-ins:}` candidates were added, so the story file is byte-identical to its Phase A state. Two items are held as unverified below (one print-suspect word, one speaker-attribution ambiguity); both need the user or a re-opened scan, not text edits. Loc below is keyed `pNN:Pm` (NN = scan sequence 20 + `{pgb}`-span ordinal, Pm = lint chunk number) plus the first two words as anchor.

## Findings

No findings.

## Unverified

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| U1 | p021:P4 धोतकस्य गमनानन्तरं (`आससखी इन्दुलेखा`) | `आससखी` | `आप्तसखी`? | LEX | minor | low* | `आससखी` is not a Sanskrit word; intimate-friend sense wants `आप्तसखी` (प्त vs स glyph question, images closed in Phase B) |
| U2 | p022:P10 लतादेव्याः मुखे → p023:P2 कलाप्राज्ञतां विमृशति (king's `"चिन्तयतु इत्युक्ते ... तस्याः प्रस्तावेन किं प्रयोजनम्?"`) | whole span as printed | ? | STY | minor | low* | speaker attribution inside the span is ambiguous (king voicing an objection vs relaying Suketu); grammar flows either way, so no rupture and no block |

## Coverage

p020:P1 {x-com:}: skip layout-only chunk
p020:P2 # राजकुमार्याः: skip title
p020:P3 स्वर्णपुरस्य राजकुमारी : clean
p020:P4 एकदा धोतकः : clean
p020:P5 धोतकस्य वचनेन : clean
p020:P6 केषाञ्चित् दिनानाम् : clean
p020:P7 राजकुमारस्य। स : clean
p020:P8 चित्रलेखनानन्तरं लतादेव्याः : clean
p020:P9 एवं स्थिते : clean
p020:P10 {author:}: skip metadata footer
p021:P1 {x-com:}: skip layout-only chunk
p021:P2 भाति। अतः : clean
p021:P3 महाराजः दूतद्वारा : clean
p021:P4 धोतकस्य गमनानन्तरं : U1
p021:P5 'इन्दुलेखायाः वचनं : clean
p021:P6 तदा लतादेवी : clean
p021:P7 किं करणीयम् : clean
p021:P8 मन्त्री उक्तवान् : clean
p022:P1 {x-com:}: skip layout-only chunk
p022:P2 उद्घोषयामः। तेन : clean
p022:P3 अनन्तरदिने देशे : clean
p022:P4 अत्रान्तरे सुकेतुः : clean
p022:P5 तदा राजा : clean
p022:P6 "प्रभो! अस्याः : clean
p022:P7 तदा मन्त्री : clean
p022:P8 अस्माकं का : clean
p022:P9 महाराजः एतत् : clean
p022:P10 लतादेव्याः मुखे : U2
p023:P1 {x-com:}: skip layout-only chunk
p023:P2 कलाप्राज्ञतां विमृशति : U2
p023:P3 "प्रभो! चिन्तायाः : clean
p023:P4 तदा राजकुमारी : clean
p023:P5 पराकाष्ठा मया : clean
p023:P6 तदा महाराजः : clean
p023:P7 सुकेतुः मन्दहासं : clean
J1 p020:P6 {pb} -> p020:P7 {pc} : ok (कस्यचित् → राजकुमारस्य, column continuation)
J2 p020:P9 {pb} -> p021:P2 {pc} : ok (दुःखिता इति → भाति, page-turn speech continuation)
J3 p021:P3 {pb} -> p021:P4 fresh : ok (clean column break, Dhotaka episode to Indulekha episode)
J4 p021:P8 {pb} -> p022:P2 {pc} : ok (दीयते इति → उद्घोषयामः, page-turn speech continuation)
J5 p022:P7 {pb} -> p022:P8 {pc} : ok (अवकाशदानेन → अस्माकं का हानिः, column continuation)
J6 p022:P10 {wb} -> p023:P2 {pc} : ok (चित्र → कलाप्राज्ञतां, solid word join across page turn)
J7 p023:P4 {pb} -> p023:P5 {pc} : ok (कौशलस्य → पराकाष्ठा, column continuation)
J8 p023:P7 {pb} -> END : ok (clean story close, reward declined, teaching begins)
