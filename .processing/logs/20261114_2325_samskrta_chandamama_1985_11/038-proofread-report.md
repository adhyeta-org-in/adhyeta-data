## Summary

Six findings: two errors, one likely, three style. The three proofread-gate unbalanced-quote notes all resolve inside narration punctuation: two stray print singles deleted (F1, F2) and one missing reported-content open supplied (F3); all five pages now lint-clean at exit 0. Two low-text-certainty words travel as held `{del:}/{sug-ins:}` pairs for the user (F4, F5) and one agreement slip is kept as seen without a block (F6). The inherited `{sug-}` queue was empty (no Phase A candidates on file); the `orth` scanner run on deblocked text reports no hits. No passage was left unchecked; the text is a manual transcription, not OCR output. Loc uses story coordinates `pNN:Pm` (lint chunk numbers) with the word index in the chunk plus anchor words; no corrected-text section (corrections travel as blocks).

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p038:P4 "एतद्विषये अहम् :7 | `इति 'आश्वासनं दत्तवान्` | `इति आश्वासनं दत्तवान्` | STY | style | high | lone single opens plain narration with no mate, no reporting verb and no `इति`; supplying a mate would invent a quotation around non-speech, so deleted via `{del:'}` |
| F2 | p039:P5 "तथास्तु" इति :17 | `यदा ज्ञातं' तदा` | `यदा ज्ञातं तदा` | STY | style | high | lone single closes nothing in narration (यदा...तदा clause; the `"तथास्तु"` pair is already complete); deleted via `{del:'}` |
| F3 | p042:P5 अनन्योपायः शिवः span-before-w15 | `आसीत् यत् उभाभ्याम् ... भविष्यति' इति` | `आसीत् यत् 'उभाभ्याम् ... भविष्यति' इति` | STY | style | high | यत्...इति closure pins the race rule as reported content; single open supplied via `{ins:'}` to match print's close (house parallel `'...' इति` at p039:P7 and p041:P4) |
| F4 | p038:P5 ब्रह्मविष्णुप्रभृतयः देवाः :3 | `देवाः तद्रणीयाः च` | `देवाः तद्गणीयाः च` | SPL | error | medium* | तद्रणीयाः parses as nothing (रणीय is unattested); तद्गणीयाः fits the troop-member sense and house गणीयाः usage with a single-glyph change; held as `{del:}/{sug-ins:}` pair |
| F5 | p042:P2 आसीत्। अत्रान्तरे :10 | `"ष्ण्मुख! अहं` | `"षण्मुख! अहं` | CNS | error | high* | ष्ण्मुख is no case form of the name; षण्मुख stands 6x elsewhere in this story; held as `{del:}/{sug-ins:}` pair since print-vs-transcription is unsettleable with images closed |
| F6 | p041:P4 'भवतः शिरः :37 | `कबन्धः च आगतं तदा` | `कबन्धः च आगते तदा` | AGR | likely | low* | dual subjects (शिरः कबन्धः च) with a singular participle; proximity agreement would give आगतः, the strict rule आगते; kept as seen, no block |

## Patterns

- Stray single-quote marks in narration (count 2: F1, F2): each a lone `'` with no quotable span, deleted via `{del:'}` rather than completed, since supplying mates would invent quotations around non-speech (same ruling as run report 001 F1/F2).

## Unverified

- F4 तद्रणीयाः: print re-check at 3x or tighter (र vs ग); wider-window alternatives (तद्गणाः, तदनुचराः) need story-context judgment; user acceptance of the held pair settles it.
- F5 ष्ण्मुख: story consistency (षण्मुख x6 in this range) already settles the reading; a print re-check of halant placement would confirm print-vs-transcription; user acceptance of the held pair settles it.
- F6 आगतं: print re-check (आगतं vs आगते, ं vs े) plus native-speaker judgment on singular-with-dual-subjects license; kept as seen either way unless print shows आगते.

## Coverage

