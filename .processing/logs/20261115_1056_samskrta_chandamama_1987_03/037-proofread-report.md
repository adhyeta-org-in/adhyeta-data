# Proofread report: 1987_03 p037 (काकतालीयम्, pp. 37-42)

## Summary

Five findings: three error verdicts (F2, F4, F5) landed as `{del:}`/`{ins:}` blocks in `p037.md`, and two held candidates (F1 agreement mismatch with no unique fix, F3 predicative-participle gender with a conceivable adverbial parse) kept as `{sug-del:}`/`{sug-ins:}` for the user. The systematic issue is small agreement slips in translated prose (F1, F3) plus two print misprints one stroke from the intended word (F2, F5). `Loc` is story coordinates `pNN:Pm` (scan sequence + chunk number, lint `P` numbers) with anchor words; the word index counts deblocked words of the chunk from 1. `scan.py orth` on deblocked text reported no hits; the text is direct eye transcription, not OCR. Three Phase A suspicions were checked and dropped with reason (सुवर्णापणाः/दृष्टाः both valid masc.nom.pl; कलानुगुणम् a valid tatpurusa "conforming to workmanship"; शाकटिकस्य the regular vriddhi taddhita from शकट), and three isolated print marks with no quotable role were kept out of text as `{x-illegible:}`/`{x-com:}` audit blocks (lone singles before शयानौ and after कण्ठहारः, one red smudge before मातुलानी).

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p037:P3 w45 `रामः कृष्णः` | `तयोः प्रवृत्तः जाता` | `तयोः प्रवृत्तं जातम्` or keep print | AGR | error | low* | masc.nom. प्रवृत्तः cannot agree with fem.nom. जाता; no single-word fix parses, see Unverified |
| F2 | p038:P2 w7 `गृहात् निर्गतौ` | `किञ्चिद्धूरं गमनानन्तरं` | `किञ्चिद्दूरं` | SPL | error | high | द्ध has no source in किञ्चित्+दूरम्; print द्ध verified in Phase A, smallest change to a real word |
| F3 | p040:P5 w23 `आपणिकः तत्` | `सह व्यवहारगतं वा भवान्` | `सह व्यवहारगतः` | AGR | likely | medium* | predicative participle should agree with masc. भवान्; accusative-adverb parse conceivable, see Unverified |
| F4 | p041:P2 w21 `कृष्णस्य समीपे` | `रे? वदत` | `रे? वद` | MRP | error | high | imperative number follows the addressee (singular Krishna, cf. रे), not the plural speakers |
| F5 | p041:P4 w10 `तत्र रामः` | `कालाहलतः भीतः` | `कोलाहलतः` | SPL | error | high | only कोलाहल (uproar) fits fleeing by a side path; print ा-strokes noted in Phase A, smallest change |

## Unverified

F1 (p037:P3): held forms `प्रवृत्तः जाता` / candidate `प्रवृत्तं जातम्`. Tried: (a) प्रवृत्तं जातम् — parses cleanly (subject अलसजीवनम्, neut.) but changes two words; (b) प्रवृत्तिः जाता — one-word change yet leaves एतादृशम् अलसजीवनम् without a role; (c) keep print as translator slip with sense clear ("their idle life set in"). Settles by editor's choice among (a)-(c); print re-check cannot decide grammar.
F3 (p040:P5): held forms `व्यवहारगतं` / candidate `व्यवहारगतः`. The rich man's sense ("are you dealing with another?") wants masc. predicative गतः agreeing with भवान्, but the accusative could be read as an adverbial modifier with an elided verb. Settles by editor's call on predicative vs adverbial reading.

## Coverage

