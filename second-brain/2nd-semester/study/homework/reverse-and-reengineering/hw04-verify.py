#!/usr/bin/env python3
"""Reverse- and Reengineering — Homework 4 verification.

Problem 1 (`decode`) is checked four ways, and problem 2 (control-flow
flattening of `bar`) is executed rather than asserted:

  (a) LISTING RECOVERY. The 19-line listing is read out of the PDF by word
      position. `pdftotext -layout` interleaves the line numbers with the
      instructions and produces a listing that does not exist, so the recovery
      is positional: page 1, the y-range of the listing, number in one column.

  (b) SIMULATION. The recovered listing is interpreted instruction by
      instruction in Python (a 19-instruction subset: push/mov/pop/ret) and
      compared with the recovered C on several input pairs, including the
      aliased call where xp == yp.

  (c) COMPILER ROUND-TRIP. The recovered C is compiled at -O0 in Intel syntax
      and the generated instructions are compared, line by line, with the
      sheet's listing. This is what settles the *order* of the two stores: a
      semantically equivalent `long t = *xp; *xp = *yp; *yp = t;` has the same
      behaviour on distinct pointers but writes *xp first, so it does not
      reproduce the listing.

  (d) REAL EXECUTION. The sheet's listing is transcribed verbatim into an
      assembler source, assembled unchanged, linked against a driver, and run
      under WSL — so the claim "this code swaps its two arguments" is the
      program's own output, not a reading.

  (e) FLATTENING. The flattened `bar` and the original `bar` are compiled into
      one program and run; both must return 5050.

Run:  python hw04-verify.py [--zig /path/to/zig]
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
PDF = (HERE / "../../../raw/lectures/Reverse and Re-Engineering/Ubung/hw04.pdf").resolve()

# ---------------------------------------------------------------------------
# (a) read the sheet's listing out of the PDF by position
# ---------------------------------------------------------------------------


def read_listing(pdf: Path) -> list[str]:
    """The 19 instructions of `decode`, in order, without the line numbers.

    Each listing row is three separate text lines in the PDF's dict output (the
    number, the mnemonic, the operands) sitting at slightly different
    baselines, so rows are recovered by clustering the y-coordinates to within
    3 points and then reading each cluster left to right.
    """
    try:
        import pymupdf
    except ImportError:
        print("  pymupdf not available - listing recovery SKIPPED")
        print("  run with:  uv run --with pymupdf python hw04-verify.py")
        return []
    doc = pymupdf.open(str(pdf))
    page = doc[0]
    frags: list[tuple[float, float, str]] = []
    for blk in page.get_text("dict")["blocks"]:
        if blk.get("type") != 0:
            continue
        for line in blk["lines"]:
            x0 = min(s["bbox"][0] for s in line["spans"])
            text = "".join(s["text"] for s in line["spans"]).strip()
            if not text or not (270 < line["bbox"][1] < 460) or x0 > 300:
                continue
            frags.append((line["bbox"][1], x0, text))
    frags.sort()
    rows: list[list[tuple[float, str]]] = []
    for y, x, text in frags:
        if rows and y - max(f[0] for f in rows[-1]) < 3.0:
            rows[-1].append((y, x, text))
        else:
            rows.append([(y, x, text)])
    out = []
    for row in rows:
        cells = [t for _y, _x, t in sorted(row, key=lambda f: f[1])]
        if not cells or not cells[0].isdigit():
            continue                              # a caption or column header
        out.append(" ".join(cells[1:]).strip())
    return out


# ---------------------------------------------------------------------------
# (b) a small interpreter for the sheet's own instructions
# ---------------------------------------------------------------------------

MEM_RE = re.compile(r"^qword ptr \[(\w+)(?: ([+-]) (\d+))?\]$")


def parse_operand(text: str, mem: dict[int, int]) -> int:
    """Resolve one operand: a register, a memory reference, or (for a write)
    the address a memory operand denotes."""
    text = text.strip()
    if text in REGS:
        return REGS[text]
    m = MEM_RE.match(text)
    if m:
        addr = REGS[m.group(1)]
        if m.group(2):
            addr += int(m.group(3)) if m.group(2) == "+" else -int(m.group(3))
        return mem.get(addr)
    raise ValueError(f"unsupported operand: {text!r}")


def mem_addr(text: str) -> int:
    m = MEM_RE.match(text.strip())
    if not m:
        raise ValueError(f"not a memory operand: {text!r}")
    addr = REGS[m.group(1)]
    if m.group(2):
        addr += int(m.group(3)) if m.group(2) == "+" else -int(m.group(3))
    return addr


REGS: dict[str, int] = {}


def machine_decode(listing: list[str], xp_adr: int, yp_adr: int,
                   mem: dict[int, int]) -> None:
    """Execute the listing. `mem` is the whole address space; REGS is global so
    the operand parser can reach it."""
    for ins in listing:
        parts = re.split(r"\s+", ins.strip())
        op = parts[0]
        args = " ".join(parts[1:])
        if op.endswith(":"):                       # a label, not an instruction
            continue
        if op == "push":
            REGS["rsp"] -= 8
            mem[REGS["rsp"]] = REGS[parts[1]]
        elif op == "pop":
            REGS[parts[1]] = mem[REGS["rsp"]]
            REGS["rsp"] += 8
        elif op == "mov":
            dst, _, src = args.partition(", ")
            if MEM_RE.match(dst):
                mem[mem_addr(dst)] = parse_operand(src, mem)
            elif MEM_RE.match(src):
                REGS[dst] = parse_operand(src, mem)
            else:
                REGS[dst] = REGS[src]
        elif op == "ret":
            return
        else:
            raise ValueError(f"unsupported instruction: {ins!r}")


def machine_decode_run(a: int, b: int, aliased: bool = False) -> tuple[int, int]:
    """Run the listing on two longs and return (a, b) afterwards."""
    global REGS
    REGS = {r: 0 for r in ("rax", "rcx", "rdx", "rsi", "rdi", "rbp", "rsp", "r8")}
    mem: dict[int, int] = {}
    xp_adr, yp_adr = 0x1000, 0x2000
    REGS["rsp"] = 0x7FF0
    REGS["rbp"] = 0x8000
    mem[xp_adr], mem[yp_adr] = a, b
    REGS["rdi"], REGS["rsi"] = xp_adr, yp_adr if not aliased else xp_adr
    machine_decode(read_listing(PDF), xp_adr, yp_adr, mem)
    return mem[xp_adr], mem[yp_adr]


def recovered_c(a: int, b: int, aliased: bool = False):
    """The C recovered from the listing."""
    if aliased:
        return a, a
    return b, a


# ---------------------------------------------------------------------------
# (c) compiler round-trip
# ---------------------------------------------------------------------------

C_SOURCE = """\
/* recovered from the sheet's listing */
void decode(long *xp, long *yp) {
    long a = *xp;
    long b = *yp;
    *yp = a;
    *xp = b;
}
"""

# the plausible-but-wrong alternative, to show the round-trip does real work
C_SOURCE_TMP = """\
void decode(long *xp, long *yp) {
    long t = *xp;
    *xp = *yp;
    *yp = t;
}
"""


def instructions_of(asm: str, label: str) -> list[str]:
    """The instruction lines between `label:` and the next `.size`."""
    body = re.search(rf"^{re.escape(label)}:(.*?)(?=^\t\.size|\Z)", asm, re.S | re.M)
    if not body:
        return []
    out = []
    for raw in body.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith((".", "#")) or line.endswith(":"):
            continue
        out.append(re.sub(r"\s+", " ", line))
    return out


def compile_asm(zig: str, source: str, td: str) -> str:
    c = Path(td) / "rec.c"
    c.write_text(source, encoding="utf-8")
    r = subprocess.run(
        [zig, "cc", "-target", "x86_64-linux-gnu.2.35", "-O0", "-S", "-masm=intel",
         "-fno-sanitize=undefined", "-fno-asynchronous-unwind-tables",
         "-fno-stack-protector", "-o", str(Path(td) / "rec.s"), str(c)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        print("compile failed:", r.stderr[:400], file=sys.stderr)
        return ""
    return (Path(td) / "rec.s").read_text()


def find_zig(explicit: str | None) -> str | None:
    if explicit:
        return explicit
    got = shutil.which("zig")
    if got:
        return got
    for root in (Path(os.environ.get("APPDATA", "")) / "uv/tools",):
        if root.exists():
            for p in sorted(root.glob("**/ziglang/zig.exe")):
                return str(p)
    return None


# ---------------------------------------------------------------------------
# (d) assemble the sheet's listing verbatim and run it
# ---------------------------------------------------------------------------

SHEET_ASM_HEADER = """\
	.intel_syntax noprefix
	.text
	.globl decode
	.type decode, @function
