#!/usr/bin/env python3
"""
Homework 1 (Reverse- and Reengineering, 20.10.2026) - CFG, PDG and program slices,
computed from a model of the program rather than drawn by hand.

Program (from the sheet):

     1 int main() {
     2 int x, y, prod, lcm, gcd=1;
     3 scanf("%d", &x);
     4 scanf("%d", &y);
     5 for (int i=1;i <= x && i <= y; ++i) {
     6     if (x%i==0 && y%i==0) {
     7        gcd=i;
     8     }
     9 }
    10 prod=x*y;
    11 lcm=prod/gcd;
    12 printf("gcd=%d",gcd);
    13 printf("prod=%d", prod);
    14 printf("lcm=%d", lcm);
    15 }

The sheet's instruction: "Assume scanf defines the variable and printf uses the variable."

Model:
  * one node per source line (statement granularity)
  * node 9 is the loop latch, node 15 the exit block
  * def/use sets follow the sheet: scanf defines, printf uses
  * the declaration line 2 defines gcd (=1) only; x, y, prod and lcm are declared
    there and defined later, so line 2 contributes no definition of them
  * line 5 both defines i (init) and increments it (++i); both are modelled as the
    single definition "i is defined at line 5", which is the standard treatment for
    a for-header with a loop-carried variable

Analyses:
  * intraprocedural CFG
  * reaching definitions (iterative, flow-sensitive, "must") -> data dependencies
  * post-dominators -> control dependencies (Cytron et al., restricted to branching
    nodes, which is the usual implementation)
  * PDG = data dependencies + control dependencies
  * backward slice of line 13 and of line 14, forward slice of `int i=1` (line 5),
    each computed twice: on data dependencies alone, and on data + control

Run:  python hw01-slices.py
"""

from collections import defaultdict

EXIT = "EXIT"

# --------------------------------------------------------------------------
# The program
# --------------------------------------------------------------------------

# node -> (label, defs, uses)
PROGRAM = {
    1:  ("int main() {",                 [],       []),
    2:  ("int x,y,prod,lcm,gcd=1;",      ["gcd"], []),
    3:  ('scanf("%d", &x);',             ["x"],   []),
    4:  ('scanf("%d", &y);',             ["y"],   []),
    5:  ("for (int i=1; i<=x && i<=y; ++i) {", ["i"], ["x", "y"]),
    6:  ("if (x%i==0 && y%i==0) {",      [],      ["x", "y", "i"]),
    7:  ("gcd=i;",                       ["gcd"], ["i"]),
    8:  ("}",                            [],      []),
    9:  ("}",                            [],      []),
    10: ("prod=x*y;",                     ["prod"], ["x", "y"]),
    11: ("lcm=prod/gcd;",                 ["lcm"], ["prod", "gcd"]),
    12: ('printf("gcd=%d",gcd);',         [],      ["gcd"]),
    13: ('printf("prod=%d", prod);',      [],      ["prod"]),
    14: ('printf("lcm=%d", lcm);',        [],      ["lcm"]),
    15: ("}",                            [],      []),
}

NODES = sorted(PROGRAM)

# intraprocedural control flow graph
CFG = {
    1:  [2],
    2:  [3],
    3:  [4],
    4:  [5],
    5:  [5, 6, 10],      # back edge, body, loop exit
    6:  [7, 9],          # then, else
    7:  [8],
    8:  [9],
    9:  [5],             # latch
    10: [11],
    11: [12],
    12: [13],
    13: [14],
    14: [15],
    15: [EXIT],
}

PRED = defaultdict(list)
for a, succs in CFG.items():
    for b in succs:
        PRED[b].append(a)

BRANCHING = {n for n in NODES if len(CFG[n]) > 1}


def label(n):
    if n == EXIT:
        return "exit"
    return PROGRAM[n][0]


def name(n):
    return f"L{n}" if n != EXIT else "EXIT"


# --------------------------------------------------------------------------
# Reaching definitions  ->  data dependencies
# --------------------------------------------------------------------------

def defs_of(var):
    return {n for n in NODES if var in PROGRAM[n][1]}


def gen_kill(n):
    gen, kill = set(), set()
    for var in PROGRAM[n][1]:
        gen.add((var, n))
        for d in defs_of(var):
            if d != n:
                kill.add((var, d))
    return gen, kill


