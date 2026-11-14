# Proofread report: p029 (1984_07, scans 29–32)

## Summary

5 findings: four punctuation (STY, likely, high) supplying print-dropped quote marks and correcting one thought/speech sort (F2–F5), and one morphology candidate (MRP, likely, medium*) held unverified (F1). No sandhi, agreement, karaka, compound, or consistency error found; proper nouns (गोविन्दः, पूर्णिमा, मुनिः) spell consistently, gerunds (गत्वा, दृष्ट्वा, क्षिप्त्वा, आनीय, नीत्वा, निष्कास्य) and periphrastic pasts (स्वच्छीकुर्वन् आसीत्) govern correctly, and dual भवतोः correctly addresses the couple. Orth scanner (`scan.py orth`) on deblocked text reports no hits. Loc below is `pNN:Pm anchor wN`: NN = scan-sequence span (p029 = 29.jpg through p032 = 32.jpg), Pm = chunk number within that span matching lint `P` numbers, anchor = first two words of the chunk, word-N counted whitespace-separated on the chunk from 1. Text is hand transcription, not OCR; every sentence of every chunk was read for continuity.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p031:P2 गोविन्दः सामान्यनि w2 | `गोविन्दः सामान्यनि एतानि` | `{sug-del:सामान्यनि}{sug-ins:सामान्यानि}` | MRP | likely | medium* | neuter -अ plural needs -आनि (सामान्यानि); held since Phase A left no glyph flag and images stay closed |
| 2 | p032:P3 पूर्णिमा विनयेन w35 | `वदन्ति। अतः अहम्` | `वदन्ति। {ins:"}अतः अहम्` | STY | likely | high | Purnima's second speech sentence reopens after narrative इति भवान् जानाति एव plus proverb; print keeps the close but drops the open |
| 3 | p032:P4 तदा मुनिः w5 | `उक्तवान् --- भवत्या` | `उक्तवान् --- {ins:"}भवत्या` | STY | likely | high | reporting verb plus --- with इति-closure pins a double open; print shows only the close |
| 4 | p032:P7 पूर्णिमायाः बुद्धिमत्तां w8 | `"मया वराः सुपात्राय एव दत्ताः इति` | `{del:"}{ins:'}मया वराः सुपात्राय एव दत्ताः{ins:'} इति` | STY | likely | high | thought (चिन्तितवान्) takes singles per story house use ('मुनेः का गतिः?', 'वररूपेण किम् इच्छामि?'); print opens with a double and drops the inner close |
| 5 | p032:P7 पूर्णिमायाः बुद्धिमत्तां w20 | `उक्तवान् --- वत्से!` | `उक्तवान् --- {ins:"}वत्से!` | STY | likely | high | direct speech (उक्तवान् plus ---) with इति-closure needs its double open; print keeps only the close after रक्षतु |

## Patterns

1. Print-dropped speech opens with kept closes (F2, F3, F5): three reported speeches open without a mark but close with `"`; each open is pinned by a reporting verb (उक्तवती, उक्तवान्) plus --- and an इति-closure. Fixed by supplying `{ins:"}` at the pinned sentence boundary; closes kept as printed.

## Unverified

- F1 `सामान्यनि` vs `सामान्यानि`: morphology says सामान्यानि (सामान्य + आनि, cf. फलानि), but without a dictionary/heritage check and without a Phase A glyph flag the print reading cannot be overruled from text alone. Settles with: (a) a 3x print check of सामान्यनि vs सामान्यानि, or (b) a dictionary confirmation that no stem सामान्यन exists; until then the `{sug-del:}/{sug-ins:}` pair is held for the user.

## Checked print-faithful (no blocks)

