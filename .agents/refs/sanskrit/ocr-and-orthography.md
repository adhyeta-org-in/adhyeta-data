# OCR artifacts and orthography

Read this after running `.agents/tools/sanskrit/scan.py orth`. The scanner catches character-level defects. This file covers what it cannot: confusable letters, dropped signs, and spelling rules that are mechanical enough to check by eye.

## Contents

- Confusable Devanagari letters (OCR hypotheses)
- Dropped or damaged signs
- Punctuation
- Legitimate orthographic variation (do not flag these as errors)
- Mechanical spelling rules worth checking
- Consistency checks

## Confusable Devanagari letters

These are the substitutions that scanned or low-resolution Devanagari most often produces. Treat each as a hypothesis: the word is wrong *and* the swapped letter yields a better word. If both readings are valid words, check which one the sentence needs.

| Printed | Often misread as | Notes |
|---|---|---|
| ब | व | `बनम्` / `वनम्` |
| भ | म | `भम` / `मम` |
| घ | ध | `घन` / `धन` |
| ट | ठ | |
| ड | ढ | also `ड` ↔ `ङ` |
| त | न | worst in blurred scans: `तर` / `नर` |
| प | ष | `पर` / `षर` |
| च | व | |
| ज | ञ | `ज` ↔ `ञ` when the headline is faint |
| ख | रव | one glyph read as two; `सुरव` for `सुख` |
| क्ष, ज्ञ, त्र, श्र | split into pieces | `क्ष` read as `क + ष`; check each conjunct |
| ि / ी | each other | length of i, so `पति` / `पती` |
| ु / ू | each other | |
| े / ै, ो / ौ | each other | |
| ृ | ु or र | |

## Dropped or damaged signs

The most common OCR damage is a small sign vanishing, which produces a word that looks plausible:

- **Halant (्) dropped**: `तत` for `तत्`, `जगत` for `जगत्`, `विद्वान` for `विद्वान्`. A Sanskrit word ending in a bare consonant letter with inherent `a` is often damaged when the final consonant should be bare. Check every word-final consonant letter for whether the stem really ends in `-a`.
- **Anusvāra (ं) dropped**: `वन गच्छति` for `वनं गच्छति`. Look for accusatives, neuter nominatives and first-person verb forms (`गच्छामि`) with missing final `ं` or `म्`.
- **Visarga (ः) dropped or turned into a colon**: `रामः` / `राम` / `राम:`. The scanner finds colons. Missing visarga is only detectable by grammar: a masculine nominative singular subject ending in bare `-a` is damaged unless the next word begins with a vowel (`राम इति` is correct, since visarga drops there) or sandhi turned it into `-o` (`रामो गच्छति`).
- **Avagraha (ऽ) dropped**: `सोऽपि` printed as `सोपि`, `तेऽपि` as `तेपि`. Forms such as `सोपि` or `तेपि` are damaged readings of `सोऽपि` and `तेऽपि`.
- **Repha (र्) dropped or misplaced**: `धर्म` / `धम`, `कर्म` / `कम`. Repha sits above the *following* consonant; misplacement produces `कर्म` read as `कमर्`.
- **Repha and matra combinations treated as some other matra**: `स्पर्धते` read as `स्पधति`
- **Danda, double danda**: see Punctuation.

## Punctuation

- `।` ends a sentence and `॥` ends a verse (with the verse number in Devanagari digits, such as `॥ ३ ॥`).
- OCR turns `।` into `|`, `I`, `l`, `1` or `!`, and `॥` into `||`. The scanner catches these.
- Mid-sentence dandas are not an error in verse, but in prose they are an editorial choice (a Chandamama sentence normally ends with a single danda, sometimes with a paragraph break after it).
- A comma, full stop or Western quotation marks in a Devanagari text is a typesetting choice: flag as `STY` only if inconsistent within the text.

## Legitimate orthographic variation

Do not report these as errors. If the text is inconsistent, report one `CNS` finding.

- **Anusvāra versus homorganic nasal** within a word: `गङ्गा` and `गंगा` are both valid. The same holds for `अङ्क` and `अंक`, `सम्पूर्ण` and `संपूर्ण`.
- **Word-final `म्` versus `ं`** before a pause or a consonant: `वनम्` and `वनं` are both fine.
- **`ऽ`** for the avagraha, and its omission in editions that do not print it (rare in Sanskrit, common in Hindi-influenced printing).
- **Spaces versus sandhi**: some editions print a space where sandhi applies (`रामः अपि`). Judge consistency and match the edition's convention.
- **`ऋ` versus `रि`** in anglicised Devanagari such as `ऋषि` / `रिषि`: the second is wrong in Sanskrit.

## Mechanical spelling rules

These are rules where a violation is almost certainly an error, and where you can state the rule.

- **Natva (n becomes ṇ)**: after `ऋ`, `र` or `ष` within the same word, a following dental `न` becomes `ण` unless something intervenes. So `रामेण`, `वृक्षेण`, `पुरुषाणाम्`, `नराणाम्`, never `रामेन`, `वृक्षेन`, `नरानाम्`. The instrumental `-ेन`, genitive plural `-ानाम्` and locative `-ेषु` are the places that go wrong.
- **Ṣatva (s becomes ṣ)**: the locative plural ends in `-षु` after `इ`, `उ`, `ए`, `ओ`, `ऋ` and similar: `रामेषु`, `फलेषु`, `वृक्षेषु`, `कविषु`. A form such as `रामेसु` is a Prakrit-ism.
- **Pausal finals**: a sentence-final or verse-final word may end only in a vowel, `क्`, `ट्`, `त्`, `प्`, `ङ्`, `ण्`, `न्`, `म्`, `ं` or `ः`. A word ending in bare `च्`, `ज्`, `द्`, `ब्`, `ग्` or `ह्` at a pause is damaged (`वाच्` should be `वाक्`).
- **`श / ष / स` before a dental or retroflex**: `अस्ति`, `पश्चात्`, `निष्ठा`, `कष्ट`. Wrong sibilants are typical learner errors.
- **Vowel length in common words**: `पुत्री`, `नदी`, `राजानम्`, `ब्राह्मणी`. Feminine nouns in `-ī` and `-ū` are a common failure point.

## Consistency checks

Stories repeat names and terms. After the word-level pass, list every capitalised or recurring proper noun (character names, towns, kingdoms) with its spellings and flag any variant spelling as `CNS`. An OCR error in a name will appear next to the correct form elsewhere in the same text, which also gives you the correct reading with high confidence.
