#!/usr/bin/env python3
"""Render an issue PDF to scan JPGs (one per page).

Usage:
  python3 render.py <ISSUE> [--dpi N] [--force]

Renders `.processing/samskrta_chandamama/<ISSUE>.pdf` to `.processing/samskrta_chandamama/<ISSUE>/<NN>.jpg`
(`<NN>` = scan sequence, 1-based, no zero-pad) via pdftoppm. Skips pages
already rendered unless --force. Verifies the count against pdfinfo when
available. Paths resolve from the repo root regardless of cwd.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("%s failed:\n%s" % (" ".join(cmd), r.stderr.strip()), file=sys.stderr)
        sys.exit(1)
    return r


def main():
    args = sys.argv[1:]
    if "--help" in args or "-h" in args:
        print(__doc__.strip())
        sys.exit(0)
    force = "--force" in args
    args = [a for a in args if a != "--force"]
    dpi = 300
    if "--dpi" in args:
        i = args.index("--dpi")
        if i + 1 >= len(args):
            print("usage: render.py <ISSUE> [--dpi N] [--force]", file=sys.stderr)
            sys.exit(2)
        dpi = int(args[i + 1])
        args = args[:i] + args[i + 2:]
    if len(args) != 1:
        print("usage: render.py <ISSUE> [--dpi N] [--force]", file=sys.stderr)
        sys.exit(2)
    issue = args[0]
    pdf = ROOT / ".processing" / "samskrta_chandamama" / (issue + ".pdf")
    outdir = ROOT / ".processing" / "samskrta_chandamama" / issue
    if not pdf.is_file():
        print("no such PDF: %s" % pdf, file=sys.stderr)
        sys.exit(1)
    if shutil.which("pdftoppm") is None:
        print("pdftoppm not found (install poppler-utils)", file=sys.stderr)
        sys.exit(1)
    outdir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=issue + "-") as tmp:
        prefix = os.path.join(tmp, "page")
        run(["pdftoppm", "-r", str(dpi), "-jpeg", str(pdf), prefix])
        rendered, skipped = 0, 0
        for src in sorted(Path(tmp).glob("page-*.jpg")):
            n = int(src.stem.split("-")[-1])  # 1-based already
            dst = outdir / ("%d.jpg" % n)
            if dst.is_file() and not force:
                skipped += 1
                continue
            shutil.copy(src, dst)
            rendered += 1
    total = len(sorted(outdir.glob("*.jpg")))
    print("rendered %d, skipped %d existing, %d total in %s (dpi=%d)" % (rendered, skipped, total, outdir, dpi))
    if shutil.which("pdfinfo") is not None:
        r = run(["pdfinfo", str(pdf)])
        for ln in r.stdout.splitlines():
            if ln.startswith("Pages:"):
                want = int(ln.split(":")[1])
                if want != total:
                    print("WARNING: pdf has %d pages but %d JPGs present" % (want, total), file=sys.stderr)
                    sys.exit(1)
                break
    else:
        print("(pdfinfo absent: count unverified)", file=sys.stderr)


if __name__ == "__main__":
    main()
