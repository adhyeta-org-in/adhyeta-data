# Proofread report: 1986_01 p007 (सम्माननयोग्यता, scan pages 7-9)

## Summary

Two findings on this three-page span, which holds the complete story: one dropped visarga promoted from the Phase A candidate (`उद्युक्त` for `उद्युक्तः`) and one supplied close quote in the king's two-part announcement (print's double-open/double-open/single-close resolved as close-plus-reopen at the dash). No repeats, so no Patterns section. Every body chunk was read sentence by sentence for continuity; the orth scanner reported no hits on deblocked text. Loc below is story coordinates pNN:Pm plus anchor words, counting words on the chunk from 1. All six joints are text-continuous with unique grammatical fit, so no rupture moves are proposed.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p008:P7 w4 (गङ्गाधरमिश्रः किमपि) `वक्तुम् उद्युक्त।` | `वक्तुम् उद्युक्तः।` | OCR | error | high | masculine nominative singular predicate with `गङ्गाधरमिश्रः` needs the visarga; Phase A verified its absence at 3x |
| 2 | p008:P3 w15 (माणिक्यवर्मा मन्दहासं) `निवेदयामि --- "विरिञ्चि` | `निवेदयामि" --- "विरिञ्चि` | STY | style | high | print opens twice and closes once; the `---` after `निवेदयामि` is a genuine close-plus-reopen into the announced content, so the first speech takes its close there |

Filed as blocks in the story file: `उद्युक्त{ins:ः}` and `निवेदयामि{ins:"}`. Kept as print: the balanced thought-singles in `'कः महाराजेन सम्मान्यते?'` (explicitly unspoken `विचारः`, closed with its own mark), the nested singles in `'मम सम्माननं किमर्थम्'` inside doubles, the `सुवर्णकुन्तलस्य`/`स्वर्णकुन्तल` spelling mix, all open-sandhi/house spellings (e.g. `तस्य आस्थाने`, `मम सम्माननं` unjoined), the print comma in `किमर्थं न, कृतम्`, and the respectful third-person `न चिन्तयतु` and `मास्तु` (मा + अस्तु) as grammatical in context.

## Unverified

None. No held candidates; both rulings are high confidence from text, house pattern, and story context, and the inherited `{sug-ins:ः}` queue is empty.

## Coverage

p007:P1 {x-com:layout:} : skip (layout chunk)
p007:P2 सम्माननयोग्यता : skip (title)
p007:P3 पूर्वं कर्पूरदेशं : clean
p007:P4 एकदा माणिक्यवर्मा : clean
p007:P5 एतदनन्तरं कदाचित् : clean
p007:P6 {pc}दूतद्वारा एतां : clean
p007:P7 "एतत् न : clean
p007:P8 "महाराजः यं : clean
p007:P9 एतां वार्तां : clean
p007:P10 {author:} : skip (metadata)
p008:P1 {x-com:layout:} : skip (layout chunk)
p008:P2 {pc}"भवतः जन्मदिनोत्सवसन्दर्भे : clean
p008:P3 माणिक्यवर्मा मन्दहासं : F2
p008:P4 गङ्गाधरमिश्रः क्षणकालं : clean
p008:P5 तदा माणिक्यवर्मा : clean
p008:P6 {pc}चिन्तितवान् अहम्। : clean
p008:P7 गङ्गाधरमिश्रः किमपि : F1
p008:P8 तदा गङ्गाधरमिश्रः : clean
p008:P9 माणिक्यवर्मा किमपि : clean
p009:P1 {x-com:layout:} : skip (layout chunk)
p009:P2 {pc}पृष्टवान् च : clean
p009:P3 महाराजस्य प्रश्नेन : clean
p009:P4 तदा आश्चर्यं : clean
p009:P5 स्वर्णकुन्तलः शान्तस्वरेण : clean
p009:P6 {pc}अपरिचितः च। : clean
p009:P7 तदा गङ्गाधरमिश्रः : clean
p009:P8 गङ्गाधरमिश्रस्य वचनेन : clean
p009:P9 स्वजन्मदिनोत्सवदिने : clean
J1 p007:P5 {pb} -> p007:P6 {pc} (continues) : ok (राजा + दूतद्वारा subject + instrumental, single fit)
J2 p007:P9 {pb} -> p008:P2 {pc} (continues) : ok (--- introduces the court speech; {pc} holds the opening mate)
J3 p008:P5 {pb} -> p008:P6 {pc} (continues) : ok (इति + चिन्तितवान् iti-clause + verb, single fit)
J4 p008:P9 {pb} -> p009:P2 {pc} (continues) : ok (स्वर्णकुन्तलम् + पृष्टवान् accusative + verb across the page turn, single fit)
J5 p009:P5 {pb} -> p009:P6 {pc} (continues) : ok (same speech continues past the sentence boundary; fragment अपरिचितः च। cannot open a fresh para)
J6 p009:P9 {pb} -> END (clean break) : ok (double honour closes the story arc)
