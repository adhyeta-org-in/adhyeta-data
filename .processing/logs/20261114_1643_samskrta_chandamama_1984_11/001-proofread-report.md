# Proofread report: 1984_11, p001 (scans 1-4, शम्भुनाथस्य कथा)

## Summary

Range p001 covers scans 1-4 (pp. 1-4 of the issue run): the opening of शम्भुनाथस्य कथा through शम्भुनाथः कमपि उद्दिश्य कथां न उक्तवान्।. Extract gate and proofread gate both pass (exit 0, 0 error paras, 0 story findings); the Sanskrit orth scanner raised one hit (final `!` in समाप्तिरेव न भवति) which is genuine print punctuation, consistent with किल!/तात!/शिवराम!, and was dismissed. Two word-level holds below high glyph confidence (images closed, no Phase A note on file for either, so no verdict blocks): कथाकथनव्यप्रः for व्यग्रः and क्रिडितुम् for क्रीडितुम्. Loc below is `pNN:Pm:word` (word counted on the chunk from 1) with the chunk's first two words as anchor, matching lint chunk numbers.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p001:P4:14 (कदाचित् शम्मुनाथः) | कथाकथनव्यप्रः भवति | कथाकथनव्यग्रः | OCR | likely | medium* | व्यप्रः is not a word; the standard idiom is कथाकथनव्यग्रः (absorbed in narration), व्याप्रः (tiger) discarded as unidiomatic; ग्र/प्र glyph unverified with images closed |
| F2 | p003:P4:6 (शम्मुनाथः बहु) | क्रिडितुम् | क्रीडितुम् | OCR | likely | medium* | root is क्रीड्, spelled क्रीड् five times elsewhere in this file (क्रीडायाम्, क्रीडनार्थम्, क्रीडितुं, क्रीडामि); short-इ glyph unverified with images closed |

## Patterns

- Title-vs-body sort variance (kept as printed, no finding): display title reads शम्भुनाथस्य (unambiguous भ), while all ~15 small-body instances read शम्मु- (verified म्म at 5x on p001:P3 and p002). Systematic within each typeface, so recorded as a house/type variance; body kept print-faithful, no consistency verdict issued against verified glyphs.
- Print single-quote sorts kept as seen (3 passages, no finding): 'आगच्छतु, कथां शृणोतु' (p001:P3, urging speech), 'समाप्तिपर्यन्तं कथां शृणोमि' (p002:P7, interior resolve), 'पितामहः मिलितः चेत् कष्टम्' (p004:P9, thought via चिन्तयन्). All pairs balance; per the 1984_04 proofread precedent (speech-with-singles kept), sorts stand and no marks were supplied — every speech in the range already carries both marks, including the page-turn continuations.

## Unverified

- F1 कथाकथनव्यप्रः/व्यग्रः: linguistic evidence strongly favors व्यग्रः, but the ग्र/प्र conjunct was never verified on scan (no Phase A note); reopening scan 1 at 3x+ on यदा कथाकथनव्यप्रः भवति would settle accept vs drop.
- F2 क्रिडितुम्/क्रीडितुम्: क्रीड् is certain from five same-file instances, but the ह्रस्व/दीर्घ-i glyph was never verified on scan; reopening scan 3 at 3x+ on शिवरामाय क्रिडितुम् would settle accept vs drop.

## Coverage

