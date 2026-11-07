"""Mahabharata BCE work adapter (BORI Critical Edition, Poona).

Work-native keys: index | PP | PP.AAA  (PP = parvan 01-18 zero-padded,
AAA = adhyaya zero-padded to 3 digits, e.g. 01.001, 12.325).
Source files: MBh01.txt .. MBh18.txt, lines PPAAAVVVP<space>text
(see translate). PP zero-padding keeps keys lexically sortable,
unlike the Ramayana adapter where single-digit kandas sufficed.
Fragments: fragments/<KEY>_summary|_hook|_beats  (see tools.fragments)
Combined: summaries.tsv / hooks.tsv / beats.tsv / uuids.tsv (KEY<TAB>value)

Reuses tools.fragments + tools.names alongside works.ramayana_bce.
"""

WORK_ID = "mahabharata-bce"
SITE_SLUG = "mahabharata-bce"
SOURCE_SUFFIX = "TODO-SOURCE-BORI"
SRC_TXT_GLOB = "MBh*.txt"
SRC_SKIP_FIRST = "MBh00.txt"


def adhyaya_key(parvan: int, adhyaya: int) -> str:
    return f"{parvan:02d}.{adhyaya:03d}"


def parvan_key(parvan: int) -> str:
    return f"{parvan:02d}"


def line_prefix(parvan: int, adhyaya: int) -> str:
    """BCE line prefix for an adhyaya, e.g. parvan 1 adhyaya 7 -> '01007'."""
    return f"{parvan:02d}{adhyaya:03d}"


def parse_key(key: str):
    """index -> ('index',), '01' -> ('parvan', 1), '01.007' -> ('adhyaya', 1, 7)."""
    if key == "index":
        return ("index",)
    if "." not in key:
        return ("parvan", int(key))
    p, a = key.split(".", 1)
    return ("adhyaya", int(p), int(a))
