#!/usr/bin/env python
"""Mechanical checks for Devanagari Sanskrit.

Usage:
    scan.py orth  FILE   # orthography / OCR-artifact scan (FILE may be '-' for stdin)
    scan.py meter FILE   # laghu-guru scan of verse segments (pass ONLY the verse text)

Output is JSON on stdout. These are hints for the proofreader, not verdicts.
"""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Literal

Severity = Literal["high", "medium", "low"]
Weight = Literal["L", "G"]

# --- Devanagari character classes -------------------------------------------------

INDEP_SHORT = "अइउऋऌ"
INDEP_LONG = "आईऊॠॡएऐओऔ"
MATRA_SHORT = "\u093f\u0941\u0943\u0962"
MATRA_LONG = "\u093e\u0940\u0942\u0944\u0947\u0948\u094b\u094c\u0963"
MATRAS = MATRA_SHORT + MATRA_LONG
VIRAMA = "\u094d"
NUKTA = "\u093c"
ANUSVARA = "\u0902"
VISARGA = "\u0903"
CANDRABINDU = "\u0901"
COMBINING = MATRAS + VIRAMA + NUKTA + ANUSVARA + VISARGA + CANDRABINDU
INDEP_VOWELS = INDEP_SHORT + INDEP_LONG


def is_consonant(ch: str) -> bool:
    return "\u0915" <= ch <= "\u0939" or "\u0958" <= ch <= "\u095f"


# --- Data model -------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Finding:
    line: int  # 1-based
    col: int  # 1-based character offset
    snippet: str
    kind: str
    severity: Severity
    message: str
    suggestion: str | None = None


@dataclass(frozen=True, slots=True)
class OrthReport:
    lines: int
    findings: list[Finding]


@dataclass(frozen=True, slots=True)
class Rule:
    pattern: re.Pattern[str]
    kind: str
    severity: Severity
    message: str
    suggestion: str | None = None


@dataclass(frozen=True, slots=True)
class SegmentScan:
    line: int
    text: str
    syllables: int
    pattern: str  # e.g. "LGLGLGGL"; last syllable of a pada is anceps
    hints: list[str]
    notes: list[str]


@dataclass(frozen=True, slots=True)
class MeterHint:
    pada_syllables: int
    name: str


@dataclass(slots=True)
class _Unit:
    long_vowel: bool
    nasal: bool = False
    trailing: int = 0  # consonants between this vowel and the next vowel


# --- Orthography scan -------------------------------------------------------------

# Linter-owned checks were removed here: pipe-for-danda, colon-for-visarga,
# stray Latin/digits, NFC, and spacing are caught by the sidecar linter.
# This scanner keeps only what the linter cannot see on clean story text.
RULES: tuple[Rule, ...] = (
    Rule(
        re.compile(r"(?<=[\u0900-\u097f])\.(?=\s|$)"),
        "fullstop-for-danda",
        "low",
        "Full stop after Devanagari; Sanskrit prose normally uses danda",
        "।",
    ),
    Rule(
        re.compile(r"(?<=[\u0900-\u097f])\s*[Il1!]\s*$"),
        "latin-for-danda",
        "medium",
        "Latin I / l / 1 / ! at end of line is probably a danda",
        "।",
    ),
    Rule(re.compile("\ufffd"), "replacement-char", "high", "Unicode replacement character: lost glyph"),
    Rule(
        re.compile(r"[\u0980-\u0dff]"),
        "other-script",
        "high",
        "Character from another Indic script (look-alike glyph)",
    ),
    Rule(
        re.compile("[ऍऎऑऒ\u0945\u0946\u0949\u094a]"),
        "non-sanskrit-vowel",
        "medium",
        "Hindi/Marathi/English-loan vowel sign; not Sanskrit",
    ),
    Rule(
        re.compile("[ळऴऱऩ]"),
        "non-classical-letter",
        "low",
        "Vedic/Marathi/Dravidian letter; check whether intended (usually ल / र / न)",
    ),
    Rule(re.compile("[\u200c\u200d]"), "zwj-zwnj", "low", "ZWJ/ZWNJ present: check that conjunct rendering is intended"),
    Rule(
        re.compile(r"॥\s*[\d०-९]*\s*$"),
        "verse-candidate",
        "low",
        "Line ends with double danda: possible verse; run `scan.py meter` on it",
    ),
)


def mark_findings(line_no: int, line: str) -> list[Finding]:
    """Combining marks that have no valid base character."""
    found: list[Finding] = []
    for i, ch in enumerate(line):
        if ch not in COMBINING:
            continue
        prev = line[i - 1] if i > 0 else " "
        if ch in MATRAS or ch == VIRAMA:
            valid = is_consonant(prev) or prev == NUKTA
        elif ch == NUKTA:
            valid = is_consonant(prev)
        else:  # anusvara, candrabindu, visarga
            valid = is_consonant(prev) or prev in MATRAS or prev in INDEP_VOWELS
        if not valid:
            found.append(
                Finding(
                    line_no,
                    i + 1,
                    line[max(0, i - 2) : i + 2],
                    "orphan-or-stacked-mark",
                    "high",
                    "Vowel sign / virama / anusvara / visarga without a valid base (OCR fragment or double mark)",
                )
            )
    return found


