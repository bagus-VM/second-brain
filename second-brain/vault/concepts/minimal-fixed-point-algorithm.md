---
title: "Minimal Fixed Point Algorithm (MFP)"
tags: [concept, software-analyse, semester-1, data-flow, fixpoint, worklist]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[monotone-framework]]", "[[iterative-data-flow-analysis]]", "[[mop-vs-mfp]]"]
---

## One-line Summary
The Minimal Fixed Point (MFP) algorithm is the iterative, worklist-based implementation of the [[monotone-framework|monotone framework]] — it computes the [[mop-vs-mfp|least fixed point]] of the global transfer function over the product lattice of program points, and is the practical way to solve a data flow problem.

## Core Intuition
The [[monotone-framework|monotone framework]] tells us: a least fixed point exists, is unique, and can be found by iterating the transfer function from ⊥. The MFP algorithm is the *practical* version of this. It uses a worklist to remember which edges still need to be propagated, and re-processes a block only when its predecessor's output has changed. This avoids the waste of re-iterating every block in the CFG on every round (as the naive algorithm does).

The algorithm is:
1. Initialise every block's analysis value to ⊥
2. Add every edge to the worklist
3. While the worklist is not empty:
   - Pop an edge (n, n')
   - Compute the *new* OUT of n' using the new IN
   - If the new OUT is strictly greater than the current OUT of n', update and add all successor edges to the worklist
4. Return the analysis values

Termination: in a finite-height lattice, the values can only increase, so the algorithm terminates in at most h(L) iterations per block.

## Formal Definition / Statement

```
Procedure MFP(⊥, ⊔, ⊑, CFG, trans, is-backward)
begin
  if is-backward then reverse edges(CFG);
  worklist := edges(CFG);
  foreach n ∈ nodes(CFG) do
    analysis[n] = ⊥;
  done
  while not empty(worklist) do
    ⟨n, n'⟩ := pop(worklist);
    if trans_n(analysis[n]) ⊐ analysis[n'] then begin
      analysis[n'] := analysis[n'] ⊔ trans_n(analysis[n]);
      foreach n'' ∈ successor-nodes(CFG, n') do
        push(worklist, ⟨n', n''⟩);
      done
    end
  done
  return analysis;
end
```

Key properties:
- `analysis[n]` is the abstract value at block n's exit (or entry, for backward analyses)
- `trans_n` is the transfer function for block n
- The worklist contains edges to be re-processed
- The condition `trans_n(analysis[n]) ⊐ analysis[n']` checks whether anything actually changed
- The update `analysis[n'] := analysis[n'] ⊔ trans_n(analysis[n])` performs the join

## Key Properties / Complexity

### Termination guarantee
- The lattice is finite-height (h(L) < ∞)
- `analysis[n]` can only increase (by monotonicity of trans and the join)
- So in at most h(L) iterations per block, the values stabilise
- Total work: O(|E| · h(L)) in the worst case

### Soundness
- The algorithm computes the MFP of the global transfer function F: L^CFG → L^CFG
- By Knaster-Tarski, this is the least fixed point
- By the [[mop-vs-mfp|MOP/MFP theorem]], for distributive frameworks this equals MOP
- For non-distributive frameworks, MFP is still *sound* (it over-approximates MOP)

### Optimisations
- **Worklist with set semantics**: avoid pushing the same edge twice; use a hash set or similar
- **Reverse postorder (forward) / postorder (backward)**: pre-sort the worklist to process in topological-like order, often giving convergence in one pass
- **Strongly connected components**: process SCCs individually; cycle through each SCC until it stabilises

### Forward vs backward
- Forward analyses: process the CFG in the natural direction; OUT depends on IN
- Backward analyses: reverse the CFG edges first, then run the same algorithm; IN depends on OUT
- The `is-backward` parameter handles this generically

## Worked Example

The lecture's [[zero-analysis-worked-example|Zero Analysis]] example:
- Program: x := 8; y := x; z := 0; while y > -1 do { x := x/y; y := y - 2; z := 5; }
- Lattice: L_ZI = {⊥, Z, NZ, MZ} with height 2
- Program lattice: L_Z = L_ZI^3 (three variables x, y, z), height 6

Iteration 1 (one pass over the CFG):
- σ at entry = []
- After x := 8: σ = [x → NZ]
- After y := x: σ = [x → NZ, y → NZ]
- After z := 0: σ = [x → NZ, y → NZ, z → Z]
- (Enter while) y > -1: σ unchanged
- After x := x/y: σ = [x → NZ, y → MZ, z → Z]  ← join with previous
- After y := y-2: σ = [x → NZ, y → MZ, z → Z]
- After z := 5: σ = [x → NZ, y → MZ, z → NZ]

Iteration 2 (back-edge from while-exit to while-entry):
- Join: σ at while entry ⊔ σ at while exit = [x → NZ, y → MZ, z → MZ]  (join is element-wise)
- Propagate through the loop body again:
  - x := x/y: NZ / MZ = MZ → σ = [x → MZ, y → MZ, z → MZ]
  - y := y-2: MZ - 2 = MZ → σ unchanged
  - z := 5: NZ → σ = [x → MZ, y → MZ, z → NZ]

Iteration 3 (verify no change):
- Join: same as iteration 2
- Body: no change (already at the fixed point)

The algorithm terminates. Final σ at the division point: y is MZ, so the analysis flags "this program might divide by zero".

## Common Pitfalls

- **Forgetting to join across predecessors**. At a confluence point, IN(b) = ⊔ OUT(pred(b)). The MFP algorithm does this automatically when it pops an edge and uses `analysis[n] ⊔ trans_n(analysis[n])`.
- **Using ⊓ instead of ⊔**. For *may* analyses (forward reaching-defs, backward live vars), the join at confluence is ⊔. For *must* analyses (forward available-exprs, backward very-busy-exprs), the join is ⊓. The MFP algorithm must use the correct one — this is encoded in the lattice and the `⊔` parameter.
- **Initial value**. For *may* analyses, IN(entry) = ⊥ (most precise, "no info"). For *must* analyses, IN(entry) = ⊤ (assume everything holds). The MFP algorithm starts every block at ⊥ for forward and ⊤ for backward (after the edge reversal).
- **Termination vs convergence**. The MFP algorithm terminates; that does not mean it has computed the *best* answer. For non-distributive analyses, MFP may be strictly less precise than MOP.
- **Worklist duplicates**. A naive worklist may push the same edge multiple times. Use a set-based worklist to avoid wasted re-processing.

## Connections

- [[monotone-framework]] — the MFP algorithm is the implementation
- [[iterative-data-flow-analysis]] — the worklist algorithm
- [[data-flow-analysis]] — the family of problems this solves
- [[mop-vs-mfp]] — what the MFP algorithm computes
- [[lattice]] — the underlying data structure
- [[zero-analysis-worked-example]] — the lecture's running example
- [[software-analyse-lecture-5]] — the worklist algorithm first introduced
- [[software-analyse-lecture-6]] — the lattice/fixpoint formalisation

## Open Questions

- The MFP algorithm has worst-case O(|E| · h(L)) work. For large programs and complex lattices, h(L) can be huge. What acceleration techniques (BDDs, sparse representations, demand-driven) are used in practice?
- The reverse postorder optimisation gives fast convergence for "reducible" CFGs. How does it behave on irreducible CFGs (e.g., goto-heavy code)?
- For non-distributive analyses, the MFP is sound but may be very imprecise. Are there practical algorithms that improve on MFP without paying the cost of MOP?
- How do modern compilers (GCC, LLVM) implement MFP-style analyses in practice? Are there tool-specific tricks worth knowing?
