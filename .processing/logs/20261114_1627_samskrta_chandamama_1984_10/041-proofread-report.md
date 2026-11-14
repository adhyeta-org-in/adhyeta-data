# Proofread report — 1984_10 p041 (RUN 20261114_1627_samskrta_chandamama_1984_10)

## Summary

9 findings: 8 STY/style/high (6 supplied `"` marks completing Krishna's multi-paragraph Gita speech so each paragraph opens/closes its own pair, 1 mixed-pair open promoted to double, 1 nested-double pair corrected to singles) plus 3 stray `'` deletions folded into those rows and 1 SPL/error/high (`योगब्रलेन` → `योगबलेन`). Systematic issues are unmarked speech paragraphs (PAT-1) and mate-less single opens verified at 3x+ (PAT-2). `scan.py orth` on deblocked story text gave 0 hits (one informational verse-candidate on the closing Gita-dhyana verse, kept as seen); the flow pass over all 12 joints found no rupture; no passages were left unchecked. Loc below is `pNN:Pm` (NN = scan sequence from filename `p041` plus `{pgb}`-span order; Pm = chunk number in that span, matching lint `P` numbers) plus the chunk's first two words as anchor; corrections travel only as blocks in the story file, never as silent edits.

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p041:P5 «किङ्कर्तव्यतामूढतां गतम्।» | `युक्तः 'धर्मः।` | `युक्तः {del:'}धर्मः।{ins:"}` | STY | style | high | lone single verified at 3x with no mate anywhere in the speech, so stray; the `"हे अर्जुन` span needs its page-local close |
| F2 | p041:P6 «वस्तुतः परमेश्वरः» | `वस्तुतः ... साधनमात्रम्।` | `{ins:"}वस्तुतः ... साधनमात्रम्।{ins:"}` | STY | style | high | unmarked middle paragraph of Krishna's speech; each paragraph opens and closes its own pair |
| F3 | p041:P7 «लोके यदा» + p042:P2 «करोति। भगवतः» | `लोके ... अनुसरतु।` | `{ins:"}लोके ... अनुसरतु।{ins:"}` | STY | style | high | cross-page speech paragraph unmarked on both sides of the `{pb}`/`{pc}` joint |
| F4 | p042:P3 «भवान् श्रद्धया» | `भवान् ... भवतु" इति।` | `{ins:"}भवान् ... भवतु" इति।` | STY | style | high | closing mark present with no open; final paragraph of the speech |
| F5 | p042:P4 «एतादृशम् उपदेशं» | `कृष्णः 'अर्जुनस्य` | `कृष्णः {del:'}अर्जुनस्य` | STY | style | high | stray single in narrative verified at 3x, no mate in any direction |
| F6 | p045:P2 «वन्तः। मदिरापानेन» | `आरब्धवन्तः। 'एतन्निमित्तः` | `आरब्धवन्तः। {del:'}एतन्निमित्तः` | STY | style | high | stray single in narrative verified at 3x, no mate in any direction |
| F7 | p045:P4 «यदुवंशनाशस्य वार्तां» | `{sug-del:योगब्रलेन}{sug-ins:योगबलेन}` | `{del:योगब्रलेन}{ins:योगबलेन}` | SPL | error | high | `ब्र` subscript verified at 4x; `योगब्रल` is no word, `योगबलेन` (by power of yoga) is the only reading |
| F8 | p045:P5 «द्वारकानिर्माणार्थं समुद्रराजेन» | `'भवान् ... नयतु"` | `{del:'}{ins:"}भवान् ... नयतु"` | STY | style | high | single-open/double-close mixed pair verified at 4x; spoken order promotes the open to double |
| F9 | p046:P7 «श्रीकृष्णस्य सारथिः» | `"यादवस्त्रियः सर्वाः नेतव्याः"` | `{del:"}{ins:'}यादवस्त्रियः सर्वाः नेतव्याः{del:"}{ins:'}` | STY | style | high | nested reported order inside the open `भवान्` span takes singles, as the parallel `'नगरं त्यक्तव्यम्'` shows |

## Patterns

PAT-1 unmarked speech paragraphs in Krishna's Gita address (p041–p042): 6 × `{ins:"}` (F1 close, F2 open+close, F3 open+close, F4 open) where speech sense plus sentence boundary pins each position; sorts kept as printed elsewhere (thought kept in print's doubles `राज्यार्थं`, `पुत्रमरणस्य`; singles kept `परीक्षितः`, `अङ्गुष्ठः`, `कलियुगम्`, `नगरं त्यक्तव्यम्`).
PAT-2 mate-less single opens (3 × `{del:'}`: F1, F5, F6), each verified at 3x or tighter with no possible partner in either direction, deleted from text with reason.

## Unverified

None. Every Phase A candidate was settled from text: F7's glyph at 4x with a unique sensible reading, F9's nesting pinned by the outer span plus the parallel inner single pair. Print-mix spellings kept as seen with no block: `बान्धव`, `विश्वामित्रः`/`विश्वामित्रं` (case), `अन्यकणाः` (fragments), `प्रत्यर्पणीया` (feminine gerundive, grammatical), `दैनन्दिनजीवतस्य`, `सन्न्यासिनः`, `परीक्षितवान्`, `अक्रूरं` (verified at 4x), `धृतवान्`.

## Coverage

