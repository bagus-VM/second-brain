---
title: "Homework 4 — Reverse- and Reengineering: x86-64 Assembly to C, and Control-Flow Flattening"
tags: [homework, reverse-and-reengineering, semester-2, x86, obfuscation]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-11-05
prerequisites: ["[[x86-assembly-and-abi]]", "[[control-flow-obfuscation]]"]
---

# Homework 4 (10.11.2026) — x86 Assembly and Control-Flow Flattening

The sheet states: *"This sheet is not for submission. However, we strongly encourage you to
solve the problems and bring your solutions to the tutorials for discussion."* (Prof. Dr.
Christian Hammer, Dr. Mohammad Rezaalipour.)

**How this was verified.** `hw04-verify.py` runs five checks and prints its results to
`output-hw04-verify.txt`. Nothing below is asserted that the script does not execute:

- **Listing recovery.** The 19-line listing is read out of the PDF by line position. `pdftotext
  -layout` interleaves the row numbers with the instructions and emits a listing that does not
  exist (the tail comes out as a stack of bare `mov` mnemonics with their operands on the
  following line), so the recovery is positional: each row is three separate text lines — number,
  mnemonic, operands — at slightly different baselines, clustered by y and read left to right.
- **Simulation.** The recovered listing is interpreted instruction by instruction in Python (a
  `push`/`mov`/`pop`/`ret` subset) and compared with the recovered C on four input pairs plus the
  aliased call where `xp == yp`.
- **Compiler round-trip.** The recovered C is compiled at `-O0` in Intel syntax and compared,
  instruction for instruction, with the sheet's listing.
- **Real execution.** The sheet's listing is transcribed verbatim into an assembler source,
  assembled unchanged, linked against a driver, and run under WSL.
- **Flattening.** The flattened `bar` and the original are compiled into one program and run.

Result: `RESULT: 0 mismatches`.

## 1. x86-64 Assembly — recovering `decode`

### The listing

```
 1  decode:
 2      push   rbp
 3      mov    rbp, rsp
 4      mov    qword ptr [rbp - 8], rdi
 5      mov    qword ptr [rbp - 16], rsi
 6      mov    rax, qword ptr [rbp - 8]
 7      mov    rax, qword ptr [rax]
 8      mov    qword ptr [rbp - 24], rax
 9      mov    rax, qword ptr [rbp - 16]
10      mov    rax, qword ptr [rax]
11      mov    qword ptr [rbp - 32], rax
12      mov    rcx, qword ptr [rbp - 24]
13      mov    rax, qword ptr [rbp - 16]
14      mov    qword ptr [rax], rcx
15      mov    rcx, qword ptr [rbp - 32]
16      mov    rax, qword ptr [rbp - 8]
17      mov    qword ptr [rax], rcx
18      pop    rbp
19      ret
```

### The recovered C

```c
void decode(long *xp, long *yp) {
    long a = *xp;
    long b = *yp;
    *yp = a;
    *xp = b;
}
```

**How the shape is read.** `rdi` and `rsi` are the first two integer arguments ([[x86-assembly-and-abi]]),
spilled to `[rbp-8]` and `[rbp-16]`; the frame then reserves `[rbp-24]` and `[rbp-32]` for the two
dereferenced values. Instructions 6–11 load `*xp` into `[rbp-24]` and `*yp` into `[rbp-32]`;
12–14 store the first across into `*yp`; 15–17 store the second into `*xp`. It is a swap, and the
order of the two stores is what the listing fixes.

**Why the order is part of the answer.** The natural one-liner `long t = *xp; *xp = *yp; *yp = t;`
is semantically equivalent for distinct pointers and compiles to a *different* listing. The
round-trip measures it rather than asserting it:

```
  at instruction 9:  listing `mov rax, qword ptr [rax]`  vs  alternative `mov rcx, qword ptr [rax]`
  at instruction 10:  listing `mov qword ptr [rbp - 32], rax`  vs  alternative `mov rax, qword ptr [rbp - 8]`
  at instruction 11:  listing `mov rcx, qword ptr [rbp - 24]`  vs  alternative `mov qword ptr [rax], rcx`
    (8 of 18 instructions differ: the statement order is what the round-trip pins down.)
```

