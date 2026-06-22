---
title: "Register Allocation"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[live-variable-analysis]]", "[[control-flow-graph]]"]
---
## One-line Summary
Register allocation maps program variables to a limited number of CPU registers, and when there aren't enough registers, it decides which values to temporarily store in memory (spilling).

## Core Intuition
CPUs have a small, fixed number of registers (e.g., 16 on x86-64 general purpose). A program may have hundreds of variables. The compiler must decide which variables live in which registers at each point in time. The key insight: two variables can share the same register if they are never **live simultaneously** — meaning there's no program point where both might be needed in the future. This is where [[live-variable-analysis]] comes in: it tells us which variables are live at each point, allowing us to build an **interference graph** where two variables are connected iff they are simultaneously live somewhere. Coloring this graph with k colors (k = number of registers) gives the allocation. If the graph isn't k-colorable, some variables must be **spilled** to memory.

## Formal Definition / Statement

**Register allocation via graph coloring**:

1. **Build the interference graph** G = (V, E):
   - V = set of variables (or temporaries) in the program
   - Edge (u, v) ∈ E iff u and v are **interfering**: there exists a program point where both are live simultaneously
   - Interference is computed from [[live-variable-analysis]]: u and v interfere iff u ∈ OUT(n) and v ∈ OUT(n) for some statement n, OR one is defined at n while the other is in OUT(n)

2. **Color the graph** with k colors (k = number of registers):
   - Adjacent nodes must have different colors (interfering variables cannot share a register)
   - Graph k-coloring is NP-hard for k ≥ 3 in general

3. **Simplify** (heuristic for coloring):
   - While the graph has a node with degree < k: remove it (push onto stack)
   - When all nodes removed: pop and assign colors greedily
   - If no node has degree < k: **spill** a node (assign to memory)

4. **Spill** a variable v:
   - Insert LOAD before each use of v
   - Insert STORE after each definition of v
   - Rebuild the interference graph and try again

5. **Coalesce**: if two non-interfering variables are connected by a copy (MOV), merge them into one node (eliminates the MOV instruction)

## Key Properties / Complexity

- **Graph k-coloring**: NP-hard for k ≥ 3 (Karp, 1972) — all practical allocators use heuristics
- **Chordal graphs**: if the interference graph is chordal, optimal coloring is polynomial (perfect elimination ordering)
- **Spill cost heuristic**: spill the variable with (use_count + def_count) / degree — minimize the number of memory accesses per interference edge removed
- **Linear scan** (alternative): O(n log n) allocation without graph coloring — used in JIT compilers
- **SSA-based allocation**: in SSA form, interference graphs are chordal → polynomial-time optimal allocation possible
- Spilling is expensive: each spill adds a memory access (~100 cycles vs. ~1 cycle for register)
- Coalescing reduces MOV instructions but can make the graph harder to color

## Worked Example

```
1: a = 1          // def={a}
2: b = 2          // def={b}
3: c = a + b      // use={a,b}, def={c}
4: d = a * c      // use={a,c}, def={d}
5: return d       // use={d}
```

Live-variable analysis (OUT sets):
- After 1: {a}
- After 2: {a, b}
- After 3: {a, c}  (b is dead after 3)
- After 4: {d}     (a, c are dead after 4)
- After 5: {}

Interference edges (pairs live at the same point):
- a-b: live together after stmt 2 → INTERFERE
- a-c: live together after stmt 3 → INTERFERE
- a-d: never live together → no interference
- b-c: live together at stmt 3 IN → b ∈ IN(3) = {a,b}, c is def'd here... Actually b and c: b is in IN(3), c is in OUT(3). At the statement itself, b is used and c is defined. They interfere because c is defined while b is still live.
- c-d: c ∈ OUT(3), d ∈ OUT(4)... c is in OUT(3) and d is defined at 4, so they interfere.

Interference graph:
```
a — b
a — c
b — c
c — d
```

With 2 registers (k=2):
- Node d has degree 1 (connected to c). Remove d.
- Node b has degree 1 (connected to a). Remove b.
- Node a has degree 1 (connected to c). Remove a.
- Node c has degree 0. Remove c.
- Color: c=R1, a=R2, b=R1, d=R2

Result: a→R2, b→R1, c→R1, d→R2. No spills needed!

## Common Pitfalls

- Confusing **interference** with **adjacency**: interference means "simultaneously live," not "connected in the CFG"
- Forgetting that a variable defined at statement n interferes with all variables in OUT(n) (the definition happens while others are still live)
- Not iterating after spilling: inserting loads/stores changes liveness, which changes the interference graph
- Coalescing can make the graph harder to color (increases degree) — must be done carefully
- Register allocation is for *variables within a function*; calling conventions handle inter-function register usage
- Modern compilers use **SSA form** first, then convert out of SSA during or after register allocation

## Connections

- [[live-variable-analysis]] — the data flow analysis that computes the interference graph
- [[data-flow-analysis]] — liveness is an instance of the data flow framework
- [[control-flow-graph]] — the structure over which liveness and interference are computed
- [[du-chains-ud-chains]] — definition-use chains inform spill cost heuristics
- [[dead-code-elimination]] — DCE removes dead assignments, reducing register pressure
- [[common-subexpression-elimination]] — CSE can increase register pressure by keeping more values alive
- [[monotone-framework]] — liveness analysis as a monotone framework instance
- [[software-analyse-lecture-5]] — lecture where register allocation is introduced as an application of data flow analysis

## Open Questions

- How do SSA-based register allocators (e.g., LLVM's) differ from the classic graph-coloring approach?
- What is the optimal spill heuristic for modern out-of-order CPUs with register renaming?
- How does register allocation interact with instruction scheduling (phase ordering problem)?
