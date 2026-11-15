## Summary

Single-page story `अन्धकासुरः` (one scan, 9 chunks, 6 body paragraphs, one joint). Two findings, both `STY` punctuation at `style` severity and high confidence: a stray print single-quote deleted in each of two adjacent paragraphs (`{del:'}` verdicts in the story file). Scanner `orth` run on deblocked text reports no hits. No passage was left unchecked; the text is a manual transcription, not OCR output. Loc counts deblocked words on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| F1 | p001:P6 मन्दारपर्वते अलौकिकगन्धयुक्तानि :9 | `मालां 'धृत्वा` | `मालां धृत्वा` | STY | style | high | lone single opens plain narration with no mate, no reporting verb and no `इति`; glyph verified present in Phase A (4x crop), functionless in print |
| F2 | p001:P7 पुष्पाणां अलौकिकसुगन्धेन :4 | `'अन्धकः --- "एतानि` | `अन्धकः --- "एतानि` | STY | style | high | surplus single before a speaker label where `---` already introduces direct speech (house parallel `पृष्टवान् एव --- "किमर्थं धावति?" इति`); Phase A `{sug-ins:'}` dropped as superseded since no doubled single is involved |

## Patterns

- Stray single-quote marks in narration/speaker-label position, 2x: F1 (p001:P6), F2 (p001:P7). Both compositor slips in adjacent paragraphs; each deleted via `{del:'}` rather than completed, since supplying mates would invent quotations around non-speech.

## Unverified

None held; both Phase A candidates were routed to verdicts above.

## Coverage

p001:P1 {x-com:layout: : skip (layout declaration, transparent to pairing)
p001:P2 {category: पुराणगाथावली} : skip (metadata)
p001:P3 # अन्धकासुरः : skip (title)
p001:P4 अन्धकः नाम : clean
p001:P5 गर्वातिशयेन अन्धकः : clean
p001:P6 मन्दारपर्वते अलौकिकगन्धयुक्तानि : F1
p001:P7 पुष्पाणां अलौकिकसुगन्धेन : F2
p001:P8 "मन्दारपर्वते यथेष्टं : clean
p001:P9 अन्धकः मदोन्मत्तः : clean
J1 p001:P9 {pb} -> END (clean break) : ok (story complete: asura dies at the mountain foot; terminal punctuation, fresh end)
