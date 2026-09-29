---
title: "Lecture 3: Parsing – Topic Overview"
tags: [topic-overview, software-analyse, semester-1, parsing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary

Lecture 3 covers syntax-based analysis: defining language structure with context-free grammars, building parse trees and ASTs, and parsing input via top-down (predictive/recursive descent) and bottom-up strategies including grammar transformations for unambiguous parsing.

## Core Topics

### Grammar Foundations
- [[context-free-grammar]] – the formalism for defining syntax (tokens, nonterminals, productions, start symbol)
- [[grammar-ambiguity]] – when a grammar admits multiple parse trees for the same string
- [[operator-precedence-associativity]] – resolving ambiguity by encoding precedence and associativity into grammar rules

### Parse Trees and ASTs
- [[parse-tree]] – concrete syntax tree capturing every grammar production
- [[abstract-syntax-tree]] – condensed representation that strips syntactic sugar and resolves ambiguity

### Parsing Strategies
- [[predictive-parsing]] — top-down parsing using FIRST sets; includes recursive descent and left-factoring/left-recursion elimination
- [[shift-reduce-parsing]] — bottom-up parsing using shift and reduce operations on a stack
- [[first-sets]] — the mechanism that enables predictive parsing to choose productions
- [[left-recursion-elimination]] — systematic rewrite to convert left-recursive grammars to right-recursive form
- [[left-factoring]] — eliminates common prefixes to make FIRST sets disjoint

### Translation
- [[syntax-directed-translation]] – associating semantic rules with grammar productions to compute attributes during parsing

## Connections

- Builds on [[software-analyse-lecture-1]] (lexical analysis produces the token stream consumed by the parser)
- Feeds into code generation: the lecture sketches a simple Java compiler pipeline from source to bytecode via an [[abstract-syntax-tree]]
- The CCLearner clone-detection paper uses token-frequency features; parsing refines this by understanding structural relationships between tokens

## Key Exam-Relevant Points

1. Be able to write derivations and draw parse trees for a given grammar and input string
2. Understand why ambiguity is problematic and how to fix it with grammar restructuring
3. Trace a predictive parser execution step-by-step (the `type`/`simple` example from the lecture)
4. Eliminate left recursion and apply left factoring
5. Compute FIRST sets and use them to verify predictive parse feasibility
6. Distinguish parse trees (concrete) from ASTs (abstract) and explain what information each preserves

## Open Questions

- How do LL(1) tables compare to LR(1) tables in terms of grammar coverage? (LR parsing only briefly mentioned)
- What is the relationship between syntax-directed translation and modern compiler IRs?
