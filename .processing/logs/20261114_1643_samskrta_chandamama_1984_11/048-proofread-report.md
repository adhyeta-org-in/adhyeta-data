# Proofread report: 1984_11 p048 (सेवकपरीक्षा, pp. 48-49)

## Summary

Five findings, all high confidence: four supplied double-quote mates (F1-F4, STY/style) where the print opens a speech once and closes it once across two paragraphs, and one deleted stray single stroke (F5, STY/error) with no grammatical role. The systematic issue is the print's multi-para speech punctuation (Amaranatha's and Dhanagupta's long speeches); per-para mates were supplied via `{ins:"}` for modern readability. The `orth` scan on deblocked text (21 lines) returned zero hits. Print spellings verified at 2x-4x in Phase A stand as seen (कदांचित् with anusvara, चतुर्वारं, स्नेहितः, धनस्यूतम्, वञ्चितः, प्रसङ्गः); the detached speck after रात्रिः (p48) was omitted as print noise with an `{x-com:}` on file. No held candidates. `Loc` below is story coordinates `pNN:Pm` plus the first two words as anchor, words counted on the chunk from 1.

## Findings

| # | Loc | Original | Suggestion | Cat | Sev | Conf | Why |
|---|---|---|---|---|---|---|---|
| 1 | p49:P2 (गिरिनाथस्य वचनं) w21 | `चौर्यं न जातम्।` (speech opens `"गिरिनाथस्य`, no close) | `चौर्यं न जातम्।{ins:"}` | STY | style | high | print spans one speech over two paras; each para closes its own pair |
| 2 | p49:P3 (आहारविषये अपि) w1 | `आहारविषये अपि तथैव।` (no open; speech closes `नयतु"`) | `{ins:"}आहारविषये अपि तथैव।` | STY | style | high | same speech as F1; each para opens its own pair |
| 3 | p49:P7 (एतत् श्रुत्वा) w20 | `अतः एवं पृच्छति।` (speech opens `"अहम्`, no close) | `अतः एवं पृच्छति।{ins:"}` | STY | style | high | print spans Dhanagupta's reply over two paras; each para closes its own pair |
| 4 | p49:P8 (भवान् चतुर्वारं) w1 | `भवान् चतुर्वारं वीरेन्द्रपुरं गतवान्।` (no open; speech closes `अपेक्षितः"`) | `{ins:"}भवान् चतुर्वारं वीरेन्द्रपुरं गतवान्।` | STY | style | high | same speech as F3; each para opens its own pair |
| 5 | p49:P9 (एतेन गिरिनाथः) w2 | `गिरिनाथः ' ज्ञातवान्` (isolated single stroke, 3x-verified in Phase A) | `गिरिनाथः{del:'} ज्ञातवान्` | STY | error | high | stray stroke mid-sentence with no quote function; genuine quote opens later at `यत् --- "अमर` |

## Patterns

Multi-para speech single open/close in print, per-para mates supplied: 4 cases (F1-F4), i.e. Amaranatha's testimony (p49:P2-P3) and Dhanagupta's verdict (p49:P7-P8). The page-turn pair (p48:P11 to p49:P2) and the column-turn pair (p49:P5 to p49:P6) were left open across the joint per the page/column-turn exception and needed no verdict.

## Unverified

None held. Every Phase A residual was dispositioned: the four unbalanced-print-quote notes via F1-F4, the `sq=1` note via F5, and the रात्रिः speck as omitted print noise (x-com on file).

## Coverage

p48:P1 {x-com:layout} : skip x-com-only chunk
p48:P2 सेवकपरीक्षा : skip title chunk
p48:P3 धनगुप्तः नाम : clean
p48:P4 एतां वार्तां : clean
p48:P5 उभौ अपि : clean
p48:P6 एवं कथनसमये : clean
p48:P7 महाशय वीरेन्द्रपुरे : clean
p48:P8 तदा धनगुप्तः : clean
p48:P9 तत्र वसतिगृहेषु : clean
p48:P10 एतदनन्तरं धनगुप्तः : clean
p48:P11 तदा अमरनाथः : clean
p48:P12 {misc} : skip metadata chunk
p49:P1 {x-com:layout} : skip x-com-only chunk
p49:P2 गिरिनाथस्य वचनं : F1
p49:P3 आहारविषये अपि : F2
p49:P4 धनगुप्तः प्रसन्नतां : clean
p49:P5 तदा गिरिनाथः : clean
p49:P6 इति : clean
p49:P7 एतत् श्रुत्वा : F3
p49:P8 भवान् चतुर्वारं : F4
p49:P9 एतेन गिरिनाथः : F5
J1 p048:P6 {pb} -> p048:P7 {pc} (continues) : ok
J2 p048:P11 {pb} -> p049:P2 {pc} (continues) : ok
J3 p049:P5 {pb} -> p049:P6 {pc} (continues) : ok
J4 p049:P9 {pb} -> END (clean break) : ok
