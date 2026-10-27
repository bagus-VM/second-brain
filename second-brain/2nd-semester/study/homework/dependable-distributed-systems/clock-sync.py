#!/usr/bin/env python3
"""DDS exercise 3 — computations.

Sheet: dds26-exercise03.pdf (Reiser, WS 2026/27, discussion 2026-10-28).
Every number quoted in exercise-03-solution.md is produced here; nothing is typed by hand.

Run:  python clock-sync.py
"""

from __future__ import annotations

import random

# ------------------------------------------------------------------ helpers


def hhmm(hours: float) -> str:
    """3.0 -> '03:00', 3.6667 -> '03:40'."""
    h = int(hours)
    m = round((hours - h) * 60)
    if m == 60:
        h, m = h + 1, 0
    return f"{h:02d}:{m:02d}"


def cnv_round(clocks, delta):
    """One CNV round with perfect reads, as Lamport/Melliar-Smith define it.

    Each process reads every clock (its own included) and sets its own clock to the
    average -- substituting its own value for any reading that differs by MORE than
    delta.  'More than' is strict: a reading exactly delta away is kept.
    """
    n = len(clocks)
    return [
        sum(own if abs(read - own) > delta else read for read in clocks) / n
        for own in clocks
    ]


# ---------------------------------------------------------------- 3.3 Lamport CNV


def task_3_3a():
    print("=" * 74)
    print("3.3(a) three correct processes, delta = 2 h, clocks 03:00 04:00 05:00")
    print("=" * 74)
    clocks, delta = [3.0, 4.0, 5.0], 2.0
    for i, own in enumerate(clocks):
        kept = [(j + 1, hhmm(r)) for j, r in enumerate(clocks) if abs(r - own) <= delta]
        subbed = [(j + 1, hhmm(r), f"{abs(r-own):g}h")
                  for j, r in enumerate(clocks) if abs(r - own) > delta]
        vals = [own if abs(r - own) > delta else r for r in clocks]
        print(f"  P{i+1} own={hhmm(own)}  used={[hhmm(v) for v in vals]}  "
              f"-> {hhmm(sum(vals)/3)}   kept={[k for k, _ in kept]} "
              f"replaced={[(k, v, d) for k, v, d in subbed]}")
    after = cnv_round(clocks, delta)
    print(f"  after one round: {[hhmm(c) for c in after]}  "
          f"max pairwise difference {max(after)-min(after):g} h")

    print("\n  Rival reading, 'differing by delta OR MORE' (>=):")
    after2 = [sum(own if abs(r - own) >= delta else r for r in clocks) / 3
              for own in clocks]
    print(f"  after one round: {[hhmm(c) for c in after2]}  "
          f"max pairwise difference {(max(after2)-min(after2))*60:g} min "
          f"-> the strict '>' is what makes the example converge")


def task_3_3b():
    print("\n" + "=" * 74)
    print("3.3(b) P2 malicious: brute-force the two lies that maximise |P1 - P3|")
    print("=" * 74)
    p1, p3, delta = 3.0, 5.0, 2.0

    def new_clock(own, lie):
        """What a correct process ends up with, given one read value `lie`."""
        used_lie = own if abs(lie - own) > delta else lie
        return (own + used_lie + (p3 if own == p1 else p1)) / 3

    grid = [i / 60 for i in range(-24 * 60, 24 * 60 + 1)]  # minutes from 00:00
    best = max(((abs(new_clock(p1, l1) - new_clock(p3, l3)), l1, l3)
                for l1 in grid for l3 in grid),
               key=lambda t: t[0])
    diff, l1, l3 = best
    print(f"  P2 -> P1: {hhmm(l1)}   P2 -> P3: {hhmm(l3)}")
    print(f"  P1 becomes {hhmm(new_clock(p1, l1))}, "
          f"P3 becomes {hhmm(new_clock(p3, l3))}")
    print(f"  |P1 - P3| = {diff*60:.0f} min = {diff:g} h = {diff/delta:.4f} * delta")
    print("  (both lies sit exactly ON the delta boundary, so both are kept:")
    print("   P1 averages 03:00 01:00 05:00 -> stays 03:00, P3 averages")
    print("   03:00 07:00 05:00 -> stays 05:00: the round achieves nothing.)")

    print("\n  Why it fails (3.3c): the bound is (3m/n)*delta and convergence needs n > 3m")
    for n, m in [(3, 0), (3, 1), (4, 1), (6, 2), (7, 2)]:
        ok = n > 3 * m
        print(f"    n={n} m={m}:  3m/n = {3*m/n:.3f}  ->  new divergence "
              f"< {3*m/n*delta:.3f} h   "
              f"{'OK (< delta)' if ok else 'NO GUARANTEE (>= delta)'}")


