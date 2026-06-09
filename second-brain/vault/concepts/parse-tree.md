---
title: "Parse Tree"
tags: [concept, software-analyse, semester-1, parsing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar]
---

## One-line Summary

A parse tree (concrete syntax tree) is a tree representation of a derivation where the root is the start symbol, interior nodes are nonterminals, and leaves are tokens.

## Core Intuition

A parse tree makes a derivation visible as a tree: each production A → X₁ X₂ … Xₙ becomes a node A with children X₁ through Xₙ. Reading the leaves left to right recovers the input string. Unlike an [[abstract-syntax-tree]], the parse tree preserves every syntactic detail — parentheses, keywords, intermediate nonterminals.

## Formal Definition / Statement

Given CFG G = (T, N, P, S), a parse tree is a rooted tree such that:
1. The root is labeled S (start symbol)
2. Every leaf is labeled with a terminal ∈ T or ε
3. Every interior node is labeled with a nonterminal ∈ N
4. If an interior node A has children X₁, X₂, …, Xₙ, then A → X₁ X₂ … Xₙ is a production in P

The **yield** of the tree is the concatenation of leaf labels (left to right), which is a string in L(G).

## Key Properties

- A parse tree corresponds to a **rightmost** or **leftmost** derivation (depending on the order of expansion)
- For an unambiguous grammar, every string in L(G) has exactly one parse tree
- Parse trees are **not** unique representations of derivations — different derivation orders (leftmost vs rightmost) can produce the same tree
- The tree structure directly reflects operator grouping and nesting

## Worked Example

For the grammar:
```
list  → list + digit | list - digit | digit
digit → 0 | 1 | 2 | ... | 9
```

Parse tree for `9 - 5 + 2`:
```
        list
       / | \
    list  +  digit
   / | \       |
list - digit    2
  |       |
digit    5
  |
  9
```

Reading leaves left to right: 9, -, 5, +, 2. The tree encodes that `-` binds to `list` (left operand), reflecting left-associativity: (9 - 5) + 2.

## Common Pitfalls

- Conflating parse trees with [[abstract-syntax-tree|ASTs]] — parse trees are concrete and verbose; ASTs are abstract and compact
- Drawing a parse tree that doesn't correspond to any valid derivation (every interior node must match a production)
- Forgetting that the same parse tree can arise from different derivation orders

## Connections

- [[context-free-grammar]] — defines the rules that constrain parse tree structure
- [[abstract-syntax-tree]] — a simplified version of the parse tree
- [[grammar-ambiguity]] — when multiple valid parse trees exist for the same input
- [[predictive-parsing]] — constructs the parse tree top-down from root to leaves
- [[syntax-directed-translation]] — attributes are computed by traversing the parse tree

## Open Questions

- How does the size of a parse tree relate to the length of the input string?
- In what situations is it useful to keep the full parse tree rather than converting to an AST?
