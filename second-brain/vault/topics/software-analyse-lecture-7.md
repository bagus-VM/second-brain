---
title: "Lecture 7: Interprocedural and Heap Analysis"
tags: [topic, software-analyse, semester-1, interprocedural-analysis, heap-analysis, points-to-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[software-analyse-lecture-6]]", "[[monotone-framework]]", "[[abstract-interpretation]]", "[[mop-vs-mfp]]"]
---

## One-line Summary
Lecture 7 extends [[data-flow-analysis|data flow analysis]] beyond a single function: it explains why intraprocedural analysis is too imprecise at function boundaries ([[interprocedural-analysis|interprocedural analysis]]), presents four techniques for [[context-sensitivity|context sensitivity]] (cloning, inlining, call strings, procedure summaries), introduces the precise [[meet-over-valid-paths|MVP]] ideal and its undecidability, and then opens up the heap with [[points-to-analysis|points-to analysis]] — the two classic algorithms being [[steensgaards-points-to-analysis|Steensgaard's]] (fast, equality-based, O(nα(n,n))) and [[andersens-points-to-analysis|Andersen's]] (precise, subset-based, O(n³)) — and the design space for [[heap-analysis|heap abstractions]].

## Core Intuition
L01–L05 taught you to analyse *one function at a time*. L06 showed you the lattice/abstract interpretation theory that grounds data flow. L07 says: that's not enough. The moment your program has function calls, an intraprocedural analysis must be *conservative* about what the callee does — it doesn't know, so it assumes the worst (⊤ or ⊥). This kills precision. And the moment you allocate objects on the heap, variables become *aliases* — `a.x` and `b.x` may or may not be the same field — and the analysis must track which objects each pointer can refer to.

The lecture has three parts:

### Part 1: Interprocedural analysis
- **Limitations of intraprocedural analysis**: at every call site, the analysis must either over-approximate the callee's effect (⊤) or under-approximate it (⊥). Example: `int d = f(a, 2); int e = a + d;` — without modelling f, the analysis cannot know what values d can take.
- **Interprocedural CFG**: split call sites into call node (b_cx) and return node (b_rx); add edges that pass the parameter map (for call) and result (for return).
- **Valid paths**: not all interprocedural paths are meaningful. A "valid" path follows a call to its matching return, in order. Invalid paths (e.g., enter f from call site 6, exit at return site 7) are ignored.
- **Meet Over Valid Paths (MVP)**: the interprocedural analogue of MOP. Theoretically precise (joins over all valid paths), but undecidable.
- **Context sensitivity**: a context-insensitive analysis merges all call sites of a function into one — losing information. Context-sensitive analysis distinguishes the call sites: x gets value {7} in the first call, {1} in the second. Four techniques: cloning, inlining, call strings, procedure summaries.
- **The four context-sensitivity techniques**:
  - **Cloning**: physically duplicate the function body, one copy per call site. Precise but explodes code size.
  - **Inlining**: substitute the function body at each call site. Precise but explodes code size further and may not terminate for recursion.
  - **Call strings**: keep the function as one body, but tag each call with a context (sequence of call sites). Bounded-length call strings ensure termination.
  - **Procedure summaries**: compute the function's net effect as a transfer function `trans_f = trans_bn ∘ ... ∘ trans_b0`, then apply it at each call site. Compositional, scalable, but may lose precision for symbolic inputs.

### Part 2: Heap analysis
- **Why the heap breaks analysis**: aliases. `a = new A(); b = a; c = new A(); a.x = 17; c.x = 23; b.x = 42;` — analysis must know which variables are aliases to know what `print(a.x)` prints.
- **Heap graph**: a directed graph where edges are pointers (var → object, object → field).
- **Points-to analysis**: for each variable v, compute `pts(v)` = the set of objects v can point to. Two main algorithms:
  - **Steensgaard's analysis**: *equality-based*. `pts(a) = pts(b)` after `a = b`. Fast: O(n · α(n, n)) (Union-Find). Imprecise: any two variables that ever share an assignment end up in the same points-to set.
  - **Andersen's analysis**: *subset-based* (inclusion-based). `pts(b) ⊆ pts(a)` after `a = b`. Precise: each variable gets its own points-to set. Slower: O(n³).
- **Design space for heap abstractions**: distinguish or merge by type, name, calling context, control flow, containing heap objects, field name, array index, pointer arithmetic. Modern analyses choose combinations.

