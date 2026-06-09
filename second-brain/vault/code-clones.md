---
title: "Code Clones"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis]
---

## One-line Summary
Code clones are identical or similar code fragments in source files, detected using text, token, graph, or metrics-based matching — a first application of character-level analysis.

## Core Intuition
Copy-paste is the most common reuse mechanism in software. It works in the short term but creates maintenance nightmares: if you fix a bug in one copy, you must remember to fix it in all copies. Detecting clones helps manage this debt.

## Formal Definition / Statement
**Code fragment**: a sequence of code lines.
**Code clone**: a code fragment that is identical or similar to another.

Clone types (taxonomy):
- **Type-1**: identical except for whitespace, layout, comments
- **Type-2**: syntactically equivalent with variations in identifiers, literals, types
- **Type-3**: syntactically similar with inserted/deleted/updated statements
- **Type-4**: semantically equivalent but syntactically different

Detection strategies:
- **Text matching**: string comparison (Type-1, some Type-2). No program structure considered.
- **Token sequence matching**: lexical tokens (Type-1, Type-2). Still no program structure.
- **Graph matching**: AST, CFG, PDG (Type-1 through Type-3, some Type-4). Uses syntactic/semantic structure.
- **Metrics-based**: compares code metrics rather than raw text.

## Key Properties
- 7-23% of code in typical software systems is cloned
- Clone detection is a prerequisite for clone management (refactoring, merging)
- Different detection strategies trade off precision vs. type coverage
- Graph-based methods catch more clone types but are more expensive

## Worked Example
**Type-1 clone** (whitespace/comment differences):
```java
// Version A
int sum = 0;
for (int i = 0; i < n; i++) {
    sum += arr[i];
}

// Version B
int sum = 0; // initialize
for(int i=0; i<n; i++){
    sum += arr[i];
}
```

**Type-2 clone** (identifier changes):
```java
// Version A
int total = 0;
for (int i = 0; i < n; i++) {
    total += arr[i];
}

// Version B
int sum = 0;
for (int j = 0; j < count; j++) {
    sum += data[j];
}
```

Text matching catches Type-1 but not Type-2. Token matching catches both.

## Common Pitfalls
- Assuming all clones are bad — some duplication is intentional or beneficial
- Thinking detection is the end goal — detection is step 1; management (refactoring, merging) is the real value
- Confusing clone types — Type-3 and Type-4 require more sophisticated analysis than simple text matching
- Ignoring false positives — not all detected "clones" are meaningful duplication

## Connections
- [[software-analysis]] — clone detection is a concrete application of analysis
- [[abstract-interpretation]] — graph-based clone detection uses AST/CFG abstractions
- [[static-vs-dynamic-analysis]] — clone detection is primarily static (text/token/graph matching)
- [[soundness-and-completeness]] — different detection strategies make different tradeoffs

## Open Questions
- How do we handle Type-4 (semantic) clones reliably?
- What's the relationship between clones and code evolution (e.g., fork-based development)?
- Can ML-based approaches detect clones that traditional methods miss?