def reaching_definitions():
    """Iterative must-analysis over the CFG."""
    gen, kill = {}, {}
    for n in NODES:
        g, k = gen_kill(n)
        gen[n], kill[n] = g, k

    out = {n: set(gen[n]) for n in NODES}
    inn = {n: set() for n in NODES}
    changed = True
    while changed:
        changed = False
        for n in NODES:
            new_in = set()
            for p in PRED[n]:
                new_in |= out[p]
            new_out = gen[n] | (new_in - kill[n])
            if new_in != inn[n] or new_out != out[n]:
                inn[n], out[n] = new_in, new_out
                changed = True
    return inn, out


def data_dependencies(inn):
    """Edge (d, u) when a definition d reaches a use of the same variable in u."""
    edges = set()
    for n in NODES:
        for var in PROGRAM[n][2]:
            for (v, d) in inn[n]:
                if v == var:
                    edges.add((d, n))
    return edges


# --------------------------------------------------------------------------
# Post-dominators  ->  control dependencies
# --------------------------------------------------------------------------

def reachable_from():
    """Nodes reachable from each node (including itself)."""
    reach = {n: set() for n in NODES}
    for start in NODES:
        seen, stack = {start}, [start]
        while stack:
            cur = stack.pop()
            reach[start].add(cur)
            for nxt in CFG[cur]:
                if nxt == EXIT:
                    continue
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return reach


def post_dominators():
    """
    post[n] = the set of nodes that post-dominate n, i.e. that lie on EVERY
    path from n to the exit.

    X post-dominates n iff X post-dominates every successor of n, so the
    recurrence intersects over successors.  Iterating from the universe downwards
    converges to the greatest fixed point, which is the post-dominator set.
    """
    universe = set(NODES) | {EXIT}
    post = {EXIT: {EXIT}}
    for n in NODES:
        post[n] = set(universe)
    changed = True
    while changed:
        changed = False
        for n in reversed(NODES):
            new = None
            for s in CFG[n]:
                new = set(post[s]) if new is None else (new & post[s])
            if new is None:
                new = set()
            new = new | {n}
            if new != post[n]:
                post[n] = new
                changed = True
    return post


def control_dependencies(post, reach):
    """
    Control dependence, in the sense the lecture states it: "a control dependency
    exists between two nodes A and B if node A determines the execution (if or how
    many times) of node B".

    Operationalisation:
      B is control dependent on branching node A iff
        (1) B is reachable from A, and
        (2) some path from A to the exit avoids B
            (equivalently: B does NOT post-dominate A), and
        (3) A is not B.

    Condition (2) is what makes a merge point such as the loop latch NOT control
    dependent on the inner if: every path out of the inner if passes through the
    latch, so the if does not determine whether the latch executes.

    NOTE on the alternative textbook definition (Cytron et al., via immediate
    post-dominators): that definition also reports the statement AFTER a loop as
    control dependent on the loop test, because the loop exit edge makes the
    condition "determine" it.  Under the semantic rule used here, the statement
    after a loop always executes and is therefore not control dependent on the
    loop test.  Both readings are discussed in the solution page.
    """
    edges = set()
    for a in BRANCHING:
        for b in reach[a]:
            if b == a or b == EXIT:
                continue
            if b not in post[a]:       # some path from a to the exit avoids b
                edges.add((a, b))
    return edges


# --------------------------------------------------------------------------
# Slices
# --------------------------------------------------------------------------

def _closure(criterion, back_edges):
    seen, stack = {criterion}, [criterion]
    while stack:
        n = stack.pop()
        for p in back_edges.get(n, ()):  # predecessors
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


def _closure_fwd(criterion, fwd_edges):
    seen, stack = {criterion}, [criterion]
    while stack:
        n = stack.pop()
        for s in fwd_edges.get(n, ()):  # successors
            if s not in seen:
                seen.add(s)
                stack.append(s)
    return seen


