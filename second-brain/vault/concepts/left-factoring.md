---
title: "Left Factoring"
tags: [concept, software-analyse, semester-1, parsing, grammar-transformation]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, predictive-parsing]
---

## One-line Summary

Left factoring is a grammar transformation that eliminates common prefixes among alternatives of a production, making FIRST sets disjoint so that [[predictive-parsing|predictive parsing]] can choose the correct production with one lookahead token.

## Core Intuition

If two productions for the same nonterminal start with the same symbols, a predictive parser can't tell which one to pick by looking at just one token. Left factoring "factors out" the common prefix into a shared production, pushing the distinguishing part into a new nonterminal. It's like extracting a common factor in algebra: instead of `ax + ay`, write `a(x + y)`.

## Formal Definition / Statement

Given a nonterminal A with productions that share a common prefix α:

```
A → α β₁ | α β₂ | γ
```

Left factor to:

```
A  → α A' | γ
A' → β₁ | β₂
```

More generally, if n alternatives share prefix α:

```
A → α β₁ | α β₂ | ... | α βₙ | γ₁ | γ₂ | ... | γₘ
```

becomes:

```
A  → α A' | γ₁ | γ₂ | ... | γₘ
A' → β₁ | β₂ | ... | βₙ
```

## Key Properties / Complexity

- Preserves the language L(G)
- Makes FIRST sets disjoint for the factored alternatives
- May need to be applied repeatedly (common prefixes can be arbitrarily long)
- Works hand-in-hand with [[left-recursion-elimination]] to prepare a grammar for predictive parsing
- Introduces new nonterminals and ε-productions

## Worked Example

Original grammar:
```
stmt → if expr then stmt endif
     | if expr then stmt else stmt endif
```

Both alternatives start with `if expr then stmt` — the parser can't decide after seeing `if`.

Left factor:
```
stmt     → if expr then stmt opt_else
opt_else → else stmt endif
         | endif
```

Now the parser sees `if` and knows to enter `stmt`. After parsing `if expr then stmt`, it looks ahead to decide between `else` (opt_else → else stmt endif) or `endif` (opt_else → endif).

Another example — expression types:
```
type → integer | integer [ num ]
```

Left factor:
```
type    → integer type'
type'   → [ num ] | ε
```

## Common Pitfalls

- Forgetting that left factoring may need multiple passes (nested common prefixes)
- Not realising that left factoring alone doesn't make a grammar LL(1) — [[left-recursion-elimination|left recursion elimination]] may also be needed
- Confusing left factoring with left recursion elimination — they solve different problems:
  - Left factoring: common prefixes → FIRST set overlap
  - Left recursion elimination: self-reference → infinite loop
- Introducing ε-productions without considering how they affect FOLLOW sets

## Connections

- [[predictive-parsing]] — left factoring is a prerequisite (disjoint FIRST sets)
- [[left-recursion-elimination]] — the other grammar transformation needed for predictive parsing
- [[context-free-grammar]] — the transformation produces an equivalent CFG
- [[grammar-ambiguity]] — left factoring doesn't fix ambiguity directly, but common prefixes can be a symptom of ambiguous grammars
- [[operator-precedence-associativity]] — expression grammars rarely need left factoring (different operators have different FIRST tokens)

## Open Questions

- How does left factoring interact with ε-productions and FOLLOW sets?
- Can left factoring increase the number of grammar rules significantly?
- How do parser generators handle common prefixes without explicit left factoring?
