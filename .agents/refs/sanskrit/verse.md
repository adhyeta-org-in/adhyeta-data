# Verse and meter

Use this for Step 4, only when the text contains verse. In Chandamama-style stories that is usually a single subhāṣita or a moral couplet quoted inside the prose, most often in anuṣṭubh. Do not apply this file to prose.

## Detecting verse

- The line ends in `॥`, optionally followed by a verse number (`॥ ३ ॥`).
- It is introduced by a verb of saying (`इति उक्तम्`, `श्लोकम् अपठत्`) or `यथा` / `तथा चोक्तम्`.
- It splits into two or four segments of equal syllable length.

If you are unsure, run the scanner on the passage. A single danda-terminated sentence of 16 syllables in the middle of a paragraph is not necessarily a verse, so look at the shape too.

## Running the scanner

Put only the verse into a file and run `python3 .agents/tools/sanskrit/scan.py meter verse.txt`. For each segment (split at `।` / `॥`) the scanner returns the syllable count, the laghu-guru pattern (`L` / `G`), possible meter names from the count, and notes on anuṣṭubh pathyā. A segment of 8, 16 or 32 syllables gets the anuṣṭubh check.

The scanner is a counting tool, not a metrist. It follows these rules, so check its output against them when a result surprises you:

- **Guru** (heavy): a long vowel (`ā ī ū ṝ e ai o au`), a vowel followed by anusvāra or visarga, or a short vowel followed by two or more consonants (a conjunct, or a consonant at the end of one word and another at the start of the next).
- **Laghu** (light): any other short vowel.
- **Final syllable of a pāda** is anceps: scan it as guru or laghu as the meter requires.
- Consonant clusters count across word boundaries. The scanner does that. Read the sandhi-joined text as it is printed, so a joined `तदात्मानं` scans as one word.
- `ऋ` is scanned as a short vowel. `ळ`, nukta and avagraha do not change weight.

## Anuṣṭubh (śloka): the case you will meet most

Four pādas of 8 syllables. In each pāda, syllables 5 to 8 carry the pattern. The normal form (pathyā) is:

- syllable 5: laghu in every pāda;
- syllable 6: guru in every pāda;
- syllable 7: guru in pādas 1 and 3, laghu in pādas 2 and 4.

Pādas 1 and 3 may take the vipulā variants, which the scanner reports as "not pathyā (may be a permitted vipulā)". Treat those as variant, not as an error. Report as a likely error only: a pāda with the wrong syllable count, syllable 5 guru or syllable 6 laghu, or syllable 7 guru in an even pāda (unless the verse is clearly archaic or Epic).

## Other meters you may see

Counts are per pāda. A scanned segment of twice these numbers is a half-verse.

| Syllables | Meter |
|---|---|
| 11 | triṣṭubh family: indravajrā, upendravajrā, upajāti (a mix of the two) |
| 12 | jagatī family: vaṃśastha, drutavilambita and others |
| 14 | vasantatilakā |
| 15 | mālinī |
| 17 | śikhariṇī, mandākrāntā |
| 19 | śārdūlavikrīḍita |
| 21 | sragdharā |

Syllable count alone cannot tell śikhariṇī from mandākrāntā, or indravajrā from upendravajrā. If the count matches one of these, name the candidate meter, say which patterns you compared, and mark the identification `unverified` unless you can match the laghu-guru string against the meter's defining pattern or a reference.

## Reporting

- A syllable count that matches no common meter is most often an `OCR` problem (a dropped anusvāra changes weight, a dropped halant changes the count), so check `ocr-and-orthography.md` before blaming the author.
- Report each metrical anomaly as `MTR` with the pāda number, the scanned pattern and the pattern expected. Quote the pāda.
- Do not change a word to repair the meter. Give the metrical reason, offer a candidate reading if the OCR hypothesis suggests one, and mark it low confidence. Transmitted verses from epics and from older collections contain genuine metrical irregularities.
- Sandhi inside verse follows the same rules as in prose, but the meter may suspend them (hiatus) or require the unsandhied form. Do not flag a hiatus in verse as `SND` if the meter needs it.
