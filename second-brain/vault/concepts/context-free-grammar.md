---
title: "Context-Free Grammar"
tags: [concept, software-analyse, semester-1, parsing, formal-languages]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

A context-free grammar (CFG) is a 4-tuple (tokens, nonterminals, productions, start symbol) that defines the syntactic structure of a language through rewrite rules.

## Core Intuition

A CFG works like a set of rewriting rules: start from a special symbol and repeatedly expand nonterminals using their production rules until only concrete tokens remain. The set of all token sequences you can reach defines the language. "Context-free" means any nonterminal can be rewritten regardless of where it appears.

## Formal Definition / Statement

A context-free grammar is a 4-tuple G = (T, N, P, S) where:
- T = finite set of **tokens** (terminal symbols)
- N = finite set of **nonterminals** (syntactic categories)
- P = finite set of **productions** of the form A → α, where A ∈ N and α ∈ (T ∪ N)*
- S ∈ N is the **start symbol**

A **sentential form** is any string derivable from S. A **sentence** is a sentential form containing only terminals. The **language** L(G) is the set of all sentences.

## Key Properties

- Every regular grammar is context-free, but not vice versa
- CFGs can describe nested/balanced structures (e.g., matching parentheses) that regular grammars cannot
- A CFG may be **ambiguous** (multiple parse trees for one string) or unambiguous
- Parsing a string against a CFG is decidable; the general problem is O(n³) but practical parsers run in linear time for programming language grammars

## Worked Example

Grammar G for simple expressions:

```
G = <{list, digit}, {+,-,0,1,...,9}, P, list>

Productions:
  list  → list + digit
  list  → list - digit
  list  → digit
  digit → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

Derivation of `9 - 5 + 2`:

```
list
⇒ list + digit
⇒ list - digit + digit
⇒ digit - digit + digit
⇒ 9 - digit + digit
⇒ 9 - 5 + digit
⇒ 9 - 5 + 2
```

Each step replaces one nonterminal with the right-hand side of one of its productions.

## Common Pitfalls

- Confusing tokens (terminals) with nonterminals — tokens are the leaves of the parse tree
- Forgetting that productions can use ε (empty string)
- Assuming a grammar is unique for a language — many grammars generate the same language
- Mixing up "derives" (⇒) with "produces" (→): ⇒ is a derivation step, → is a production rule

## Connections

- [[parse-tree]] — each derivation corresponds to a parse tree
- [[grammar-ambiguity]] — arises when a CFG admits multiple parse trees
- [[operator-precedence-associativity]] — restructuring the grammar to resolve ambiguity
- [[predictive-parsing]] — requires the grammar to have disjoint FIRST sets for alternatives
- [[left-recursion-elimination]] — a grammar transformation needed for top-down parsing

## Open Questions

- What is the boundary between context-free and context-sensitive grammars in practice?
- How do parser generators (Yacc, ANTLR) handle CFGs that are not LL(1) or LR(1)?