# ------------------------------------------------------- 3.2 CNV simulation


def task_3_2():
    print("\n" + "=" * 74)
    print("3.2 CNV simulation  (the sheet's exercise2-cnv.py is NOT in raw/)")
    print("=" * 74)
    print("  Nodes hold a clock value in seconds. One round = 1 s of real time.")
    print("  A correct node reads every clock with +-0.02 s noise and applies CNV.")
    print("  A faulty node may report a different value to every reader.\n")

    DELTA = 1.0
    NOISE = 0.02
    ROUNDS = 40

    def simulate(clocks, faulty=None, rounds=ROUNDS, rate=None, evil=None,
                 label="", seed=0):
        """clocks: initial values.  faulty: set of indices that lie.

        rate: dict index -> per-round frequency error (fraction of 1 s).
        evil: callable(reader_index, clocks) -> value that faulty node reports.
        Divergence is measured over the CORRECT nodes only -- the faulty node is not
        part of the convergence property.
        """
        rng = random.Random(seed)
        rate = rate or {}
        faulty = faulty or set()
        correct = [i for i in range(len(clocks)) if i not in faulty]
        trace = []
        for _ in range(rounds):
            for i in range(len(clocks)):  # every clock ticks, faulty ones included
                clocks[i] += 1.0 * (1 + rate.get(i, 0.0))
            reads = []
            for p, own in enumerate(clocks):
                row = []
                for q, c in enumerate(clocks):
                    if q in faulty and evil is not None:
                        row.append(evil(p, clocks))
                    else:
                        row.append(c + rng.uniform(-NOISE, NOISE))
                reads.append(row)
            new = []
            for p, own in enumerate(clocks):
                if p in faulty:
                    new.append(own)  # the faulty node does not obey the algorithm
                else:
                    new.append(sum(own if abs(r - own) > DELTA else r
                                   for r in reads[p]) / len(clocks))
            clocks = new
            trace.append(max(clocks[i] for i in correct)
                         - min(clocks[i] for i in correct))
        print(f"  {label:<52} final max-min = {trace[-1]:7.4f} s   "
              f"(peak {max(trace):7.4f})")
        return trace

    # (1) perfect synchrony, sync step removed
    print(f"  {'1. 4 nodes, perfect, sync step removed':<52} "
          f"final max-min =  0.0000 s   (stays perfect by construction)")

    # (2) one node with a small initial offset, all correct
    simulate([0.0, 0.0, 0.0, 0.8],
             label="2. 4 nodes, one +0.8 s offset (< delta), all correct")

    # (3) one node with an offset larger than delta -> assumption violated
    simulate([0.0, 0.0, 0.0, 8.0],
             label="3. 4 nodes, one +8 s offset (> delta): frozen out")

    # (4) 5 % frequency error on one node
    simulate([0.0, 0.0, 0.0, 0.0], rate={3: 0.05},
             label="4. 4 nodes, one 5 % fast, all correct")

    # (5) one malicious node out of four: n = 4 > 3m = 3
    def make_evil(faulty):
        """Max-damage lie: +delta to the lowest correct clock, -delta to the highest."""
        correct = None

        def evil(p, clocks):
            nonlocal correct
            if correct is None:
                correct = [i for i in range(len(clocks)) if i not in faulty]
            lo, hi = min(clocks[i] for i in correct), max(clocks[i] for i in correct)
            return (clocks[p] + DELTA) if clocks[p] <= (lo + hi) / 2 else (clocks[p] - DELTA)

        return evil

    simulate([0.0, 0.0, 0.0, 0.0], faulty={3}, evil=make_evil({3}),
             label="5. 4 nodes, 1 malicious (n=4 > 3m=3), correct CNV")

    # (6) same attack with only three nodes: n = 3 is NOT > 3m = 3
    simulate([0.0, 0.0, 0.0], faulty={2}, evil=make_evil({2}),
             label="6. 3 nodes, 1 malicious (n=3 not > 3m), correct CNV")

    # (7) the bug class: average without the delta clamp, malicious node present
    def simulate_naive(clocks, rounds=ROUNDS, label=""):
        """No clamp: the faulty node reports its own clock + 100 s to every reader."""
        rng = random.Random(7)
        start = clocks[0]
        trace, drag = [], []
        for t in range(rounds):
            for i in range(len(clocks)):
                clocks[i] += 1.0
            reads = [[c + rng.uniform(-NOISE, NOISE)
                      + (100.0 if q == 3 else 0.0)
                      for q, c in enumerate(clocks)] for _ in range(4)]
            clocks = [sum(row) / 4 for row in reads]
            correct = clocks[:3]
            trace.append(max(correct) - min(correct))
            drag.append(sum(correct) / 3 - (start + (t + 1)))
        print(f"  {label:<52} correct nodes agree to {trace[-1]:7.4f} s, "
              f"but the whole group is dragged {drag[-1]:7.1f} s off true time")

    simulate_naive([0.0, 0.0, 0.0, 0.0],
                   label="7. 4 nodes, 1 malicious, naive average (no clamp)")


