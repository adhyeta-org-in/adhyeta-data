# Proofread report: 1985_07 p040 (शिवपार्वती --- ५. पार्वत्याः तपश्चर्या।), scans 40--46

## Summary

9 findings: 4 SPL print-slip verdicts (systematic `स`/`म` sort error, all verified at 3x+ in Phase A), 2 STY quote verdicts (1 corrected sort, 1 deleted stray mark), 1 AGR gender verdict, and 2 held candidates (1 LEX referent, 1 SPL glyph). 1 kept style residual: the Vasishtha tale quotes open past the range end and are kept for the compiler to pair with the next installment. Orth scanner: 1 hit (title `५.` full stop, kept as the printed installment number); the text is a print transcription, not OCR. Proofread gate: 0 error paras; 1 residual story note (p046:P3, kept + documented). Loc is page-chunk:word, words counted whitespace-separated on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p041:P2:12 `इदानीं मः भस्मीभूतः` | `मः` | `सः` | SPL | error | high | `मः` is no word; `सः` (Manmatha) is the subject of `भस्मीभूतः`; print sets `म` for `स` (verified at 3x in Phase A) |
| F2 | p041:P2:24 `किन्तु मः जनानां` | `मः` | `सः` | SPL | error | high | same `स`/`म` slip; `सः` is the subject of `तिष्ठति` |
| F3 | p041:P4:24 `--- 'यत् प्रवृत्तं` | `'यत्` | `"यत्` | STY | error | high | Himavān's consolation is spoken (`---`, closes `मास्तु"`); the single open is a dropped second stroke |
| F4 | p041:P4:30 `शिवः मद्यः` | `मद्यः` | `सद्यः` | SPL | error | high | `मद्यः` is senseless here; `सद्य एव` (at once) completes `परिणेष्यति`; same `स`/`म` slip |
| F5 | p042:P2:4 `उद्देशेन 'तपः आचरति` | `'` | delete the mark | STY | error | high | lone `'` inside the open `"` speech has no inner role (direct question, cf. unmarked `कामदेवं...वा?`); stray mark |
| F6 | p042:P9:2 `पार्वती स्वस्मिन् स्निह्यति` | `स्वस्मिन्` | `मयि` or `शिवे` | LEX | likely | medium* | reflexive `स्वस्मिन्` (in herself) is grammatical but senseless; Śiva knows she loves him; exact author wording unrecoverable |
| F7 | p043:P8:43 `स्वप्ने अपि दुर्लभः` | `दुर्लभः` | `दुर्लभम्` | AGR | error | high | neuter `सुखं` needs neuter `दुर्लभम्` as predicate |
| F8 | p046:P6:3 `न साधारणः` | `साधरणः` | `साधारणः` | SPL | likely | low* | only `साधारणः` is a word; the `ध`/`धा` glyph is uncertain with images closed |
| F9 | p046:P3:13 `उक्तवान् --- "'इन्द्रसावर्णिनामकस्य` | `"` + `'` opens | `?` (keep as printed) | STY | style | high | tale opens whose mates lie beyond the range; the serial continues (`अनुवर्तते`); kept for the compiler to pair |

## Patterns

1. `स` set as `म` in print (3×): F1, F2, F4 (`मः`, `मः`, `मद्यः`). Phase A verified the glyph shapes at 3x+ against same-page `सः` (`सः तपः त्यक्त्वा`); the error is systematic, not a reading slip.
2. House-open sandhi kept as variant (3+): `जगतः हितार्थं` (p040:P7), `तत् हिताय एव` (p041:P4), `एतत् सर्वं श्रुतवताम्` (p045:P8). Classical sandhi would join; this print keeps openings throughout, so nothing flagged.
3. Epic `मा` + imperative kept as variant (1): `मा विस्मरतु` (p046:P2). Classical prose prefers `मा` + aorist; the Epic construction stands as seen.

## Unverified

- H1 = F6 (LEX, medium*): context pins a first-person/Śiva referent (`मयि` or `शिवे`) but no scan check can settle authorial intent; coordinator decides.
- H2 = F8 (SPL, low*): `ध` vs `धा` in `साधरणः`; settle by checking the scan glyph.

## Coverage

