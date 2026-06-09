---
title: "Predictive Parsing"
tags: [concept, software-analyse, semester-1, parsing, top-down-parsing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, parse-tree]
---

## One-line Summary

Predictive parsing is a top-down parsing method where a single lookahead token unambiguously determines which production to apply, typically implemented as recursive descent.

## Core Intuition

Think of parsing as a decision tree: at each nonterminal, the parser peeks at the next input token and uses a lookup (the FIRST set) to pick the correct production. No backtracking needed — each decision is deterministic. This is exactly what a recursive descent parser does: each nonterminal becomes a procedure, and each production becomes a branch in an if/else chain keyed on the lookahead.

## Formal Definition / Statement

A predictive parser (LL(1) parser) works when:
- For every nonterminal A with productions A → α | β, the sets FIRST(α) and FIRST(β) are **disjoint**
- This allows a single lookahead token to uniquely select the production

**FIRST(α)** = set of terminals that can appear as the first symbol of any string derived from α.

Key operations:
- `match(t)`: if lookahead == t, consume token; else error
- For each nonterminal A, a procedure checks `lookahead ∈ FIRST(α)` for each alternative A → α

**Grammar requirements** (may need transformation):
- No left recursion (would cause infinite loop)
- No common prefixes (would cause FIRST set overlap → use [[left-recursion-elimination|left factoring]])

## Key Properties

- Runs in O(n) time where n = input length (one token consumed per match)
- Uses exactly 1 token of lookahead (LL(1))
- Cannot handle left-recursive grammars directly
- Requires disjoint FIRST sets for alternatives of each nonterminal
- The parser is a direct transcription of the grammar into code

## Worked Example

Grammar:
```
type   → simple | ^ id | array [ simple ] of type
simple → integer | char | num dotdot num
```

FIRST sets:
```
FIRST(simple) = { integer, char, num }
FIRST(^ id)   = { ^ }
FIRST(type)   = { integer, char, num, ^, array }
```

Parsing `array [ num dotdot num ] of integer`:

Step 1: lookahead = `array` → matches `array` in type → call match('array')
Step 2: lookahead = `[`     → call match('[')
Step 3: lookahead = `num`   → ∈ FIRST(simple) → call simple()
Step 4: lookahead = `num`   → call match('num'), match('dotdot'), match('num')
Step 5: lookahead = `]`     → call match(']')
Step 6: lookahead = `of`    → call match('of')
Step 7: lookahead = `integer` → ∈ FIRST(simple) → call type() → simple() → match('integer')

The recursive descent procedures mirror the grammar directly:

```pascal
procedure type();
begin
  if lookahead in { 'integer', 'char', 'num' } then simple()
  else if lookahead = '^' then match('^'); match(id)
  else if lookahead = 'array' then
    match('array'); match('['); simple();
    match(']'); match('of'); type()
  else error()
end;
```

## Common Pitfalls

- Trying to use predictive parsing on a left-recursive grammar (parser loops forever)
- Forgetting to left-factor when productions share a common prefix (FIRST sets overlap)
- Not handling the ε-production case correctly (need FOLLOW set for ε alternatives, though not covered in this lecture)
- Confusing FIRST(α) with "first terminal in α" — FIRST follows derivations, not just literal first symbol

## Connections

- [[context-free-grammar]] — the grammar must satisfy LL(1) constraints
- [[left-recursion-elimination]] — required transformation before predictive parsing
- [[operator-precedence-associativity]] — grammar restructuring that affects FIRST sets
- [[parse-tree]] — predictive parsing constructs the parse tree top-down (root to leaves)
- [[syntax-directed-translation]] — semantic actions can be embedded into the recursive descent procedures
- Contrast with bottom-up (shift-reduce) parsing which builds the tree leaves-to-root

## Open Questions

- How does predictive parsing extend to LL(k) for k > 1?
- What are the practical trade-offs between recursive descent and table-driven LL parsing?
- How do parser generators like ANTLR handle grammars that are not LL(1)?