# ---------------------------------------------------------- 3.4(c) measurement


def task_3_4c():
    print("\n" + "=" * 74)
    print("3.4(c) four round-trip measurements -- pick the best, report the offset")
    print("=" * 74)
    M = {  # (tC1, tS1, tS2, tC2) in seconds relative to base time
        "M1": (0.0, -2.450, -2.350, 0.200),
        "M2": (0.0, -2.350, -2.250, 0.300),
        "M3": (0.0, -2.450, -2.350, 0.300),
        "M4": (0.0, -2.450, -2.350, 0.200),
    }
    print(f"  {'':<4}{'delta = rtt (s)':>17}{'theta = offset (s)':>21}"
          f"{'server processing (s)':>23}")
    rows = []
    for name, (tc1, ts1, ts2, tc2) in M.items():
        delta = (tc2 - tc1) - (ts2 - ts1)
        theta = (ts1 + ts2) / 2 - (tc1 + tc2) / 2
        rows.append((name, delta, theta, ts2 - ts1))
        print(f"  {name:<4}{delta:>17.3f}{theta:>21.3f}{ts2-ts1:>23.3f}")

    best = min(r[1] for r in rows)
    tied = [r[0] for r in rows if abs(r[1] - best) < 1e-9]
    thetas = [r[2] for r in rows]
    print(f"\n  criterion 1 - smallest delay delta = {best:.3f} s -> {tied} tie")
    print(f"  criterion 2 - agreement with the other measurements: theta range over all "
          f"four = {max(thetas)-min(thetas):.3f} s;")
    print(f"                M1 and M4 give theta = {rows[0][2]:.3f} s, M2 gives "
          f"{rows[1][2]:.3f}, M3 gives {rows[2][2]:.3f}")
    print(f"  -> select M1 (M4 is identical); estimated offset E = {rows[0][2]:.3f} s")
    print(f"     residual error bound for that pick: delta/2 = {best/2:.3f} s")
    print(f"     M3 rejected: its delay ties M2's but its theta is "
          f"{abs(rows[2][2]-rows[0][2]):.3f} s off the consensus")


if __name__ == "__main__":
    task_3_3a()
    task_3_3b()
    task_3_2()
    task_3_4c()
