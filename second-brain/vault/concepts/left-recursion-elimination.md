---
title: "Left Recursion Elimination"
tags: [concept, software-analyse, semester-1, parsing, grammar-transformation]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, predictive-parsing]
---

## One-line Summary

Left recursion elimination is a grammar transformation that rewrites left-recursive productions into right-recursive form, enabling top-down (predictive) parsing to terminate.

## Core Intuition

A left-recursive production like `A → Aα | β` means "keep expanding A on the left forever" — a top-down parser would loop infinitely trying to expand A. The fix is to "unroll" the loop: instead of building up on the left, build up on the right, using a fresh nonterminal R to handle the repetition. The result is `A → βR` and `R → αR | ε`, which produces the same strings but without left recursion.

## Formal Definition / Statement

Given a left-recursive nonterminal with productions:

```
A → Aα | β
```

(Where α is non-empty and β does not start with A)

Transform to:

```
A  → βR
R  → αR | ε
```

More generally, if A has multiple left-recursive and non-left-recursive alternatives:

```
A → Aα₁ | Aα₂ | ... | Aαₙ | β₁ | β₂ | ... | βₘ
```

Transform to:

```
A  → β₁R | β₂R | ... | βₘR
R  → α₁R | α₂R | ... | αₙR | ε
```

Additionally, **left factoring** is needed when productions share a common prefix:

```
stmt → if expr then stmt endif
     | if expr then stmt else stmt endif
```

becomes:

```
stmt     → if expr then stmt opt_else
opt_else → else stmt endif | endif
```

## Key Properties

- The transformation preserves the language L(G)
- The transformed grammar is right-recursive (suitable for top-down parsing)
- The transformation may introduce ε-productions
- After elimination, [[predictive-parsing|predictive parsing]] can be applied
- The transformation may change the parse tree structure (but the [[abstract-syntax-tree|AST]] can be made equivalent)

## Worked Example

Original grammar (left-recursive, with precedence):
```
expr   → expr + term
       | expr - term
       | term
term   → term * factor
       | term / factor
       | factor
factor → ( expr )
       | ID
       | NUMBER
```

Step 1: Eliminate left recursion from `expr`:
- Left-recursive: `expr → expr + term | expr - term` (α₁ = `+ term`, α₂ = `- term`)
- Non-left-recursive: `expr → term` (β = `term`)

Result:
```
expr  → term expr'
expr' → + expr | - expr | ε
```

Step 2: Eliminate left recursion from `term`:
- Left-recursive: `term → term * factor | term / factor`
- Non-left-recursive: `term → factor`

Result:
```
term  → factor term'
term' → * term | / term | ε
```

Final grammar:
```
expr   → term expr'
expr'  → + expr | - expr | ε
term   → factor term'
term'  → * term | / term | ε
factor → ( expr ) | ID | NUMBER
```

This grammar generates the same language and is suitable for [[predictive-parsing|predictive parsing]].

## Common Pitfalls

- Applying the transformation when there is indirect left recursion (A → Bα, B → Aβ) — must resolve indirect recursion first (topological sort of nonterminals)
- Forgetting that the transformation changes the parse tree shape (the new nonterminal R adds a layer)
- Not recognizing that left recursion in a top-down parser causes an **infinite loop**, not just wrong results
- Confusing left recursion elimination with left factoring — they solve different problems (looping vs. FIRST set overlap)

## Connections

- [[predictive-parsing]] — left recursion elimination is a prerequisite for predictive/recursive descent parsing
- [[context-free-grammar]] — this is a grammar-to-grammar transformation
- [[operator-precedence-associativity]] — expression grammars are naturally left-recursive (for left-associativity) and need this transformation
- [[grammar-ambiguity]] — sometimes restructuring to fix ambiguity also introduces left recursion
- [[abstract-syntax-tree]] — the AST construction must account for the new nonterminals introduced by the transformation

## Open Questions

- How does right-recursion affect stack depth during parsing compared to left-recursion?
- Are there grammar classes where left recursion elimination significantly increases grammar size?
- How do LR parsers handle left recursion without this transformation?
