---
title: "Homework 3 — Reverse- and Reengineering: x86 assembly to C, and the assembly CFG"
tags: [homework, reverse-and-reengineering, semester-2, x86, reverse-engineering]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-29
prerequisites: ["[[x86-assembly-and-abi]]"]
---

# Homework 3 (3.11.2026) — x86 Assembly and Control Flow Graphs

The sheet states: *"This sheet is not for submission. However, we strongly encourage you to
solve the problems and bring your solutions to the tutorials for discussion."*

**How this was verified.** `hw03-verify.py` does two independent checks and both are in
`output-hw03-verify.txt`:

- **Semantic.** The recovered C is simulated in Python and compared, instruction by
  instruction, with the sheet's own machine code, read out of the PDF's *blocks* (each listing
  line is its own text block, so the two side-by-side columns split cleanly). `f1` and `f2` agree.
- **Compiler round-trip.** The recovered C was compiled at `-O0` (zig 0.16 / clang 21,
  `x86_64-linux-gnu`) and the generated mnemonics compared with the sheet's listing.
  **Exact match, instruction for instruction**, both functions.

The round-trip is not decoration. It is what settles two things the reading alone leaves open:
that `sar` — an *arithmetic* shift — is what the listing says, and that the comparison operator
in Task 2 is `>=`, not `>` (see below).

## 1. x86 Assembly — recovering `f1` and `f2`

### The listings

The sheet prints the two listings side by side. `pdftotext -layout` interleaves the columns into
a listing that does not exist; the listings below come from the PDF's block positions, splitting
page 1 at x = 300.

**Listing 1 — `f1`:**

```asm
1 push  rbp
2 mov   rbp, rsp
3 mov   dword ptr [rbp - 4], 15
4 mov   dword ptr [rbp - 8], 2
5 mov   eax, dword ptr [rbp - 4]
6 mov   ecx, dword ptr [rbp - 8]
7 sar   eax, cl
8 pop   rbp
9 ret
```

**Listing 2 — `f2`:**

```asm
1 push  rbp
2 mov   rbp, rsp
3 mov   dword ptr [rbp - 4], 10
4 mov   dword ptr [rbp - 8], 2
5 mov   eax, dword ptr [rbp - 4]
6 mov   ecx, dword ptr [rbp - 8]
7 shl   eax, cl
8 pop   rbp
9 ret
```

### The recovered C

```c
int f1(void) {
    int x = 15;
    int y = 2;
    return x >> y;
}

int f2(void) {
    int x = 10;
    int y = 2;
    return x << y;
}
```

`f1()` is **3** and `f2()` is **40**. Both were produced by running the compiled original, not by
hand.

### Why these are not functions of their arguments

The first thing to notice is what is *not* in the listing: no store of `edi`, `esi` or any other
argument register. Both functions take no parameters. The two values they shift are compile-time
constants (`15` and `2`, `10` and `2`) that the compiler has spilled to `[rbp-4]` and `[rbp-8]`
because optimisation is off. A student who reflexively assumes "two `mov`s into the frame from
`edi`/`esi`" reads in arguments that are not there.

### The shift that is not a division, and the shift that is not a multiplication

```asm
mov ecx, dword ptr [rbp - 8]    ; the shift count MUST be in cl
sar eax, cl                     ; arithmetic: fills with the sign bit
shl eax, cl                     ; logical left
```

Three details carry the marks.

**The count lives in `cl`.** x86 has no "shift by an immediate in a named register" form when the
count is a variable: the count is either an immediate or `cl`. Note also that x86 masks the count
to **five bits** for 32-bit operands, so `x >> 40` shifts by 8, not by 40.

**`sar` is arithmetic, `shr` is logical.** `sar` replicates the sign bit; `shr` shifts zeros in.
That distinction is the whole reason the recovered C is `>>` on a *signed* `int`:

```
  v     sar v>>2      shr v>>2
 -16       -4       1073741820
  -8       -2       1073741822
  -1       -1       1073741823
   0        0                0
   7        1                1
```

