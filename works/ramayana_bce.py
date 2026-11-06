"""Ramayana BCE work adapter (Baroda Critical Edition).

Work-native keys: index | K | K.SSS  (K = kanda 1-7, SSS zero-padded sarga)
Source files: Ram01.txt .. Ram07.txt, lines KSSSVVP<space>text (see translate).
Fragments: fragments/<KEY>_summary|_hook|_beats  (see tools.fragments)
Combined: summaries.tsv / hooks.tsv / beats.tsv / uuids.tsv (KEY<TAB>value)

Future works (Mahabharata, Puranas, Kalidasa) add a sibling adapter
(e.g. works/mahabharata_bce.py) reusing tools.fragments + tools.names.
"""

WORK_ID = "valmikiramayanam-bce"
SITE_SLUG = "valmikiramayanam-bce"
SOURCE_SUFFIX = "Baroda Critical Edition"
SRC_TXT_GLOB = "Ram*.txt"
SRC_SKIP_FIRST = "Ram00.txt"


def sarga_key(kanda: int, sarga: int) -> str:
    return f"{kanda}.{sarga:03d}"


def line_prefix(kanda: int, sarga: int) -> str:
    """BCE line prefix for a sarga, e.g. kanda 1 sarga 7 -> '1007'."""
    return f"{kanda}{sarga:03d}"


def parse_key(key: str):
    """index -> ('index',), '3' -> ('kanda', 3), '3.012' -> ('sarga', 3, 12)."""
    if key == "index":
        return ("index",)
    if "." not in key:
        return ("kanda", int(key))
    k, s = key.split(".", 1)
    return ("sarga", int(k), int(s))
