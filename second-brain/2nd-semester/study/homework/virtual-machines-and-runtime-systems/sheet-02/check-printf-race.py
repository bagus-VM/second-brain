#!/usr/bin/env python3
"""Problem 3(c) evidence check — printf is not reentrant.

Reads the raw runs produced by

    ./printf-race naive    > naive-N.txt
    ./printf-race deferred > deferred-N.txt

and reports, per file: bytes, how many records came out complete (a header plus
exactly 200 '<' then exactly 200 '>' then a newline), how many markers were
written, how many records were TORN (cut off in the middle by another record's
header), and how many (thread, index) records appear more than once.

Program under test: printf-race.c in this directory. Build:
    gcc -Wall -U_FORTIFY_SOURCE -o printf-race printf-race.c
Loop bound is 200 records per thread and there are 2 threads, so a correct run
is exactly 400 complete records in 162800 bytes.
"""
import collections
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECORD = re.compile(r"([AB]) (\d{3}) ")
FULL = re.compile(r"[AB] \d{3} <{200}>{200}\n")


def check(path: Path):
    text = path.read_bytes().decode("utf-8", "replace")
    complete = len(FULL.findall(text))
    markers = len(RECORD.findall(text))

    torn = 0
    for m in RECORD.finditer(text):
        seg = text[m.end():m.end() + 401]
        run = len(re.match(r"<*", seg).group())
        if run != 200 or seg[run:run + 200] != ">" * 200 or seg[run + 200:run + 201] != "\n":
            torn += 1

    counts = collections.Counter(m.group(0).strip() for m in RECORD.finditer(text))
    dupes = sum(1 for v in counts.values() if v > 1)
    return len(text.encode()), complete, markers, torn, dupes, max(counts.values(), default=0)


def main(argv):
    files = [Path(a) for a in argv] or sorted(HERE.glob("naive-*.txt")) + sorted(HERE.glob("deferred-*.txt"))
    if not files:
        print("no race-*.txt found — run ./printf-race naive > naive-1.txt first")
        return 1

    head = f"{'file':20}{'bytes':>9}{'complete':>10}{'markers':>9}{'torn':>7}{'dup pairs':>11}{'max rep':>9}"
    print(head)
    print("-" * len(head))
    for f in files:
        b, c, m, t, d, r = check(f)
        print(f"{f.name:20}{b:9}{c:10}{m:9}{t:7}{d:11}{r:9}")

    print()
    print("expected for a correct run: 400 complete, 400 markers, 0 torn, 0 duplicated")
    print("naive    -> extra markers + torn records + duplicated work: stdio state damaged")
    print("deferred -> exact, and byte-identical across runs")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
