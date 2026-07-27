---
title: "Lexical Analysis"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [code-clones]
---

## One-line Summary
Lexical analysis is the first phase of compilation that **converts a character stream into a sequence of tokens**, using pattern matching based on regular expressions and finite automata.

## Core Intuition
Before a compiler can understand the *structure* of a program (syntax), it must first group raw characters into meaningful chunks. Just as reading words requires recognising letter groups as units, a lexer recognizes character sequences like `result`, `=`, `100`, and `;` as distinct tokens. This separation of concerns — characters to tokens, then tokens to syntax — makes both phases simpler and more efficient.

## Formal Definition / Statement
A **lexical analyser** (lexer/scanner) is a pattern matcher for character strings that:
1. Identifies substrings of the source program that belong together (called **lexemes**)
2. Classifies each lexeme into a **lexical category** (called a **token**)
3. Skips comments and whitespace
4. Inserts lexemes into the symbol table for later processing
5. Detects and reports lexical errors (e.g., malformed floating-point literals)

The lexer is typically implemented as a function called by the parser when it needs the next token.

**Syntax analysis** consists of two parts:
- **Low-level**: Lexical analyser — mathematically, a [[finite-automata]] based on a regular grammar
- **High-level**: Syntax analyser (parser) — mathematically, a push-down automaton based on a context-free grammar (BNF)

## Key Properties / Complexity
- **Simplicity**: Separating lexical from syntactic analysis allows simpler approaches for each phase
- **Efficiency**: The lexer can be independently optimized (it's called most frequently)
- **Portability**: The lexer handles platform-specific character sets; the parser is always portable
- Lexers are specified using either:
  - Regular expressions → tool-generated (e.g., [[lex-and-flex]])
  - State transition diagrams → hand-implemented

## Worked Example
Input: `result = oldsum - value / 100;`

| Token       | Lexeme |
| ----------- | ------ |
| IDENT       | result |
| ASSIGN-OP   | =      |
| IDENT       | oldsum |
| SUBTRACT-OP | -      |
| IDENT       | value  |
| DIVISION-OP | /      |
| INT-LIT     | 100    |
| SEMICOLON   | ;      |

The lexer scans left-to-right, matching each character sequence against token patterns. Reserved words (like `while`, `if`) are typically recognized as IDENT tokens first, then looked up in a reserved-word table — this is simpler and faster than having separate patterns for each keyword.

## Common Pitfalls
- Confusing **lexeme** (the actual character string) with **token** (the category name). "result" is a lexeme; IDENT is the token.
- Thinking the lexer handles syntax — it only groups characters; the parser handles grammar.
- Forgetting that the lexer is the *most frequently called* component, so its efficiency matters greatly.

## Connections
- [[tokenization-and-token-types]] — the core output of the lexer
- [[finite-automata-and-regular-expressions]] — the mathematical foundation for lexer specifications
- [[lex-and-flex]] — practical tools for generating lexers from regular expressions
- [[code-clones]] — token-level analysis is used for clone detection (e.g., [[ccfinder]])
- [[code-naturalness-hypothesis]] — tokens produced by the lexer are the input to n-gram language models

## Open Questions
- How does the lexer interact with the symbol table in more detail?
- What happens when lexical grammar is ambiguous (longest match rule)?
- How do modern IDEs use incremental lexing for syntax highlighting?
