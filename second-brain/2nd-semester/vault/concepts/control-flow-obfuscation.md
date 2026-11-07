---
title: "Control-Flow Obfuscation — Flattening, Opaque Predicates, Function Joining, Virtualization"
tags: [concept, reverse-and-reengineering, semester-2, obfuscation, control-flow]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[code-obfuscation]]", "[[control-flow-graph]]", "[[basic-block]]"]
---

## One-line Summary
Control-flow obfuscation destroys the shape of the program — which block runs next — while leaving the set of instructions alone, so the analyst still has code they can read but no structure to read it in.

## Core Intuition
A control-flow graph is information the analyst gets *for free*: it comes from the jump structure, not from understanding what any instruction means. This family of techniques removes that free information. The deck's statement of the goal is blunt: "obfuscation of control flow to prevent building an accurate CFG" — which "hinders manual/automatic understanding of code" (slide 15).

The six mechanisms the deck names are one idea in six strengths. Outlining and inlining move code across the function boundary until the boundary stops meaning anything; OS-based control indirection routes control through exception handlers or `longjmp` so the edge does not appear as a jump; opaque predicates add edges that always exist and are never taken; function joining merges unrelated functions into one body; **control-flow flattening** deletes the graph outright and replaces it with a dispatch loop; and **virtualization** generalises flattening until the machine code that executes is not the program's machine code at all. The escalation is deliberate — and so is the cost, because each step is more work to write and more overhead to run.

## Formal Definition / Statement
**Control-flow flattening (slide 18).** Destroy the CFG almost completely. The recipe from the slide, in its own steps:

1. **Basic blocks are numbered** ([[basic-block]]).
2. **Add a dispatcher** — a `switch` statement jumping to the given basic block number.
3. **All control-flow instructions are replaced by a jump to the dispatcher with the successor's number.**
4. It "can be combined with spurious basic blocks and/or dead code paths".

The result has exactly one kind of edge: *block → dispatcher* and *dispatcher → block*. Every loop, branch and return becomes a number written to a variable.

**Opaque predicates (slide 16).** Insert spurious branches — an "indirect jump that always takes one direction". This blows up the CFG with unused jump targets and potential cycles. The definition is an *epistemic* one, not a semantic one: an opaque predicate is "at least at runtime a constant expression, hard to prove constant by analysis". The slide's examples are arithmetic theorems, `(x*x >= 0)` and `(x << 1 % 2 == 0)`. Countermeasures, as listed: pattern matching by a given tool; brute force over all possible input values (2^32 or 2^64); SMT (satisfiability-modulo-theories solvers); dynamic analysis ignoring unused code.

**Function joining (slide 17).** Merge two unrelated functions to obfuscate semantics, with an additional argument selecting which one runs. The total size of the actual arguments should match "to avoid easy detection"; it is undefined behaviour in C but needs no cast in assembly. The slide's own example:

```c
int  foo(int x, char *z)  { /* do foo */ return x * 2; }
char bar(char *f, char *z) { /* do bar */ return f[0];  }

void *foobar(int t, void *a, void *b) {
    if (t > 0) return (int)a * 2;      /* do foo */
    else       return ((char *)a)[0];  /* do bar */
}
```

Countermeasures: split according to the selector argument; select the function to call at the call site based on the selector value; potentially remove the cast at the call site.

**Virtualization (slides 19–20).** The generalized version of flattening: "use a virtual machine to execute instructions", one of the strongest schemes, with commercial tools. The layout: an opcode with (e.g. two) operand numbers stored in a **code array**, a **virtual program counter** (vpc) used to move through that array, and operands that are pointers to a **virtual data array**. Unvirtualization, step by step: identify the vpc; statically execute the program computing the vpc ([[symbolic-execution]]); clone each block for each opcode at the vpc; connect the blocks based on vpc successors; then use compiler optimisations to clean up — [[constant-propagation]], [[dead-code-elimination]] and jump threading.

## Key Properties
- **Instructions survive; structure does not.** Flattening and opaque predicates do not add or remove the operations the program performs, so a semantics-preserving rewrite is exactly what they are.
- **One join point replaces many edges.** After flattening, the CFG's in-degree is concentrated in the dispatcher; the successor relation is *data* (a number in a variable), not control.
- **Opaque predicates are undecidable in general, cheap in practice.** Proving a runtime-constant expression constant is what the analyst cannot do quickly; brute force over 2^64 is what they will not do at all.
- **Joining is detectable by argument arity.** The slide says the argument sizes should match — i.e. a mismatched signature leaks the merge.
- **Virtualization subsumes everything else.** Flattening is a special case where the "instruction set" is one `switch`.
- **Every step costs speed**, which is why these appear on sensitive parts and not on whole programs.

## Worked Example
**Flattening the sheet's own loop.** Homework 4 problem 2 ([[reverse-and-reengineering-exercise-4]]) asks for exactly this transformation on `bar`, so it is worth doing concretely. The original:

```c
int bar() { int i = 1; int s = 0; while (i <= 100) { s += i; i++; } return s; }
```

has three basic blocks: **B1** the loop test, **B2** the body, **B3** the code after the loop. Numbered and dispatched, with the dispatcher's state variable called `next`:

```c
int bar_flat() {
    int i = 1;
    int s = 0;
    int next = 1;                        /* entry -> B1 */
    for (;;) {
        switch (next) {                  /* the dispatcher */
        case 1:  if (i <= 100) next = 2; else next = 3; break;   /* B1 */
        case 2:  s += i; i++; next = 1; break;                    /* B2 */
        case 3:  return s;                                        /* B3 */
        default: return -1;                                       /* unreachable */
        }
    }
}
```

