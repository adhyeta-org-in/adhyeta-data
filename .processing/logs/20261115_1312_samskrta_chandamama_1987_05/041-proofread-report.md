## Summary

13 findings: 7 OCR/error/high single-akshara print misprints and 6 STY/likely/high supplied quote marks closing multi-para speech pairs. Systematic problems: (1) print drops or swaps similar aksharas (त/न, lost ि-matra, doubled ष, stray र, म/न); (2) long quoted tales leave the outer speech pair open across paragraphs. Orth scanner on deblocked text: 0 hits. Loc is `pNN:Pm:W` (scan-sequence page, lint chunk, 1-based word index on the deblocked chunk) plus the chunk's first two words as anchor. No held candidates; images stayed closed throughout Phase B. Checked print-faithful with reason: `परपुष्टसस्यस्य` (p041:P6, parasitic-life image fits the sponging sons), `विरुध्य` (p045:P3, gerund governing व्यवहरेम), `सहनया`/`अवकृपाम्`/`तत्रत्या`/`उद्युक्तः` (all grammatical), and the print's `अन्यदेशीय`/`विदेशीय` alternation (each verified as printed).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p041:P4:45 द्वितीयविधाः दुर्मार्गिणः | `कदाचित् जताः सम्भूय` | `जनाः` | OCR | error | high | जताः is not a word; people gathering together pins जनाः |
| F2 | p042:P3:1 पत्रोः मार्गदर्शनं | `पत्रोः मार्गदर्शनं पुत्रयोः` | `पित्रोः` | OCR | error | high | पत्रोः is no form of पितृ; the पुत्रयोः parallel pins the parents |
| F3 | p042:P3:9 पत्रोः मार्गदर्शनं | `तौ पत्रोः वचनानुगुणम्` | `पित्रोः` | OCR | error | high | same slip as F2, second occurrence in the same sentence |
| F4 | p042:P4:67 ग्रामज्येष्ठौ ग्रामीणानां | `बुद्धिः विकर्मति, सन्तोषश्च` | `विकसति` | OCR | error | high | विकर्मति is not a word; the पुण्य/बुद्धि-विकास/सन्तोष triad pins विकसति |
| F5 | p042:P5:15 ग्रामज्येष्ठयोः पुत्रयोः | `करणीयम् आर्पतितम्।` | `आपतितम्` | OCR | error | high | आर्पतितम् is not a word; duty befalling them pins आपतितम् (one stray र) |
| F6 | p043:P7:26 "जयविजयौ वैकुण्ठे | `करणीया" इति।` at para end | `{ins:"}` after `इति।` | STY | likely | high | multi-para tale-speech; each paragraph closes its own pair |
| F7 | p043:P8:1 प्रवेशानिराकरणेन कुपिताः | para start, tale continues | `{ins:"}` before `प्रवेशानिराकरणेन` | STY | likely | high | same speech continued; each paragraph opens its own pair |
| F8 | p044:P2:34 सूचयामि। सत्कार्याणि | `सूचनीयम्" इति।` at para end | `{ins:"}` after `इति।` | STY | likely | high | page-turn continuation supplies the opening; the pair closes here |
| F9 | p044:P5:1 च शिशुपाल-दन्तवक्त्ररूपेण | para start after `{pc}` | `{ins:"}` after `{pc}` | STY | likely | high | column-turn continuation carries the tale; the print close at para end needs this open mate |
| F10 | p044:P6:70 ग्रामज्येष्ठयोः ज्येष्ठः | `भवेत्" इति।` at page end | `{ins:"}` after `इति।` | STY | likely | high | elder-to-villagers frame speech continues next page; each paragraph closes its own pair |
| F11 | p045:P2:1 विष्णुः कलिपुरुषस्य | para start, speech resumes | `{ins:"}` before `विष्णुः` | STY | likely | high | same frame speech resumed fresh; the print close `वदन्तु"` needs this open mate |
| F12 | p045:P4:2 एतादृशे विशिषष्टे | `एतादृशे विशिषष्टे शतानन्दवनग्रामे` | `विशिष्टे` | OCR | error | high | विशिषष्टे is not a word; the stock एतादृशे विशिष्टे pins it (one doubled ष) |
| F13 | p047:P3:22 तदा तत्रत्या | `रोगात् मुक्तः म जातः।` | `न` | OCR | error | high | म is ungrammatical here; not recovering despite treatment pins न |

## Patterns

Print single-akshara slips: 7 findings (F1, F2, F3, F4, F5, F12, F13) — dropped matras (पत्रोः/पित्रोः twice), swapped dentals (जताः/जनाः, म/न), stray conjunct parts (विकर्मति/विकसति, आर्पतितम्/आपतितम्, विशिषष्टे/विशिष्टे).

Multi-para speech outer-pair supplies: 6 findings (F6, F7, F8, F9, F10, F11) — the Jaya-Vijaya tale narration (F6 close, F7 open, F8 close, F9 open) and the elder's Kali-tale frame speech (F10 close, F11 open).

## Unverified

No held candidates. Every Phase A flag was ruled to a verdict above; nothing stays `{sug-}` for the user.

## Coverage

p041:P1 {x-com:layout: : skip x-com-only
p041:P2 # प्रत्युपकारः : skip title
p041:P3 लोके महापुरुषाः : clean
p041:P4 द्वितीयविधाः दुर्मार्गिणः : F1
p041:P5 एतादृशी परिस्थितिः : clean
p041:P6 ग्रामेऽपि उत्पन्ना। : clean
p041:P7 तौ पुत्रौ : clean
p041:P8 पुत्रयोः व्यवहारः : clean
p041:P9 {misc: : skip metadata
p042:P1 {x-com:layout: : skip x-com-only
p042:P2 वाटिकाः प्रविश्य : clean
p042:P3 पत्रोः मार्गदर्शनं : F2, F3
p042:P4 ग्रामज्येष्ठौ ग्रामीणानां : F4
p042:P5 ग्रामज्येष्ठयोः पुत्रयोः : F5
p042:P6 भागवतश्रवणसन्दर्भे ग्रामीणानां : clean
p042:P7 "श्रीकृष्णः बाल्ये : clean
p042:P8 बहवः ग्रामस्थाः : clean
p042:P9 "भवतां सन्देहाः : clean
p043:P1 {x-com:layout: : skip x-com-only
p043:P2 परिहारं कथयिष्यावः" : clean
p043:P3 ग्रामीणानां निर्गमनानन्तरं : clean
p043:P4 अपरः ज्येष्ठः : clean
p043:P5 सम्पन्नम्। पुराणकथाः : clean
p043:P6 तद्दिने तौ : clean
p043:P7 "जयविजयौ वैकुण्ठे : F6
p043:P8 प्रवेशानिराकरणेन कुपिताः : F7
p044:P1 {x-com:layout: : skip x-com-only
p044:P2 सूचयामि। सत्कार्याणि : F8
p044:P3 तदा जयविजयौ : clean
p044:P4 एतदनुगुणं तौ : clean
p044:P5 च शिशुपाल-दन्तवक्त्ररूपेण : F9
p044:P6 ग्रामज्येष्ठयोः ज्येष्ठः : F10
p045:P1 {x-com:layout: : skip x-com-only
p045:P2 विष्णुः कलिपुरुषस्य : F11
p045:P3 "जयविजययोः अवतारभूतौ : clean
p045:P4 एतादृशे विशिषष्टे : F12
p045:P5 जयविजयौ दुष्टकार्याणि : clean
p045:P6 अन्यदेशीयः सः : clean
p045:P7 सम्भ्रान्तः दानेशः : clean
p046:P1 {x-com:layout: : skip x-com-only
p046:P2 वदामि? एतद्विषये : clean
p046:P3 आश्चर्यचकितः अन्यदेशीयः : clean
p046:P4 सा अपि : clean
p046:P5 तदनन्तरं सः : clean
p046:P6 आश्चर्यम् अनुभवन् : clean
p046:P7 एवम् अटनसमये : clean
p046:P8 तत्र कटे : clean
p046:P9 विदेशीयः तान् : clean
p046:P10 तं प्रश्नं : clean
p047:P1 {x-com:layout: : skip x-com-only
p047:P2 विदेशीयः तस्य : clean
p047:P3 तदा तत्रत्या : F13
p047:P4 विदेशीयस्य चिकित्सार्थं : clean
p047:P5 एव कस्यचित् : clean
p047:P6 "एतत् सर्वथा : clean
p047:P7 तदा विदेशीयः : clean
p047:P8 इदानीं ते : clean
p047:P9 (अनुवर्तते) : clean
J1 p041:P5 {wb} -> p041:P6 {pc} (continues) : ok
J2 p041:P8 {pb} -> p042:P2 {pc} (continues) : ok
J3 p042:P5 {pb} -> p042:P6 fresh (clean break) : ok
J4 p042:P9 {pb} -> p043:P2 {pc} (continues) : ok
J5 p043:P4 {pb} -> p043:P5 {pc} (continues) : ok
J6 p043:P8 {pb} -> p044:P2 {pc} (continues) : ok
J7 p044:P4 {pb} -> p044:P5 {pc} (continues) : ok
J8 p044:P6 {pb} -> p045:P2 fresh (clean break) : ok
J9 p045:P2 {pb} -> p045:P3 fresh (clean break) : ok
J10 p045:P7 {pb} -> p046:P2 {pc} (continues) : ok
J11 p046:P5 {pb} -> p046:P6 {pc} (continues) : ok
J12 p046:P10 {pb} -> p047:P2 fresh (clean break) : ok
J13 p047:P4 {pb} -> p047:P5 {pc} (continues) : ok
J14 p047:P9 {pb} -> END (clean break) : ok
