# Proofread report: 1986_11 p024 (scans 24–25, तीर्थयात्रा)

## Summary

Range p024 (2 spans, scans 24–25) transcribes a complete pilgrimage-gem episode: Keśava and Śyāmalā's vow, the hidden gem, and Śyāmalā's rebuke that pilgrimage needs clay-like indifference to jewels. One held style candidate (F1), `style` / `medium` / `unverified*`: a full stop where the surrounding list uses commas. No systematic problem, no unchecked passage (every chunk read sentence by sentence for continuity), and the text is hand transcription, not OCR. Orth scan (`scan.py orth`) gives one `low` hit (the same full stop), reviewed and held; `lint --phase proofread` exits 0. `Loc` is `pNN:Pm` plus the chunk's first two words, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p024:P4 रामशर्मा समीचीनं w26 | `गृहं. क्षेत्रं` | `गृहं, क्षेत्रं` | STY | style | medium* | Period breaks a comma-list governed by one `चिन्तनं विना` |

## Unverified

F1 held: the dot is clearly printed (Phase A 2x crop), so the glyph is settled and only the intent is open; list logic favours a comma but a cleaner print would settle it. Considered and kept without a block: `तत्र तदा तदा लभ्यन्ते` read as distributive āmreḍita (`from time to time`), and visarga kept before voiced consonants throughout as the edition's unjoined house style.

## Coverage

p024:P1 layout-only : skip x-com-only
p024:P2 title : skip title
p024:P3 देवावरनामके ग्रामे : clean
p024:P4 रामशर्मा समीचीनं : F1
p024:P5 निश्चिते दिने : clean
p024:P6 पुण्यक्षेत्राणां दर्शनं : clean
p024:P7 नद्याः पार्श्वे : clean
p024:P8 तस्य आगमनसमये : clean
p024:P9 इदानीं किं : clean
p024:P10 misc-only : skip metadata
p025:P1 layout-only : skip x-com-only
p025:P2 चिन्तितवान् सः : clean
p025:P3 एवं चिन्तयित्वा : clean
p025:P4 तस्याः जागरणानन्तरं : clean
p025:P5 मार्गे केशवः : clean
p025:P6 दृष्टवान् वा? : clean
p025:P7 सः संशयदृष्ट्या : clean
p025:P8 सः मणिः : clean
p025:P9 तादृशी इच्छा : clean
p025:P10 तस्याः वचनं : clean
J1 p024:P5 {pb} -> p024:P6 {pc} (continues) : ok
J2 p024:P9 {pb} -> p025:P2 {pc} (continues) : ok
J3 p025:P6 {pb} -> p025:P7 fresh (clean break) : ok
J4 p025:P10 {pb} -> END (clean break) : ok