### Part 3: Limitations
- The lecture ends with a sobering note: even with context sensitivity and points-to analysis, real-world analyses still suffer precision loss. The "composed transfer function" of a function may degenerate to ⊤, or to a symbolic expression as complex as the function itself.

## Key Concepts

### Interprocedural
- [[interprocedural-analysis]] — the general topic; extending analysis across function calls
- call/return nodes — split each call site b_x into b_cx (call) and b_rx (return)
- [[valid-paths|valid paths]] — paths that respect call-return matching
- [[meet-over-valid-paths|Meet Over Valid Paths (MVP)]] — the precise but undecidable interprocedural solution
- [[context-sensitivity]] — distinguishing different calling contexts of a function
- [[cloning-context-sensitivity|Cloning]] — duplicate the function body per call site
- [[inlining-context-sensitivity|Inlining]] — substitute the body at each call site
- [[call-strings]] — tag call with sequence of call sites
- [[procedure-summaries]] — pre-compute a function's net transfer function
- Composed transfer function — the transfer function for an entire procedure

### Heap
- [[heap-analysis]] — the topic; analysing heap-allocated memory
- [[aliasing]] — multiple names for the same memory location
- [[points-to-analysis]] — determining which objects each pointer can refer to
- points-to sets — `pts(v)` = the set of objects v can point to
- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — equality-based, fast
- [[andersens-points-to-analysis|Andersen's analysis]] — subset-based, precise
- [[union-find-data-structure|Union-Find]] — the data structure that makes Steensgaard's analysis fast
- locations — static, stack-dynamic, heap-dynamic; the three flavours of memory location

## Formal Statement: Meet Over Valid Paths (MVP)

For a program with a call graph G and procedures P₁, ..., P_k:

A **path** in the interprocedural CFG is a sequence of blocks. A path is **valid** (a "realizable interprocedural path") if:
- It respects the call-return matching: if you enter procedure P at call site c of P, you must exit P at the return site of c, in order
- The grammar from the lecture: `Path ::= ⟨P⟩* ⟨M⟩`, `P ::= b_x | b_cy`, `M ::= b_cx ⟨M⟩ b_rx | b_y ⟨M⟩ | ⟨M⟩ b_y | ε`

**MVP at block b_i**:
MVP(b_i) = ⊔ { trans_{p_k} ∘ ... ∘ trans_{p_0} (⊥) | [p_0, ..., p_k] ∈ vpath(b_i) }

where vpath(b_i) is the (possibly infinite) set of *valid* paths to b_i. MVP is the interprocedural analogue of MOP — precise but undecidable.

The MFP solution of the interprocedural analysis gives a sound *and* computable under-approximation of MVP.

## Key Properties

### Why intraprocedural fails at call sites
Consider:
```c
int a = 7;
int d = f(a, 2);     // call to f
int e = a + d;        // uses d
```
Without interprocedural information, the analysis cannot know what values d takes. After `d = f(a, 2)`, the analysis can only say d ∈ ⊤ (any value). After `e = a + d`, e ∈ ⊤. The actual result depends on what f does — which the intraprocedural analysis doesn't know.

With interprocedural analysis that traces f's body, the analysis can compute d's possible values precisely and propagate them to e.

### The four context-sensitivity techniques — tradeoffs

| Technique | Precision | Scalability | Termination guarantee | Best for |
|-----------|-----------|-------------|------------------------|----------|
| Cloning | Perfect | O(C × \|P\|) code | Yes (if C is finite) | Small programs, very few call sites |
| Inlining | Perfect | O(C × \|P\|) code | **No** for recursion | Small programs, no recursion |
| Call strings (k-bounded) | Good | O(S × k) where S = callsite count | Yes (k is bounded) | General-purpose analysis |
| Procedure summaries | Good | O(\|P\| × \|summaries\|) | Yes | Large programs, deep call chains |

### Steensgaard vs Andersen — the speed/precision tradeoff
| Algorithm | Constraint | Complexity | Precision |
|-----------|-----------|-----------|-----------|
| Steensgaard | `pts(a) = pts(b)` after `a = b` | O(n · α(n, n)) | Imprecise (one set per equivalence class) |
| Andersen | `pts(b) ⊆ pts(a)` after `a = b` | O(n³) | Precise (one set per variable) |

Steensgaard's is the algorithm you'd ship in a compiler that needs to scale to millions of lines of code. Andersen's is the algorithm you'd use in a static bug finder for security-critical code.

### Why Andersen's is harder
Subset constraints require solving a system of inclusions: for every assignment, propagate `pts(b)` into `pts(a)`. This requires a worklist (or similar iterative algorithm), and the worst case is cubic in the number of variables.

## Worked Example: cloning on the lecture's running program

```c
int a = 7;
int d = f(a, 2);
int e = f(1, 5);

int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```

**Context-insensitive analysis** (merge all call sites):
- f is analysed once
- x and y are seen with values {7, 2} from call 1 and {1, 5} from call 2
- After merge: x = {1, 2, 5, 7}, y = {1, 2, 5, 7}
- d = f(a, 2) → d = {1, 2, 5, 7}
- e = f(1, 5) → e = {1, 2, 5, 7}
- Both d and e are reported as having all four possible values — the analysis cannot tell which call produced which value

**Context-sensitive with cloning**:
- f is duplicated: f_1 (called from b6) and f_2 (called from b7)
- f_1 sees x = {7}, y = {2} → z = {7} → return z = {7} → d = {7}
- f_2 sees x = {1}, y = {5} → z = {5} → return z = {5} → e = {5}
- Now we have: d = {7} and e = {5} — perfectly precise

Cloning blows up code size (2 copies of f instead of 1), but gives the best precision.

**Context-sensitive with procedure summary**:
- Compute trans_f once: z = {x, y} (in the body, the conditional gives z the max of x and y)
- At call site 1: d = trans_f(7, 2) = {7}
- At call site 2: e = trans_f(1, 5) = {5}
- Same precision as cloning, but no code duplication

This is the lecture's worked example — slides 49-50.

## Common Pitfalls

- **Cloning and inlining are not the same**. Cloning duplicates the function *body* (still has call/return). Inlining substitutes the body *at the call site* (no call/return). Inlining is more aggressive and doesn't terminate for recursion.
- **Context sensitivity ≠ precision**. Even with context sensitivity, the analysis can still be imprecise. Procedure summaries, for example, lose precision when the symbolic result is too complex.
- **Andersen's analysis is *not* the most precise**. There are even more precise analyses (e.g., flow-sensitive, context-sensitive, field-sensitive combinations). Andersen's is the *practical* sweet spot.
- **Steensgaard's analysis is "almost linear" in practice**, but its worst case is O(n · α(n, n)) for the Union-Find operations. For n = 10⁶ variables, this is still tractable.
- **Points-to analysis is *not* the same as alias analysis**. Points-to says what objects a variable *can* point to. Alias says which variables are *currently* pointing to the same object. They're related but not identical.
- **Context-insensitive analyses are not "wrong"**. They are sound. They're just imprecise. For many real-world analyses, the imprecision is acceptable.
- **The "composed transfer function" of a recursive procedure may not exist** (the transfer function is not a well-defined closed form). Recursive procedures need fixpoint computation, just like data flow analyses.

## Connections

- [[software-analyse-lecture-5]] — the intraprocedural foundation that L07 extends
- [[software-analyse-lecture-6]] — the lattice/abstract interpretation theory that grounds both
- [[monotone-framework]] — extends to interprocedural setting
- [[abstract-interpretation]] — the general framework
- [[data-flow-analysis]] — the family being extended
- [[mop-vs-mfp]] — MFP/MVP is the interprocedural analogue
- [[zero-analysis-worked-example]] — intraprocedural example that motivates the extension
- [[context-sensitivity]] — the central concept of L07
- [[points-to-analysis]] — the second half of L07
- [[aliasing]] — the problem heap analysis solves
- [[iterative-data-flow-analysis]] — extends naturally to interprocedural

## Open Questions

- How do modern static analyzers (Infer, CodeQL, Semgrep) combine context sensitivity and points-to analysis? What are the engineering tradeoffs?
- For very large programs (millions of LOC), is *any* sound interprocedural analysis tractable? What approximations do production tools make?
- How do demand-driven analyses (compute only the facts needed for a specific query) change the precision/scalability tradeoff?
- The lecture lists "object sensitivity" and "field sensitivity" as design choices. How do these interact with context sensitivity?
- Are there interprocedural analyses that are tractable in linear time *and* precise enough for bug finding? What's the current research frontier?
