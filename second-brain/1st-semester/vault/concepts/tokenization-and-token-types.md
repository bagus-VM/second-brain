---
title: "Tokenization and Token Types"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [lexical-analysis]
---

## One-line Summary
Tokenization splits source code into categorized units (tokens) such as identifiers, literals, operators, and separators — the fundamental representation for both compilers and statistical code analysis.

## Core Intuition
Every programming language has a finite set of token categories. Regardless of how long or complex a program is, it's built from the same building blocks: names (IDENT), numbers (INT-LIT), operators (+, -, =), and structural markers (;, {, }). Recognizing these categories is the lexer's job, and the resulting token sequence is the foundation for both parsing and NLP-based code analysis.

## Formal Definition / Statement
A **token** is the name for a set of lexemes that share the same grammatical significance for the parser.

A **lexeme** is the actual character sequence in the source code that matches a token pattern.

Common token types:
| Token Type | Examples | Pattern |
|------------|----------|---------|
| IDENT | result, value, oldsum | Letter followed by letters/digits |
| INT-LIT | 100, 42, 0 | One or more digits |
| ASSIGN-OP | = | Single character |
| ADD-OP | + | Single character |
| SUBTRACT-OP | - | Single character |
| MULTIPLY-OP | * | Single character |
| DIVISION-OP | / | Single character |
| SEMICOLON | ; | Single character |
| LPAREN, RPAREN | (, ) | Single character |

The **symbol table** stores lexemes for identifiers for later phases (semantic analysis, code generation).

## Key Properties / Complexity
- Tokens form a **finite alphabet** — the vocabulary of the programming language at the token level
- The token sequence is a **lossy** representation: whitespace, comments, and exact formatting are discarded
- Reserved words (keywords) are typically handled as special cases of IDENT tokens via table lookup, not as separate token types
- Token-level representation is the standard input for [[code-naturalness-hypothesis]] and [[n-gram-language-models]] applied to code

## Worked Example
From the lecture's CCFinder example, the C++ program:
```cpp
int main() {
    int i = 0;
    static int j = 5;
    while(i < 20) {
        i = i + j;
    }
    std::cout << "Hello World" << i << std::endl;
    return 0;
}
```

After tokenization (type-2 clone abstraction with `$p` for identifiers):
```
$p $p() { $p $p = $p; $p $p = $p; while($p < $p) { $p = $p + $p; } $p << $p << $p << $p; return $p; }
```

This abstraction enables detecting that structurally similar programs differ only in identifier names — useful for [[code-clones]] detection.

## Common Pitfalls
- Treating tokenization as trivial — edge cases (string literals, comments inside strings, unicode identifiers) make real lexers complex
- Forgetting that different analysis tasks may need different token granularities (e.g., CCFinder uses abstracted tokens, while a compiler uses exact tokens)
- Confusing the token stream (1D sequence) with the AST (tree structure built by the parser)

## Connections
- [[lexical-analysis]] — the process that produces tokens
- [[finite-automata-and-regular-expressions]] — how token patterns are formally specified
- [[lex-and-flex]] — tools that generate tokenizers from specifications
- [[code-clones]] — token sequences enable Type-1 and Type-2 clone detection
- [[ccfinder]] — converts programs to token sequences for clone detection
- [[n-gram-language-models]] — tokens are the "words" in code language models
- [[code-naturalness-hypothesis]] — token-level statistical regularities in source code

## Open Questions
- How do different token granularities affect n-gram model quality?
- What's the impact of including/excluding separators on code naturalness metrics?
- How do modern tokenizers handle multi-language files (e.g., HTML + JavaScript)?
