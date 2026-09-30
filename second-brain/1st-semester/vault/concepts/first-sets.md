---
title: "FIRST Sets"
tags: [concept, software-analyse, semester-1, parsing, formal-languages]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, predictive-parsing]
---

## One-line Summary

FIRST(α) is the set of terminal symbols that can appear as the first token of any string derived from the grammar symbol sequence α, and is the core mechanism for choosing productions in [[predictive-parsing|predictive parsing]].

## Core Intuition

When a predictive parser sees a lookahead token, it needs to decide which production to apply. FIRST sets answer the question: "If I expand this nonterminal (or sequence), what tokens could possibly come first?" If the FIRST sets of the alternatives are disjoint, one lookahead token is enough to pick the right production.

## Formal Definition / Statement

For a grammar symbol sequence α ∈ (T ∪ N)*:

**FIRST(α)** = { a ∈ T | α ⇒* aβ for some β ∈ (T ∪ N)* }

That is, FIRST(α) is the set of all terminals that can appear as the first symbol of any string derivable from α.

**Computation rules**:
1. If X is a terminal, FIRST(X) = { X }
2. If X is a nonterminal and X → Y₁Y₂...Yₖ is a production:
   - Add FIRST(Y₁) \ {ε} to FIRST(X)
   - If ε ∈ FIRST(Y₁), add FIRST(Y₂) \ {ε} to FIRST(X)
   - Continue: if ε ∈ FIRST(Y₁)...FIRST(Yᵢ₋₁), add FIRST(Yᵢ) \ {ε} to FIRST(X)
   - If ε ∈ FIRST(Y₁)...FIRST(Yₖ), add ε to FIRST(X)
3. If X → ε is a production, add ε to FIRST(X)

## Key Properties / Complexity

- FIRST sets are computed iteratively until a fixed point is reached
- For a nonterminal A with alternatives A → α | β, predictive parsing requires FIRST(α) ∩ FIRST(β) = ∅
- If a production can derive ε, the FOLLOW set of the nonterminal is also relevant (not covered in this lecture but important for complete LL(1) parsing)
- FIRST sets depend only on the grammar, not the input

## Worked Example

Grammar:
```
type   → simple | ^ id | array [ simple ] of type
simple → integer | char | num dotdot num
```

Computing FIRST sets:
```
FIRST(integer)     = { integer }
FIRST(char)        = { char }
FIRST(num)         = { num }
FIRST(simple)      = { integer, char, num }
FIRST(^ id)        = { ^ }
FIRST(array)       = { array }
FIRST(type)        = FIRST(simple) ∪ { ^ } ∪ { array }
                   = { integer, char, num, ^, array }
```

Verification: FIRST(simple), FIRST(^ id), and FIRST(array [ simple ] of type) are all pairwise disjoint:
- { integer, char, num } ∩ { ^ } = ∅ ✓
- { integer, char, num } ∩ { array } = ∅ ✓
- { ^ } ∩ { array } = ∅ ✓

Therefore, the grammar is LL(1) and predictive parsing works.

**Using FIRST in the parser**:
```
procedure type();
begin
  if lookahead in FIRST(simple) then    -- { integer, char, num }
    simple()
  else if lookahead in FIRST(^ id) then -- { ^ }
    match('^'); match(id)
  else if lookahead in FIRST(array [ simple ] of type) then -- { array }
    match('array'); match('['); simple();
    match(']'); match('of'); type()
  else error()
end;
```

## Common Pitfalls

- Forgetting to propagate ε through FIRST sets (if Y₁ can derive ε, must check Y₂ too)
- Computing FIRST of a single symbol vs. a sequence — FIRST(AB) ≠ FIRST(A) in general
- Not iterating to fixed point — some FIRST sets depend on others
- Confusing FIRST with FOLLOW — FIRST looks at what can start a derivation; FOLLOW looks at what can follow a nonterminal in some sentential form

## Connections

- [[predictive-parsing]] — FIRST sets directly determine which branch to take
- [[context-free-grammar]] — FIRST sets are derived from the production rules
- [[left-factoring]] — needed when FIRST sets of alternatives overlap
- [[left-recursion-elimination]] — left recursion makes FIRST computation diverge
- [[grammar-ambiguity]] — overlapping FIRST sets can indicate ambiguity (though not always)

## Open Questions

- How do FOLLOW sets complement FIRST sets in handling ε-productions?
- What is the relationship between FIRST sets and the LL(1) parsing table?
- How do FIRST sets generalize to LL(k) for k > 1?