- p030:P3 शाखाः-पार्श्वे keeps print's mid-line hyphen (hugs word characters both sides, so `-` not em-dash); sense (throwing branches aside) does not pin a spacing correction.
- Open sandhi stands throughout (तत् दुःखस्य, एतत् दुःखस्य-pattern, यत् यत्-style openness): the edition mixes open and joined forms, logged as house variants, never flagged.
- p031:P8 / p032:P2 सम्पादिता तपःशक्तिः feminine agreement kept as printed; no correction needed.
- p032:P3 keeps print's double close after भविष्यति and the single-quoted proverb 'विना श्रमं प्राप्तम् ऐश्वर्यम् अहितस्य मूलम्' as seen; only the missing reopen (F2) is supplied.
- Exclamations after interjections (अस्ति!, वत्से!, श्रीमन्!) kept as printed: `!` directly after the word with no preceding space per transcription rule.

## Coverage

- p029:P1 {x-com:layout:} : skip layout
- p029:P2 वरत्रयम् : skip title
- p029:P3 पूर्वं रुद्रपुरे : clean
- p029:P4 गोविन्दः बाल्यात् : clean
- p029:P5 एतयोः दम्पत्योः : clean
- p029:P6 अरण्ये एकः : clean
- p029:P7 {pc}आसीत्। गोविन्दः : clean
- p029:P8 एकदा गोविन्दः : clean
- p029:P9 गोविन्दः मुनेः : clean
- p029:P10 {category:} : skip metadata
- p030:P1 {x-com:layout:} : skip layout
- p030:P2 {pc}गत्वा दृष्टवान्। : clean
- p030:P3 गोविन्दः शीघ्रं : clean
- p030:P4 गोविन्दः वृष्टिप्रसङ्गस्य : clean
- p030:P5 {pc}वा? भवान् : clean
- p030:P6 तदा मुनिः : clean
- p030:P7 गोविन्दः किञ्चित् : clean
- p030:P8 अस्तु, तथैव : clean
- p030:P9 गोविन्दः मुनिं : clean
- p030:P10 पूर्णिमा 'वररूपेण : clean
- p031:P1 {x-com:layout:} : skip layout
- p031:P2 गोविन्दः सामान्यनि : F1
- p031:P3 तत्क्षणम् एव : clean
- p031:P4 अपरस्मिन् दिने : clean
- p031:P5 गोविन्दः मुनिं : clean
- p031:P6 मुनिः आश्चर्येण : clean
- p031:P7 तदा गोविन्दः : clean
- p031:P8 मुनेः मनसि : clean
- p032:P1 {x-com:layout:} : skip layout
- p032:P2 {pc}तपःशक्तिः एतदर्थं : clean
- p032:P3 पूर्णिमा विनयेन : F2
- p032:P4 तदा मुनिः : F3
- p032:P5 श्रीमन्! एतानि : clean
- p032:P6 {pc}कदापि न : clean
- p032:P7 पूर्णिमायाः बुद्धिमत्तां : F4, F5
- J1 p029:P6 -> p029:P7 {pb}/{pc} (continues) : ok (तस्य आश्रमः + आसीत् completes the copula sentence)
- J2 p029:P9 -> p030:P2 {pb}/{pc} (continues) : ok (समीपं + गत्वा दृष्टवान् completes the approach clause)
- J3 p030:P4 -> p030:P5 {pb}/{pc} (continues) : ok (अहं गच्छामि + वा? completes Govinda's alternative question)
- J4 p030:P10 -> p031:P2 fresh (clean break) : ok (पर्याप्तम्" इति। then गोविन्दः सामान्यनि, new paragraph)
- J5 p031:P4 -> p031:P5 fresh (clean break) : ok (याचितम्?" इति। then गोविन्दः मुनिं नमस्कृत्य, new speech)
- J6 p031:P8 -> p032:P2 {pb}/{pc} (continues) : ok (सम्पादिता + तपःशक्तिः completes the passive agent phrase)
- J7 p032:P5 -> p032:P6 {pb}/{pc} (continues) : ok (लक्ष्मीविरहः + कदापि न भविष्यति completes the never-without-Lakshmi clause)
- J8 p032:P7 -> END (clean break) : ok (स्वपर्ण-शालां गतवान्। story ends, next story at 33)