def slices(criterion, data_edges, ctrl_edges):
    """Return (value slice, conservative slice) for a slicing criterion."""
    back_data, fwd_data = defaultdict(set), defaultdict(set)
    for (d, u) in data_edges:
        back_data[u].add(d)
        fwd_data[d].add(u)

    back_all = defaultdict(set)
    fwd_all = defaultdict(set)
    for k, v in back_data.items():
        back_all[k] |= v
    for k, v in fwd_data.items():
        fwd_all[k] |= v
    for (b, a) in ctrl_edges:
        back_all[a].add(b)      # a is controlled by b
        fwd_all[b].add(a)

    return (_closure(criterion, back_data), _closure(criterion, back_all),
            _closure_fwd(criterion, fwd_data), _closure_fwd(criterion, fwd_all))


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

def print_edges(title, edges):
    print(title)
    by_src = defaultdict(list)
    for (a, b) in sorted(edges):
        by_src[a].append(b)
    if not by_src:
        print("    (none)")
    for a in sorted(by_src):
        outs = ", ".join(name(b) for b in sorted(by_src[a]))
        print(f"    {name(a):>4} ({label(a)})  ->  {outs}")
    print()


def main():
    inn, _out = reaching_definitions()
    data_edges = data_dependencies(inn)
    post = post_dominators()
    reach = reachable_from()
    ctrl_edges = control_dependencies(post, reach)

    print("=" * 78)
    print("Homework 1 - Intra-procedural CFG, PDG and program slicing")
    print("=" * 78)
    print()

    print("-" * 78)
    print("1. Intra-procedural control flow graph")
    print("-" * 78)
    print()
    print_edges("    CFG edges:", {(a, b) for a in CFG for b in CFG[a]})

    print("-" * 78)
    print("2. Program dependence graph")
    print("-" * 78)
    print()
    print_edges("    Data dependencies (definition -> use):", data_edges)
    print_edges("    Control dependencies (branch -> controlled statement):", ctrl_edges)
    print("    PDG = data dependencies + control dependencies")
    print("    Post-dominator sets (used for the control dependencies):")
    for n in NODES:
        print(f"        post[L{n}] = {{{', '.join(name(x) for x in sorted(post[n], key=str))}}}")
    print()

    print("-" * 78)
    print("3. Backward slices")
    print("-" * 78)
    print()
    for crit, desc in ((13, 'line 13  printf("prod=%d", prod)'),
                       (14, 'line 14  printf("lcm=%d", lcm)')):
        val, cons, _, _ = slices(crit, data_edges, ctrl_edges)
        print(f'    Backward slice of {desc}:')
        print('        value slice (data dependencies only):')
        for n in sorted(val):
            print(f"            {name(n):>4}  {label(n)}")
        print('        conservative slice (data + control dependencies):')
        for n in sorted(cons):
            print(f"            {name(n):>4}  {label(n)}")
        print()

    print("-" * 78)
    print("4. Forward slice")
    print("-" * 78)
    print()
    crit = 5
    _, _, val, cons = slices(crit, data_edges, ctrl_edges)
    print('    Forward slice of the statement `int i=1` at line 5:')
    print('        value slice (data dependencies only):')
    for n in sorted(val):
        print(f"            {name(n):>4}  {label(n)}")
    print('        conservative slice (data + control dependencies):')
    for n in sorted(cons):
        print(f"            {name(n):>4}  {label(n)}")
    print()

    print("-" * 78)
    print("5. Statements excluded from each slice, and the reaching definitions")
    print("-" * 78)
    print()
    _, b13, _, _ = slices(13, data_edges, ctrl_edges)
    _, b14, _, _ = slices(14, data_edges, ctrl_edges)
    _, _, f5, _ = slices(5, data_edges, ctrl_edges)
    print("    conservative backward slice of 13 excludes:",
          ", ".join(name(n) for n in sorted(set(NODES) - b13)))
    print("    conservative backward slice of 14 excludes:",
          ", ".join(name(n) for n in sorted(set(NODES) - b14)))
    print("    conservative forward slice of 5 excludes:",
          ", ".join(name(n) for n in sorted(set(NODES) - f5)))
    print()
    print("    reaching definitions at each use site:")
    for n in NODES:
        uses = PROGRAM[n][2]
        if not uses:
            continue
        rd = {}
        for (v, d) in inn[n]:
            rd.setdefault(v, []).append(d)
        txt = ", ".join(f"{v}@{sorted(rd[v])}" for v in sorted(rd) if v in uses)
        print(f"        L{n}: uses {uses}  <-  {txt}")
    print()


if __name__ == "__main__":
    main()