def scan_line(line_no: int, line: str) -> list[Finding]:
    found: list[Finding] = []
    for rule in RULES:
        for m in rule.pattern.finditer(line):
            found.append(
                Finding(line_no, m.start() + 1, m.group().strip() or repr(m.group()), rule.kind, rule.severity, rule.message, rule.suggestion)
            )
    found.extend(mark_findings(line_no, line))
    found.sort(key=lambda f: f.col)
    return found


def scan_orthography(text: str) -> OrthReport:
    lines = text.splitlines()
    findings = [f for i, line in enumerate(lines, start=1) for f in scan_line(i, line)]
    return OrthReport(lines=len(lines), findings=findings)


# --- Meter scan -------------------------------------------------------------------

METER_HINTS: tuple[MeterHint, ...] = (
    MeterHint(8, "anuṣṭubh (śloka)"),
    MeterHint(11, "triṣṭubh family (indravajrā / upendravajrā / upajāti, ...)"),
    MeterHint(12, "jagatī family (vaṃśastha, drutavilambita, ...)"),
    MeterHint(14, "vasantatilakā"),
    MeterHint(15, "mālinī"),
    MeterHint(17, "śikhariṇī / mandākrāntā"),
    MeterHint(19, "śārdūlavikrīḍita"),
    MeterHint(21, "sragdharā"),
)


def syllabify(text: str) -> list[Weight]:
    """Return laghu/guru weights. Guru = long vowel, anusvara/visarga, or 2+ following consonants."""
    units: list[_Unit] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch in INDEP_VOWELS:
            units.append(_Unit(long_vowel=ch in INDEP_LONG))
            i += 1
        elif is_consonant(ch):
            i += 1
            if i < n and text[i] == NUKTA:
                i += 1
            if units:
                units[-1].trailing += 1
            if i < n and text[i] == VIRAMA:
                i += 1  # consonant without its own vowel
            else:
                long_vowel = False
                if i < n and text[i] in MATRAS:
                    long_vowel = text[i] in MATRA_LONG
                    i += 1
                units.append(_Unit(long_vowel=long_vowel))
        elif ch in (ANUSVARA, VISARGA, CANDRABINDU):
            if units:
                units[-1].nasal = True
            i += 1
        else:
            i += 1
    return ["G" if u.long_vowel or u.nasal or u.trailing >= 2 else "L" for u in units]


def check_anustubh_pada(pattern: str, pada_no: int) -> list[str]:
    """pada_no is 1-based within the verse (odd/even matters)."""
    notes: list[str] = []
    if pattern[4] != "L" or pattern[5] != "G":
        notes.append(f"pada {pada_no}: syllables 5-6 are {pattern[4:6]}, expected LG")
    if pada_no % 2 == 0 and pattern[6] != "L":
        notes.append(f"pada {pada_no}: syllable 7 is guru in an even pada (non-pathyā)")
    if pada_no % 2 == 1 and pattern[4:7] != "LGG":
        notes.append(f"pada {pada_no}: syllables 5-7 are {pattern[4:7]}; not pathyā LGG (may be a permitted vipulā)")
    return notes


def scan_segment(line_no: int, text: str) -> SegmentScan:
    weights = syllabify(text)
    pattern = "".join(weights)
    n = len(weights)
    hints: list[str] = []
    notes: list[str] = []
    for hint in METER_HINTS:
        for mult in (1, 2, 4):
            if n == hint.pada_syllables * mult:
                hints.append(f"{n} = {mult} x {hint.pada_syllables}: possible {hint.name}")
    if n in (8, 16, 32):
        for k in range(n // 8):
            notes.extend(check_anustubh_pada(pattern[k * 8 : k * 8 + 8], k + 1))
    if not hints:
        notes.append(f"{n} syllables matches no common pada length; check for scribal/OCR error or a rarer meter")
    return SegmentScan(line_no, text, n, pattern, hints, notes)


def scan_meter(text: str) -> list[SegmentScan]:
    scans: list[SegmentScan] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for part in re.split(r"[।॥]+", line):
            cleaned = re.sub(r"[\d०-९]+", "", part).strip()
            if cleaned:
                scans.append(scan_segment(line_no, cleaned))
    return scans


# --- CLI --------------------------------------------------------------------------


def read_input(path: str) -> str:
    return sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("orth", "meter"):
        sub.add_parser(name).add_argument("file")
    args = parser.parse_args()
    text = read_input(args.file)
    payload = asdict(scan_orthography(text)) if args.command == "orth" else [asdict(s) for s in scan_meter(text)]
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
