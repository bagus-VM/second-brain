---
title: "Software Analyse - Lecture 9: Dynamic Analysis"
tags: [topic, software-analyse, semester-1, dynamic-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [static-vs-dynamic-analysis, program-dependence-graph, dynamic-slicing]
---

## One-line Summary
Dynamic analysis observes actual program executions to collect traces, enabling instrumentation, fault localization, and debugging — trading completeness for precision.

## Core Intuition
Static analysis is conservative — it must account for all possible executions, including infeasible paths. Dynamic analysis runs the program with real inputs and watches what actually happens. This gives precise results (no false positives for observed behavior) but only covers the paths you actually test. The art is choosing representative inputs and instrumenting efficiently.

## Lecture Structure

### Why Dynamic Analysis?
Static analysis suffers from:
- **Infeasible paths**: branch combinations that can never occur together
- **Conservative over-approximation**: warns about things that never happen
- **Precision loss**: more paths = more uncertainty

Dynamic analysis solves this by observing real executions, but introduces:
- **Storage overhead**: seconds of execution = hundreds of MB of trace data
- **Heisenberg principle**: observing affects behavior (performance overhead)
- **Accuracy dependency**: results only as good as the input set

### Program Traces
Recording which instructions/statements/methods were executed, plus attributes:
- Data state (variable values)
- Call stack
- Object instance information

**Collection levels:**
| Level | Method |
|-------|--------|
| Application | Manually add logging statements |
| Instrumentation | Automatically add monitoring using libraries (e.g., AspectJ) |
| Virtual Machine | Built-in language tracing support (some languages) |
| Operating System | Built-in to BSD/Linux/macOS (DTrace) |

### Method Call Instrumentation
Two approaches:
1. **Method entry instrumentation**: add logging at start of each method
2. **Call site instrumentation**: add logging before each call

**Call graph vs call tree vs calling context tree:**
- **Call graph**: each method = node, no context sensitivity
- **Call tree**: context-sensitive, shows full call sequence
- **Calling context tree**: collapse nodes with same hierarchical context

(All built on the [[control-flow-graph]])

### Aspect-Oriented Programming (AOP)
Programs have behaviors that don't fit into single modules (logging, security, database access span many modules). See the full concept page at [[aspect-oriented-programming]].

**Core concepts:**
- **Crosscutting concerns**: system-wide behaviors spanning multiple modules
- **Aspects**: units of modularity implementing crosscutting concerns
- **Weaving**: linking aspects with core modules (compile-time, load-time, runtime)

**AspectJ terminology:**
- **Join points**: identifiable execution points (method call, field access, object creation)
- **Pointcuts**: declarations selecting join points and capturing context
- **Advice**: code executed at join points (before, after, around)
- **Aspect**: unit of modularity containing fields, methods, like a class but cannot be instantiated

**Context capture:**
- `this()`: current object
- `target()`: target object of method call
- `args()`: arguments passed to method/constructor

**Advice types:**
- **Before**: executes prior to join point
- **After**: executes following join point (can distinguish normal vs exceptional)
- **Around**: surrounds join point execution, can proceed/bypass/alter context

### Automated Debugging
Three techniques:
1. **Dynamic slicing** (see [[dynamic-slicing]], [[program-slicing]])
2. **Fault localization** (see [[fault-localization]])
3. **Delta debugging** (see [[delta-debugging]])

### Fault Localization
**Insight**: if a test case fails, its execution must have covered the faulty code. Entities primarily executed by failed tests are more likely faulty.

**Algorithm:**
1. Run test suite, record which statements each test executes
2. Build execution matrix (statements × tests)
3. Compute suspiciousness score for each statement

**Suspiciousness formulas:**
- **Tarantula**: `Susp(s) = fail(s)/totalfail / (fail(s)/totalfail + pass(s)/totalpass)`
- **Ochiai**: equivalent to cosine similarity between execution vector and error vector
- **Op2**, **Barinel**, **Dstar**: other similarity coefficients

**Visualization**: color-code statements by suspiciousness (red = high, green = low)

### Delta Debugging
**Problem**: "Yesterday my program worked. Today it does not. Why?"

**Approach**: binary search for minimal failure-inducing input change.

**Algorithm:**
1. Split input into n subsets (initially n=2)
2. If removing any subset still fails, proceed with that subset
3. Otherwise, increase granularity: n := min(2n, |input|)
4. Repeat until minimal failure-inducing change found

**Example**: Mozilla bug — simplified from 896 lines to 1 line (`<SELECT NAME="op_sys" MULTIPLE SIZE=7>`)

**Benefits:**
- Ease of communication (smaller test cases)
- Easier debugging (smaller states, shorter executions)
- Identify duplicates (simplified cases subsume duplicates)

## Key Properties
- **Precision**: very precise for observed behavior, no superfluous results
- **Depth**: can provide variable values, data types, call stacks
- **Storage**: large trace files (terabytes possible with cloud storage)
- **Heisenberg**: observation affects behavior (performance overhead)
- **Input dependency**: results only as good as test inputs

## Common Pitfalls
- Thinking dynamic analysis is "complete" because it uses real data — it only covers tested paths
- Ignoring storage overhead of traces
- Forgetting that instrumentation changes program behavior (Heisenberg)
- Assuming fault localization identifies THE bug — it ranks statements by suspiciousness, not certainty
- Confusing call graph (no context) with call tree (context-sensitive)

## Connections
- [[static-vs-dynamic-analysis]] — dynamic analysis is the "observation" paradigm
- [[dynamic-analysis]] — this lecture's topic: the field, its tradeoffs, and its techniques
- [[program-traces]] — traces are the foundational artifact of dynamic analysis (instructions, data state, call stack)
- [[dynamic-slicing]] — dynamic slicing is a dynamic analysis technique
- [[program-slicing]] — slicing can be static or dynamic; dynamic slicing is a subtopic
- [[program-dependence-graph]] — PDGs used in dynamic slicing
- [[control-flow-graph]] — call graphs, call trees, and CCTs are all built on the CFG
- [[aspect-oriented-programming]] — AOP is the mechanism for instrumentation
- [[fault-localization]] — detailed concept page with Tarantula/Ochiai walkthrough
- [[delta-debugging]] — detailed concept page with algorithm and examples
- [[hierarchy-of-analysis]] — dynamic analysis is the "observation" paradigm in the 4-level hierarchy
- [[software-analysis]] — overarching field
- [[abstract-interpretation]] — static counterpart to dynamic analysis
- [[soundness-and-completeness]] — dynamic tends toward completeness (no false positives for observed paths)
- [[software-analyse-lecture-10]] — concolic execution extends dynamic analysis with symbolic constraint collection for systematic path exploration

## Open Questions
- How do modern profilers (VisualVM, YourKit) implement insertion vs sampling?
- What's the practical tradeoff between Tarantula and Ochiai in real fault localization?
- How does delta debugging handle dependent changes (not independent subsets)?