p041:P3 «श्रीकृष्णः अर्जुनस्य» : clean
p041:P4 «एवं चिन्तयन्» : clean
p041:P5 «किङ्कर्तव्यतामूढतां गतम्।» : F1
p041:P6 «वस्तुतः परमेश्वरः» : F2
p041:P7 «लोके यदा» : F3
p041:P8 «{category: भगवद्गीता}{pgb}» : skip metadata
p042:P2 «करोति। भगवतः» : F3
p042:P3 «भवान् श्रद्धया» : F4
p042:P4 «एतादृशम् उपदेशं» : F5
p042:P5 «भगवतः विश्वरूपे» : clean
p042:P6 «जगतः सृष्टौ,» : clean
p042:P7 «एतत् विश्वरूपं» : clean
p042:P8 «इदानीम् अर्जुनस्य» : clean
p042:P9 «पूर्वं शान्तिदूतरूपेण» : clean
p042:P10 «अभिमन्युरूपेण स्थितः» : clean
p043:P2 «भूदेव्याः उपरि» : clean
p043:P3 «दुर्योधनस्य मरणेन» : clean
p043:P4 «पुत्रशोकेन सन्तप्ता» : clean
p043:P5 «श्रीकृष्णः मन्दहासं» : clean
p043:P6 «पाण्डवानां वंशं» : clean
p043:P7 «निद्रावस्थायां स्थितान्» : clean
p043:P8 «"नरकवाससदृशं जीवनम्» : clean
p043:P9 «श्रीकृष्णस्य वचनानुसारम्» : clean
p043:P10 «शरशय्यायां शयितः» : clean
p044:P2 «उत्तरायणस्य प्रतीक्षायाम्» : clean
p044:P3 «युधिष्ठिरस्य राज्याभिषेकः» : clean
p044:P4 «श्रीकृष्णः यादवप्रमुखाः» : clean
p044:P5 «कदाचित् महर्षिः» : clean
p044:P6 «गर्भिणीवेषं धारितवन्तः।» : clean
p044:P7 «असभ्यचेष्टया कुपितः» : clean
p044:P8 «अनन्तरम् अपि» : clean
p044:P9 «युद्धं समाप्य» : clean
p044:P10 «एवं क्षिप्तम्» : clean
p044:P11 «मुसलस्य अन्यकणाः» : clean
p044:P12 «कानिचन वर्षाणि» : clean
p045:P2 «वन्तः। मदिरापानेन» : F6
p045:P3 «एवं प्रकारेण» : clean
p045:P4 «यदुवंशनाशस्य वार्तां» : F7
p045:P5 «द्वारकानिर्माणार्थं समुद्रराजेन» : F8
p045:P6 «अनन्तरं श्रीकृष्णः» : clean
p045:P7 «यदुकुलं यदा» : clean
p045:P8 «अन्ते श्रीकृष्णः» : clean
p046:P2 «लेपयितुम् आज्ञापितवान्।» : clean
p046:P3 «बाणस्पर्शेन अङ्गुष्ठतः» : clean
p046:P4 «तदा श्रीकृष्णः» : clean
p046:P5 «जन्मनि पूर्वकृतस्य» : clean
p046:P6 «एवं उक्त्वा» : clean
p046:P7 «श्रीकृष्णस्य सारथिः» : F9
p046:P8 «सारथिः अश्रूणि» : clean
p046:P9 «श्रीकृष्णः पुनः» : clean
p046:P10 «श्रीकृष्णस्य मरणसमनन्तरम्» : clean
p046:P11 «कृष्णस्य मरणानन्तरम्» : clean
p047:P2 «कृष्णतत्त्वानां प्रसारं» : clean
p047:P3 «विष्णोः अवतारभूतः» : clean
p047:P4 «दुष्टशिक्षणं, शिष्टपरिपालनम्» : clean
p047:P5 «तथैव लोके» : clean
p047:P6 «कृष्णः मानवरूपधारी» : clean
p047:P7 «तस्य निर्गमनानन्तरम्» : clean
p047:P8 «तपःशक्तिः सर्वथा» : clean
p047:P9 «कृष्णेन अनुगृहीतः» : clean
p047:P10 «मोक्षप्रतिपादकः एषः» : clean
p047:P11 «सर्वोपनिषदः गावः» : clean
J1 p041:P4 {pb} -> p041:P5 {pc} (continues) : ok (मनः + किङ्कर्तव्यतामूढतां, spaced column joint)
J2 p041:P7 {pb} -> p042:P2 {pc} (continues) : F3 (अवतारं + करोति, spaced page joint)
J3 p042:P5 {pb} -> p042:P6 fresh (clean break) : ok (terminal ।, column turn)
J4 p042:P10 {pb} -> p043:P2 {pc} (continues) : ok (तदनुसारं + भूदेव्याः, spaced page joint)
J5 p043:P6 {pb} -> p043:P7 fresh (clean break) : ok (terminal ।, column turn; print order of the two Ashvatthama episodes kept)
J6 p043:P10 {pb} -> p044:P2 {pc} (continues) : ok (भीष्मः + उत्तरायणस्य, spaced page joint)
J7 p044:P5 {pb} -> p044:P6 {pc} (continues) : ok (साम्बेन + गर्भिणीवेषं, spaced column joint)
J8 p044:P12 {wb} -> p045:P2 {pc} (continues) : ok (पीत + वन्तः = पीतवन्तः, solid page joint)
J9 p045:P8 {wb} -> p046:P2 {pc} (continues) : ok (उप + विश्य = उपविश्य, solid page joint)
J10 p046:P4 {pb} -> p046:P5 {pc} (continues) : ok (अस्मिन् + जन्मनि, spaced column joint)
J11 p046:P11 {pb} -> p047:P2 {pc} (continues) : ok (गत्वा + कृष्णतत्त्वानां, spaced page joint)
J12 p047:P11 {pb} -> END (clean break) : ok (verse close ॥, story end)
