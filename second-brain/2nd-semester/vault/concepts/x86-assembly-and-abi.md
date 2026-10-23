---
title: "x86 Assembly and ABI"
tags: [concept, reverse-and-reengineering, semester-2, x86, assembly]
course: "Reverse- and Reengineering"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: ["[[binary-reverse-engineering]]"]
---

## One-line Summary
The x86 family is a CISC instruction set whose 16-, 32- and 64-bit generations differ in
registers, addressing modes and calling convention, and a binary analyst must decode all three
to read machine code.

## Core Intuition

Everything a reverse engineer does at the code level is downstream of three facts about x86:
the instruction encoding is **variable-length** (1 to 15 bytes), the **addressing modes are
powerful** (base + index × scale + displacement), and the **register file is inhomogeneous**
(some registers only work with some instructions). A byte stream is therefore not a list of
instructions until it is decoded, and the decoding rules change between generations. That is why
the lecture spends its second half on the ISA rather than on analysis technique: the analyst
cannot find the basic blocks without knowing where one instruction ends and the next begins,
and cannot find the call frames without knowing the ABI.

The second intuition is that x86 is a *historical* ISA. It is not one design but a stack of
compatibilities: 16-bit real mode with memory segmentation, then protected mode, then 32-bit
registers and a protected-mode address space, then MMX and SIMD extensions, then a 64-bit form
that removes certain 16/32-bit instructions. Each generation is constrained by the previous
one, which is exactly why the 64-bit mode keeps the same register names with a prefix and keeps
partial-register semantics.

## Formal Definition / Statement

**Evolution (slide 15).** As the slides state it:

- 16-bit architecture: 8086 and 8088 (only 8-bit bus).
- Real mode (only), memory segmentation.
- 80286: protected mode.
- 32-bit architecture (ia32): 80386 with 32-bit registers and protected-mode address space.
- Pentium family introduced MMX + MMX registers, SIMD extensions.
- 64-bit architecture (ia64) — the slide's own label — with Pentium 4 / AMD Athlon 64: "32 bit
  registers and address space", and removal of certain instructions of the 16/32-bit cores.

**Registers, 16/32-bit (slide 16).** Instruction pointer `(e)ip`; stack pointer `(e)sp`; base
pointer `(e)bp`; general purpose `(e)ax, (e)bx, (e)cx, (e)dx, (e)si, (e)di`, with a further
split of `ax` into `al` and `ah`, same for b, c, d; segment registers `cs, ds, ss, es, (fs, gs)`;
floating point as an 8-register stack `st(0)`–`st(7)`; `eflags` with 16 bits for CF, PF, AF,
ZF, SF, 0F, TF, IF, DF; and SIMD registers `mmx0`–`mmx7`.

**Registers, 64-bit (slide 17).** `rip`, `rsp`, `rbp`; `rax, rbx, rcx, rdx, rsi, rdi, r8, …,
r15`; segment registers `cs, ds, ss, es, fs, gs`; the same 8-register FP stack `st(0)`–`st(7)`;
the same 16 `eflags` bits; SIMD registers `xmm0`–`xmm15`.

**Subregisters (slide 19).** `rax`/`eax`/`ax`/`al`/`ah`; `rsi`/`esi`/`si`/`sil`; `r8`/`r8d`/
`r8w`/`r8b`. Backwards compatibility rules: writing `eax` zeroes the significant 32 bits of
`rax`; writing `ax`, `al` or `ah` does **not** zero the significant parts (or `al`) of the
"superregister" (`eax` or `ax`).

**The ABI (slide 18), titled "ia64 ABI" on the slide.** It differs from the previous Intel
processors (16/32-bit). Volatile (potentially changed by callee on return): `RAX, RCX, RDX, R8,
R9, R10, R11`, and `XMM0–XMM5`. Nonvolatile (must be saved and restored by a function using
them): `RBX, RBP, RDI, RSI, RSP, R12, R13, R14, R15`, and `XMM6–XMM15`. Integer arguments are
passed in `RCX, RDX, R8, R9`; space must be reserved on the stack for the callee to spill them;
further parameters are passed on the stack in right-to-left order. Floating point arguments are
passed in `XMM0L, XMM1L, XMM2L, XMM3L`. The return value is stored in `RAX` or `XMM0`.

**Instruction anatomy (slide 21).** Instructions consist of an opcode and zero or more
operands. The opcode defines the operation (move data, call a function, …). Operands are
parameters in three classes: register (read or write), immediate (constant), and memory
address — constant (direct) or computed (indirect).

**RISC vs CISC (slide 20).** RISC (e.g. MIPS): many registers, typically 32; few simple
addressing modes; load/store architecture; three-address code `Rz ← Rx ⊕ Ry`; constant-length
instruction encoding, typically 4 bytes. CISC: fewer registers, 8–16; complex address modes;
memory operands; two-address code `Rx ← Rx ⊕ Ry`; variable-length instruction encoding (x86: 1
to 15 bytes).

## Key Properties

- **CISC with 8 registers (16 in 64-bit mode).**
- **Powerful addressing modes**: base register + (1, 2, 4) × index register + constant. For many
  instructions one operand can be a memory cell instead of a register.
- **Inhomogeneous register usage**: some registers only work with some instructions.
- **Hundreds of instructions in the vector extensions.**
- **Base/index/scale/displacement format** for quickly accessing array elements.
- **Partial-register writes are asymmetric**: 32-bit writes zero the upper half, 8- and 16-bit
  writes do not.
- **The calling convention splits registers by volatility**, which is what makes a stack frame
  reconstructible: knowing which registers the callee owns and which the caller owns tells you
  what the prologue saved.
- **Two-address code is the default arithmetic form**, which is why the three-address
  formulation `Rz ← Rx ⊕ Ry` appears on the slide as the RISC counterpoint.

