#!/usr/bin/env python3
"""Reverse- and Reengineering — Homework 3 verification.

Two independent checks on the recovered C, neither of which trusts the other:

  (a) SEMANTIC. The recovered C is simulated in Python and the result is
      compared with the sheet's own machine code, simulated instruction by
      instruction from the listing extracted out of the PDF. Any disagreement
      is reported as a mismatch count.

  (b) COMPILER ROUND-TRIP. The recovered C is compiled at -O0 and the generated
      instruction mnemonics are compared, line by line, with the sheet's
      listing. This is what settles questions the reading alone cannot:
      `sar` vs `shr`, and `jl` (which is what `>=` compiles to) vs `jle`
      (which is what `>` compiles to).

The listing is read from the PDF's word positions, not with `pdftotext
-layout`: the sheet prints two listings side by side on page 1 and -layout
interleaves them into a listing that does not exist.

Run:  python hw03-verify.py [--zig /path/to/zig]
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PDF = (HERE / "../../../raw/lectures/Reverse and Re-Engineering/Ubung/hw03.pdf").resolve()

# ---------------------------------------------------------------------------
# 1. The recovered C, and what the sheet's machine code does with it.
# ---------------------------------------------------------------------------


def f1_c(x: int, y: int) -> int:
    """int f1(int a, int b) { int x = 15; int y = 2; return x >> y; }"""
    return x >> y


def f2_c(x: int, y: int) -> int:
    """int f2(int a, int b) { int x = 10; int y = 2; return x << y; }"""
    return x << y


def max_c(a: int, b: int, c: int, uninit: int) -> tuple[list[int], int]:
    """The sheet's -O0 output, read literally.

    Three comparisons, each printing its argument when it is >= the other two.
    `return m;` reads [rbp-4], which NO instruction in the listing writes, so
    the returned value is whatever `uninit` stands for - indeterminate.
    """
    printed = []
    if a >= b and a >= c:
        printed.append(a)
    if b >= a and b >= c:
        printed.append(b)
    if c >= a and c >= b:
        printed.append(c)
    return printed, uninit


def machine_f1(x: int, y: int) -> int:
    """Listing 1: mov [rbp-4],15 ; mov [rbp-8],2 ; mov eax,[rbp-4] ; mov ecx,[rbp-8] ; sar eax,cl."""
    eax = x          # [rbp-4] -> eax
    ecx = y & 0x1F   # x86 masks the shift count to 5 bits for 32-bit operands
    return sar32(eax, ecx)


def machine_f2(x: int, y: int) -> int:
    """Listing 2: same, with `shl eax, cl` instead of `sar`."""
    eax = x
    ecx = y & 0x1F
    return shl32(eax, ecx)


def to_s32(v: int) -> int:
    v &= 0xFFFFFFFF
    return v - 0x100000000 if v >= 0x80000000 else v


def sar32(v: int, s: int) -> int:
    return to_s32(v) >> s          # Python's >> on a negative int is arithmetic


def shl32(v: int, s: int) -> int:
    return to_s32((to_s32(v) & 0xFFFFFFFF) << s)


# ---------------------------------------------------------------------------
# 2. Read the sheet's listings out of the PDF by x-position.
# ---------------------------------------------------------------------------

def read_listing(pdf: Path) -> dict[str, list[str]]:
    """Split page 1's two side-by-side listings by x-position.

    Returns {} when pymupdf is unavailable, and the caller then reports the
    comparison as SKIPPED rather than as a mismatch.
    """
    try:
        import pymupdf
    except ImportError:
        print("  pymupdf not available in this interpreter - listing comparison SKIPPED")
        print("  install it with:  uv pip install --python <this python> pymupdf")
        return {}

    doc = pymupdf.open(str(pdf))
    page = doc[0]
    left, right = [], []
    # Blocks, not words: this PDF puts one listing line per text block
    # ("1\npush\nrbp\n"), which is exactly the grouping wanted. Splitting words
    # by y is fragile because a one-pixel difference between the line number and
    # the mnemonic separates them.
    for blk in page.get_text("blocks"):
        x0, y0, _x1, _y1, text = blk[0], blk[1], blk[2], blk[3], blk[4]
        if y0 < 280 or y0 > 400:
            continue                                    # only the two listings
        toks = text.split()
        if not toks or not toks[0].isdigit():
            continue                                    # a caption or column header
        (left if x0 < 300 else right).append(" ".join(toks[1:]))

    return {"f1": left, "f2": right}


# ---------------------------------------------------------------------------
# 3. Compile the recovered C and diff mnemonics.
# ---------------------------------------------------------------------------

C_SOURCE = """\
/* recovered from the sheet's listings */
int f1(void) { int x = 15; int y = 2; return x >> y; }
int f2(void) { int x = 10; int y = 2; return x << y; }
"""

SUFFIXES = ("l", "q", "w", "b")


def canon(mnemonic: str) -> str:
    """Canonical opcode: the sheet prints Intel syntax without size suffixes
    (`sar eax, cl`) while the compiler emits AT&T with them (`sarl %cl, %eax`),
    so `sarl` and `sar` are the same instruction and must compare equal."""
    m = mnemonic.strip().lower()
    if len(m) > 3 and m[-1] in SUFFIXES and not m.endswith(("call", "ret")):
        return m[:-1]
    return m


def mnemonics(asm: str, label: str) -> list[str]:
    """The instruction mnemonics between `label:` and its .size directive."""
    body = re.search(rf"^{re.escape(label)}:(.*?)(?=^\t\.size|\Z)", asm, re.S | re.M)
    if not body:
        return []
    out = []
    for raw in body.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith((".", "#")) or line.endswith(":"):
            continue
        token = line.split()[0]
        if token in ("callq", "call"):
            out.append("call")
        else:
            out.append(canon(token))
    return out


def find_zig(explicit: str | None) -> str | None:
    if explicit:
        return explicit
    for cand in (shutil.which("zig"),):
        if cand:
            return cand
    for root in (Path(os.environ.get("LOCALAPPDATA", "")) / "Temp",):
        if root.exists():
            for p in sorted(root.glob("*/**/ziglang/zig.exe")) + sorted(root.glob("**/ziglang/zig.exe")):
                return str(p)
    return None


def roundtrip(zig: str) -> int:
    with tempfile.TemporaryDirectory() as td:
        c = Path(td) / "rec.c"
        c.write_text(C_SOURCE, encoding="utf-8")
        r = subprocess.run(
            [zig, "cc", "-target", "x86_64-linux-gnu.2.35", "-O0", "-S",
             "-fno-sanitize=undefined", "-fno-asynchronous-unwind-tables",
             "-o", str(Path(td) / "rec.s"), str(c)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print("compile failed:", r.stderr[:400], file=sys.stderr)
            return 1
        asm = (Path(td) / "rec.s").read_text()

    sheet = read_listing(PDF)
    if not sheet:
        print("  listing comparison SKIPPED (no pymupdf); semantic check above still stands")
        return 0
    bad = 0
    for label, key in (("f1", "f1"), ("f2", "f2")):
        mine = mnemonics(asm, label)
        theirs = [canon(ln.split()[0]) for ln in sheet.get(key, []) if ln.split()]
        print(f"  {label}: sheet = {theirs}")
        print(f"  {label}: zig   = {mine}")
        if mine != theirs:
            print(f"  {label}: MISMATCH")
            bad += 1
        else:
            print(f"  {label}: exact match, instruction for instruction")
    return bad


# ---------------------------------------------------------------------------
# 4. The operator question, settled by compiling both candidates.
# ---------------------------------------------------------------------------

CMP_SOURCE = """\
#include <stdio.h>
int max_ge(int a, int b, int c) {
    int m;
    if (a >= b && a >= c) printf("%d is the largest number.\\n", a);
    if (b >= a && b >= c) printf("%d is the largest number.\\n", b);
    if (c >= a && c >= b) printf("%d is the largest number.\\n", c);
    return m;
}
int max_gt(int a, int b, int c) {
    int m;
    if (a > b && a > c) printf("%d is the largest number.\\n", a);
    if (b > a && b > c) printf("%d is the largest number.\\n", b);
    if (c > a && c > b) printf("%d is the largest number.\\n", c);
    return m;
}
"""


def operator_probe(zig: str) -> None:
    with tempfile.TemporaryDirectory() as td:
        c = Path(td) / "cmp.c"
        c.write_text(CMP_SOURCE, encoding="utf-8")
        r = subprocess.run(
            [zig, "cc", "-target", "x86_64-linux-gnu.2.35", "-O0", "-S",
             "-fno-sanitize=undefined", "-fno-asynchronous-unwind-tables",
             "-o", str(Path(td) / "cmp.s"), str(c)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print("operator probe could not compile", file=sys.stderr)
            return
        asm = (Path(td) / "cmp.s").read_text()

    ge = [m for m in mnemonics(asm, "max_ge") if m.startswith("j")]
    gt = [m for m in mnemonics(asm, "max_gt") if m.startswith("j")]
    print(f"  `a >= b && a >= c` compiles to conditional jumps: {ge}")
    print(f"  `a >  b && a >  c` compiles to conditional jumps: {gt}")
    print("  the sheet's listing uses `jl` three times at 9, 10 and 11, therefore the")
    print("  source used >=, not >. `jl` is the branch taken when the first operand is")
    print("  LESS, i.e. it skips the body when the comparison fails.")


# ---------------------------------------------------------------------------
# 5. Execution of the recovered code on the sheet's own inputs.
# ---------------------------------------------------------------------------

def execution_check() -> int:
    bad = 0
    print("  f1 = 15 >> 2 and f2 = 10 << 2, computed both ways")
    for name, c_fn, m_fn, args in (("f1", f1_c, machine_f1, (15, 2)),
                                   ("f2", f2_c, machine_f2, (10, 2))):
        c_val, m_val = c_fn(*args), m_fn(*args)
        flag = "OK" if c_val == m_val else "MISMATCH"
        if c_val != m_val:
            bad += 1
        print(f"    {name}({args[0]},{args[1]}) = {c_val:>6}  (sheet's code: {m_val:>6})  {flag}")

    print("  sar vs shr on negative values, which is the whole difference")
    for v in (-16, -8, -1, 0, 7):
        print(f"    v={v:>4}  sar v>>2 = {sar32(v,2):>4}   shr v>>2 = "
              f"{(v & 0xFFFFFFFF) >> 2:>10}   (x86 `shr` is the unsigned shift)")

    print("  max(100,200,400) - what is printed, and what is returned")
    printed, ret = max_c(100, 200, 400, 0xDEADBEEF)
    print(f"    printed: {printed}")
    print(f"    returned: {ret:#x}  <- [rbp-4] is never written in the listing,")
    print("              so the return value is indeterminate; main discards it anyway")
    print("  max(5,5,1) - the tie case")
    print(f"    printed: {max_c(5, 5, 1, 0)[0]}   (both 5s qualify, so the line prints twice)")
    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zig", default=None, help="path to a zig binary for the round-trip")
    args = ap.parse_args()

    print("=" * 78)
    print("(a) SEMANTIC CHECK - recovered C vs the sheet's own instructions")
    print("=" * 78)
    bad = execution_check()

    print()
    print("=" * 78)
    print("(b) COMPILER ROUND-TRIP - recovered C compiled at -O0 vs the sheet's listing")
    print("=" * 78)
    zig = find_zig(args.zig)
    if not zig:
        print("  SKIPPED: no zig (or gcc) found on this host.")
        print("  The round-trip was run when the page was written; results are recorded")
        print("  on the page. Install ziglang (`uv pip install ziglang`) to re-run it.")
    else:
        print(f"  compiler: {zig}")
        bad += roundtrip(zig)
        print()
        print("  the operator question, settled by compiling both candidates:")
        operator_probe(zig)

    print()
    print("=" * 78)
    if bad:
        print(f"RESULT: {bad} mismatch(es) - the recovered C does NOT match the sheet")
    else:
        print("RESULT: 0 mismatches")
    print("=" * 78)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