- p001:P1 {x-com:layout:} : skip layout-only chunk
- p001:P2 # शम्भुनाथस्य : skip title heading
- p001:P3 कथाकथने शम्मुनाथस्य : clean
- p001:P4 कदाचित् शम्मुनाथः : F1
- p001:P5 कथासु रुचिम् : clean
- p001:P6 "शिवरामः किमर्थं : clean
- p001:P7 {pc}बहुधा चिन्तितवान्। : clean
- p001:P8 ज्येष्ठानां तु : clean
- p001:P9 तदा शम्मुनाथः : clean
- p001:P10 एतदनन्तरं सः : clean
- p001:P11 {misc:} : skip footer metadata, deblocks empty
- p002:P1 {x-com:layout:} : skip layout-only chunk
- p002:P2 {pc}तदा तत्र : clean
- p002:P3 वस्तुतः ज्येष्ठाः : clean
- p002:P4 एवम् एव : clean
- p002:P5 {pc}दातव्यः" : clean
- p002:P6 शम्मुनाथः यद्यपि : clean
- p002:P7 कदाचित् शम्मुनाथः : clean
- p002:P8 तेषु एव : clean
- p002:P9 एकदा नवीनः : clean
- p002:P10 तदा शिवरामः : clean
- p002:P11 बालकः उत्साहेन : clean
- p002:P12 "तर्हि भवान् : clean
- p003:P1 {x-com:layout:} : skip layout-only chunk
- p003:P2 "युक्ता आलोचना : clean
- p003:P3 अनन्तरदिने शिवरामः : clean
- p003:P4 शम्मुनाथः बहु : F2
- p003:P5 तस्यां कथायां : clean
- p003:P6 एतां कथां : clean
- p003:P7 "अपहरतु नाम, : clean
- p003:P8 बालकः उक्तवान् : clean
- p003:P9 {pc}अवश्यं तत्र : clean
- p003:P10 एतं प्रश्नं : clean
- p003:P11 तदा सः : clean
- p004:P1 {x-com:layout:} : skip layout-only chunk
- p004:P2 {pc}वा? प्रायः : clean
- p004:P3 "आम्, आम्" : clean
- p004:P4 एवं कथाम् : clean
- p004:P5 तदा बालकः : clean
- p004:P6 शम्मुनाथः दीर्घं : clean
- p004:P7 बालकः जलम् : clean
- p004:P8 {pc}यन् वृद्धः : clean
- p004:P9 शिवरामः एतं : clean
- p004:P10 दीर्घं निश्वसन् : clean
- p004:P11 एतेन शिवरामः : clean
- p004:P12 एतदनन्तरं शम्मुनाथः : clean
- J1 p001:P3 {pb} -> p001:P4 fresh (clean break) : ok
- J2 p001:P4 {pb} -> p001:P5 fresh (clean break) : ok
- J3 p001:P5 {pb} -> p001:P6 fresh (clean break) : ok
- J4 p001:P6 {pb} -> p001:P7 {pc} (continues) : ok
- J5 p001:P7 {pb} -> p001:P8 fresh (clean break) : ok
- J6 p001:P8 {pb} -> p001:P9 fresh (clean break) : ok
- J7 p001:P9 {pb} -> p001:P10 fresh (clean break) : ok
- J8 p001:P10 {pb} -> p002:P2 {pc} (continues) : ok
- J9 p002:P2 {pb} -> p002:P3 fresh (clean break) : ok
- J10 p002:P3 {pb} -> p002:P4 fresh (clean break) : ok
- J11 p002:P4 {pb} -> p002:P5 {pc} (continues) : ok
- J12 p002:P5 {pb} -> p002:P6 fresh (clean break) : ok
- J13 p002:P6 {pb} -> p002:P7 fresh (clean break) : ok
- J14 p002:P7 {pb} -> p002:P8 fresh (clean break) : ok
- J15 p002:P8 {pb} -> p002:P9 fresh (clean break) : ok
- J16 p002:P9 {pb} -> p002:P10 fresh (clean break) : ok
- J17 p002:P10 {pb} -> p002:P11 fresh (clean break) : ok
- J18 p002:P11 {pb} -> p002:P12 fresh (clean break) : ok
- J19 p002:P12 {pb} -> p003:P2 fresh (clean break) : ok
- J20 p003:P2 {pb} -> p003:P3 fresh (clean break) : ok
- J21 p003:P3 {pb} -> p003:P4 fresh (clean break) : ok
- J22 p003:P4 {pb} -> p003:P5 fresh (clean break) : ok
- J23 p003:P5 {pb} -> p003:P6 fresh (clean break) : ok
- J24 p003:P6 {pb} -> p003:P7 fresh (clean break) : ok
- J25 p003:P7 {pb} -> p003:P8 fresh (clean break) : ok
- J26 p003:P8 {pb} -> p003:P9 {pc} (continues) : ok
- J27 p003:P9 {pb} -> p003:P10 fresh (clean break) : ok
- J28 p003:P10 {pb} -> p003:P11 fresh (clean break) : ok
- J29 p003:P11 {pb} -> p004:P2 {pc} (continues) : ok
- J30 p004:P2 {pb} -> p004:P3 fresh (clean break) : ok
- J31 p004:P3 {pb} -> p004:P4 fresh (clean break) : ok
- J32 p004:P4 {pb} -> p004:P5 fresh (clean break) : ok
- J33 p004:P5 {pb} -> p004:P6 fresh (clean break) : ok
- J34 p004:P6 {pb} -> p004:P7 fresh (clean break) : ok
- J35 p004:P7 {wb} -> p004:P8 {pc} (continues) : ok
- J36 p004:P8 {pb} -> p004:P9 fresh (clean break) : ok
- J37 p004:P9 {pb} -> p004:P10 fresh (clean break) : ok
- J38 p004:P10 {pb} -> p004:P11 fresh (clean break) : ok
- J39 p004:P11 {pb} -> p004:P12 fresh (clean break) : ok
- J40 p004:P12 {pb} -> END (clean break) : ok