p037:P2 `# काकतालीयम्` : skip title
p037:P3 `रामः कृष्णः` : F1
p037:P4 `पिता कानिचन` : clean
p037:P5 `तदा रामः` : clean
p037:P6 `क्लेशाय। अस्माकं` : clean
p037:P7 `"कः सः` : clean
p037:P8 `"आवां प्रातः` : clean
p037:P9 `"उत्तमः उपायः` : clean
p037:P10 `अनन्तरदिने प्रातः` : clean
p038:P2 `गृहात् निर्गतौ` : F2
p038:P3 `"पश्यतु भोः!` : clean
p038:P4 `"सत्यं किल?` : clean
p038:P5 `अनन्तरं तौ` : clean
p038:P6 `मिलित्वा दूरं` : clean
p038:P7 `तत्समये तेन` : clean
p038:P8 `रुद्राम्बा धनिका।` : clean
p038:P9 `"ग्रामस्य हितार्थम्` : clean
p038:P10 `"उत्तमकार्यम् एतत्।` : clean
p038:P11 `प्रकाशमानं तत्` : clean
p038:P12 `"एतस्य कङ्कणयुगलस्य` : clean
p038:P13 `"आं, विलम्बः` : clean
p039:P2 `एतस्याः रुद्राम्बायाः` : clean
p039:P3 `यदा तौ` : clean
p039:P4 `रामः कृष्णम्` : clean
p039:P5 `अनन्तरं रामः` : clean
p039:P6 `कृष्णः आपणं` : clean
p039:P7 `तत्समये सर्वे` : clean
p039:P8 `कृष्णः कङ्कणं` : clean
p040:P2 `मूल्य दशसहस्रतः` : clean
p040:P3 `आपणिकः कृष्णस्य` : clean
p040:P4 `रुद्राम्बया यादृशं` : clean
p040:P5 `आपणिकः तत्` : F3
p040:P6 `सोढुं न` : clean
p040:P7 `'उत्तमः ग्राहकः` : clean
p040:P8 `आपणिकस्य चीत्कारं` : clean
p040:P9 `तान् दृष्ट्वा` : clean
p040:P10 `कृष्णस्य मुखतः` : clean
p040:P11 `रक्षकभटाः कृष्णं` : clean
p041:P2 `कृष्णस्य समीपे` : F4
p041:P3 `कृष्णः अश्रूणि` : clean
p041:P4 `तत्र रामः` : F5
p041:P5 `"भोः एतादृशम्` : clean
p041:P6 `अत्रान्तरे रामः` : clean
p041:P7 `आरूढवान्।` : clean
p041:P8 `शकटे अपरः` : clean
p041:P9 `तदा रामः` : clean
p041:P10 `शकटे स्थितः` : clean
p042:P2 `मूल्यम् एव` : clean
p042:P3 `रामः क्षणकालं` : clean
p042:P4 `तयोः कलहः` : clean
p042:P5 `तत्समये रक्षकप्रमुखस्य` : clean
p042:P6 `कृष्णः कलहायमानयोः` : clean
p042:P7 `रक्षकभटाः यदा` : clean
p042:P8 `एव।" इति` : clean
p042:P9 `तत्र रामः` : clean
p042:P10 `कृतककङ्कणयोः दात्री` : clean
p042:P11 `आलस्यस्य फलं` : clean
J1 p037:P5 {pb} -> p037:P6 {pc} (continues) : ok
J2 p037:P10 {pb} -> p038:P2 fresh (clean break) : ok
J3 p038:P5 {pb} -> p038:P6 {pc} (continues) : ok
J4 p038:P13 {pb} -> p039:P2 {pc} (continues) : ok
J5 p039:P8 {pb} -> p040:P2 {pc} (continues) : ok
J6 p040:P5 {pb} -> p040:P6 {pc} (continues) : ok
J7 p040:P11 {pb} -> p041:P2 fresh (clean break) : ok
J8 p041:P6 {pb} -> p041:P7 {pc} (continues) : ok
J9 p041:P10 {pb} -> p042:P2 {pc} (continues) : ok
J10 p042:P7 {pb} -> p042:P8 {pc} (continues) : ok
J11 p042:P11 {pb} -> END (clean break) : ok