The listing's version loads both values before writing either, so it is also correct when
`xp == yp` — which the alternative is too, for different reasons, and which the driver checks.

### Round-trip

The recovered C, compiled at `-O0` with `-masm=intel`:

```
  EXACT MATCH, instruction for instruction
```

All 18 instructions, in order and with identical operands. (The sheet numbers 19 rows because row
1 is the label.)

### But the listing is not merely consistent with the C — it *runs* as the C predicts

The sheet's listing was transcribed into `decode_sheet.s`, assembled without alteration, and
linked against a driver that calls both implementations:

```
  distinct  in (7, 42) -> sheet (42, 7)  C (42, 7)  same
  negative  in (-1, 0) -> sheet (0, -1)  C (0, -1)  same
  equal     in (5, 5) -> sheet (5, 5)  C (5, 5)  same
  extreme   in (9223372036854775807, -9223372036854775808) -> sheet (-9223372036854775808, 9223372036854775807)  C (-9223372036854775808, 9223372036854775807)  same
  aliased   in (&v, &v) v=99 -> v=99
```

The "extreme" row is the interesting one for a 64-bit swap: the values are exchanged through
`rax`/`rcx`, so there is no arithmetic, no overflow and no sign question — a swap is exact for
every pair of bit patterns.

## 2. Control-Flow Flattening

### The original and its blocks

```c
int bar(){
    int i = 1;
    int s = 0;
    while (i <= 100) { s += i; i++; }
    return s;
}
```

Three basic blocks ([[basic-block]]): **B1** the loop test `i <= 100`, **B2** the body
`s += i; i++`, **B3** the code after the loop, `return s`. The entry block (initialising `i`, `s`
and the dispatcher state) is numbered B0 for the drawing only.

### 2.1 The transformation

Number the blocks; add a dispatcher that jumps to a block by number; replace every control-flow
instruction by "write the successor's number, jump to the dispatcher" ([[control-flow-obfuscation]]):

```c
int bar(){
    int i = 1;                        /* B0: entry */
    int s = 0;
    int next = 1;                     /* -> B1 */
    for (;;) {
        switch (next) {               /* the dispatcher */
        case 1:                       /* B1: the loop test */
            if (i <= 100) next = 2;   /* true  -> B2 */
            else          next = 3;   /* false -> B3 */
            break;
        case 2:                       /* B2: the loop body */
            s += i;
            i++;
            next = 1;                 /* -> B1 */
            break;
        case 3:                       /* B3: after the loop */
            return s;
        default:                      /* unreachable; kept for completeness */
            return -1;
        }
    }
}
```

Both versions compiled and run together:

```
  bar() = 5050   bar_flat() = 5050   equal
```

5050 is 1+2+…+100, so the transformation preserves the sheet function's result on its own test.

### 2.2 The flattened CFG

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

Block B1 has two exits and they differ only in the number written to `next`; both go to the same
place. The loop edge — the single edge the original CFG was *built around* — is now the constant
`next = 1`, and the only structural fact left in the graph is that everything passes through the
dispatcher. That is exactly the deck's claim that flattening destroys the CFG "almost completely":
the blocks survive, their arrangement does not.

`hw04-verify.py` prints each version's instructions and the run output; the C sources are embedded
in the script, so both problems can be re-run with
`uv run --with pymupdf python hw04-verify.py --zig <path to zig>`.

## Where this leaves the two problems

| Problem | Deliverable | State |
|---|---|---|
| 1. `decode` | C equivalent + round-trip + execution | **verified four ways** — simulation, exact compiler round-trip, assembled and run, aliasing case |
| 2. Control-Flow Flattening | flattened C + flattened CFG | **run**: flattened and original agree (5050); CFG drawn above |

The sheet is not for submission; the value here is that both answers were checked against something
other than persuasion — the compiler for problem 1, execution for problem 2.
