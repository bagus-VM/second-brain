---
title: "Flash Memory"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[mosfet]]"]
---

## One-line Summary
*A floating gate traps electrons to store data permanently — no power needed, but writes wear out the cell.*

## Core Intuition
A flash memory cell is a MOSFET with an extra gate — the floating gate — buried in oxide between the control gate and the channel. Electrons can be injected into the floating gate (programming) or removed (erasing) through quantum tunneling (Fowler-Nordheim) or hot-carrier injection. Trapped electrons shift the transistor's threshold voltage: high Vt = "0" (programmed), low Vt = "1" (erased). The oxide traps the charge permanently — no power needed to retain data. But each program/erase cycle damages the oxide slightly, limiting endurance to ~10K-100K cycles.

## Formal Definition / Statement

**Cell structure:**
- Control gate: external terminal for read/program/erase operations
- Floating gate: electrically isolated conductor sandwiched in oxide
- Tunnel oxide: thin oxide layer (~10 nm) allows electron tunneling
- Source, drain, channel: standard MOSFET structure

**Two architectures:**
- **NOR flash:** cells in parallel (like a NOR gate) → random access, byte-level read → used for code storage (firmware, BIOS)
- **NAND flash:** cells in series (like a NAND gate) → sequential access, page-level read/write → higher density, used for SSDs, USB drives, SD cards

**Operations:**
- **Read:** Apply normal gate voltage → if floating gate has trapped electrons (high Vt), transistor is off → "0". If no trapped electrons (low Vt), transistor is on → "1".
- **Program:** Apply high voltage to control gate → electrons tunnel through thin oxide into floating gate (Fowler-Nordheim tunneling or hot-carrier injection)
- **Erase:** Apply high voltage to source/bulk → electrons tunnel out of floating gate

## Key Properties

- **Non-volatile:** data retained without power (years to decades)
- **Block erasure:** must erase entire blocks (128 KB - 256 KB) before writing
- **Write endurance:** limited to ~10K-100K program/erase cycles per cell
- **Read endurance:** essentially unlimited (reads don't damage the cell)
- **Asymmetric speeds:** reads are fast (μs), writes are slow (ms), erases are very slow (ms)
- **Wear leveling:** controllers distribute writes across cells to maximize lifetime
- **Multi-level cells (MLC):** store 2+ bits per cell by using multiple threshold levels

## Worked Example

NOR flash cell with VDD = 3.3 V:
- Erased state (low Vt = 1 V): transistor turns on at Vgs = 1 V → reads as "1"
- Programmed state (high Vt = 5 V): transistor never turns on at Vgs = 3.3 V → reads as "0"

Read at Vgs = 3.3 V:
- Erased cell: Vgs (3.3) > Vt (1.0) → ON → current flows → "1"
- Programmed cell: Vgs (3.3) < Vt (5.0) → OFF → no current → "0"

Multi-level cell (2 bits, 4 levels):
- Vt < 0.5 V → "11"
- 0.5 V < Vt < 1.5 V → "10"
- 1.5 V < Vt < 2.5 V → "01"
- Vt > 2.5 V → "00"

## Common Pitfalls

- **Confusing NOR and NAND flash.** NOR has random access (like RAM), NAND has sequential access (like a disk). NOR is for code, NAND is for data.
- **Thinking flash is infinitely writable.** Each cell has a limited number of program/erase cycles. Wear leveling is essential.
- **Forgetting block erasure.** You can't overwrite a single byte. You must erase the entire block first, then write. This is why SSDs have write amplification.
- **Confusing floating gate with charge trap.** Modern 3D NAND uses charge trap (silicon nitride) instead of floating gate (polysilicon). The principle is the same, but the structure differs.
- **Assuming data retention is permanent.** Flash cells lose charge over time (years to decades, depending on temperature and wear). Enterprise SSDs have stricter retention requirements.

## Connections

- [[sram-cell]] — SRAM is volatile but infinitely writable; flash is non-volatile but limited writes
- [[dram-cell]] — DRAM is volatile and needs refresh; flash is non-volatile and needs no refresh
- [[mosfet]] — flash cell is a MOSFET with an added floating gate
- [[microelectronics-lecture-9]] — lecture that introduces flash memory

## Open Questions

- How does 3D NAND scaling compare to planar NAND? What are the limits?
- What is the relationship between write endurance and the number of bits per cell (SLC vs MLC vs TLC vs QLC)?
- How do SSD controllers manage wear leveling and garbage collection?
- What is the future of flash memory? Will it be replaced by new NVM technologies (ReRAM, MRAM)?
