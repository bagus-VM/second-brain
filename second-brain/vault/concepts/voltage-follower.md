---
title: "Voltage Follower (Unity-Gain Buffer)"
tags: [concept, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[microelectronics-lecture-8]]", "[[analog-amplifier]]"]
---

## One-line Summary
*The output follows the input exactly — no amplification, no inversion — but it isolates the source from the load.*

## Core Intuition
A voltage follower is the simplest OpAmp circuit: connect the output directly to the inverting input (100% feedback). The gain is 1. So why bother? Because the OpAmp has very high input impedance (draws almost no current from the source) and very low output impedance (can drive heavy loads without voltage drop). It acts as an impedance transformer: a weak source (high output impedance) can drive a heavy load (low input impedance) without losing voltage. Without the buffer, the load would form a voltage divider with the source impedance and reduce the signal.

## Formal Definition / Statement

**Circuit:** Non-inverting amplifier with R2 = 0 (short circuit from output to inverting input) and R1 removed (open circuit from inverting input to ground).

**Gain:** Vout/Vin = 1 + R2/R1 = 1 + 0/∞ = 1

**Alternative derivation:** Non-inverting amplifier gain = 1 + R2/R1. Set R2 = 0 → gain = 1. Or equivalently, connect output directly to inverting input → 100% negative feedback → output must equal input.

## Key Properties / Complexity

- Gain = 1 (unity gain, no amplification)
- No phase inversion (output in phase with input)
- Very high input impedance (set by OpAmp input, typically MΩ to GΩ)
- Very low output impedance (set by OpAmp output stage, typically < 1 Ω)
- Bandwidth is maximal (no feedback resistors → maximum feedback → widest bandwidth)
- Used for impedance transformation, stage isolation, driving capacitive loads

## Worked Example

A sensor with 10 kΩ output impedance needs to drive a 1 kΩ load. Without buffer:

V_load = V_sensor × R_load / (R_source + R_load) = V_sensor × 1k / 11k = 0.091 × V_sensor

90% of the signal is lost! With a voltage follower between sensor and load:

V_load = V_sensor × 1 (the buffer's high Zin draws no current from sensor, low Zout drives load fully)

The buffer preserves the full signal voltage.

## Common Pitfalls

- **Thinking it's useless because gain = 1.** The value is impedance transformation, not amplification.
- **Confusing with the inverting buffer.** There's no "inverting buffer" with gain = -1 in the same sense. An inverting amplifier with R1 = R2 gives gain = -1, but it has low input impedance (R1).
- **Ignoring bandwidth limitations.** At high frequencies, the OpAmp's gain drops and the follower stops being ideal. The gain-bandwidth product still applies.
- **Forgetting about offset voltage.** Real OpAmps have input offset voltage (mV). The follower passes this through, so Vout = Vin + Voffset.

## Connections

- [[weighted-summer]] — a voltage follower after a summer buffers the output
- [[microelectronics-lecture-8]] — non-inverting amplifier with R2 = 0
- [[microelectronics-lecture-9]] — lecture that introduces voltage followers
- [[analog-amplifier]] — voltage follower is the simplest amplifier (gain = 1)
- [[negative-feedback]] — 100% negative feedback gives maximum stability
- [[impedance-matching]] — the primary purpose of a voltage follower

## Open Questions

- How does the voltage follower's bandwidth compare to a non-inverting amplifier with gain > 1?
- What happens when the voltage follower drives a purely capacitive load? Does it oscillate?
- How do you choose between a voltage follower and a resistive voltage divider for impedance matching?
