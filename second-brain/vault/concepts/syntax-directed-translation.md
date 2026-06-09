---
title: "Syntax-Directed Translation"
tags: [concept, software-analyse, semester-1, parsing, compiler]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, parse-tree, abstract-syntax-tree]
---

## One-line Summary

Syntax-directed translation augments a CFG with attributes and semantic rules so that parsing also computes a translation (e.g., intermediate code, type annotations, or postfix notation).

## Core Intuition

Parsing tells you the structure of the input. Syntax-directed translation says: "now that you know the structure, compute something." Each grammar symbol gets attributes (data fields), and each production gets semantic rules (equations) that compute those attributes from children or siblings. A traversal of the parse tree evaluates all rules, yielding a translated result at the root.

## Formal Definition / Statement

A **syntax-directed definition** (SDD) is a triple (G, A, R) where:
- G is a context-free grammar
- A is a set of attributes for each (non)terminal
- R is a set of semantic rules for each production

**Attribute types**:
- **Synthesized attributes**: computed from children → flow bottom-up
- **Inherited attributes**: computed from parent/siblings → flow top-down or sideways

**Translation scheme**: an alternative notation that embeds semantic **actions** `{ ... }` directly in productions:

```
rest → + term { print("+") } rest
```

Actions execute in the order they appear during a left-to-right depth-first traversal.

## Key Properties

- Synthesized attributes can always be evaluated in a single bottom-up pass (post-order traversal)
- Inherited attributes may require multiple passes or careful ordering
- A translation scheme with embedded actions must ensure actions are placed where they will be executed in the correct order (especially important for top-down parsing)
- SDDs are more declarative (specify what to compute); translation schemes are more procedural (specify when to compute)

## Worked Example

**Attribute grammar** for translating infix to postfix:

| Production | Semantic Rule |
|---|---|
| expr → expr₁ + term | expr.t := expr₁.t // term.t // "+" |
| expr → expr₁ - term | expr.t := expr₁.t // term.t // "-" |
| expr → term | expr.t := term.t |
| term → 0 | term.t := "0" |
| term → 1 | term.t := "1" |
| ... | ... |
| term → 9 | term.t := "9" |

(Where `//` denotes string concatenation)

Annotated parse tree for `9 - 5 + 2`:

```
         expr.t = "95-2+"
        /   |    \
  expr.t="95-"  +   term.t="2"
   /   |    \        |
expr.t="9" - term.t="5"    2
   |           |
term.t="9"    5
   |
   9
```

Evaluation via depth-first traversal:
1. Visit leaf `9` → term.t = "9", expr.t = "9"
2. Visit leaf `5` → term.t = "5"
3. At `expr → expr₁ - term` → expr.t = "9" // "5" // "-" = "95-"
4. Visit leaf `2` → term.t = "2"
5. At `expr → expr₁ + term` → expr.t = "95-" // "2" // "+" = "95-2+"

Result at root: postfix notation "95-2+".

**Translation scheme** equivalent (procedural):
```
expr → expr + term { print("+") }
expr → expr - term { print("-") }
expr → term
term → 0 { print("0") }
term → 1 { print("1") }
...
term → 9 { print("9") }
```

Traversal prints postfix notation directly during parse.

## Common Pitfalls

- Placing actions in wrong positions in a translation scheme (especially with top-down parsing, actions must come after all references to inherited attributes)
- Forgetting that synthesized attributes flow up (children → parent) while inherited attributes flow down/sideways
- Confusing SDDs (declarative) with translation schemes (procedural)
- Assuming all attributes can be evaluated in one pass — some SDDs require multiple tree traversals

## Connections

- [[parse-tree]] — the tree that is traversed to evaluate semantic rules
- [[abstract-syntax-tree]] — AST construction is itself a syntax-directed translation
- [[context-free-grammar]] — the grammar provides the structural framework
- [[predictive-parsing]] — actions can be embedded in recursive descent procedures
- The lecture's "Simple Java Compiler" uses syntax-directed translation to go from tokens to bytecode

## Open Questions

- How do synthesized vs. inherited attributes relate to L-attributed and S-attributed grammars?
- What is the computational power of syntax-directed translations compared to Turing machines?
