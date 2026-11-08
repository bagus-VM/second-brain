---
title: "Grammar Ambiguity"
tags: [concept, software-analyse, semester-1, parsing, formal-languages]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [context-free-grammar, parse-tree]
---

## One-line Summary

A grammar is ambiguous if at least one string in its language has more than one valid parse tree, meaning the syntactic structure is not uniquely determined.

## Core Intuition

Ambiguity means the grammar is "underspecified" — it doesn't tell us which parse tree is correct. Consider `9 - 5 + 2`: should this be `(9 - 5) + 2` or `9 - (5 + 2)`? If the grammar allows both parses, it's ambiguous. In practice, ambiguity is always resolved — either by restructuring the grammar or by external disambiguation rules (e.g., precedence declarations in parser generators).

## Formal Definition / Statement

A context-free grammar G is **ambiguous** if there exists at least one string w ∈ L(G) that has **two or more distinct parse trees** (equivalently, two or more distinct leftmost derivations).

An **unambiguous grammar** for the same language guarantees exactly one parse tree per string.

## Key Properties / Complexity

- Ambiguity is a property of the **grammar**, not the language — the same language can be described by both ambiguous and unambiguous grammars
- The ambiguity problem (determining if a CFG is ambiguous) is **undecidable** in general
- Every ambiguous grammar can be replaced by an unambiguous grammar for the same language (though this may require restructuring)
- In practice, parser generators handle ambiguity via precedence/associativity declarations rather than grammar rewriting

## Worked Example

Ambiguous grammar:
```
string → string + string | string - string | 0 | 1 | ... | 9
```

The string `9 - 5 + 2` has two parse trees:

Parse tree 1 (groups as `(9 - 5) + 2`):
```
       string
      /  |  \
  string - string
    |         |
    9    string + string
              |       |
              5       2
```

Parse tree 2 (groups as `9 - (5 + 2)`):
```
       string
      /  |  \
  string - string
    |         |
 string + string   2
   |       |
   9       5
```

Fix: rewrite with explicit precedence levels:
```
expr → expr + term | expr - term | term
term → digit
digit → 0 | 1 | ... | 9
```

Now `9 - 5 + 2` has only one parse tree: `expr(expr(9) - term(5)) + term(2)`.

## Common Pitfalls

- Thinking ambiguity means "the language is ambiguous" — it's always the grammar
- Assuming you can algorithmically detect ambiguity for any CFG (you can't — it's undecidable)
- Forgetting that even if the semantics are clear to humans, the parser needs a unique tree
- Confusing ambiguity with left recursion — they are independent issues

## Connections

- [[context-free-grammar]] — ambiguity is defined relative to CFGs
- [[parse-tree]] — ambiguity manifests as multiple parse trees for one string
- [[operator-precedence-associativity]] — the standard technique for resolving ambiguity in expression grammars
- [[predictive-parsing]] — requires unambiguous grammars (disjoint FIRST sets)
- [[abstract-syntax-tree]] — the AST resolves ambiguity even if the grammar doesn't

## Open Questions

- Are there inherently ambiguous context-free languages (languages where every CFG is ambiguous)? Yes — there exist such languages, though they are artificial.
- How do tools like Yacc/Bison handle ambiguity via `%left`, `%right`, `%prec` declarations?
