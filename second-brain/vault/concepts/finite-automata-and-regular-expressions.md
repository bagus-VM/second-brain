---
title: "Finite Automata and Regular Expressions"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lexical-analysis]
---

## One-line Summary
Regular expressions define token patterns formally, and finite automata (state diagrams) implement them — together they form the mathematical foundation of [[lexical-analysis]].

## Core Intuition
A lexer needs to recognize patterns like "a letter followed by zero or more letters or digits" (IDENT) or "one or more digits" (INT-LIT). Regular expressions provide a concise mathematical notation for these patterns, and finite automata provide the execution model. The key insight: every regular expression can be converted to a finite automaton, and every finite automaton can be converted to a regular expression — they are equivalent in expressive power.

## Formal Definition / Statement
**Regular expressions** over an alphabet Σ are built from:
- **ε** (empty string)
- **a** (single character, a ∈ Σ)
- **r|s** (union: match r or s)
- **rs** (concatenation: match r then s)
- **r*** (Kleene star: zero or more repetitions of r)
- **(r)** (grouping)

**Finite automata** (FA) are the simplest computational model with memory:
- **Deterministic FA (DFA)**: for each state and input character, exactly one transition
- **Nondeterministic FA (NFA)**: multiple transitions possible for same input; can include ε-transitions

**Key theorem**: For every regular expression, there exists an equivalent DFA, and vice versa. This means regular expressions and DFAs characterize exactly the **regular languages**.

## Key Properties
- Lexical grammars are regular (not context-free) — this is why simpler DFA-based tools suffice
- DFAs are guaranteed to run in **O(n)** time where n = input length
- NFAs may require backtracking but are easier to construct from regular expressions
- Practical tools (Lex/Flex) convert regex → NFA → DFA → minimized DFA → C code
- Regular languages are strictly less powerful than context-free languages (which parsers handle)

## Worked Example
Token patterns from the lecture:

**IDENT** pattern: `letter (letter | digit)*`
**INT_LIT** pattern: `digit+`

State diagram for IDENT (from lecture):
```
         letter
  [Start] ──────> [InIdent]
                    │   ↑
                    │   │ letter or digit
                    └───┘
                      │
                   other → [Accept: IDENT]
```

Implementation sketch (C):
```c
case LETTER:
    addChar();
    getChar();
    while (charClass == LETTER || charClass == DIGIT) {
        addChar();
        getChar();
    }
    return lookup(lexeme);  // check if it's a reserved word
```

The `lookup()` function checks a reserved-word table — it's simpler to recognize all names with one pattern and disambiguate afterward than to have separate patterns for each keyword.

## Common Pitfalls
- Regular expressions cannot handle nested structures (like matching parentheses) — that requires a context-free grammar
- Greedy matching (longest match) is the default in lexers — `==` is matched as one token (EQUAL), not two ASSIGN-OP tokens
- ε-transitions in NFAs don't consume input — they model "free" state changes

## Connections
- [[lexical-analysis]] — FA/regex are the mathematical foundation for lexers
- [[tokenization-and-token-types]] — token patterns are defined as regular expressions
- [[lex-and-flex]] — practical tools that compile regex to DFA-based C code
- [[code-clones]] — Type-1 clone detection operates at the token level matched by these patterns

## Open Questions
- What are the practical differences between Thompson's construction (regex → NFA) and the subset construction (NFA → DFA)?
- How does DFA minimization work and why does it matter for lexer performance?
- Can lexer generators handle Unicode character classes efficiently?
