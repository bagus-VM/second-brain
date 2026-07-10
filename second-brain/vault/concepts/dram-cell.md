---
title: "DRAM Cell"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[mosfet]]", "[[capacitor]]"]
---

## One-line Summary
*One transistor and one capacitor store a bit as charge — tiny, dense, but the charge leaks and needs refreshing.*

## Core Intuition
A DRAM cell is the simplest possible memory: a capacitor stores charge (1 = charged, 0 = discharged), and a transistor acts as a switch to access it. The capacitor is tiny (femtofarads), which is why DRAM is dense — but that tiny charge leaks away in milliseconds. The system must periodically read and rewrite every cell (refresh) to prevent data loss. Reading is destructive: accessing the cell drains some charge from the capacitor, so the data must be written back after every read.

## Formal Definition / Statement

**Structure:** 1 transistor + 1 capacitor per cell
- Access transistor (nMOS): gate connected to word line, connects capacitor to bit line
- Storage capacitor: holds charge representing the bit

**Operation:**
- **Write:** Word line high → transistor on → bit line voltage charges/discharges capacitor
- **Read:** Word line high → transistor on → capacitor shares charge with bit line → small voltage change on bit line → sense amplifier detects and latches
- **Refresh:** Every ~64 ms, read each row and write back the data (the sense amplifier does this automatically)

**Organization:**
- Cells arranged in a 2D array: rows × columns
- Word line = row select (activates all cells in a row)
- Bit line = column data (one per column, shared by all cells in that column)
- Row address + column address selects one cell

## Key Properties

- **Volatile:** loses data when power is removed
- **Dense:** 1T + 1C per bit → ~6-10 F² per bit (much smaller than SRAM's 120-200 F²)
- **Destructive read:** reading drains charge from capacitor → must rewrite after read
- **Refresh required:** every ~64 ms, all rows must be read and rewritten
- **Slower than SRAM:** charge sensing takes time; refresh cycles steal bandwidth
- **Used for:** main memory (RAM modules), GPU memory, embedded DRAM

## Worked Example

DRAM cell storing "1" (capacitor charged to VDD = 1.2 V):
- Capacitor: C = 30 fF
- Bit line capacitance: CBL = 300 fF (10× larger than cell capacitor)

Read operation:
1. Precharge bit line to VDD/2 = 0.6 V
2. Word line goes high → transistor connects capacitor to bit line
3. Charge sharing: V_bitline = (C × VDD + CBL × VDD/2) / (C + CBL)
   = (30f × 1.2 + 300f × 0.6) / (30f + 300f)
   = (36f + 180f) / 330f = 0.655 V
4. Voltage change: ΔV = 0.655 - 0.6 = 0.055 V (55 mV)
5. Sense amplifier detects this small difference and latches to full logic levels
6. Sense amplifier also restores the cell charge (write-back)

## Common Pitfalls

- **Confusing destructive read with volatility.** Destructive read means reading destroys the data (must rewrite). Volatility means data is lost without power. Both apply to DRAM, but they're different concepts.
- **Thinking refresh is optional.** It's not. Without refresh, data is lost in ~64 ms. The memory controller handles this automatically, but it consumes bandwidth.
- **Underestimating the bit line capacitance.** The bit line is much longer than the cell capacitor. The voltage change is tiny (tens of mV). That's why sense amplifiers are critical.
- **Confusing row and column access.** A row activate opens an entire row. Column access selects specific bits from the open row. Multiple column accesses can happen without re-opening the row.

## Connections

- [[sram-cell]] — the alternative memory cell (6T, faster, larger)
- [[sense-amplifier]] — essential for detecting the tiny voltage change on read
- [[capacitor]] — the storage element (charge = data)
- [[mosfet]] — the access transistor
- [[microelectronics-lecture-9]] — lecture that introduces DRAM

## Open Questions

- How does DRAM scaling work as feature sizes shrink? Does the capacitor get too small to hold enough charge?
- What is the difference between DDR4, DDR5, and LPDDR in terms of cell architecture?
- How does refresh power scale with memory size? At what point does it dominate total power?
