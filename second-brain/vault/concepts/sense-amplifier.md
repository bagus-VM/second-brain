---
title: "Sense Amplifier"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[dram-cell]]", "[[sram-cell]]"]
---

## One-line Summary
*A sense amplifier detects the tiny voltage difference on a memory's bit lines and amplifies it to full logic levels.*

## Core Intuition
When a memory cell is read, it creates only a small voltage change on the bit line — tens of millivolts for DRAM, slightly more for SRAM. This is far too small to drive logic gates. The sense amplifier is a differential amplifier that compares the bit line to a reference voltage, amplifies the difference to full logic levels (0 V or VDD), and latches the result. It also restores the cell charge (write-back), making destructive reads non-destructive in practice.

## Formal Definition / Statement

**DRAM sense amplifier:**
1. Bit lines precharged to VDD/2
2. Word line activates cell → small voltage change ΔV on bit line
3. Sense amplifier compares BL to BL̄ (or to a reference)
4. Cross-coupled inverter pair latches: pulls one line to VDD, the other to GND
5. Full logic levels restored on bit lines → cell charge restored (write-back)

**SRAM sense amplifier:**
- SRAM cell actively drives bit lines (stronger signal than DRAM)
- Sense amplifier still used for speed: amplifies the small difference faster than waiting for full swing

**Equalization and precharging:**
- Before each read, bit lines are equalized to the same voltage (VDD/2)
- This ensures the sense amplifier starts from a known state
- Without equalization, residual charge from previous reads would corrupt the result

## Key Properties

- Converts tiny analog signals (mV) to digital logic levels (V)
- Cross-coupled latch topology: fast, low power, self-timing
- Differential sensing: immune to common-mode noise (both lines shift equally)
- Write-back: the sense amplifier restores cell charge after destructive read
- Critical path: sense amplifier speed directly affects memory access time

## Worked Example

DRAM read with:
- VDD = 1.2 V, precharge = 0.6 V
- Cell capacitor = 30 fF, bit line capacitance = 300 fF
- Cell stores "1" (charged to 1.2 V)

After word line activation:
- BL voltage rises by ΔV ≈ 55 mV (from charge sharing)
- BL̄ stays at 0.6 V (reference cell or complementary bit line)

Sense amplifier:
1. Detects: BL (0.655 V) > BL̄ (0.6 V)
2. Latches: pulls BL to 1.2 V, BL̄ to 0 V
3. Write-back: BL at 1.2 V recharges cell capacitor to 1.2 V

Total sense time: ~1-5 ns (depends on technology node)

## Common Pitfalls

- **Thinking the sense amplifier is just an amplifier.** It's a latch — it amplifies AND holds the result. The cross-coupled structure makes it self-timing.
- **Forgetting equalization.** Without precharging, the sense amplifier starts from an unknown state and may latch incorrectly.
- **Confusing SRAM and DRAM sensing.** SRAM cells drive bit lines more strongly, so the signal is larger. DRAM needs more sensitive sensing because the charge is tiny.
- **Ignoring offset voltage.** Real sense amplifiers have input offset (mismatch between the two sides). This limits the minimum detectable signal.

## Connections

- [[dram-cell]] — DRAM depends critically on sense amplifiers (tiny charge signal)
- [[sram-cell]] — SRAM uses sense amplifiers for speed (though signal is stronger)
- [[microelectronics-lecture-9]] — lecture that introduces sense amplifiers
- [[mosfet]] — sense amplifiers are built from MOSFETs
- [[analog-amplifier]] — sense amplifier is a specialized differential amplifier

## Open Questions

- How does sense amplifier offset affect yield in large memory arrays?
- What is the relationship between sense amplifier speed and memory frequency?
- How do modern DDR memories calibrate sense amplifiers to compensate for process variation?
