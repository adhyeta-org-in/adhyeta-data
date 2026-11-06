"""Shared name authority: canonical transliteration + drift clustering.

Two classes (locked per SUMMARIZE_RAMAYANA.md):
  - summary-colloquial: ASCII only (Rama, Sita, Dasharatha, Vishvamitra)
  - iso-content: ISO-15919 UTF-8 for hooks/beats
    (Rama, Sita, Dasartha, Visvamitra, plus ring-below r/l and macron e/o)

Pipeline:
  1. extract vocab from fragments/TSVs (summaries vs hooks+beats separately)
  2. cluster near-duplicates by folded edit distance
  3. human picks canonical per cluster -> canonical-names.tsv
     lines: <class><TAB><variant><TAB><canonical>
     class is summary-colloquial | iso-content
  4. apply script rewrites fragments (word-boundary, case-preserving),
     recombine TSVs via tools.fragments, re-verify counts.

Stdlib only.
"""

import re
import unicodedata
from collections import Counter

WORD_RE = re.compile(r"[A-Za-zĀāĪīŪūṚṛṜṝḶḶḸḹṜṜ̄ĒēŌōṄṅÑñṆṇṬṭḌḍṆṇŚśṢṣṂṃḤḥḷṝṛṚṝ]+(?:['’][A-Za-z]+)?")


def fold_ascii(s: str) -> str:
    """Fold for comparison: NFKD strip diacritics, lower, v/w merge."""
    n = unicodedata.normalize("NFKD", s)
    n = "".join(c for c in n if not unicodedata.combining(c))
    n = n.lower()
    n = n.replace("w", "v")
    return n


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    la, lb = len(a), len(b)
    if abs(la - lb) > 3:
        return 99
    prev = list(range(lb + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * lb
        for j, cb in enumerate(b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
        prev = cur
    return prev[lb]


def extract_words(paths: list) -> Counter:
    """Count words across fragment/TSV files (values only, keys ignored)."""
    c: Counter = Counter()
    for fp in paths:
        with open(fp, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if "\t" in line and not fp.endswith(("_summary", "_hook", "_beats")):
                    line = line.split("\t", 1)[1]
                for w in WORD_RE.findall(line):
                    c[w] += 1
    return c


def cluster(words: list, max_dist: int = 2) -> list:
    """Group spelling variants: same folded base, edit distance <= max_dist."""
    groups: dict = {}
    for w in sorted(set(words), key=fold_ascii):
        f = fold_ascii(w)
        placed = False
        for base in list(groups):
            if abs(len(f) - len(base)) <= 2 and levenshtein(f, base) <= max_dist:
                groups[base].append(w)
                placed = True
                break
        if not placed:
            groups[f] = [w]
    return [sorted(v) for v in groups.values() if len(v) > 1]
