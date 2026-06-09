---
title: "Digital Logic"
tags: [concept, microelectronics, digital-design, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The representation and manipulation of information using discrete voltage levels (HIGH/LOW) through logic gates.*

## Core Intuition
Digital logic is the bridge between analog electronics and computing. Instead of worrying about exact voltages, digital logic defines two states — HIGH (1) and LOW (0) — and builds everything from there. Logic gates combine these states to perform arithmetic, make decisions, and store data. Every computation your phone performs is ultimately billions of simple logic operations happening billions of times per second.

## Formal Definition / Statement
Digital logic uses discrete voltage levels to represent binary information.

**Logic families:**
- CMOS: complementary MOSFET (dominant modern technology)
- TTL: transistor-transistor logic (legacy, 74xx series)
- ECL: emitter-coupled logic (high speed, high power)

**Basic gates (CMOS):**
- NOT (inverter): 1 PMOS + 1 NMOS
- NAND: 2 PMOS (parallel) + 2 NMOS (series) — 4 transistors
- NOR: 2 PMOS (series) + 2 NMOS (parallel) — 4 transistors
- AND = NAND + NOT, OR = NOR + NOT
- XOR: 4 NAND gates or 12 transistors

**Boolean algebra:**
- AND (·): A·B = 1 iff A=1 and B=1
- OR (+): A+B = 1 iff A=1 or B=1
- NOT ('): A' = 1 iff A=0
- De Morgan's: (A·B)' = A'+B', (A+B)' = A'·B'

**Combinational vs sequential:**
- Combinational: output depends only on current inputs (gates, multiplexers, adders)
- Sequential: output depends on current inputs AND state (flip-flops, registers, counters)

**Logic minimization:**
- Karnaugh maps (K-maps): visual minimization for ≤6 variables
- Quine-McCluskey: tabular method for exact minimization
- Espresso: heuristic minimizer for large functions

## Key Properties / Complexity
- NAND and NOR are universal: any function can be built from NAND-only or NOR-only
- CMOS NAND/NOR have equal rise and fall times (with proper sizing)
- Fan-out: one gate output can drive multiple gate inputs (limited by capacitive loading)
- Noise margins: difference between guaranteed output levels and required input levels
- Propagation delay: time for input change to appear at output (typically 10ps–10ns)
- Power-delay product: figure of merit for logic families

## Worked Example
Building a 1-bit full adder from gates:
- Inputs: A, B, C_in (carry in)
- Sum = A ⊕ B ⊕ C_in (two XOR gates)
- C_out = A·B + C_in·(A ⊕ B) (AND, OR, XOR gates)
- CMOS implementation: ~28 transistors
- Propagation delay: 3 gate delays × 50ps = 150ps (at 65nm)
- 32-bit ripple carry adder: 32 × 150ps = 4.8ns
- Carry-lookahead adder: ~1ns (more gates, less delay)

## Common Pitfalls
- **Glitches**: Combinational circuits can produce brief incorrect outputs during input transitions
- **Race conditions**: Sequential circuits can malfunction if setup/hold times are violated
- **Power consumption**: Switching activity × frequency × capacitance = dynamic power
- **Metastability**: Flip-flops can enter an indeterminate state when setup/hold times are barely violated
- **Fan-out limitations**: Driving too many loads increases delay and may cause logic errors

## Connections
- [[cmos-inverter]] — The fundamental CMOS gate
- [[mosfet]] — MOSFETs are the transistors in CMOS logic
- [[nmos-transistor]] — NMOS half of CMOS gates
- [[common-subexpression-elimination]] — Compiler optimization on logic expressions
- [[finite-automata]] — Sequential logic circuits are finite state machines
- [[register-allocation]] — Registers are built from sequential logic (flip-flops)

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
