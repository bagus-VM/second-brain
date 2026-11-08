---
title: "CMOS NOR Gate"
tags: [concept, microelectronics, digital-logic, semester-1, course-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[cmos-inverter]]", "[[nmos-transistor]]", "[[pmos-transistor]]"]
---

## One-line Summary
A CMOS NOR gate uses two nMOS in parallel (pull-down) and two pMOS in series (pull-up) to compute ¬(A ∨ B) in 4 transistors — the structural dual of the NAND gate.

## Core Intuition
NOR is to CMOS what NAND is, with the networks swapped:

- **Pull-down network (nMOS)**: two nMOS in **parallel** between output and GND. Parallel = OR. Either A or B being HIGH pulls the output LOW.
- **Pull-up network (pMOS)**: two pMOS in **series** between V_DD and output. Series = AND. Both A and B must be LOW to pull the output HIGH.

Again the two networks are logical duals. Exactly one is open for any input. Static power is zero in steady state.

NOR and NAND are duals in the Boolean sense (¬(A ∨ B) = ¬A ∧ ¬B) and in the CMOS sense (parallel/series swapped). For a 2-input gate, the transistor count is identical (4). The difference shows up in performance:

- Series nMOS (NAND) is slower to pull down → NAND is slower on the falling edge
- Series pMOS (NOR) is slower to pull up → NOR is slower on the rising edge

Modern CMOS libraries typically offer both, with NAND slightly preferred for general logic because the falling-edge penalty is smaller than the rising-edge penalty (electrons are more mobile than holes).

## Formal Definition / Statement

A 2-input CMOS NOR gate has:
- 2 pMOS transistors in **series** between V_DD and output, gates driven by A and B
- 2 nMOS transistors in **parallel** between output and GND, gates driven by A and B
- Output Y = ¬(A ∨ B)

**Truth table:**

| A | B | pMOS_A | pMOS_B | nMOS_A | nMOS_B | Y |
|---|---|--------|--------|--------|--------|---|
| 0 | 0 | ON | ON | OFF | OFF | V_DD |
| 0 | 1 | OFF | ON | OFF | ON | GND |
| 1 | 0 | ON | OFF | ON | OFF | GND |
| 1 | 1 | OFF | OFF | ON | ON | GND |

## Key Properties / Complexity
- 4 transistors, single-stage delay
- Static power ≈ 0
- The series pMOS stack in the pull-up network has higher on-resistance than parallel pMOS → the 1-to-0 transition (output rising) is the slow path
- Universal gate: {NOR} alone is functionally complete, like NAND

## Worked Example

NOT from a 2-input NOR: tie A = B = input. When input = 0, both pMOS ON, both nMOS OFF → output = V_DD. When input = 1, both pMOS OFF, both nMOS ON → output = GND. ¬(A ∨ A) = ¬A. One NOR gives you NOT, at 4 transistors.

## Common Pitfalls
- Confusing NAND and NOR transistor arrangements: NAND has series nMOS / parallel pMOS, NOR has parallel nMOS / series pMOS. They are *opposites*.
- The series pMOS in NOR makes it slower on the rising edge than NAND on the falling edge (because hole mobility is lower than electron mobility). This is why NAND is the preferred primitive in standard cell libraries.

## Connections
- [[cmos-inverter]] — NOR generalises the inverter
- [[cmos-nand-gate]] — the dual, with series nMOS / parallel pMOS
- [[cmos-xor-gate]] — XOR doesn't fit the dual-CMOS pattern
- [[cmos-logic-gates]] — the family overview
- [[nmos-transistor]] — the pull-down device
- [[pmos-transistor]] — the pull-up device
- [[digital-logic]] — Boolean function implementation
- [[microelectronics-lecture-6]] — source lecture

## Open Questions
- Are there specific applications where NOR is preferred over NAND at the cell-library level? (SRAM cell decoding, certain sense-amp designs use NOR.)
