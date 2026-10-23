"""
Dependable Distributed Systems (Reiser, 5880V/UE) — exercise computations.

Every number printed here is computed, not copied from a slide. The two
executable results are:

  * Exercise 1.3(c)  — availability of system A vs. system B.
  * Exercise 2.6     — Lamport and vector timestamps for the time-space
                       diagram, plus a total order derived from each, plus a
                       check that the timestamps do not depend on which
                       linearisation of the concurrent events is chosen.

The diagram of Exercise 2.6 was read out of the PDF's vector geometry, not
from the garbled text layer: the three process lifelines are horizontal
(y = 254.4 P1, 282.8 P2, 311.1 P3) and time runs left to right along the
"t" arrow at the bottom. Dots and the single message arrow m1:

    P1 :  e1,1 (x=223.9)   e1,2 (x=308.9)   e1,3 (x=408.1)
    P2 :  e2,1 (x=252.2)   e2,2 (x=379.8)
    P3 :  e3,1 (x=238.1)   e3,2 (x=365.6)
    m1 :  e2,1 -> e3,2      (arrowhead on P3 at e3,2)

Run:  python logical-clocks.py
"""

from itertools import permutations

# --------------------------------------------------------------------------
# Exercise 1.3(c):  which system is more available?
# --------------------------------------------------------------------------
# Availability = MTBF / (MTBF + MTTR)   (slide: "Dependability attributes")

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24


def availability(mtbf_hours: float, mttr_hours: float) -> float:
    return mtbf_hours / (mtbf_hours + mttr_hours)


# A: fails once per year, takes one day to repair.
A_MTBF = DAYS_PER_YEAR * HOURS_PER_DAY
A_MTTR = 1 * HOURS_PER_DAY
# B: fails once per week, takes one hour to repair.
B_MTBF = 7 * HOURS_PER_DAY
B_MTTR = 1


def exercise_1_3c():
    a = availability(A_MTBF, A_MTTR)
    b = availability(B_MTBF, B_MTTR)
    print("=" * 72)
    print("Exercise 1.3(c) -- availability")
    print("=" * 72)
    print("  A: MTBF = {:>5.0f} h, MTTR = {:>3.0f} h  ->  A = MTBF/(MTBF+MTTR) = "
          "{:.6f}".format(A_MTBF, A_MTTR, a))
    print("  B: MTBF = {:>5.0f} h, MTTR = {:>3.0f} h  ->  B = MTBF/(MTBF+MTTR) = "
          "{:.6f}".format(B_MTBF, B_MTTR, b))
    print("  downtime fraction  A = {:.6f}   B = {:.6f}".format(1 - a, 1 - b))
    more = "A" if a > b else "B"
    print("  -> system {} is more available, by {:.6f} percentage points."
          .format(more, 100 * abs(a - b)))
    print("     A's MTBF is {:.0f}x longer than B's, but A needs {:.0f}x longer to repair;"
          .format(A_MTBF / B_MTBF, A_MTTR / B_MTTR))
    print("     repair time is negligible against either failure interval, so the")
    print("     failure rate decides. Availability is not 'how often' but 'how long'.")
    return a, b


# --------------------------------------------------------------------------
# Exercise 2.6: the time-space diagram
# --------------------------------------------------------------------------
# Program order per process, and the one message.
PROCESS_OF = {
    "e1,1": 1, "e1,2": 1, "e1,3": 1,
    "e2,1": 2, "e2,2": 2,
    "e3,1": 3, "e3,2": 3,
}
PROGRAM_ORDER = [
    ("e1,1", "e1,2"), ("e1,2", "e1,3"),   # P1
    ("e2,1", "e2,2"),                    # P2
    ("e3,1", "e3,2"),                    # P3
]
MESSAGES = [("m1", "e2,1", "e3,2")]      # (name, send event, receive event)
EVENTS = list(PROCESS_OF)

# Real-time order of the diagram (x coordinate, time runs to the right).
REAL_TIME_ORDER = [
    "e1,1",   # x = 223.9
    "e3,1",   # x = 238.1
    "e2,1",   # x = 252.2
    "e1,2",   # x = 308.9
    "e3,2",   # x = 365.6
    "e2,2",   # x = 379.8
    "e1,3",   # x = 408.1
]


def causal_predecessors():
    """happens-before predecessors of every event."""
    preds = {e: set() for e in EVENTS}
    for a, b in PROGRAM_ORDER:
        preds[b].add(a)
    for _name, snd, rcv in MESSAGES:
        preds[rcv].add(snd)
    return preds


def linear_extensions():
    """All total orders of the events consistent with happens-before."""
    preds = causal_predecessors()
    order, remaining = [], list(EVENTS)
    while remaining:
        for e in list(remaining):
            if preds[e] <= set(order):
                order.append(e)
                remaining.remove(e)
                break
        else:
            raise RuntimeError("cycle in happens-before")
    return order


