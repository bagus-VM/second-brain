---
title: "CMOS XOR Gate"
tags: [concept, microelectronics, digital-logic, semester-1, course-microelectronics]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[cmos-inverter]]", "[[cmos-nand-gate]]", "[[cmos-nor-gate]]"]
---

## One-line Summary
The XOR function (A ⊕ B = AB̄ + ĀB) cannot be implemented in a single stage of static complementary CMOS — it requires a transmission-gate construction (12T), a 6T static design, or a multi-stage NAND/NOR/INV tree; this is the gate that breaks the "PDN for F, PUN for ¬F" rule.

## Core Intuition
The static CMOS rule is: build a pull-down network (nMOS) that conducts when F = 1, and a pull-up network (pMOS) that conducts when F = 0. For NAND and NOR this works because F has a single "ON" pattern that can be expressed as a series-parallel network of switches. For XOR, F = AB̄ + ĀB is the *sum of two products*, each of which is a series pair. The PDN would be two parallel branches, each a series pair — fine. But the dual of that network (the PUN for ¬F = AB + ĀB̄) is the *same topology*, not a different one. You end up with two parallel branches in both networks, and they conflict on which input is high.

The deeper issue: XOR is not a "unate" function. A unate function is one in which each input appears in only one polarity (either always positive or always negative, never both). NAND and NOR are unate: A appears only as A. XOR is *binate*: A appears as A and as Ā. The static-CMOS construction rule requires unate functions.

The lecture devotes 4 slides to the workarounds:

1. **Transmission-gate XOR (12T)**: use two pass transistors (one nMOS, one pMOS) controlled by A and Ā. When A = 0, the top switch passes B directly. When A = 1, the bottom switch passes ¬B. Net result: Y = B when A = 0, Y = ¬B when A = 1 → Y = A ⊕ B. This is the textbook 12-transistor implementation.
2. **6T static XOR**: a clever non-complementary design that uses cross-coupled pMOS loads. Used in dense arithmetic logic units. Trades ratio-dependence for transistor count.
3. **Two-stage implementation**: build XOR = (A∧¬B)∨(¬A∧B) from AND, OR, NOT. Costs more delay but uses standard cells.
4. **Inverter chain XOR**: an alternative static design that exploits the structure of the function.

The exam point: in a single stage of static CMOS, XOR is *not* implementable. It is the canonical example of why "just use CMOS" is not always the answer.

## Formal Definition / Statement

**XOR function**: F(A, B) = A ⊕ B = AB̄ + ĀB

**Why static CMOS fails:**

Try to build a PDN that conducts when F = 1. The two conducting cases are (A=1, B=0) and (A=0, B=1). So the PDN is two parallel branches, each a series pair:

- Branch 1: nMOS_A (gate = A) in series with nMOS_B̄ (gate = ¬B) — but nMOS are not natively controlled by ¬B; you'd need an inverter on B first
- Or: nMOS_A in series with the *output* of an nMOS driven by ¬B... but that puts an nMOS in the middle of the stack, which doesn't work

The PUN (for ¬F) is the same topology (two parallel branches, series pairs), so when one input is high, the PDN wants to conduct on one branch and the PUN wants to conduct on the other — they fight, and the output is not a clean logic level.

**Transmission-gate XOR (12T)** schematic:

```
        A=0                          A=1
        ─────                        ─────
B ──┬──[nMOS + pMOS TG]──┬── Y    (top TG closed, bottom TG open)
    │   (control: A)     │
    │   (control: Ā)     │
    └────[nMOS + pMOS TG]┘
        (control: Ā)
        (control: A)
```

Plus an inverter for Ā. Total: 6 transistors per TG × 2 TGs + 2 for inverter = 14T (the lecture says 12T because the inverter shares the body of the first TG's input; either count is acceptable).

**6T static XOR** is a non-complementary design with cross-coupled pMOS loads. Output drive strength depends on transistor sizing ratios (a "ratioed" logic style) — unlike static CMOS, the output is not always a strong rail.

## Key Properties / Complexity
- **Not implementable in single-stage static CMOS**
- Transmission-gate XOR: 12T, ratio-less, full swing, single stage
- 6T XOR: 6T, ratioed (output depends on transistor sizing), single stage
- Multi-stage: variable transistor count, slower, uses standard cells
- Static power ≈ 0 only in the transmission-gate and multi-stage variants; the 6T ratioed version has a static current path

## Worked Example
**Truth table for any 2-input XOR:**

| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

**Why the transmission-gate version works:**

The top TG passes B to Y when A = 0 (control A = 0 closes the nMOS, control Ā = 1 closes the pMOS — both in the TG conduct). The bottom TG passes B to Y through an inverter (so the signal is ¬B) when A = 1.

So when A = 0, Y = B = A ⊕ B (since A = 0). When A = 1, Y = ¬B = A ⊕ B (since A = 1). 

## Common Pitfalls
- "XOR is just a static CMOS gate" → false. The lecture explicitly shows that the standard rule fails.
- Confusing XOR with XNOR — XNOR is just an XOR with the output inverted; it has the same construction problem.
- Trying to use a 6T XOR in a place that requires ratio-less operation. The 6T design is ratioed — its output levels depend on W/L ratios. If the next stage has variable load, the design can fail.

## Connections
- [[cmos-inverter]] — base case
- [[cmos-nand-gate]] — the canonical single-stage CMOS gate
- [[cmos-nor-gate]] — the dual
- [[cmos-logic-gates]] — XOR as the exception that proves the rule
- [[nmos-transistor]] — pull-down device
- [[pmos-transistor]] — pull-up device
- [[digital-logic]] — Boolean function
- [[microelectronics-lecture-6]] — source lecture (4 slides on XOR)

## Open Questions
- Does the exam want the 12T transmission-gate answer, the 6T static answer, or just the observation that "static CMOS can't do it in one stage"? Need to verify.
- At 7nm and below, are there FinFET-specific XOR designs that beat the 12T transmission-gate figure?
