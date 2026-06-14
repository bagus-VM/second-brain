---
title: "CMOS NAND Gate"
tags: [concept, microelectronics, digital-logic, semester-1, course-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[cmos-inverter]]", "[[nmos-transistor]]", "[[pmos-transistor]]"]
---

## One-line Summary
A CMOS NAND gate uses two nMOS in series (pull-down) and two pMOS in parallel (pull-up) to compute ¬(A ∧ B) in 4 transistors, with the same near-zero static power as a CMOS inverter.

## Core Intuition
NAND is the most important gate in CMOS design. Every flip-flop, every SRAM cell, every adder is built from NANDs (and inverters). The reason is structural: NAND is the *smallest* gate that gives you universal Boolean completeness with the least transistors.

Build it by extending the CMOS inverter:

- **Pull-down network (nMOS)**: put two nMOS in **series** between output and GND. Series = AND. Both A and B must be HIGH to conduct.
- **Pull-up network (pMOS)**: put two pMOS in **parallel** between V_DD and output. Parallel = OR. Either A or B being LOW turns on one of them.

The two networks are **logical duals** of each other — exactly one conducts at any time. When the PDN conducts, the PUN is off, and the output is pulled LOW. When the PDN is off, the PUN is open, and the output is pulled HIGH.

## Formal Definition / Statement

A 2-input CMOS NAND gate has:
- 2 pMOS transistors, sources tied to V_DD, drains tied to output node, gates driven by A and B
- 2 nMOS transistors, source/drain in series between output and GND, gates driven by A and B
- Output Y = ¬(A ∧ B)

**Truth table:**

| A | B | pMOS_A | pMOS_B | nMOS_A | nMOS_B | Y |
|---|---|--------|--------|--------|--------|---|
| 0 | 0 | ON | ON | OFF | OFF | V_DD |
| 0 | 1 | ON | OFF | OFF | ON | V_DD |
| 1 | 0 | OFF | ON | ON | OFF | V_DD |
| 1 | 1 | OFF | OFF | ON | ON | GND |

**Static power**: zero in steady state (exactly one of PDN/PUN is open for any input).

**Transistor count**: 4 (plus wells, contacts). Compare to AND = NAND + NOT = 6 transistors. NAND is the cheaper primitive.

## Key Properties / Complexity
- 4 transistors, single-stage delay
- Full output swing (rail-to-rail)
- Universal gate: {NAND} alone is functionally complete (you can build NOT, AND, OR, XOR from NAND)
- Static power ≈ 0 (same CMOS advantage as the inverter)
- Slightly slower than NOR in practice because the series nMOS stack has higher on-resistance

## Worked Example

Build a NOT gate from a 2-input NAND: tie both inputs together (A = B = input). When input = 0, both pMOS ON, both nMOS OFF → output = V_DD. When input = 1, both pMOS OFF, both nMOS ON → output = GND. That is ¬(A ∧ A) = ¬A = NOT. One NAND gives you NOT, at 4 transistors.

Build a 3-input NAND: stack 3 nMOS in series for the PDN, put 3 pMOS in parallel for the PUN. Transistor count goes 2N. This is why deep-NAND trees exist in standard cell libraries.

## Common Pitfalls
- "NAND is the complement of AND" → true logically, but in CMOS the *PDN* implements AND (the function that pulls down), and the *output* is the AND inverted. Don't confuse the function implemented by the network with the function the gate computes.
- Series nMOS have higher on-resistance than a single nMOS → the 0-to-1 transition (PDN on) is slower than the 1-to-0 transition. The pull-up path (parallel pMOS) is fast on its own, but the asymmetric drive strength can cause issues in heavily loaded circuits.

## Connections
- [[cmos-inverter]] — NAND generalises the inverter
- [[cmos-nor-gate]] — the dual, with parallel nMOS / series pMOS
- [[cmos-xor-gate]] — the gate that breaks the dual-CMOS rule
- [[cmos-logic-gates]] — the family overview
- [[nmos-transistor]] — the pull-down device
- [[pmos-transistor]] — the pull-up device
- [[transistor]] — general 3-terminal device context
- [[digital-logic]] — Boolean function implementation
- [[microelectronics-lecture-6]] — source lecture

## Open Questions
- Why is the standard cell library 4-transistor NAND rather than 3 (e.g., pseudo-nMOS with a single pull-up pMOS and a weak feedback)? Trade-off is static power vs. area.
- How do NAND-based designs compare to NOR-based designs in terms of speed at modern nodes?
