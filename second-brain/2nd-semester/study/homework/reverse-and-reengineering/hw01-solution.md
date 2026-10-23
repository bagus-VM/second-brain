---
title: "Homework 1 — Reverse- and Reengineering: CFG, PDG and program slicing"
tags: [homework, reverse-and-reengineering, semester-2, program-slicing]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

# Homework 1 (20.10.2026) — Intra-Procedural CFG, PDG and Program Slicing

The sheet states: *"This sheet is not for submission. However, we strongly encourage you to
solve the problems and bring your solutions to the tutorials for discussion."* The solutions
below were **computed**, not drawn by hand: `hw01-slices.py` models the program, builds the CFG,
runs a reaching-definitions analysis for the data dependencies, computes post-dominators for the
control dependencies, and derives the three slices. The recorded run is in
`hw01-slices-output.txt`.

## The program

```c
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
```

The sheet's instruction: *"Assume scanf defines the variable and printf uses the variable."*

**Modelling decisions** (they change the answer, so they are stated):

- One node per source line (statement granularity). Line 9 is the loop latch, line 15 the exit.
- Line 2 defines `gcd` (=1) only. `x`, `y`, `prod` and `lcm` are *declared* there and defined
  later, so line 2 contributes no definition of them — this is why line 2 does not appear in the
  backward slice of line 13.
- Line 5 both defines `i` (init) and increments it (`++i`). Both are modelled as the single
  definition "i is defined at line 5", the standard treatment for a for-header with a
  loop-carried variable.

## 1. The intra-procedural CFG

```
      entry
        |
        v
  L1 --> L2 --> L3 --> L4 --> L5
                                   |   \\\\
                                   |    \ (loop exit)
                                   |     v
                                   |    L10 --> L11 --> L12 --> L13 --> L14 --> L15 --> EXIT
                                   |     ^
                                   |    /
                                   v   /
                            L6 --> L9
                            |     ^
                            v     |
                            L7 -> L8
```

- `L5` has three successors: the **back edge** to itself (next iteration), `L6` (loop body) and
  `L10` (loop exit). The condition `i <= x && i <= y` is false on the first test for `L10`.
- `L6` (the `if`) branches to `L7` (then) or `L9` (else). `L9` is the loop latch and goes back to
  `L5`.

## 2. The program dependence graph

The PDG drops the statement order and keeps two kinds of edge: **data dependencies** and **control
dependencies**. The lecture's definitions:

> "Control dependence: a control dependency exists between two nodes A and B if node A determines
> the execution (if or how many times) of node B."

> "Data dependence: There is a data dependence between two nodes A and B if: B uses a variable
> that was assigned a value at A, and there is a path from A to B in the control flow graph
> without a value being assigned to this variable again."

### Data dependencies (computed by reaching definitions)

| From | To | Variable |
|------|----|----------|
| L2 `gcd=1` | L11 `lcm=prod/gcd`, L12 `printf(gcd)` | gcd |
| L3 `scanf(&x)` | L5, L6, L10 | x |
| L4 `scanf(&y)` | L5, L6, L10 | y |
| L5 `int i=1` | L6, L7 | i |
| L7 `gcd=i` | L11, L12 | gcd |
| L10 `prod=x*y` | L11, L13 | prod |
| L11 `lcm=prod/gcd` | L14 | lcm |

The reaching-definition sets that produce this table are in the recorded output, e.g. at line 11
the reaching definitions of `gcd` are `{gcd@2, gcd@7}` — the initialiser *and* the assignment
inside the loop — because the loop may execute zero times.

### Control dependencies (computed from post-dominators)

| Branch | Controls |
|--------|----------|
| L5 (the `for` test) | L6, L7, L8, L9 |
| L6 (the `if`) | L7, L8 |

**A note on the definition.** The classical Cytron et al. formulation (via immediate
post-dominators) also reports the statement *after* a loop as control dependent on the loop test,
because the loop-exit edge makes the condition "determine" it. Under the lecture's own wording —
"determines the execution (if or how many times)" — the statement after a loop always executes
and is therefore *not* control dependent on the loop test. This vault uses the lecture's
semantic reading, so `L10` is not control dependent on `L5`. The two readings are recorded here
because the difference is exactly the kind of detail an exam question can turn on.

## 3. Backward slices

**Backward slice of line 13** (`printf("prod=%d", prod)`) — the statements that can influence it:

```
L3   scanf("%d", &x);
L4   scanf("%d", &y);
L10  prod=x*y;
L13  printf("prod=%d", prod);
```

