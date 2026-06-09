---
title: "Abstract Syntax Tree"
tags: [concept, software-analyse, semester-1, parsing, compiler]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [parse-tree, context-free-grammar]
---

## One-line Summary

An abstract syntax tree (AST) is a condensed form of the parse tree that discards syntactic details (parentheses, keywords, punctuation) and resolves ambiguity, keeping only semantically meaningful structure.

## Core Intuition

A [[parse-tree|parse tree]] records every step of the derivation — every intermediate nonterminal, every matched keyword, every pair of parentheses. An AST strips this down to the essential structure: operators become internal nodes, operands become children, and chains of single productions are collapsed. This makes the AST the ideal input for semantic analysis and code generation.

## Formal Definition / Statement

An AST is a tree where:
- **Interior nodes** represent operators or constructors (e.g., `+`, `*`, `if`, `while`)
- **Leaves** represent atomic values: identifiers (pointers to symbol table entries) or literal numbers
- **Chain collapse**: if a nonterminal has only one production (a single-production chain), it is eliminated and its child promoted
- All ambiguity is resolved by the tree structure itself (e.g., `a + b + c` has a unique AST reflecting left-associativity)

Nodes are typically represented as records:
- `mknode(op, left, right)` — operator node
- `mkleaf(id, entry)` — identifier leaf pointing to symbol table
- `mkleaf(num, val)` — numeric literal leaf

## Key Properties

- ASTs are **smaller** than parse trees (collapsed chains, no punctuation nodes)
- ASTs are **unambiguous** — even if the underlying grammar is ambiguous, the AST for a specific parse is unique
- ASTs discard: whitespace, comments, parentheses (structure encodes grouping), keyword tokens like `then`/`do`/`begin`
- The same AST can correspond to multiple parse trees (different derivation orders)
- ASTs are the standard interface between front-end (parsing) and back-end (code generation/optimization)

## Worked Example

Parse tree for `id1 + id2 * id3`:
```
       E
      /|\
     E  +  T
     |    /|\
     T   T  *  F
     |   |     |
     F   F    id3
     |   |
   id1  id2
```

AST for the same expression:
```
     +
    / \
 id1   *
      / \
   id2  id3
```

Notice: intermediate nonterminals (E, T, F) are gone. Parentheses would be implicit in the tree structure — `id1 + (id2 * id3)` produces the same AST.

Construction via translation rules:
```
E := E1 + T   →  E.ptr = mknode(+, E1.ptr, T.ptr)
E := T         →  E.ptr = T.ptr        (chain collapse)
T := T1 * F   →  T.ptr = mknode(*, T1.ptr, F.ptr)
F := id        →  F.ptr = mkleaf(id, entry.id)
F := num       →  F.ptr = mkleaf(num, val)
```

## Common Pitfalls

- Thinking the AST is "just a smaller parse tree" — it's a fundamentally different abstraction that encodes semantic meaning, not derivation steps
- Forgetting that parentheses disappear in the AST (their role is captured by tree structure)
- Not realizing that a chain-collapse rule like `E.ptr = T.ptr` means no node is created for E in that case

## Connections

- [[parse-tree]] — the AST is derived from the parse tree by simplification
- [[syntax-directed-translation]] — the mechanism for constructing ASTs during parsing
- [[context-free-grammar]] — the grammar defines what structure the AST must capture
- [[predictive-parsing]] — the parsing strategy that builds the parse tree from which the AST is derived
- Feeds into code generation: the lecture's "Simple Java Compiler" uses the AST to emit bytecode for an abstract stack machine

## Open Questions

- How do modern compilers (GCC, LLVM) represent ASTs internally? (Often as typed IR rather than generic trees)
- What is the relationship between an AST and three-address code or SSA form?
