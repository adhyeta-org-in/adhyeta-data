# Proofread report — 1984_10 p001 (RUN 20261114_1627_samskrta_chandamama_1984_10)

## Summary

9 findings: 7 verified missing-quote insertions (STY / style / high, F1–F7) and 2 held word candidates (F8 CNS, F9 SPL; likely / medium*, unverified). The systematic issue is print-dropped quote marks across multi-paragraph speech, all pinned by speech sense plus sentence boundary (see Patterns). `scan.py orth` on deblocked story text gave 0 hits; word, sandhi, and flow passes found nothing else; no passages were left unchecked. Loc below is `pNN:Pm` (NN = scan sequence from filename `p001` plus `{pgb}`-span order; Pm = chunk number in that span, matching lint `P` numbers) plus the chunk's first two words as anchor; corrections travel only as blocks in the story file, never as silent edits.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p002:P2 «लब्धम्। "राज्ञि» | `प्रदर्शयन्ति स्म। एतत् दृष्ट्वा` | `प्रदर्शयन्ति स्म।{ins:"} एतत् दृष्ट्वा` | STY | style | high | quoted speech ends where third-person narration resumes; print's close is missing |
| F2 | p003:P8 «तदा प्रजाप्रतिनिधयः» | `प्रशंसां कृतवान्।{pb}{pgb: ९}` | `प्रशंसां कृतवान्।{ins:"}{pb}{pgb: ९}` | STY | style | high | page-final close of the representatives' speech; next page opens a new pair |
| F3 | p004:P2 «एषा तु» | `एषा तु वस्तुस्थितिः" इति।` | `{ins:"}एषा तु वस्तुस्थितिः" इति।` | STY | style | high | close plus इति present with no open; short closing sentence of the speech |
| F4 | p004:P6 «"राजा धीरसेनः» | `पश्यन्ति एव। + धीरसेनः (next para)` | `पश्यन्ति एव।{ins:"}` | STY | style | high | multi-para speech: this paragraph ends its sentence and closes its own pair |
| F5 | p004:P7 «धीरसेनः राजोचितं» | `धीरसेनः राजोचितं ...{pb}` | `{ins:"}धीरसेनः राजोचितं ...{pb}` | STY | style | high | middle paragraph of the same speech opens its own pair (closes in F6) |
| F6 | p004:P8 «त्यक्त्वा प्रजानां» | `हितार्थं कार्यं करोति। + महाराजस्य (next para)` | `हितार्थं कार्यं करोति।{ins:"}` | STY | style | high | column-continued paragraph ends its sentence and closes its own pair |
| F7 | p004:P9 «महाराजस्य विषये» | `प्रामाणिकाः। यथा राजा तथा प्रजाः" ...वन्तः` | `प्रामाणिकाः। {ins:"}यथा राजा तथा प्रजाः" ...वन्तः` | STY | style | high | punchline restates the title moral; close present, open pinned before यथा |
| F8 | p004:P12 «एतदनन्तरं अल्पे» | `विजयनगरस्य अपि जनाः` | `{sug-del:विजयनगरस्य}{sug-ins:जयनगरस्य} अपि जनाः` | CNS | likely | medium* | the story kingdom is जयनगर throughout; no विजयनगर is ever introduced |
| F9 | p004:P9 «महाराजस्य विषये» | `विश्वासः तावन् अस्ति` | `विश्वासः {sug-del:तावन्}{sug-ins:तावत्} अस्ति` | SPL | likely | medium* | तावन् is not a word; तावत् (so much) governs the यत्-clause |

## Patterns

PAT-1 print-dropped quote marks in multi-paragraph speech: 7 × `{ins:"}` supplied where speech sense plus sentence boundary pins the position (F1 speech-to-narration switch; F2 page-final close; F3 close-with-इति lacking open; F4–F6 one speech standing alone per paragraph across a clean break and a column joint; F7 title-moral punchline). Sorts kept as printed throughout: doubles for reported speech, singles for thought/interior (`'वणिजा उक्तं...'` mind-reading, `'अत्र महाराजस्य...'` speech-inside-speech, `'प्रजाप्रतिनिधीनां...'` inward assent).

## Unverified

F8 `विजयनगरस्य` → `जयनगरस्य` (CNS, medium*): narrative evidence is strong (जयनगर in p001:P3, no other kingdom named) but a deliberate second-kingdom reading cannot be excluded from text alone; a print re-check is closed, so held for the user. F9 `तावन्` → `तावत्` (SPL, medium*): grammar wants the indeclinable तावत् and orth scan did not flag it either way; glyph re-check is closed, so held for the user. Print-mix spellings kept as seen with no block: `वणिज्/वणिक्`, `प्रामाणिक` (ण), `मनस्सु`, hyphenated compounds (`उपायन-रूपेण`, `नीति-शिक्षणं`, `समुचित-विकासार्थं`), open sandhi (`तद् दिने`-type openness absent here; `स्वराजं/स्वराजस्य` both grammatical in place).

## Coverage

p001:P1 «{x-com:layout:» : skip layout
p001:P2 «# यथा» : skip title
p001:P3 «जयनगर-राज्यस्य राजा» : clean
p001:P4 «पार्श्वराज्ये प्रतापनगरे» : clean
p001:P5 «प्रतापनगरस्य राजा» : clean
p001:P6 «कारणं ज्ञात्वा» : clean
p001:P7 «एतत् श्रुत्वा» : clean
p001:P8 «"धीरसेनः स्वप्रजानां» : clean
p001:P9 «परेयुः उभौ» : clean
p001:P10 «{author: माणवकः}{pgb}» : skip metadata
p002:P1 «{x-com:layout:» : skip layout
p002:P2 «लब्धम्। "राज्ञि» : F1
p002:P3 «"महाराजस्य विषये» : clean
p002:P4 «सञ्चारसमये राजा» : clean
p002:P5 «विक्रयणं न» : clean
p002:P6 «सञ्चारतः प्रतिनिवृत्तः» : clean
p002:P7 «एतदनन्तरं वीरभद्रः» : clean
p002:P8 «एकत्र राजा» : clean
p002:P9 «"राजा एव» : clean
p002:P10 «प्रजानाम् एतादृशं» : clean
p003:P1 «{x-com:layout:» : skip layout
p003:P2 «कृत्वा तत्रत्यं» : clean
p003:P3 «किञ्चित्कालं यावत्» : clean
p003:P4 «वीरभद्रः मन्त्रिणाम्» : clean
p003:P5 «मासद्वयानन्तरं ते» : clean
p003:P6 «च अस्ति"» : clean
p003:P7 «एतत् श्रुत्वा» : clean
p003:P8 «तदा प्रजाप्रतिनिधयः» : F2
p004:P1 «{x-com:layout:» : skip layout
p004:P2 «एषा तु» : F3
p004:P3 «किञ्चिदिव तुष्टः» : clean
p004:P4 «"महाराज! धूलिमध्ये» : clean
p004:P5 «'प्रजाप्रतिनिधीनां वचनं» : clean
p004:P6 «"राजा धीरसेनः» : F4
p004:P7 «धीरसेनः राजोचितं» : F5
p004:P8 «त्यक्त्वा प्रजानां» : F6
p004:P9 «महाराजस्य विषये» : F7, F9
p004:P10 «प्रतिनिधीनां वचनेन» : clean
p004:P11 «सः सद्यः» : clean
p004:P12 «एतदनन्तरं अल्पे» : F8
J1 p001:P5 {wb} -> p001:P6 {pc} (continues) : ok (आगमन + कारणं = आगमनकारणं, solid column joint)
J2 p001:P9 {pb} -> p002:P2 {pc} (continues) : ok (स्वागतं + लब्धम् = स्वागतं लब्धम्, page turn)
J3 p002:P4 {wb} -> p002:P5 {pc} (continues) : ok (क्रय + विक्रयणं = क्रयविक्रयणं, solid column joint)
J4 p002:P10 {pb} -> p003:P2 {pc} (continues) : ok-text (print `इति कृत्वा` kept as seen; speech continues across the page turn)
J5 p003:P5 {pb} -> p003:P6 {pc} (continues) : ok (समर्थः + च, spaced column joint)
J6 p003:P8 {pb} -> p004:P2 fresh (clean break) : F2, F3 (speech closes its pair on each side of the page turn)
J7 p004:P7 {pb} -> p004:P8 {pc} (continues) : ok (भोगविलासादिकं + त्यक्त्वा, spaced column joint)
J8 p004:P12 {pb} -> END (clean break) : ok