p040:P1 `{x-com:layout:` : skip layout chunk; p040:P2 `# शिवपार्वती` : skip title; p040:P3 `वज्राङ्गः ब्रह्मणः` : clean; p040:P4 `'यावत् शिवस्य` : clean; p040:P5 `मन्मथप्रभावेण वनं` : clean; p040:P6 `मन्मथः स्वपुष्पबाणैः` : clean; p040:P7 `पत्युः मरणेन` : clean; p040:P8 `तदा शिवः` : clean; p041:P1 `{x-com:layout:` : skip layout chunk; p041:P2 `मोहम् उत्पादितवान्` : F1, F2; p041:P3 `कामवशात् शिवस्य` : clean; p041:P4 `शिवस्य नेत्राग्निना` : F3, F4; p041:P5 `एव भवतीं` : clean; p041:P6 `शिवस्य व्यवहारेण` : clean; p041:P7 `एकदा हिमवतः` : clean; p041:P8 `पार्वती इष्टसिद्ध्यर्थं` : clean; p041:P9 `शृङ्गतीर्थे निवसन्ती` : clean; p041:P10 `'कदाचित् वा` : clean; p041:P11 `किन्तु प्रतिदिनं` : clean; p042:P1 `{x-com:layout:` : skip layout chunk; p042:P2 `केन वा` : F5; p042:P3 `तदा पार्वती` : clean; p042:P4 `अपरत्र शिवः` : clean; p042:P5 `स्वागतानन्तरं ते` : clean; p042:P6 `एतत् श्रुत्वा` : clean; p042:P7 `तदा ब्रह्मा` : clean; p042:P8 `शिवः तेषां` : clean; p042:P9 `पार्वती स्वस्मिन्` : F6; p043:P1 `{x-com:layout:` : skip layout chunk; p043:P2 `दिभिः तं` : clean; p043:P3 `"अहं ब्रह्मवंशीयः` : clean; p043:P4 `"अहं मेनाहिमवतोः` : clean; p043:P5 `नारदस्य मन्त्रोपदेशानुसारं` : clean; p043:P6 `तदा वटुः` : clean; p043:P7 `"भवतः सूचनार्थं` : clean; p043:P8 `"का इयं` : F7; p044:P1 `{x-com:layout:` : skip layout chunk; p044:P2 `ष्यति। रात्रौ` : clean; p044:P3 `तदा कोपम्` : clean; p044:P4 `अनन्तरं पार्वती` : clean; p044:P5 `पार्वत्याः विवाहविषये` : clean; p044:P6 `तद्दिने एव` : clean (`तद्`+`दिन` locative, valid; kept); p044:P7 `सप्तर्षयः शिवस्य` : clean; p045:P1 `{x-com:layout:` : skip layout chunk; p045:P2 `आहूतवान्? आज्ञादानेन` : clean; p045:P3 `"महर्षयः! अहम्` : clean; p045:P4 `सप्तर्षयः सन्तोषेण` : clean; p045:P5 `हिमवान् आदरपूर्वकं` : clean; p045:P6 `उक्तवान् "महर्षयः` : clean; p045:P7 `सप्तर्षयः उक्तवन्तः` : clean; p045:P8 `हिमवान् गम्भीरस्वरेण` : clean; p045:P9 `हिमवतः वचनेन` : clean; p046:P1 `{x-com:layout:` : skip layout chunk; p046:P2 `जाता इति` : clean; p046:P3 `एतत्सन्दर्भे महर्षिः` : F9; p046:P4 `महाराजस्य अनरण्यस्य` : clean; p046:P5 `एकदा पद्मावती` : clean; p046:P6 `पिप्पलादः न` : F8; p046:P7 `पिप्पलादः पद्मावत्याः` : clean; p046:P8 `मुनेः पिप्पलादस्य` : clean; p046:P9 `राजसभायां मौनम्` : clean; p046:P10 `(अनुवर्तते)` : clean.

J1 p040:P4 `{pb}` -> p040:P5 fresh : ok (clean break, left-to-right column turn); J2 p040:P8 `{pb}` -> p041:P2 `{pc}` : ok (`पुत्रीविषयकं मोहम्` continues); J3 p041:P4 `{pb}` -> p041:P5 `{pc}` : ok (`सद्य एव` continues); J4 p041:P11 `{pb}` -> p042:P2 `{pc}` : ok (`त्यक्त्वा केन` continues); J5 p042:P6 `{pb}` -> p042:P7 fresh : ok (clean break, Śiva's speech ends, Brahmā speaks); J6 p042:P9 `{wb}` -> p043:P2 `{pc}` : ok (`अर्घ्यपाद्यादिभिः` solid join); J7 p043:P4 `{pb}` -> p043:P5 `{pc}` : ok (`अहं नारदस्य` continues); J8 p043:P8 `{wb}` -> p044:P2 `{pc}` : ok (`भविष्यति` solid join); J9 p044:P3 `{pb}` -> p044:P4 fresh : ok (clean break, Pārvatī sends the vaṭu off, Śiva reveals himself); J10 p044:P7 `{pb}` -> p045:P2 `{pc}` : ok (`अस्मान् आहूतवान्` continues); J11 p045:P5 `{pb}` -> p045:P6 `{pc}` : ok (`सत्कृत्य उक्तवान्` continues); J12 p045:P9 `{pb}` -> p046:P2 `{pc}` : ok (`अंशेन जाता` continues); J13 p046:P5 `{pb}` -> p046:P6 fresh : ok (fresh para within the continuing tale; tale quotes kept open per F9); J14 p046:P10 `{pb}` -> END : ok (range ends clean on `(अनुवर्तते)`; serial continues next issue).
