---
title: "Lecture 9 - Operational Amplifiers: Integrators, Differentiators, and Memories"
tags: [lecture, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: [[microelectronics-lecture-8]], [[opamp-basics]], [[cmos-inverter]]
---

## One-line Summary
*By swapping resistors for capacitors in OpAmp feedback networks you get integrators and differentiators, and this lecture also covers voltage adders, buffers, and how digital memories store bits using transistors and capacitors.*

## Core Intuition
The inverting amplifier from Lecture 8 has two impedances: Z1 at the input and Z2 in the feedback path. The gain is always -Z2/Z1 regardless of what those impedances are. When you replace a resistor with a capacitor, its impedance becomes frequency-dependent (1/jωC), so the gain becomes frequency-dependent too. A capacitor in feedback makes the circuit integrate (low-pass): it accumulates charge over time, smoothing the signal. A capacitor at the input makes the circuit differentiate (high-pass): it passes fast changes and blocks slow ones. This same impedance-swapping idea extends to non-inverting topologies.

The voltage adder and buffer are natural extensions of the basic amplifier: the adder uses multiple inputs to combine signals, and the buffer uses unity gain to isolate circuits from each other without changing the signal.

The memory section shifts from analog to digital: SRAM and DRAM are the two fundamental ways to store a bit using transistors, with different tradeoffs in speed, density, and complexity. Sense amplifiers solve the problem of reading tiny charge signals from memory cells.

## Formal Definition / Statement

### Integrators

Replace R2 (feedback resistor) with a capacitor C. Keep R1 as a resistor at the input.

- Z1 = R (resistor at input)
- Z2 = 1/jωC (capacitor at feedback)
- Gain = -Z2/Z1 = -1/(jωRC)

In the time domain: **Vout(t) = -(1/RC) ∫ Vin(t) dt**

The output is the integral of the input, scaled by -1/RC. Low-pass behavior: at high frequencies, the capacitor's impedance drops, reducing gain. At DC (ω → 0), the capacitor is an open circuit and gain becomes infinite in theory — in practice, DC offset accumulates and saturates the output.

**Practical fix:** Add a large resistor Rf in parallel with the capacitor to limit DC gain to -Rf/R, preventing saturation while preserving integrator behavior over the frequency range of interest.

### Differentiators

Replace R1 (input resistor) with a capacitor C. Keep R2 as a resistor in the feedback path.

- Z1 = 1/jωC (capacitor at input)
- Z2 = R (resistor at feedback)
- Gain = -Z2/Z1 = -jωRC

In the time domain: **Vout(t) = -RC dVin/dt**

The output is the derivative of the input, scaled by -RC. High-pass behavior: at low frequencies, the capacitor blocks the signal; at high frequencies, gain increases without bound in theory.

**Practical fix:** Add a small resistor Rs in series with the input capacitor to limit high-frequency gain to -R/Rs, reducing noise amplification.

### Non-inverting Integrator and Differentiator

Same impedance substitution applied to the non-inverting topology where gain = 1 + Z2/Z1:

- Non-inverting integrator: gain = 1 + 1/(jωRC)
- Non-inverting differentiator: gain = 1 + jωRC

These retain the frequency-dependent behavior but without phase inversion.

### Voltage Adder / Weighted Summer

Multiple input resistors R1, R2, ..., Rn connected to the inverting terminal. Single feedback resistor Rf.

**Vout = -Rf × (V1/R1 + V2/R2 + ... + Vn/Rn)**

Each input is weighted by the ratio Rf/Ri. Special case when all resistors are equal (R1 = R2 = ... = Rn = R):

**Vout = -(V1 + V2 + ... + Vn)** — a simple summing amplifier.

### Voltage Follower / Buffer

Non-inverting amplifier with R2 = 0 (short circuit in feedback) and R1 removed (open circuit).

- Gain = 1 + 0/∞ = 1 (unity gain)
- Output follows input exactly: Vout = Vin

Purpose: impedance transformation. The OpAmp's very high input impedance draws negligible current from the source. Its very low output impedance can drive low-impedance loads without voltage drop. This isolates stages and prevents loading effects.

### SRAM (Static Random-Access Memory)

- 6-transistor cell: two cross-coupled inverters + two access transistors
- Holds data as long as power is supplied — no refresh needed
- Fast access (nanoseconds)
- Used for CPU caches (L1, L2, L3)
- Larger cell size → lower density than DRAM
- Volatile: loses data when power is removed

### DRAM (Dynamic Random-Access Memory)

- 1-transistor + 1-capacitor cell
- Stores data as charge on a capacitor — charge leaks over time
- Requires periodic refresh (typically every 64 ms)
- Higher density than SRAM (smaller cell)
- Slower than SRAM (needs refresh cycles, charge sensing)
- Used for main memory (RAM modules)
- Volatile
- Organization: array of cells in rows and columns, accessed via word lines and bit lines

### Sense Amplifiers

- Detect and amplify the small voltage difference on bit lines during memory read
- DRAM: capacitor charge is tiny (femtofarads) → bit line voltage change is millivolts
- SRAM: cross-coupled inverters drive bit lines more strongly, but sense amps still used for speed
- Equalization: bit lines are precharged to a reference voltage before read
- Sense amplifier compares bit line voltage to a reference and latches the result
- Critical for speed and reliability of memory read operations

### ROM and Flash Memory

- ROM (Read-Only Memory): programmed at manufacture, non-volatile
- PROM: one-time programmable (fuses)
- EPROM: UV-erasable (quartz window)
- EEPROM: electrically erasable, byte-level access
- Flash Memory: block-erasable EEPROM, the dominant non-volatile storage
  - NOR flash: random access, used for code storage (firmware)
  - NAND flash: sequential access, higher density, used for SSDs and USB drives
  - Floating gate transistor: trapped charge changes threshold voltage

## Key Properties

- Integrator gain: -1/(jωRC), behaves as a low-pass filter, time domain: Vout = -(1/RC) ∫ Vin dt
- Differentiator gain: -jωRC, behaves as a high-pass filter, time domain: Vout = -RC dVin/dt
- Both circuits extend the basic inverting amplifier by replacing a resistor with a capacitor
- Integrator practical issue: DC offset accumulation — fix with large parallel resistor
- Differentiator practical issue: high-frequency noise amplification — fix with small series resistor
- Voltage adder: Vout = -Rf × Σ(Vi/Ri), each input weighted by Rf/Ri
- Voltage follower: unity gain (1×), high input impedance, low output impedance, isolates stages
- SRAM: 6T cell, fast, no refresh, low density, used in caches
- DRAM: 1T1C cell, slower, needs refresh every ~64 ms, high density, used in main memory
- Sense amplifiers: required because DRAM bit line signals are millivolt-scale
- Flash memory: block-erasable EEPROM using floating gate transistors, non-volatile

## Worked Example

**Integrator:** R = 10 kΩ, C = 100 nF, Vin = 1 V (DC step applied at t = 0):

RC = 10×10³ × 100×10⁻⁹ = 1×10⁻³ s = 1 ms

Vout(t) = -(1/RC) ∫ 1 dt = -t / (1 ms)

At t = 5 ms: Vout = -5 V. The output ramps down linearly. Without a parallel resistor, it would eventually saturate at the OpAmp's negative supply rail.

**Differentiator:** Same R and C, Vin(t) = 2t (a ramp rising at 2 V/s):

Vout(t) = -RC × d(2t)/dt = -1×10⁻³ × 2 = -2 mV

The derivative of a ramp is a constant, so the output is a constant -2 mV.

**Voltage adder:** Rf = 10 kΩ, R1 = 10 kΩ, R2 = 20 kΩ, V1 = 1 V, V2 = 2 V:

Vout = -10k × (1/10k + 2/20k) = -10k × (0.1 mA + 0.1 mA) = -10k × 0.2 mA = -2 V

Each input contributes a weighted amount: V1 contributes -Rf/R1 × V1 = -1 V, V2 contributes -Rf/R2 × V2 = -1 V. Total: -2 V.

## Common Pitfalls

- Forgetting that the integrator accumulates DC offsets. Without a parallel resistor, even a tiny input offset voltage causes the output to ramp to saturation over time.
- The differentiator amplifies high-frequency noise aggressively. A raw differentiator is rarely used in practice without the series resistor fix.
- Confusing the integrator's low-pass behavior with the differentiator's high-pass behavior. Integrator = capacitor in feedback = low-pass. Differentiator = capacitor at input = high-pass.
- Thinking the voltage follower is pointless because it has gain = 1. Its value is impedance transformation, not amplification.
- Assuming SRAM and DRAM differ only in density. SRAM is significantly faster because it does not need refresh cycles or charge sensing.
- Forgetting that DRAM requires periodic refresh. Without refresh, stored charge leaks and data is lost within tens of milliseconds.
- Mixing up the voltage adder formula signs. The inverting topology always inverts: Vout = -Rf × Σ(Vi/Ri), not +Rf.
- Thinking Flash memory is the same as EEPROM. Flash erases in blocks, EEPROM erases byte-by-byte. This block erasure enables higher density.

## Connections

- [[microelectronics-lecture-8]] — Previous lecture established the inverting and non-inverting amplifier. This lecture extends them by swapping resistors for capacitors.
- [[capacitor]] — The key component that makes integrators and differentiators work. Its frequency-dependent impedance 1/jωC is what creates the integral/derivative behavior.
- [[analog-amplifier]] — Integrators, differentiators, adders, and buffers are all analog amplifier circuits.
- [[mosfet]] — SRAM cells use six MOSFETs; DRAM cells use one MOSFET as an access transistor.
- [[cmos-inverter]] — SRAM cells are built from two cross-coupled CMOS inverters.
- [[microelectronics-lecture-7]] — Memory cells use transistor circuits (inverter pairs, pass transistors) from earlier lectures.
- [[opamp-integrator]] — Dedicated concept page for integrator circuits.
- [[opamp-differentiator]] — Dedicated concept page for differentiator circuits.
- [[weighted-summer]] — Dedicated concept page for the voltage adder.
- [[voltage-follower]] — Dedicated concept page for the buffer.
- [[sram-cell]] — Dedicated concept page for 6T SRAM cell design.
- [[dram-cell]] — Dedicated concept page for 1T1C DRAM cell design.
- [[sense-amplifier]] — Dedicated concept page for bit line sensing circuits.
- [[flash-memory]] — Dedicated concept page for floating gate and Flash storage.

## Open Questions

- How does the parallel resistor in a practical integrator affect the integration accuracy? At what frequency does it start to deviate from ideal integrator behavior?
- What determines the maximum integration time before saturation, and how do you choose the RC time constant for a given application?
- Why is NAND flash denser than NOR flash at the architectural level? Is it purely the serial vs. parallel access topology?
- How does the floating gate transistor's charge retention time vary with temperature and process node?
- What is the relationship between sense amplifier offset voltage and memory read reliability?
- How do modern DRAM chips handle refresh overhead — is it truly 64 ms for all rows, or is it staggered?