`prod` depends only on `x` and `y`, so the whole gcd/lcm computation drops out: `L2`, `L5`, `L6`,
`L7`, `L8`, `L9`, `L11` and `L12` are **not** in the slice. That is the payoff of slicing — 4 of
15 statements instead of all of them.

**Backward slice of line 14** (`printf("lcm=%d", lcm)`):

```
L2   int x,y,prod,lcm,gcd=1;
L3   scanf("%d", &x);
L4   scanf("%d", &y);
L5   for (int i=1; i<=x && i<=y; ++i) {
L6   if (x%i==0 && y%i==0) {
L7   gcd=i;
L10  prod=x*y;
L11  lcm=prod/gcd;
L14  printf("lcm=%d", lcm);
```

`lcm` depends on `prod` *and* on `gcd`, and `gcd` is assigned inside the loop from `i`, so the
loop and the `if` come back in. `L8` and `L9` are the closing braces and drop out.

## 4. Forward slice

**Forward slice of `int i=1` at line 5** — the statements it can influence:

```
L5   for (int i=1; i<=x && i<=y; ++i) {
L6   if (x%i==0 && y%i==0) {
L7   gcd=i;
L11  lcm=prod/gcd;
L12  printf("gcd=%d",gcd);
L14  printf("lcm=%d", lcm);
```

`i` reaches the `if` test, the `gcd` assignment, and then `gcd` flows into `lcm` and the two
prints that use it. **`L10` (`prod=x*y`) and `L13` are not in the slice**: `prod` does not depend
on `i`. That asymmetry — `i` is not in the backward slice of `prod`, and `prod` is not in the
forward slice of `i` — is the point of slicing.

The script also reports a "conservative" variant of every slice, computed over data **and**
control dependencies. It is included because the lecture lists slicing variants explicitly:

> "Static vs Dynamic: static slicing considers only information available at compile time, while
> dynamic slicing also includes runtime information; Underlying data flow analysis: slicing is
> based on an underlying analysis algorithm — slices vary depending on the underlying algorithm;
> Considered data unit: determines whether the slicing criterion refers to a single variable, a
> set of variables, or an entire row."

So a slice is not one answer but a family of answers, and the definition used has to be stated
alongside it.

## 5. Task 2 — the interprocedural CFG

The second program uses a **function pointer**:

```cpp
int add(int x, int y) { return x+y; }
int sub(int x, int y) { return x-y; }
int main() {
    int x, y, a, b;
    int (*func)(int, int) = nullptr;
    std::cin >> x >> a >> b;
    if (x%2 == 0) { func = &add; } else { func = &sub; }
    y = func(a,b);
    std::cout << y;
}
```

The interprocedural CFG:

```
  main
   |---> add(x,y)   [ body: return x+y ]
   |---> sub(x,y)   [ body: return x-y ]
   |
   +---> the indirect call site  y = func(a,b)
             |                ^
             |                |
             +-- may reach ---+
             either add or sub
```

Three things make this harder than the intra-procedural case, and they are exactly the four
questions the lecture's "Slicing Specification" slide asks about a language:

1. **The call is indirect.** `func` may hold `&add` or `&sub`, so the call edge is not a single
   known edge — it is a set of possible edges, and a sound analysis must consider both.
2. **Late binding.** The target is not known until the `if` has run, so a context-insensitive
   analysis cannot pick one.
3. **The callees are called from one site only**, so the interprocedural CFG here has no cycles
   — no recursion, so the standard fixpoint iteration converges immediately.
4. **No `goto` and no concurrency** in this program, so those two language questions the slide
   raises do not apply.

Note also that the call graph of the *lecture's* running example (`main` → `read`, `sort`,
`limit` → `swap`, `compare`) is the same kind of object, just with statically known targets.

## Reproducing this

```bash
python hw01-slices.py
```

Output is in `hw01-slices-output.txt` (recorded 2026-10-22).

## Open Questions

- The sheet does not say whether the grader expects control dependencies in the PDG under the
  classical post-dominator definition or under the lecture's wording. The two differ on the
  statement after the loop, and this page reports the lecture's reading.
- The sheet does not state the granularity of the graph. Statement-per-line is assumed; a
  basic-block-per-node CFG would merge `L7`/`L8` and `L9` and change the node set (though not
  the slices).
- Whether the *declaration* on line 2 counts as a definition of `x`, `y`, `prod` and `lcm` is not
  stated. It is modelled as not defining them, which is why `L2` appears in the backward slice of
  line 14 (via `gcd=1`) but not in the backward slice of line 13.
