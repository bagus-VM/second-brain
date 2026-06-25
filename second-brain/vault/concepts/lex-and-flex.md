---
title: "Lex and Flex"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [finite-automata-and-regular-expressions]
---

## One-line Summary
Lex (and its GNU successor Flex) are lexer generators that automatically convert regular expression specifications into efficient DFA-based C code for [[lexical-analysis]].

## Core Intuition
Writing a lexer by hand from a state diagram is tedious and error-prone. Lex/Flex automate this: you describe your tokens as regular expressions, and the tool generates a complete lexical analyser. This is the practical bridge between the theory ([[finite-automata-and-regular-expressions]]) and working compiler infrastructure.

## Formal Definition / Statement
A Lex/Flex specification has three sections separated by `%%`:

```
%{
  C declarations and includes
%}
  Lex definitions (aliases for regex patterns)
%%
  Rules: pattern-action pairs
%%
  C code (main function, helper functions)
```

Each rule consists of a **regular expression** and a **C action** (in braces). When the input matches a pattern, the corresponding action executes. The longest match wins; ties broken by rule order.

## Key Properties
- Lex generates a **DFA-based scanner** — guaranteed O(n) performance
- The generated code uses the function `yylex()` which the parser calls when it needs the next token
- `yytext` contains the matched lexeme; `yyleng` its length
- Flex is the GNU replacement for Lex — faster, more features, but same interface
- Lex/Flex handle the low-level character processing; they work alongside Yacc/Bison for parsing

## Worked Example
From the lecture, a simple Flex specification:

```c
%{
#include <stdio.h>
%}
%option noyywrap
%%
[0-9]+              { printf("Saw an integer: %s\n", yytext); }
[A-Za-z][A-Za-z0-9]+ { printf("Saw an id: %s\n", yytext); }
.|\\n               { /* Ignore all other characters. */ }
%%
int main(void) {
    yylex();
    return 0;
}
```

Input: `result = 42;`
Output:
```
Saw an id: result
Saw an integer: 42
```

The patterns `[0-9]+` and `[A-Za-z][A-Za-z0-9]+` are regular expressions that Flex compiles into a DFA internally.

## Common Pitfalls
- Rule order matters when multiple patterns match the same input — Lex picks the longest match, then the first rule in case of ties
- Forgetting `%option noyywrap` causes linker errors in modern Flex
- The `.` in Lex matches any character except newline — use `[\s\S]` or add explicit `\n` handling for "match everything"
- Lex-generated code is C — interfacing with C++ parsers requires care

## Connections
- [[finite-automata-and-regular-expressions]] — Lex/Flex compile regex to DFA (the theoretical foundation)
- [[lexical-analysis]] — Lex/Flex produce the lexer, the first compiler phase
- [[tokenization-and-token-types]] — the patterns define the token types
- [[ccfinder]] — CCFinder performs its own tokenization (similar principles)

## Open Questions
- How do modern alternatives (e.g., re2c, Ragel) compare to Flex?
- What are the limitations of Lex/Flex for real-world programming languages?
- How does the generated DFA handle Unicode input?
