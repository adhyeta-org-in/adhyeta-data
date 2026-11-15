## Summary

Range p002 (scans 2–9: उदारमनस्कता complete on scans 2–6, धैर्यशाली complete on scans 7–9): 19 findings — 1 stray-mark deletion (F1), 16 direct-speech sort normalizations singles-to-doubles (F2–F17), 2 held candidates (F18, F19). Systematic issue: file transcribed several speeches with single quotes where Era print uses doubles (crop-verified doubles in Phase A for most); all pinned speech normalized to doubles via verdicts. Orth scanner (`scan.py orth`) on 80 deblocked lines: 0 hits. No joint ruptures, so no Moves. Two items held for the user (F18, F19); nothing else unverified. Loc below is `pNN:Pm` (scan sequence + chunk per lint `P` numbers) plus the first two words as anchor, with 1-based word counts excluding blocks.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p005:P5 अङ्गुलीयकस्य विक्रयणेन w1 | `अङ्गुलीयकस्य' विक्रयणेन` | `{del:'}` (drop the stray mark) | STY | style | high | lone single with no mate anywhere; inked print defect, no quote function |
| F2 | p003:P5 युवकः दृढकायः w1 | `'युवकः…मास्तु?'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F3 | p003:P6 समूहतः द्वौ w7 | `'एषः…एतस्य` / `मुखतः…आनाययामः'` | `{del:'}{ins:"}…{del:'}{ins:"}` edge-spanning pair | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F4 | p003:P8 तदा युवकः w5 | `'भोः…अत्र'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F5 | p003:P10 तदा युवकः w8 | `'भोः…स्थापितवान्'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F6 | p005:P7 युवकः एतत्सर्वं w7 | `'अनन्तरकाले…आसीत्'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F7 | p005:P9 ज्येष्ठाः एतदर्थम् w1 | `'ज्येष्ठाः…अविचार्य'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F8 | p006:P2 हस्ततः धनस्यूतं w7 | `'अद्य…कारयिष्यामि'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F9 | p006:P3 तदा तस्य w6 | `'सुवर्णहारः…कारयतु'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F10 | p006:P4 सुमतिः पितुः w7 | `'इदानीं…वयः?'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F11 | p006:P5 किमर्थम् इदानीं w1 | `'किमर्थम्…करोति'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F12 | p006:P6 एषः युवकः w1 | `'एषः…तस्य` / `सेवाम्…आगमिष्यामि'` | `{del:'}{ins:"}…{del:'}{ins:"}` edge-spanning pair | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F13 | p006:P8 दशरथः तस्य w18 | `'एतत्…आगच्छाम'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F14 | p006:P9 अद्य देवदर्शनं w1 | `'अद्य…भवेत्'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech with reporting verb + इति takes doubles (print verified double in Phase A) |
| F15 | p007:P3 पूर्वं नारायणपुरे w25 | `'इदानीं किं करणीयम्?'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech (पृष्टवान् + इति) takes doubles though print uses singles |
| F16 | p007:P4 श्रीमन् कृषिकाः w1 | `'श्रीमन्!…अपि'` (outer; inner `'विलम्बेन…नास्ति'` kept) | `{del:'}{ins:"}…{del:'}{ins:"}` outer only | STY | style | high | outer direct speech takes doubles; inner thought keeps singles (proper DQ…SQ…DQ nesting) |
| F17 | p007:P7 सप्ताहात्मके अवधौ w14 | `'दिनत्रयाभ्यन्तरे…भवेत्'` | `{del:'}{ins:"}…{del:'}{ins:"}` | STY | style | high | direct speech (order content + इति) takes doubles though print uses singles |
| F18 | p005:P4 एवं पिपासां w22 | `कृत्वा यममानाय एतत्` | `{sug-del:यममानाय}{sug-ins:यजमानाय}` | OCR | likely | medium* | यममानाय is not a word; father means the householder (यजमान); one-letter print-or-read slip |
| F19 | p006:P7 सेवाम् इदानीं w22 | `भवेत् {x-illegible: possible quote mark}अपि।` | `?` (drop the block as stray, or supply a mate) | STY | likely | low* | single inked stroke mid-speech verified at 6x in Phase A; keeping it crosses the enclosing `"…"` pair, so held |

## Patterns

P1 — speech singles normalized to doubles (16 spots, F2–F17): file carried singles for pinned direct speech; verdicts supply doubles. Example locs: p003:P5 युवकः दृढकायः, p006:P6 एषः युवकः, p007:P4 श्रीमन् कृषिकाः. Inner thought singles kept throughout (`'सः निश्चयेन…'` p004:P4, `'पुनः अपि…'` p005:P4, `'विलम्बेन…'` p007:P4, `'प्रतियामम्…'` p008:P6, `'जीवन्…'` p008:P9).

P2 — print spelling variants kept as house forms, no blocks: कानिचन (p003:P10) vs कानिचन (p003 right column, both crop-verified in Phase A); coin terms रूप्यकाणि / रजतनाणकानि / सुवर्णनाणकानि used synonymously; रायपुरं / रायपुरम् accusative alternation. No verdicts; Chandamama mixes open and joined sandhi.

## Unverified

F18 (`यममानाय` → `यजमानाय`, p005:P4 w22): held as `{sug-del:}{sug-ins:}`. Would settle it: re-examine scan 5 left column (`'पुनः अपि…ददामि'` line) for ज vs म, or dictionary check that यममान- has no stem. Sense strongly favors यजमानाय (give the ring to the householder).

F19 (stray stroke before `अपि`, p006:P7 w22): held as `{x-illegible: possible quote mark}` in file. Verified inked single stroke at 6x in Phase A; a dropped second stroke (`""` re-open) is conceivable but there is no column-edge reason for a re-open, so likely a stray sort. Would settle it: editorial decision — recommended drop (compiler deletes the block token; stroke documented here as print defect).

## Coverage

p002:P1 {x-com:layout: : skip (layout chunk)
p002:P2 उदारमनस्कता : skip (title)
p002:P3 रायपुरग्रामस्य पार्श्वे : clean
p002:P4 दशरथः रायपुरवासी : clean
p002:P5 दशरथः यदा : clean (J1 trailing)
p002:P6 वस्त्रं न : clean (J1)
p002:P7 दशरथः गृहं : clean
p002:P8 भीतिपूर्णं तदीयं : clean
p002:P9 अतः धावन् : clean (J2 trailing)
p002:P10 {author: : skip (footer + page close)
p003:P1 {x-com:layout: : skip (layout chunk)
p003:P2 वदतु अन्यथा : clean (J2)
p003:P3 अकस्मात् प्रवृत्तया : clean
p003:P4 दशरथस्य उच्चध्वनिं : clean
p003:P5 युवकः दृढकायः : F2
p003:P6 समूहतः द्वौ : F3 (J3 trailing)
p003:P7 मुखतः एव : F3 (J3)
p003:P8 तदा युवकः : F4
p003:P9 सुमतिः झटिति : clean
p003:P10 तदा युवकः : F5
p003:P11 सर्वे तं : clean (J4 trailing)
p003:P12 {pgb} : skip (page close)
p004:P1 {x-com:layout: : skip (layout chunk)
p004:P2 आसन् दशरथः : clean (J4)
p004:P3 द्वादशवर्षेभ्यः पूर्वम् : clean
p004:P4 पितुः कश्चन : clean (thought singles kept as seen)
p004:P5 {pgb} : skip (page close)
p005:P1 {x-com:layout: : skip (layout chunk)
p005:P2 सायङ्कालपर्यन्तम् अन्वेषणे : clean (J5)
p005:P3 अनन्योपायः पिता : clean
p005:P4 एवं पिपासां : F18 (thought singles kept as seen)
p005:P5 अङ्गुलीयकस्य विक्रयणेन : F1 (J6 trailing)
p005:P6 पुत्रं नगरं : clean (J6)
p005:P7 युवकः एतत्सर्वं : F6
p005:P8 नमस्कारपूर्वकं सर्वं : clean
p005:P9 ज्येष्ठाः एतदर्थम् : F7
p005:P10 युवकः ततः : clean (J7 trailing)
p005:P11 {pgb} : skip (page close)
p006:P1 {x-com:layout: : skip (layout chunk)
p006:P2 हस्ततः धनस्यूतं : F8 (J7)
p006:P3 तदा तस्य : F9
p006:P4 सुमतिः पितुः : F10
p006:P5 किमर्थम् इदानीं : F11
p006:P6 एषः युवकः : F12 (J8 trailing)
p006:P7 सेवाम् इदानीं : F19 (J8; x-illegible held)
p006:P8 दशरथः तस्य : F13
p006:P9 अद्य देवदर्शनं : F14
p006:P10 अल्पवयस्कायाः अपि : clean (J9 trailing)
p007:P1 {x-com:layout: : skip (layout chunk)
p007:P2 धैर्यशाली : skip (title)
p007:P3 पूर्वं नारायणपुरे : F15
p007:P4 श्रीमन् कृषिकाः : F16 (inner thought singles kept)
p007:P5 नारायणस्वामिनः उपायम् : clean (J10 trailing)
p007:P6 करसङ्ग्रहार्थं प्रस्थितवान् : clean (J10)
p007:P7 सप्ताहात्मके अवधौ : F17
p007:P8 भटाः सङ्गृहीतं : clean
p007:P9 सूर्यास्तसमये ते : clean
p007:P10 ग्रामस्य परिस्थितिं : clean (J11 trailing)
p007:P11 {author: : skip (footer + page close)
p008:P1 {x-com:layout: : skip (layout chunk)
p008:P2 अस्माकं भोजनादीनां : clean (J11)
p008:P3 तदा भटेषु : clean
p008:P4 अस्तु तावत् : clean
p008:P5 भूस्वामिनः गमनानन्तरं : clean
p008:P6 अल्पे एव : clean (J12 trailing; resolve singles kept)
p008:P7 उत्पन्नम् : clean (J12)
p008:P8 त्रयः अपि : clean
p008:P9 भयङ्कराकारस्य एतस्य : clean (proverb singles kept as thought)
p008:P10 गाढनिद्रायां मग्नः : clean (J13 trailing)
p009:P1 {x-com:layout: : skip (layout chunk)
p009:P2 पलायनकारणम् अजानन् : clean (J13)
p009:P3 भीत्या धाविताः : clean
p009:P4 भवन्तः सर्वे : clean
p009:P5 तत्र तैः : clean
p009:P6 भूस्वामी सुन्दरेशस्य : clean
p009:P7 धावनपूर्वकं प्रत्यागतानां : clean (J14 trailing)
p009:P8 सुन्दरेशः गृहं : clean (J14)
p009:P9 धैर्यशाली अस्ति : clean (J15)
p009:P10 मम धैर्यं : clean
p009:P11 एवं वा : clean (J16)
J1 p002:P5 -> p002:P6 : ok (continues)
J2 p002:P9 -> p003:P2 : ok (continues)
J3 p003:P6 -> p003:P7 : ok (continues; F3 edge-spanning pair)
J4 p003:P11 -> p004:P2 : ok (continues)
J5 p004:P4 -> p005:P2 : ok (clean break)
J6 p005:P5 -> p005:P6 : ok (continues; F1 stray deleted at edge)
J7 p005:P10 -> p006:P2 : ok (continues)
J8 p006:P6 -> p006:P7 : ok (continues; F12 edge-spanning pair; F19 held inside P7)
J9 p006:P10 -> p007:P2 : ok (title, clean break)
J10 p007:P5 -> p007:P6 : ok (continues)
J11 p007:P10 -> p008:P2 : ok (continues)
J12 p008:P6 -> p008:P7 : ok (continues)
J13 p008:P10 -> p009:P2 : ok (continues)
J14 p009:P7 -> p009:P8 : ok (continues)
J15 p009:P8 -> p009:P9 : ok (continues, solid wb join एतावद्धैर्यशाली)
J16 p009:P11 -> END : ok (clean break)
