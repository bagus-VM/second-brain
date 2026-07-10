---
title: "SRAM Cell"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[mosfet]]", "[[cmos-inverter]]"]
---

## One-line Summary
*Six transistors form a bistable latch that holds one bit as long as power is supplied — fast but large.*

## Core Intuition
An SRAM cell is two cross-coupled CMOS inverters. Inverter A's output feeds inverter B's input, and vice versa. This creates a stable feedback loop: if A outputs high, B outputs low, which reinforces A's high output. The cell has two stable states (0 and 1) and stays in whichever state it was set to. Two access transistors connect the cell to the bit lines for reading and writing. Because the cross-coupled inverters actively drive the bit lines, SRAM is fast — no charge sensing needed.

## Formal Definition / Statement

**Structure:** 6 transistors per cell
- M1, M2: first CMOS inverter (M1 = pMOS pull-up, M2 = nMOS pull-down)
- M3, M4: second CMOS inverter (cross-coupled with first)
- M5, M6: access transistors (nMOS), controlled by the word line

**Operation:**
- **Hold:** Word line is low → M5, M6 are off → cell is isolated → cross-coupled inverters hold state
- **Read:** Word line goes high → M5, M6 turn on → cell drives bit lines (BL and BL̄) → sense amplifier detects the small voltage difference
- **Write:** Word line goes high → driver transistors force BL and BL̄ to desired values → overpower the cell's inverters → cell flips to new state

## Key Properties

- **Volatile:** loses data when power is removed
- **Fast:** access time ~1-10 ns (no refresh needed, inverters actively drive lines)
- **No refresh:** data is held by active feedback, not stored charge
- **Large cell:** 6 transistors → ~120-200 F² per bit (F = feature size)
- **Low density:** compared to DRAM, fewer bits per chip area
- **Used for:** CPU caches (L1, L2, L3), register files, small fast memories
- **Power:** static power consumption (leakage current in modern nodes)

## Worked Example

A 6T SRAM cell storing "1":
- Node Q = VDD (high), node Q̄ = GND (low)
- Inverter 1 (M1, M2): input = Q̄ = low → output Q = high ✓
- Inverter 2 (M3, M4): input = Q = high → output Q̄ = low ✓
- Cross-coupling: each inverter's output drives the other's input → stable

Read "1":
1. Precharge BL and BL̄ to VDD/2
2. Raise word line → M5, M6 turn on
3. Cell at Q=high pulls BL slightly above VDD/2
4. Cell at Q=low pulls BL̄ slightly below VDD/2
5. Sense amplifier detects the small difference and latches

## Common Pitfalls

- **Confusing SRAM with DRAM.** SRAM uses 6 transistors and active feedback. DRAM uses 1 transistor + 1 capacitor and stored charge. SRAM is faster but larger.
- **Thinking SRAM doesn't need power.** It does — the cross-coupled inverters need power to maintain state. Remove power → data lost.
- **Underestimating cell size.** 6 transistors per bit is expensive. That's why CPU caches are small (KB to MB) while DRAM is large (GB).
- **Confusing bit lines with data lines.** Bit lines (BL, BL̄) are the differential pair inside the memory array. Data lines carry data to/from the I/O.

## Connections

- [[dram-cell]] — the alternative memory cell (1T + 1C, smaller but slower)
- [[sense-amplifier]] — needed to detect the small voltage difference on bit lines
- [[cmos-inverter]] — the building block of the SRAM cell
- [[mosfet]] — all 6 transistors are MOSFETs
- [[microelectronics-lecture-9]] — lecture that introduces SRAM

## Open Questions

- How does the cell ratio (β ratio) affect read stability and write ability?
- What is the hold voltage margin, and how does it scale with supply voltage?
- How do soft errors (alpha particles, cosmic rays) affect SRAM reliability?