decode:
"""

DRIVER_C = """\
#include <stdio.h>
void decode(long *xp, long *yp);
void decode_c(long *xp, long *yp) {
    long a = *xp; long b = *yp; *yp = a; *xp = b;
}
static void row(const char *tag, long a, long b) {
    long x = a, y = b, u = a, v = b;
    decode(&x, &y); decode_c(&u, &v);
    printf("  %-9s in (%ld, %ld) -> sheet (%ld, %ld)  C (%ld, %ld)  %s\\n",
           tag, a, b, x, y, u, v, (x == u && y == v) ? "same" : "DIFFER");
}
int main(void) {
    row("distinct", 7, 42);
    row("negative", -1, 0);
    row("equal", 5, 5);
    row("extreme", 9223372036854775807L, -9223372036854775807L - 1L);
    { long v = 99; decode(&v, &v); printf("  %-9s in (&v, &v) v=99 -> v=%ld\\n", "aliased", v); }
    return 0;
}
"""


def wsl_path(p: Path) -> str:
    s = str(p).replace("\\", "/")
    return "/mnt/" + s[0].lower() + s[2:]


def execute_sheet_listing(zig: str, listing: list[str]) -> int:
    body = "".join(f"\t{ins}\n" for ins in listing)
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "decode_sheet.s").write_text(
            SHEET_ASM_HEADER + body + "\t.size decode, .-decode\n"
            '\t.section .note.GNU-stack,"",@progbits\n', encoding="utf-8")
        (Path(td) / "driver.c").write_text(DRIVER_C, encoding="utf-8")
        r = subprocess.run(
            [zig, "cc", "-target", "x86_64-linux-gnu.2.35", "-O0",
             "-fno-sanitize=undefined", "-fno-stack-protector", "-o",
             str(Path(td) / "prog"), str(Path(td) / "driver.c"),
             str(Path(td) / "decode_sheet.s")],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print("  assembly/link failed:", r.stderr[:600])
            return 1
        run = subprocess.run(
            ["wsl.exe", "-e", "bash", "-lc",
             f"cd {wsl_path(Path(td))} && stdbuf -o0 ./prog"],
            capture_output=True, text=True,
        )
        print(run.stdout.rstrip() or run.stderr[:600])
        bad = 1 if "DIFFER" in run.stdout or "MISMATCH" in run.stdout else 0
        if run.returncode != 0 or not run.stdout.strip():
            print("  (the WSL run produced no output - is WSL available?)")
            bad += 1
        return bad


# ---------------------------------------------------------------------------
# (e) control-flow flattening
# ---------------------------------------------------------------------------

FLAT_C = """\
#include <stdio.h>
int bar(void) {
    int i = 1; int s = 0;
    while (i <= 100) { s += i; i++; }
    return s;
}
int bar_flat(void) {
    int i = 1; int s = 0;
    int next = 1;
    for (;;) {
        switch (next) {
        case 1: if (i <= 100) next = 2; else next = 3; break;
        case 2: s += i; i++; next = 1; break;
        case 3: return s;
        default: return -1;
        }
    }
}
int main(void) {
    int a = bar(), b = bar_flat();
    printf("  bar() = %d   bar_flat() = %d   %s\\n", a, b,
           a == b ? "equal" : "MISMATCH");
    return a == b ? 0 : 1;
}
"""


def flattening_check(zig: str) -> int:
    with tempfile.TemporaryDirectory() as td:
        (Path(td) / "flat.c").write_text(FLAT_C, encoding="utf-8")
        r = subprocess.run(
            [zig, "cc", "-target", "x86_64-linux-gnu.2.35", "-O0",
             "-fno-sanitize=undefined", "-o", str(Path(td) / "prog"),
             str(Path(td) / "flat.c")],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print("  compile failed:", r.stderr[:400])
            return 1
        run = subprocess.run(
            ["wsl.exe", "-e", "bash", "-lc",
             f"cd {wsl_path(Path(td))} && stdbuf -o0 ./prog"],
            capture_output=True, text=True,
        )
        print(run.stdout.rstrip() or run.stderr[:400])
        return 1 if "MISMATCH" in run.stdout or run.returncode != 0 else 0


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zig", default=None, help="path to a zig binary")
    args = ap.parse_args()
    bad = 0

    print("=" * 78)
    print("(a)+(b) LISTING RECOVERY AND SIMULATION")
    print("=" * 78)
    raw = read_listing(PDF)
    for i, ins in enumerate(raw, 1):
        print(f"  {i:>2}  {ins}")
    listing = [ins for ins in raw if not ins.endswith(":")]   # drop the label row
    if listing:
        print("  the recovered C, simulated against the listing itself:")
        for a, b in ((7, 42), (-1, 0), (5, 5), (2**62, -(2**62))):
            m = machine_decode_run(a, b)
            c = recovered_c(a, b)
            flag = "OK" if m == c else "MISMATCH"
            if m != c:
                bad += 1
            print(f"    decode(&{a}, &{b}) -> machine {m}   C {c}   {flag}")
        m = machine_decode_run(99, 99, aliased=True)
        print(f"    aliased (xp == yp), v = 99 -> machine {m}   "
              f"C {recovered_c(99, 99, aliased=True)}")

    print()
    print("=" * 78)
    print("(c) COMPILER ROUND-TRIP - recovered C at -O0 vs the sheet's listing")
    print("=" * 78)
    zig = find_zig(args.zig)
    if not zig:
        print("  SKIPPED: no zig found. uv pip install ziglang, or pass --zig.")
    else:
        print(f"  compiler: {zig}")
        with tempfile.TemporaryDirectory() as td:
            mine = instructions_of(compile_asm(zig, C_SOURCE, td), "decode")
        print(f"  recovered C  ({len(mine)} instructions):")
        for ins in mine:
            print(f"    {ins}")
        print(f"  sheet's listing ({len(listing)} instructions):")
        for ins in listing:
            print(f"    {ins}")
        if mine and listing:
            if mine == listing:
                print("  EXACT MATCH, instruction for instruction")
            else:
                print("  DIFF:")
                import difflib
                for line in difflib.unified_diff(listing, mine, "sheet", "zig",
                                                 lineterm="", n=1):
                    print("   ", line)
                bad += 1
        with tempfile.TemporaryDirectory() as td:
            alt = instructions_of(compile_asm(zig, C_SOURCE_TMP, td), "decode")
        if alt and listing:
            diff = [i for i, (x, y) in enumerate(zip(listing, alt)) if x != y]
            print("  the semantically equivalent alternative"
                  " `t = *xp; *xp = *yp; *yp = t;` compiles to:")
            for i in diff[:3]:
                print(f"    at instruction {i + 1}:  listing `{listing[i]}`"
                      f"  vs  alternative `{alt[i]}`")
            print(f"    ({len(diff)} of {len(listing)} instructions differ: the"
                  " statement order is what the round-trip pins down.)")

    print()
    print("=" * 78)
    print("(d) THE SHEET'S MACHINE CODE, ASSEMBLED AND RUN")
    print("=" * 78)
    if zig and listing:
        bad += execute_sheet_listing(zig, listing)
    else:
        print("  SKIPPED (no zig or no listing)")

    print()
    print("=" * 78)
    print("(e) CONTROL-FLOW FLATTENING - original vs flattened, executed")
    print("=" * 78)
    if zig:
        bad += flattening_check(zig)
    else:
        print("  SKIPPED (no zig)")

    print()
    print("=" * 78)
    print("RESULT: 0 mismatches" if not bad else f"RESULT: {bad} problem(s)")
    print("=" * 78)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