def all_linear_extensions():
    """Every linear extension (small enough to enumerate exhaustively)."""
    preds = causal_predecessors()
    results = []

    def rec(prefix, remaining):
        if not remaining:
            results.append(list(prefix))
            return
        for e in list(remaining):
            if preds[e] <= set(prefix):
                rec(prefix + [e], [r for r in remaining if r != e])

    rec([], list(EVENTS))
    return results


def lamport_timestamps(order):
    """Slide rule: local action/send C = C+1; receive C = max(C, tm)+1."""
    c = {p: 0 for p in (1, 2, 3)}
    ts = {}
    sent = {}                       # message -> timestamp carried
    recv_event = {rcv: (name, snd) for name, snd, rcv in MESSAGES}
    for e in order:
        p = PROCESS_OF[e]
        if e in recv_event:
            name, snd = recv_event[e]
            c[p] = max(c[p], sent[name]) + 1
        else:
            c[p] = c[p] + 1
        ts[e] = c[p]
        for name, snd, rcv in MESSAGES:
            if snd == e:
                sent[name] = c[p]
    return ts


def vector_timestamps(order, n=3):
    """Slide rule: own component +1 per local event; merge on receive."""
    v = {p: [0] * n for p in (1, 2, 3)}
    ts = {}
    sent = {}
    recv_event = {rcv: (name, snd) for name, snd, rcv in MESSAGES}
    for e in order:
        p = PROCESS_OF[e]
        if e in recv_event:
            name, snd = recv_event[e]
            v[p][p - 1] += 1
            for k in range(n):
                v[p][k] = max(v[p][k], sent[name][k])
        else:
            v[p][p - 1] += 1
        ts[e] = tuple(v[p])
        for name, snd, rcv in MESSAGES:
            if snd == e:
                sent[name] = tuple(v[p])
    return ts


def lamport_total_order(ts):
    """(C_i, i) lexicographic -- the lecture's extension of the partial order."""
    return sorted(ts, key=lambda e: (ts[e], PROCESS_OF[e]))


def vector_total_order(ts):
    """Lexicographic on the vector; a linear extension of the causal order."""
    return sorted(ts, key=lambda e: (ts[e], PROCESS_OF[e]))


def vector_le(a, b):
    """Vector-clock causality: a happens-before b."""
    return all(x <= y for x, y in zip(a, b)) and a != b


def check_linear_extension(order, ts, causal):
    """Every causally ordered pair must appear in the given order."""
    pos = {e: i for i, e in enumerate(order)}
    for a, b in causal:
        if pos[a] > pos[b]:
            return False, "{} precedes {} but {} happens-before {}".format(b, a, a, b)
    return True, ""


def exercise_2_6():
    print()
    print("=" * 72)
    print("Exercise 2.6 -- the diagram")
    print("=" * 72)
    print("  P1: e1,1 -> e1,2 -> e1,3")
    print("  P2: e2,1 -> e2,2")
    print("  P3: e3,1 -> e3,2")
    print("  m1: e2,1 -> e3,2   (the only message; e3,2 receives it)")

    causal = causal_predecessors()
    causal_pairs = []
    for a, b in PROGRAM_ORDER:
        causal_pairs.append((a, b))
    for _n, snd, rcv in MESSAGES:
        causal_pairs.append((snd, rcv))

    # ---- Lamport ---------------------------------------------------------
    ts = lamport_timestamps(REAL_TIME_ORDER)
    print()
    print("  (a) Lamport timestamps")
    for e in REAL_TIME_ORDER:
        print("      {:5}  C = {}".format(e, ts[e]))

    order = lamport_total_order(ts)
    print("      total order via (C_i, i):")
    print("        " + "  <  ".join(order))
    ok, why = check_linear_extension(order, ts, causal_pairs)
    print("      is a linear extension of happens-before: {} {}".format(ok, why))

    # ---- Vector ----------------------------------------------------------
    vts = vector_timestamps(REAL_TIME_ORDER)
    print()
    print("  (b) Vector timestamps")
    for e in REAL_TIME_ORDER:
        print("      {:5}  V = {}".format(e, vts[e]))

    vorder = vector_total_order(vts)
    print("      total order via lexicographic vector comparison:")
    print("        " + "  <  ".join(vorder))
    ok2, why2 = check_linear_extension(vorder, vts, causal_pairs)
    print("      is a linear extension of happens-before: {} {}".format(ok2, why2))
    print("      (lexicographic order is a valid linear extension because")
    print("       causality gives V(a) <= V(b) componentwise and V(a) != V(b),")
    print("       so the first differing component is strictly smaller for a)")

    # ---- Do the timestamps depend on the linearisation? -------------------
    exts = all_linear_extensions()
    lam = {tuple(lamport_timestamps(o)[e] for e in EVENTS) for o in exts}
    vec = {tuple(vector_timestamps(o)[e] for e in EVENTS) for o in exts}
    print()
    print("  Robustness: {} linear extensions of happens-before exist.".format(len(exts)))
    print("    distinct Lamport assignments over all of them: {}".format(len(lam)))
    print("    distinct vector assignments over all of them:  {}".format(len(vec)))
    print("    -> the timestamps are determined by causality alone, not by")
    print("       the order in which concurrent events are listed.")

    # ---- Which events are concurrent? -------------------------------------
    print()
    print("  Concurrency (neither a->b nor b->a):")
    concurrent = []
    for a in EVENTS:
        for b in EVENTS:
            if a < b and not vector_le(vts[a], vts[b]) and not vector_le(vts[b], vts[a]):
                concurrent.append((a, b))
    for a, b in concurrent:
        print("      {} || {}   (C: {} / {},  V: {} / {})".format(
            a, b, ts[a], ts[b], vts[a], vts[b]))
    return ts, vts, order, vorder, len(exts)