## Worked Example

**Addressing mode (slide 22, source material).**

```asm
int *A;          ; ebx = A, ecx = i
... mov eax, 100
A[i+2] += 100    ; add [ebx + ecx*4 + 8], eax
```

`ebx` is the base, `ecx` the index, `4` the scale (size of an `int`), `8` the displacement (two
elements). The source-level array access survives compilation only in this encoded form.

**Instruction classes (slides 21, 23, 24, source material).**

```asm
mov dword ptr [0xdeafbeef], ebx   ; store ebx into 4 bytes at the given virtual address
mov ah, byte ptr [0x100]         ; load 1 byte at that address into ah
xor eax, eax                     ; equivalent to but shorter than mov eax, 0
lea eax, [edx*4 + ebp]           ; set eax to the address of the memory operand
cmp op1, op2                     ; set flags for op1 - op2
test eax, eax                    ; set flags for op1 & op2
je/jz addr                       ; jump if equal (i.e. zero)
jne/jnz, jl, jg, jle, jge        ; not equal, less, greater (or equal)
```

**Arithmetic conventions (slide 23).** `mul op` multiplies the operand by `eax` and stores the
result into `edx:eax`; `div op` divides `edx:eax` by the operand and stores the quotient into
`eax` and the remainder into `edx`; `imul` and `idiv` are the signed counterparts.

**Call stack (slide 25, source material).** A calls B; the prologue and epilogue:

```asm
mov [RSP + 8], RCX
push R15
push R14
push R13
sub RSP, 0x40        ; fixed-allocation-size
lea RBP, 64[RSP]
lea RSP, -64[RBP]    ; epilogue proper starts here
add RSP, 0x40        ; fixed-allocation-size
pop R13
pop R14
pop R15
ret
```

The `sub RSP, 0x40` / `add RSP, 0x40` pair is the frame's fixed allocation, and the
`lea RBP, 64[RSP]` / `lea RSP, -64[RBP]` pair establishes and tears down a frame pointer at a
known offset — the classic pattern a stack-frame recovery tool looks for.

## Common Pitfalls

- **Reading the "64 bit architecture (ia64)" label as correct.** The slide says ia64, but the
  rest of the slide describes 64-bit registers `rax`–`r15` and `xmm0`–`xmm15`, which is the
  x86-64 (AMD64) design; `ia64` is Itanium, a different architecture with a different register
  file and calling convention. Recorded as the slide states it; see Open Questions.
- **Reading the 64-bit generation's "32 bit registers and address space" as coherent.** The
  slide's own wording is internally inconsistent with the 64-bit register list on slide 17.
- **Ignoring partial-register semantics.** Writing `ax` does not clear the upper bits of `rax`;
  writing `eax` does clear the upper 32 bits of `rax`. Assuming the opposite corrupts the
  recovered state.
- **Assuming a fixed instruction length.** x86 instructions run from 1 to 15 bytes; decoding
  from a wrong boundary yields a plausible but wrong disassembly.
- **Forgetting that many instructions can take a memory operand.** The operand-class model
  (register / immediate / memory) with a memory cell replacing a register changes the register
  pressure of a function.
- **Ignoring register homogeneity limits.** `mmx0`–`mmx7` are eight registers, `xmm0`–`xmm15` are
  sixteen, and the FP unit is an 8-register *stack* — order matters there in a way it does not
  in the general-purpose file.
- **Misreading the volatility split.** Nonvolatile registers are the callee's obligation to save
  and restore; volatile ones may be clobbered. Getting this backwards misidentifies which
  pushed values in a prologue belong to the frame.

## Connections

- [[binary-reverse-engineering]] — the analysis activity this ISA serves.
- [[reverse-engineering]] — the general activity; x86 decoding is its code-level instantiation.
- [[basic-block]] — the unit that instruction decoding produces, once boundaries are known.
- [[control-flow-graph]] — reconstructed from the jump and call instructions above.
- [[debugging]] — dynamic inspection of the same registers and stack frames.
- [[process-memory-layout]] — what `RSP`, `RBP` and the addressing modes point into.
- [[static-vs-dynamic-analysis]] — the two families of technique the ISA supports.
- [[dynamic-analysis]] — running the code to confirm what the disassembly suggests.
- [[reverse-and-reengineering-lecture-2]] — the lecture that supplies slides 15–25.

## Open Questions

- **Is the "ia64" label a typo for x86-64, and what does the 64-bit slide's "32 bit registers and
  address space" mean?** The registers listed (`rax`–`r15`, `xmm0`–`xmm15`) and the
  argument-passing rules match the x86-64 convention, while the label says ia64; and the 64-bit
  bullet's "32 bit registers and address space" contradicts slide 17's 64-bit register list.
  Whether either is a slide error is not stated, and this page records the slides as they are
  without silently correcting them.
- **The floating-point model is only described as a stack.** The slides give `st(0)`–`st(7)` but
  never explain the top-of-stack discipline, how `xmm` registers coexist with `st` registers, or
  how floating-point arguments and return values interact with the `XMM0L`–`XMM3L` and `XMM0`
  rules.
- **The prologue's `mov [RSP + 8], RCX` line and the segment registers are unexplained.** The
  instruction stores the first integer argument into the caller's frame area, but the slide gives
  no rule about which arguments are stored versus spilled; and `cs, ds, ss, es, (fs, gs)` are
  listed with `fs`/`gs` in parentheses for the 16/32-bit mode, without a description of their
  role beyond the real-mode segmentation model.
- **The vector extensions are named only in bulk.** "Hundreds of instructions in vector
  extensions" is given without a representative instruction, so no SIMD idiom can be recovered
  from this material alone.