The flattened CFG has one edge shape repeated:

```
        +---------------------------+
        |  B0  i=1; s=0; next=1     |
        +-------------+-------------+
                      | next = 1
                      v
        +---------------------------+      <---------------------+
        |  dispatcher: switch(next) |                            |
        +--+----------+-----------+--+                            |
   next=1  |    next=2 |   next=3  |                               |
           v           v           v                               |
   +--------------+ +-----------+ +-----------------+              |
   | B1 test      | | B2 body   | | B3 after loop   |              |
   | i <= 100     | | s += i    | | return s        |              |
   | next = 2 | 3 | | i++       | |                 |              |
   |              | | next = 1  | |                 |              |
   +------+-------+ +-----+-----+ +-----------------+              |
          |               |                                        |
          +---------------+----------------------------------------+
                 (both successors return to the dispatcher)
```

Both versions were compiled and run (`study/homework/reverse-and-reengineering/hw04-verify.py`, output in `output-hw04-verify.txt`):

```
  bar() = 5050   bar_flat() = 5050   equal
```

5050 is the sum 1..100, so the transformation is semantics-preserving on the sheet's own test, and the analyst's loss is visible in the diagram: the loop edge is no longer an edge, it is `next = 1`.

**The slide's two opaque predicates, checked.** Both are quoted from the deck, and both are worth checking before copying them into an exam answer:

- `(x*x >= 0)` holds in the integers but **not** in 32-bit arithmetic. The smallest positive 32-bit `x` where the product's sign bit flips is **46341**: `46341² = 2 147 488 281`, which wraps to `−2 147 479 015`. As an opaque predicate it is therefore only sound for unsigned or wide arithmetic — the deck's own example is exactly the kind of theorem that needs its width stated.
- `(x << 1 % 2 == 0)` is ambiguous. In C, `%` binds tighter than `<<`, so it parses as `(x << 1) == 0`, which is true only for `x == 0` — not a tautology at all. The intended predicate is `((x << 1) % 2 == 0)`, which *is* always true, for the trivial reason that the low bit of a left shift is 0. Written correctly it is a genuine opaque predicate; written as the slide writes it, it is a bug.

## Common Pitfalls
- **Assuming flattening needs a `switch`.** Any indirect dispatch works — a jump table, a computed indirect jump, or a virtual machine's opcode loop. The slide's `switch` is the readable form.
- **Reading a flattened function as a state machine with meaning.** The state numbers are block indices, chosen by the obfuscator; looking for meaning in them wastes time. The structures worth recovering are the reverse edges.
- **Believing opaque predicates prove unreachability.** The analysis has to *prove* the predicate constant — that is the entire difficulty — and the predicate may be constant only on the values the program actually reaches.
- **Copying the slide's arithmetic without checking the width.** See `(x*x >= 0)` above: the theorem, not the instruction, is what holds.
- **Expecting function joining to be invisible.** The slide itself notes argument sizes should match and that the C is undefined behaviour — a mismatched arity or a cast at the call site is the leak.
- **Assuming virtualization implies a full interpreter written by hand.** What the slide describes is a code array plus a virtual program counter and operands, which is a great deal less than a general VM — and correspondingly easier to unvirtualize.
- **Forgetting that unvirtualization ends in ordinary compiler work.** Identifying the vpc is the creative step; constant propagation, dead code elimination and jump threading are what make the result readable again.

## Connections
- [[code-obfuscation]] — the parent taxonomy; this is the control-flow family inside it.
- [[control-flow-graph]] and [[basic-block]] — the artefacts being destroyed, which is why this family is priced in the analyst's loss of them.
- [[reverse-and-reengineering-lecture-4]] — the slides these mechanisms come from.
- [[reverse-and-reengineering-exercise-4]] — the sheet that asks for the flattening transform and the flattened CFG, worked above.
- [[symbolic-execution]] — the unvirtualization engine: execute statically, compute the vpc, clone blocks.
- [[constant-propagation]] and [[dead-code-elimination]] — the cleanup half of unvirtualization; the same passes a compiler runs.
- [[interprocedural-analysis]] — function joining and inlining/outlining are attacks on exactly the call-graph structure that analysis depends on.
- [[disassembly]] — jump-into-opcode is the sibling technique at the byte level: both attack the analyst's entry points.
- [[binary-packing]] — the next escalation: hiding the code rather than its shape.
- [[refactoring-and-code-smells]] — flattening is a refactoring run backwards; both are semantics-preserving transformations of a CFG.

## Open Questions
- **"At least at runtime a constant expression" is doing a lot of work.** The slide never says whether the obfuscator guarantees the predicate for *all* inputs or only the inputs the program reaches; the two make different claims about the obfuscation's strength.
- **How many basic blocks a real flattening creates** — and whether spurious blocks are factored in — is not stated, so the "blows up the CFG" claim (opaque predicates) has no size attached.
- **Function joining's countermeasure "split according to the selector argument"** is given in one bullet with no worked case; whether the exam wants the transformation or only the detection heuristic is unclear.
- **No slide says how a virtual machine's original instruction set is recovered.** Unvirtualization as listed clones blocks per opcode, which presupposes knowing the opcodes; the deck does not bridge that step.
- **`(x << 1 % 2 == 0)` is printed without the parentheses that make it true.** Whether the slide is a typo or the course's own test of C precedence is not recorded anywhere in the deck.
- **The performance overhead of flattening and virtualization** is asserted in general ("disadvantage of obfuscation: slow down") but never measured; the whole family's design trade-off is therefore qualitative only.