# --------------------------------------------------------------------------
# Cross-check: the professor's own example on slide 34
# --------------------------------------------------------------------------
# Slide 34 shows P1 with Lamport times 1,2,5,6,7 and P2 with 3,4,5,6,7,8,
# and three messages: P1(2) -> P2(7), P2(4) -> P1(5), P2(6) -> P1(7).
# Every printed number satisfies the slide's rule EXCEPT P2's first event,
# which is printed as 3 although no message precedes it.


def check_slide_34():
    print()
    print("=" * 72)
    print("Cross-check -- the professor's example (lecture 2, slide 34)")
    print("=" * 72)
    # Read out of the PDF's vector geometry (page 42), not the text layer:
    #   P2 line y=78.35, P1 line y=138.89, time runs left to right.
    #   P2 dots: x=85.4(3) 120.0(4) 163.2(5) 206.4(6) 241.0(7) 292.9(8)
    #   P1 dots: x=94.0(1) 120.0(2) 171.8(5) 206.4(6) 258.3(7)
    #   arrows: (120.0,138.9)->(241.0,78.4)   P1's 2  -> P2's 7   label (2)
    #           (120.0, 78.4)->(171.8,138.9)  P2's 4  -> P1's 5   label (4)
    #           (206.4, 78.4)->(258.3,138.9)  P2's 6  -> P1's 7   label (6)
    #
    # Rule under test:  receive  ->  C = max(C_before_receive, t_message) + 1
    #                   local    ->  C = C + 1
    p1 = [(94.0, 1), (120.0, 2), (171.8, 5), (206.4, 6), (258.3, 7)]
    p2 = [(85.4, 3), (120.0, 4), (163.2, 5), (206.4, 6), (241.0, 7), (292.9, 8)]
    # (clock before the receive, timestamp carried by the message)
    receives = {
        ("P1", 171.8): (2, 4),   # P1 receives (4): C was 2, message carries 4
        ("P1", 258.3): (6, 6),   # P1 receives (6): C was 6, message carries 6
        ("P2", 241.0): (6, 2),   # P2 receives (2): C was 6, message carries 2
    }
    problems = []
    for name, seq in (("P1", p1), ("P2", p2)):
        prev = 0
        for x, shown in seq:
            if (name, x) in receives:
                before, tm = receives[(name, x)]
                expect = max(before, tm) + 1
                kind = "receive(t={})".format(tm)
            else:
                expect = prev + 1
                kind = "local"
            if expect != shown:
                problems.append(
                    "{} x={:6.1f} shown {:>2} expected {:>2}  [{}]".format(
                        name, x, shown, expect, kind))
            prev = shown
    print("  P1 sequence as printed: {}".format([c for _x, c in p1]))
    print("  P2 sequence as printed: {}".format([c for _x, c in p2]))
    print("  messages: (2) P1->P2, (4) P2->P1, (6) P2->P1")
    if problems:
        print("  MISMATCHES:")
        for p in problems:
            print("    " + p)
    else:
        print("  all printed values satisfy the slide's rule")
    print("  -> P1's first event is 1, so P1's initial clock is 0. P2's first")
    print("     event is 3, so P2's initial clock would have to be 2. The slide")
    print("     does not say this; it presents both processes side by side.")
    return problems


if __name__ == "__main__":
    exercise_1_3c()
    ts, vts, order, vorder, n_ext = exercise_2_6()
    check_slide_34()
    print()
    print("=" * 72)
    print("done")
    print("=" * 72)