p038:P1 skip (x-com) / p038:P2 skip (title) / p038:P3 पार्वती विष्णुसमीपं : clean / p038:P4 "एतद्विषये अहम् : F1 / p038:P5 ब्रह्मविष्णुप्रभृतयः देवाः : F4 / p038:P6 अन्ये जनाः : clean / p038:P7 गजासुरः श्रुतवान् : clean / p038:P8 शिवलिङ्गस्य वर्धनेन : clean / p038:P9 skip (note footer)
p039:P1 skip (x-com) / p039:P2 {pc}समीपम् आगतम् : clean / p039:P3 "गजासुर! भवतः : clean / p039:P4 "परमेश्वर! मम : clean / p039:P5 "तथास्तु" इति : F2 / p039:P6 {pc}तान् सर्वान् : clean / p039:P7 'गजासुरस्य संहारं : clean / p039:P8 पार्वती तु : clean / p039:P9 पार्वत्या नियुक्ताः : clean / p039:P10 "वयं तु : clean
p040:P1 skip (x-com) / p040:P2 {pc}भवनस्य अन्तः : clean / p040:P3 कोलाहलं श्रुत्वा : clean / p040:P4 रुद्रगणीयानां व्यवहारेण : clean / p040:P5 ते विनायासं : clean / p040:P6 पराजिताः रुद्रगणीयाः : clean / p040:P7 शिवः तु : clean / p040:P8 पार्वत्याः भवनस्य : clean / p040:P9 पत्न्याः दुःखं : clean / p040:P10 परिस्थितेः विषमतां : clean
p041:P1 skip (x-com) / p041:P2 {pc}समीपम् आगतवान् : clean / p041:P3 पार्वती विष्णुम् : clean / p041:P4 'भवतः शिरः : F6 / p041:P5 सर्वत्र हर्षस्य : clean / p041:P6 {pc}अन्याः पुत्र्यः : clean / p041:P7 विश्वदर्शिनः प्रस्तावं : clean / p041:P8 विवाहकार्यं यदा : clean / p041:P9 शिवः पार्वत्याः : clean
p042:P1 skip (x-com) / p042:P2 आसीत्। अत्रान्तरे : F5 / p042:P3 "कुमार! इदानीं : clean / p042:P4 किन्तु षण्मुखः : clean / p042:P5 अनन्योपायः शिवः : F3 / p042:P6 {pc}अधिपतिः भविष्यति' : F3 (print close side) / p042:P7 शिवः षण्मुखाय : clean / p042:P8 लक्ष्मीगणपतिः तु : clean / p042:P9 "वत्स! भवान् : clean

J1 p038:P5 {pb} -> p038:P6 fresh (clean break) : ok (fresh paragraph अन्ये जनाः, subject shifts to the disguised party) / J2 p038:P8 {pb} -> p039:P2 {pc} (continues) : ok (यत् मरणं | समीपम् आगतम् इति completes across the column turn) / J3 p039:P5 {pb} -> p039:P6 {pc} (continues) : ok (किन्तु विष्णुः | तान् सर्वान्... object follows; F2 verdict sits inside P5, seam unaffected) / J4 p039:P10 {pb} -> p040:P2 {pc} (continues) : ok (एवं स्थिते | भवनस्य...के? question completes; dq 1+1 pair) / J5 p040:P4 {pb} -> p040:P5 fresh (clean break) : ok (fresh sentence ते विनायासं... with pronoun subject) / J6 p040:P10 {pb} -> p041:P2 {pc} (continues) : ok (पार्वत्याः | समीपम् आगतवान् genitive plus noun across the page turn) / J7 p041:P5 {pb} -> p041:P6 {pc} (continues) : ok (इच्छामि। | अन्याः पुत्र्यः... speech continues; dq 1+1 pair) / J8 p041:P9 {pb} -> p042:P2 {pc} (continues) : ok (चिन्तयन् | आसीत् participle plus auxiliary across the page turn) / J9 p042:P5 {pb} -> p042:P6 {pc} (continues) : ok (गणानाम् | अधिपतिः भविष्यति' इति completes; F3 open in P5 pairs with print close in P6) / J10 p042:P9 {pb} -> END (clean break) : ok (terminal इति।, counsel given, story complete)

Gate-note dispositions: the 3 STORY unbalanced-quotes notes (p038:P4, p039:P5->P6, p042:P5->P6) are promoted to F1, F2, F3 verdicts above; final `--phase proofread` run reports 5 pages clean, 0 story findings, exit 0. No Moves proposed (sentence-by-sentence continuity read found no rupture at any seam).
