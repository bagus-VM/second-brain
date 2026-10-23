---
title: "Homework 2 — Reverse- and Reengineering: x86-64 assembly to C"
tags: [homework, reverse-and-reengineering, semester-2, reverse-engineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

# Homework 2 (27.10.2026) — x86 Assembly: recovering C from machine code

The sheet states: *"This sheet is not for submission. However, we strongly encourage you to
solve the problems and bring your solutions to the tutorials for discussion."*

**How this was verified.** `hw02-verify.py` simulates the recovered functions instruction by
instruction and checks them exhaustively; the recorded run is in `hw02-verify-output.txt`.
Beyond that, two independent checks were run and are reported here:

- **Compiler round-trip.** The recovered C was compiled (`zig cc`, clang 21, `-O0`,
  `x86_64-linux-gnu`) and the generated assembly was compared instruction-by-instruction with the
  sheet's listings. They match exactly. The *logical* reading of the same functions produces
  completely different code (`sete`/`setne` + `movzbl`), which is what fixes the interpretation
  below.
- **Execution of the professor's own machine code.** The listing was assembled verbatim, called
  through a register shim (the listings use the Linux/SysV argument registers RDI/RSI/RDX, while
  Windows x64 uses RCX/RDX/R8), and executed over 165 input vectors. **0 mismatches** against the
  recovered C.

## 1. Recovering `bar` and `foo`

### The listings

The sheet prints two listings side by side. `pdftotext -layout` interleaves the two columns into
one text stream and produces a listing that does not exist; the listings below were recovered from
the PDF's word positions, splitting the page at x = 300.

**Listing 1 — `bar`:**

```asm
 1 push  rbp
 2 mov   rbp, rsp
 3 mov   dword ptr [rbp - 4], edi
 4 mov   dword ptr [rbp - 8], esi
 5 mov   eax, dword ptr [rbp - 4]
 6 or    eax, dword ptr [rbp - 8]
 7 xor   eax, -1
 8 pop   rbp
 9 ret
```

**Listing 2 — `foo`:**

```asm
 1 push  rbp
 2 mov   rbp, rsp
 3 mov   dword ptr [rbp - 4], edi
 4 mov   dword ptr [rbp - 8], esi
 5 mov   dword ptr [rbp - 12], edx
 6 mov   eax, dword ptr [rbp - 4]
 7 xor   eax, -1
 8 mov   ecx, dword ptr [rbp - 8]
 9 xor   ecx, -1
10 and   ecx, dword ptr [rbp - 12]
11 or    eax, ecx
12 pop   rbp
13 ret
```

### The arguments

Per the ia64 ABI slide in lecture 2, the first three integer arguments arrive in **RDI, RSI, RDX**
(`eax`, `esi`, `edx` in the 32-bit views used here).

- `bar` takes **two** arguments: `edi` → first, `esi` → second.
- `foo` takes **three** arguments: `edi` → first, `esi` → second, `edx` → third.

Both are stored to the stack frame (`[rbp-4]`, `[rbp-8]`, `[rbp-12]`), the standard x86-64
frame layout the lecture's call-stack slide shows.

### The recovered C

```c
int bar(int a, int b) {
    return ~(a | b);
}

int foo(int a, int b, int c) {
    return ~a | (~b & c);
}
```

### The trap: `xor eax, -1` is a *bitwise* NOT

`xor eax, -1` complements all 32 bits. It is **not** a logical `!`. So `bar(0, 0)` is
`0xFFFFFFFF`, not `1`, and `bar(1, 1)` is `0xFFFFFFFE`, not `0`.

The consequence is worth stating plainly, because it is the difference between two very different
answers:

| Reading | Result for boolean inputs | Compiles to |
|---------|---------------------------|-------------|
| `~(a\|b)` (bitwise — **correct**) | `0xFFFFFFFF` / `0xFFFFFFFE` | `or` + `xor $-1` |
| `!(a\|\|b)` (logical NOR) | `0` / `1` | `sete`/`setne` + `movzbl` |

The sheet's listing has `or` + `xor eax, -1`. That is the bitwise version, confirmed by the
compiler round-trip. So neither function is a boolean predicate: on boolean inputs **every** result
is nonzero, which means read as a truth value they are never "false".

The lecture's own instruction is on this point — the assembly slide states:

> "xor op, op: equivalent to but shorter than mov op, 0"

and the x86 ISA slide lists `xor eax, -1` under **bitvector** operations, not under the
comparison-and-flag operations. The compiler confirms the distinction: `xor eax, -1` is the
bitwise complement, and a logical negation would compile to `sete`/`setne`.

### De Morgan form for `foo`

`~a | (~b & c)` can be rewritten, in the bitwise world, as `~(a & (b | ~c))` — the same identity
that makes `!(a && (b || !c))` true in the boolean world. Both forms were checked on all 216
tested triples. The instruction order in the listing (`xor eax,-1` on `a` first, then the `b`/`c`
pair, then `or`) is what fixes the source as `~a | (~b & c)` rather than the De Morgan form: the
latter would compile to a different sequence.

### The oracle run

The professor's own machine code, assembled verbatim and executed over 165 vectors:

```
bar 0 0 -> -1        bar 0 1 -> -2        bar 0 2 -> -3        bar 0 3 -> -4
foo 0 0 0 -> -1      foo 0 0 1 -> -1      foo 1 0 0 -> -2      foo 1 0 1 -> -1
foo 1 1 0 -> -2      foo 1 1 1 -> -2
```

0 mismatches against the recovered C.

## 2. The CFG of the assembly `foo(int)`

### The listing (from the sheet)

The second program defines `foo(int)` and `main`. `foo` is:

```asm
 1 foo(int):
 2   push rbp
 3   mov rbp, rsp
 4   mov DWORD PTR [rbp-20], edi      ; n
 5   mov DWORD PTR [rbp-4], 0          ; a = 0
 6   mov DWORD PTR [rbp-8], 1          ; b = 1
 7   mov DWORD PTR [rbp-12], 0         ; result = 0
 8   cmp DWORD PTR [rbp-20], 1
 9   jg       .L2
10   mov eax, DWORD PTR [rbp-4]
11   mov DWORD PTR [rbp-12], eax
12   jmp .L3
13 .L2:
14   cmp DWORD PTR [rbp-20], 2
15   jne .L4
16   mov eax, DWORD PTR [rbp-8]
17   mov DWORD PTR [rbp-12], eax
18   jmp .L3
19 .L4:
20   mov DWORD PTR [rbp-16], 3
21   jmp .L5
22 .L6:
23   mov edx, DWORD PTR [rbp-4]
24   mov eax, DWORD PTR [rbp-8]
25   add eax, edx
26   mov DWORD PTR [rbp-12], eax
27   mov eax, DWORD PTR [rbp-8]
28   mov DWORD PTR [rbp-4], eax
29   mov eax, DWORD PTR [rbp-12]
30   mov DWORD PTR [rbp-8], eax
31   add DWORD PTR [rbp-16], 1
32 .L5:
33   mov eax, DWORD PTR [rbp-16]
34   cmp eax, DWORD PTR [rbp-20]
35   jle .L6
36 .L3:
37   mov eax, DWORD PTR [rbp-12]
38   pop rbp
39   ret
```

### The intraprocedural CFG

```
      entry
        |
        v
      B1: cmp [rbp-20], 1 ; jg .L2
        |            \
        | T (n<=1)    \ F (n>1)
        v              v
      B2: mov eax,[rbp-4]      B3: cmp [rbp-20], 2 ; jne .L4
          mov [rbp-12],eax         |                 |
          jmp .L3                  | T (n==2)        | F (n>2)
        |                           v                 v
        |                         B4: mov eax,[rbp-8]  B5: mov [rbp-16], 3
        |                           mov [rbp-12],eax      jmp .L5
        |                           jmp .L3              |
        |                           |                    v
        |                           |                  B6: cmp eax,[rbp-20] ; jle .L7
        |                           |                    |            \
        |                           |                    | T (i<=n)   \ F (i>n)
        |                           |                    v             v
        |                           |                  B7: result=a+b  (falls through to B6)
        |                           |                      a=b
        |                           |                      b=result
        |                           |                      i++
        |                           |                    |
        |                           |                    +----> B6 (back edge)
        |                           |
        +---------------------------+-----------------> B8: mov eax,[rbp-12] ; pop rbp ; ret
```

Eight basic blocks, one back edge (B7 → B6), two forward jumps to the exit (B8).

### Question 2: what does `main` call?

From the listing of `main`:

```
42 main:
43   push rbp
44   mov rbp, rsp
45   sub rsp, 16
46   lea rax, [rbp-8]
47   mov rsi, rax
48   mov edi, OFFSET FLAT:.LC0     ; the format string "%d"
49   mov eax, 0
50   call __isoc99_scanf
51   mov eax, DWORD PTR [rbp-8]
52   mov edi, eax
53   call foo(int)
54   mov DWORD PTR [rbp-4], eax
55   mov eax, DWORD PTR [rbp-4]
56   mov esi, eax
57   mov edi, OFFSET FLAT:.LC0
58   mov eax, 0
59   call printf
60   mov eax, 0
61   leave
62   ret
```

**Three calls:**

1. `__isoc99_scanf` — reads an integer into `[rbp-8]`. (The `__isoc99_` prefix is the glibc
   internal name for the C99-conforming `scanf`.)
2. `foo(int)` — the function above, called with the value read by `scanf`.
3. `printf` — prints the result with the format string `%d` (the `.LC0` literal).

So `main` reads one integer, passes it to `foo`, and prints what `foo` returns.

### Question 3: what does `foo` compute?

**The (n−1)-th Fibonacci number**, with F(0) = 0 and F(1) = 1.

The reasoning follows the CFG:

- `n <= 1` → returns `a` = **0** (block B2).
- `n == 2` → returns `b` = **1** (block B4).
- `n >= 3` → the loop runs with `i` from 3 to `n` inclusive. Each iteration sets
  `result = a + b`, then `a = b`, `b = result` — the classic two-variable Fibonacci
  update. After the iteration for `i`, the accumulator holds F(i−1), so on exit it holds **F(n−1)**.

Verified two ways — by simulation of the opcodes, and by executing the professor's machine code:

```
  n :   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
 foo :   0   0   1   1   2   3   5   8  13  21  34  55  89 144 233
F(n-1):   0   0   1   1   2   3   5   8  13  21  34  55  89 144 233
```

The oracle run (the sheet's own machine code, executed) produces exactly this sequence.

### The recovered C

```c
int foo(int n) {
    int a = 0, b = 1, result = 0;
    if (n <= 1) { result = a; }
    else if (n == 2) { result = b; }
    else {
        int i = 3;
        while (i <= n) {
            result = a + b;
            a = b;
            b = result;
            i++;
        }
    }
    return result;
}
```

## What this exercise is actually about

Three of the lecture's slides are being used at once:

- **The call stack slide** — the `push rbp / mov rbp, rsp` prologue and the `pop rbp / ret`
  epilogue, and why the frame slots are at `[rbp-4]`, `[rbp-8]`, `[rbp-12]`.
- **The instruction-types slide** — `mov` (data movement), `or`/`and`/`xor` (bitvector), `cmp`
  plus `jg`/`jne`/`jle` (comparison and conditional jumps), and `lea` (address-of, used by
  `main` to form the address of the scanf target).
- **The "information loss" problem from lecture 1** — the assembly has no names. `edi` is "the
  first argument" and nothing more; `foo` could be anything. The naming (`a`, `b`, `c`, `result`,
  `i`) is the analyst's reconstruction, and the *structure* — three arguments, an OR, two NOTs, an
  AND, an OR — is all that survives compilation. Everything else is inference.

That last point is why the compiler round-trip matters: it is the only way to tell a reconstruction
that is *equivalent* from one that merely *plausible*.

## Reproducing this

```bash
python hw02-verify.py
```

Output is in `hw02-verify-output.txt` (recorded 2026-10-22).

## Open Questions

- The sheet does not state the compiler or the optimisation level used to produce the listings.
  The round-trip match was obtained with clang at `-O0`; a different compiler or level could
  produce a different instruction sequence for the same C, so the *source* is recovered with more
  confidence than the *exact* code that produced it.
- The sheet does not say whether the parameters are `int` or `bool`. The `dword ptr` stores and
  the absence of `movzbl` argue for `int`; with `bool` parameters the same source would compile
  differently, and the "equivalent C program" would be a different answer.
- `foo_int` is a Fibonacci generator but the sheet gives no name for it, so it is not certain
  that this is the function the professor intended to exhibit rather than an incidental one.
- Whether `main`'s `sub rsp, 16` / `leave` pair is meant to be noticed (a `leave` is `mov rsp, rbp;
  pop rbp`) is not stated; the lecture's call-stack slide uses the `lea rsp, -64[rbp]` form
  instead, so the two slides do not use the same epilogue idiom.