Had the source been `unsigned x`, the compiler would have emitted `shr`. The listing says `sar`,
so the type is signed — a conclusion the reading of the operand alone does not give you. (This
is the same trap as Homework 2's `xor eax, -1`, which is a *bitwise* NOT and not a logical `!`.)

**`shl` is not multiplication by a constant.** `f2` returns `10 << 2 = 40`. Written as
multiplication it would be `×4`, but the compiler emitted a shift because the C said `<<`. On
signed overflow these differ: shifting into the sign bit is undefined behaviour in C, while
`sar`/`shl` on a machine just discard the bits.

## 2. Control Flow Graphs — `max` and `main`

### What `max` computes

**`max` prints, for each of its three arguments that is greater than or equal to the other two,
one line `%d is the largest number.`** With `main`'s arguments 100, 200, 400 exactly one line is
printed — `400 is the largest number.` Ties print more than once: `max(5, 5, 1)` prints the line
twice, once for each 5.

The recovered C:

```c
int max(int a, int b, int c) {
    int m;                                   /* [rbp - 4]: never assigned */
    if (a >= b && a >= c) printf("%d is the largest number.\n", a);
    if (b >= a && b >= c) printf("%d is the largest number.\n", b);
    if (c >= a && c >= b) printf("%d is the largest number.\n", c);
    return m;                                /* reads a slot nothing ever wrote */
}
```

### How the operator is known to be `>=` and not `>`

The listing's condition is a `cmp` followed by `jl`:

```asm
mov eax, dword ptr [rbp - 8]      ; a
cmp eax, dword ptr [rbp - 12]     ; a - b
jl  .L3                           ; if a < b, skip the body
```

`jl` is "jump if less" — it skips the body when `a < b`, i.e. it *takes* the body when
`a >= b`. Had the source said `a > b`, the compiler would have emitted `jle`. Compiling both
candidates side by side settles it:

```
`a >= b && a >= c` -> conditional jumps: jl  jl  jl  jl  jl  jl
`a >  b && a >  c` -> conditional jumps: jle jle jle jle jle jle
```

The sheet uses `jl` at lines 9, 10 and 11. The source used `>=`. This is a case where reading
the assembly tells you the *branch*, and only the compiler tells you which C comparison produces
it — which is why the round-trip is worth running.

### The return value is indeterminate

Line 40 of the listing is `mov eax, dword ptr [rbp - 4]`. Trace what writes `[rbp-4]` in `max`:
nothing. The three arguments are stored to `[rbp-8]`, `[rbp-12]` and `[rbp-16]`, and every
comparison reads those. `[rbp-4]` is a fourth slot that the function reads and never writes.

So `max` returns an **indeterminate value**. It is safe only because `main` throws the result
away: after `call max` the very next instruction is `xor eax, eax`, `main`'s `return 0`. The
observable behaviour of the program is therefore the printed lines and nothing else.

The same reading is what identifies the extra slot in `main`:

```asm
49 mov dword ptr [rbp - 4], 0     ; an int initialised to 0 and never read
50 mov dword ptr [rbp - 8], 100
51 mov dword ptr [rbp - 12], 200
52 mov dword ptr [rbp - 16], 400
53 mov edi, dword ptr [rbp - 8]
54 mov esi, dword ptr [rbp - 12]
55 mov edx, dword ptr [rbp - 16]
56 call max
```

Four frame slots, three of them the call's arguments, the fourth a variable that is written once
and never used. The recovered C:

```c
int main(void) {
    int unused = 0;          /* [rbp - 4] */
    int a = 100, b = 200, c = 400;
    max(a, b, c);
    return 0;
}
```

The compiler round-trip reproduces this too, including the argument registers: 100 → `edi`,
200 → `esi`, 400 → `edx`, the SysV order the ia64 ABI slide fixes.

### (a) Intra-procedural CFG of `max`

Basic blocks are delimited by the three labels. `jl` is a **conditional** edge; the fall-through
is the implicit edge the listing does not show.

```
        [B0] lines 1-9
   push rbp / mov rbp,rsp / sub rsp,16
   [rbp-8]=edi  [rbp-12]=esi  [rbp-16]=edx
        |
        v
   [B1] lines 10-12        mov eax,[rbp-8] ; cmp eax,[rbp-12] ; jl
     |                                    \
     | (a >= b) fall through               \ (a < b) -> jump
     v                                      \
   [B2] lines 13-16                          \
   mov eax,[rbp-8] ; cmp eax,[rbp-16] ; jl   |
     |                            \          |
     | (a >= c)                    \ (a < c) |
     v                              \        |
   [B3] lines 17-19 printf(a)        \       |
     |                               \       |
     +--------------------------------\------+
                                      \     |
                                       v    v
                                     [B4] .L3 lines 20-22
                                     mov eax,[rbp-12] ; cmp eax,[rbp-8] ; jl
                                       |              \
                                       | (b>=a)        \ (b<a)
                                       v                \
                                     [B5] lines 23-26     |
                                     mov eax,[rbp-12]     |
                                     cmp eax,[rbp-16] ; jl|
                                       |            \     |
                                       | (b>=c)      \    |
                                       v              \   |
                                     [B6] lines 27-29   \  |
                                     printf(b)          \ |
                                       |                 \|
                                       +------------------+
                                                           \
                                                            v
                                                     [B7] .L6 lines 30-32
                                                     mov eax,[rbp-16] ; cmp eax,[rbp-8] ; jl
                                                       |                \
                                                       | (c>=a)          \ (c<a)
                                                       v                  \
                                                     [B8] lines 33-36       |
                                                     mov eax,[rbp-16]       |
                                                     cmp eax,[rbp-12] ; jl  |
                                                       |        \           |
                                                       | (c>=b)  \ (c<b)     |
                                                       v          \         |
                                                     [B9] lines 37-39        |
                                                     printf(c)               |
                                                       |                     |
                                                       +---------------------+
                                                                    \
                                                                     v
                                                             [B10] .L9 lines 41-44
                                                             mov eax,[rbp-4]
                                                             add rsp,16 / pop rbp / ret
```

Fifteen basic blocks once the `printf` bodies are separated from the guard blocks; **six**
conditional branches, all `jl`, all on the same shape (`cmp` two frame slots, branch away).

### (b) Inter-procedural CFG

`main` has two blocks — prologue-plus-stores, then the call and return — and one call edge:

```
[main:B0]  lines 1-7   prologue; [rbp-4]=0; [rbp-8]=100; [rbp-12]=200; [rbp-16]=400
     |
     v   call max(a,b,c)   ---- call edge ---->  [max:B0]
[main:B1]  lines 8-11  xor eax,eax / epilogue / ret
     ^
     +-- return edge from [max:B10]
```

The inter-procedural graph is what makes the argument mapping visible: `[main:rbp-8]` → `edi` →
`[max:rbp-8]`. Same slot number, two different frames — which is exactly why an inter-procedural
analysis cannot be done by matching offsets, and why the slide on the call stack spends its time
on prologue and epilogue.

### `main` calls exactly one function

`max`, and nothing else. `printf` is called *from inside* `max`, not from `main`; a
call-graph read off `main`'s listing alone will miss it.

## What this sheet is really testing

Three ideas, all of which recur in the exam material:

1. **The operand is the evidence, the type is the inference.** `sar` versus `shr` and `jl` versus
   `jle` are one instruction each, and each one decides a fact about the C that no amount of
   staring at the values can recover. Compiling the candidate and diffing settles it.
2. **Unused and uninitialised slots are information.** The `[rbp-4]` that nothing writes is not
   noise; it is a variable in the original source, and reading it correctly is what separates
   "`max` returns the largest argument" from "`max` returns whatever was in that slot".
3. **`printf` inside a comparison ladder is a control-flow trap.** Three `if`s that look
   mutually exclusive are not: on a tie, two of them fire.

## Connections

- [[x86-assembly-and-abi]] — the registers, the `cmp`/`jl` idiom, and the call-stack slide this
  sheet's prologues follow.
- [[reverse-and-reengineering-lecture-3]] — the binaries deck; the ELF and dynamic-linking
  material that comes after this sheet.
- [[reverse-and-reengineering-exercise-3]] — the session page for this homework.
- [[control-flow-graph]] and [[basic-block]] — the structures drawn above, from Semester 1.
- [[reverse-engineering]] — where recovering C from machine code sits in the course's arc.
- [[program-dependence-graph]] — the next step after the CFG, from Homework 1.

## Open Questions

- **Which compiler produced the sheet's listing is not stated, and the frame layout differs from
  clang's.** The sheet puts the arguments at `[rbp-8]`, `[rbp-12]`, `[rbp-16]` and returns from
  `[rbp-4]`; the same C compiled here puts them at `[rbp-4]`, `[rbp-8]`, `[rbp-12]` and returns
  from `[rbp-16]`. GCC and clang differ, and the listing's own style (`mov dword ptr`, `.L3`)
  is GCC's. The instruction *sequence* matches exactly in both cases; only the slot numbering is
  shifted by one. This was not chased further because it changes nothing about the answers.
- **The `m` in `max` is never assigned.** Whether the original source really returned an
  uninitialised variable, or whether a line was lost when the sheet was prepared, cannot be
  determined from the listing — the listing simply contains no store to that slot. It is
  reported as the listing reads.
- **`max` has a `sub rsp, 16` for three arguments and no callee-saved register spills.** Nothing
  in the listing requires the 16 bytes; with `-O0` that is normal, but it means the frame size
  carries no information here.
- **The `main` listing stores five values into four slots and passes three arguments, and it
  never reads the return value.** The last is deliberate (`return 0`), but whether the sheet
  intended students to notice the discarded return, or the unused slot, is not stated.
