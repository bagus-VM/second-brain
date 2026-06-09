---
title: "Common-Source Amplifier"
tags: [concept, microelectronics, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*A MOSFET amplifier configuration where the source is grounded, providing voltage gain with 180° phase inversion.*

## Core Intuition
The common-source (CS) amplifier is the MOSFET equivalent of the BJT common-emitter amplifier. It's the most basic single-transistor voltage amplifier. The input signal modulates the gate voltage, which controls the drain current, which develops a voltage across the load resistor. The key insight: a small change in V_GS produces a large change in V_out because the transconductance amplifies the signal.

## Formal Definition / Statement
A common-source amplifier has:
- Input at the gate
- Output at the drain
- Source connected to ground (common reference)

**Small-signal analysis:**
- Voltage gain: A_v = -g_m × (r_o || R_D || R_L)
- g_m = transconductance = 2I_D/(V_GS - V_T) (saturation)
- r_o = output resistance (channel-length modulation)
- R_D = drain resistor
- Input impedance: very high (gate is insulated)
- Output impedance: r_o || R_D

**With source degeneration (R_S):**
- A_v = -g_m × (r_o || R_D) / (1 + g_m × R_S)
- Lower gain but higher linearity and input range

**Frequency response:**
- Low-frequency cutoff: coupling and bypass capacitors
- High-frequency cutoff: C_gs, C_gd (Miller effect on C_gd)
- Miller effect: C_gd appears as (1 + |A_v|) × C_gd at the input
- Gain-bandwidth tradeoff: higher gain → lower bandwidth

## Key Properties / Complexity
- Highest voltage gain of single-transistor configurations
- 180° phase shift (inverting)
- Very high input impedance (MOSFET gate)
- Moderate output impedance
- Miller effect limits high-frequency performance
- Biasing is critical for proper operation in saturation region

## Worked Example
CS amplifier design:
- V_DD = 5V, I_D = 0.5mA, R_D = 8kΩ
- MOSFET: k_n = 1mA/V², V_T = 1V
- g_m = √(2 × k_n × I_D) = √(1mA²/V²) = 1mS
- r_o = 50kΩ (early voltage V_A = 25V)
- A_v = -g_m × (r_o || R_D) = -1mS × (50k || 8k) = -1mS × 6.9k = -6.9
- Input: 100mV sine wave → Output: 690mV sine wave (inverted)
- Bandwidth: f_3dB ≈ 100MHz (with parasitic capacitances)

## Common Pitfalls
- **Biasing sensitivity**: Small changes in V_T (temperature, process) shift the operating point
- **Body effect**: If source isn't at ground potential, V_T increases, reducing gain
- **Miller multiplication**: C_gd × (1 + |A_v|) at the input severely limits bandwidth
- **Output swing**: Large R_D for high gain reduces output voltage swing
- **Process variation**: g_m and r_o vary with manufacturing, affecting gain

## Connections
- [[mosfet]] — The active device in the CS amplifier
- [[mosfet-operating-regions]] — Must operate in saturation for linear amplification
- [[threshold-voltage]] — V_T determines bias point and gain
- [[capacitor]] — Coupling capacitors and parasitic capacitances affect frequency response
- [[analog-amplifier]] — CS is one of three basic amplifier configurations
- [[cmos-inverter]] — CMOS inverter uses CS configuration for both NMOS and PMOS

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
