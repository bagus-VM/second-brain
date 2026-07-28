---
title: "Operator Precedence and Associativity"
tags: [concept, software-analyse, semester-1, parsing, grammar-design]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, grammar-ambiguity]
---

## One-line Summary

Operator precedence and associativity are encoded into a grammar by introducing separate nonterminal levels for each precedence tier and using left- or right-recursion to enforce grouping direction.

## Core Intuition

When you write `2 + 3 * 5`, you know `*` binds tighter than `+`. To make the parser know this too, you need different nonterminal "levels" in the grammar: one for low-precedence ops (+,-), one for high-precedence ops (*,/), and one for atoms (numbers, parenthesized expressions). The nesting of nonterminals encodes precedence. For associativity, recursion direction matters: left-recursion for left-associative, right-recursion for right-associative.

## Formal Definition / Statement

Given operators at precedence levels 1 (lowest) to n (highest):

**Precedence**: Introduce nonterminals N₁, N₂, …, Nₙ, Nₐₜₒₘ where:
- Nᵢ → Nᵢ opᵢ Nᵢ₊₁ | Nᵢ₊₁ (for level-i operators)
- Nₐₜₒₘ → number | id | ( N₁ )

Each level only references the next-higher level, ensuring higher-precedence operators are deeper in the parse tree ("bind more tightly").

**Associativity**:
- **Left-associative**: `left → left op term` (left-recursive production)
- **Right-associative**: `right → term op right` (right-recursive production)

## Key Properties / Complexity

- Each precedence level corresponds to one nonterminal
- Higher precedence → deeper in the parse tree (closer to leaves)
- Left-recursion encodes left-associativity (e.g., `a - b - c` groups as `(a - b) - c`)
- Right-recursion encodes right-associativity (e.g., `a = b = c` groups as `a = (b = c)`)
- This approach eliminates [[grammar-ambiguity|ambiguity]] by making grouping explicit in the grammar structure

## Worked Example

Grammar with precedence for `+` (low) and `*` (high):

```
expr   → expr + term | term
term   → term * factor | factor
factor → number | ( expr )
```

Parsing `2 + 3 * 5`:

```
         expr
        / | \
     expr  +  term
      |       / | \
    term   term  *  factor
      |     |        |
   factor factor   number
      |     |        |
   number number     5
      |     |
      2     3
```

The `*` is deeper in the tree than `+`, meaning `3 * 5` is evaluated first: `2 + (3 * 5)`.

Left-associativity example: `9 - 5 + 2`
```
         expr
        / | \
     expr  +  term
    / | \       |
 expr - term  factor
   |     |      |
 term  factor   2
   |     |
factor  number
   |      |
number    5
   |
   9
```

Groups as `(9 - 5) + 2` — the left operand of `+` is the full `expr` subtree `9 - 5`.

## Common Pitfalls

- Using a single nonterminal for all operators → ambiguous grammar
- Using right-recursion for `-` → would parse `a - b - c` as `a - (b - c)`, which is wrong
- Forgetting parentheses as the highest-precedence construct (handled by `factor`)
- Not nesting nonterminals correctly → precedence levels get mixed up

## Connections

- [[grammar-ambiguity]] — this technique is the standard way to resolve expression ambiguity
- [[context-free-grammar]] — the restructured grammar is still a CFG, just carefully designed
- [[predictive-parsing]] — the resulting grammar is typically LL(1) parseable after [[left-recursion-elimination]]
- [[abstract-syntax-tree]] — the AST reflects the precedence/associativity directly in its structure
- [[parse-tree]] — precedence determines the shape/depth of the parse tree

## Open Questions

- How do parser generators handle precedence/associativity without restructuring the grammar? (e.g., `%left`, `%prec` in Yacc)
- What about operators with the same precedence but different associativity?
