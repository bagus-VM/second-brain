---
title: "CCFinder"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [tokenization-and-token-types, code-clones]
---

## One-line Summary
CCFinder is a token-based [[code-clones|code clone]] detection tool that converts programs to token sequences and finds the longest common subsequences, using parameterized tokens for type-2 clone detection.

## Core Intuition
To detect code clones at the token level, you need to: (1) convert source code to a flat token sequence, (2) abstract away identifier names so structural similarity is visible, and (3) find common subsequences. CCFinder does exactly this — it's a practical application of [[lexical-analysis]] and [[tokenization-and-token-types]] to the clone detection problem.

## Formal Definition / Statement
CCFinder's algorithm (from the lecture):

**Step 1**: Convert a program with multiple files to a single long token sequence
**Step 2**: Find longest common subsequences of tokens

The key innovation is **parameterized tokenization** — replacing all identifiers with placeholder tokens (`$p`) so that structurally identical code with different variable names is detected as a clone.

## Key Properties
- Operates at the **token level** — handles type-1 and type-2 clones
- Parameterized abstraction (`$p` for identifiers) enables type-2 detection
- Converts entire programs to flat token sequences (lossy — whitespace, comments discarded)
- Uses suffix-tree algorithms for efficient subsequence matching
- Scales to large codebases (millions of lines)

## Worked Example
Original C++ code:
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

After parameterized tokenization:
```
$p $p() { $p $p = $p; $p $p = $p; while($p < $p) { $p = $p + $p; } $p << $p << $p << $p; return $p; }
```

Now if another file contains structurally identical code with different variable names, the parameterized token sequences will match — detecting a type-2 clone.

## Common Pitfalls
- CCFinder doesn't detect type-3 (similar but modified) or type-4 (semantically equivalent) clones
- The flat token sequence loses structural information — no AST or control flow
- Parameterized abstraction is coarse — it treats all identifiers equally, losing semantic context
- False positives from very common patterns (e.g., boilerplate code)

## Connections
- [[tokenization-and-token-types]] — CCFinder's first step is tokenization
- [[lexical-analysis]] — produces the tokens CCFinder operates on
- [[code-clones]] — CCFinder is a tool for clone detection
- [[code-naturalness-hypothesis]] — token-level analysis is shared between clone detection and naturalness measurement
- [[n-gram-language-models]] — both approaches work on token sequences

## Open Questions
- How does CCFinder compare to AST-based clone detectors?
- Can n-gram models improve clone detection by filtering common/uncommon patterns?
- How does the choice of token abstraction affect detection accuracy?
