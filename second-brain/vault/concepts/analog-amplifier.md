---
title: "Analog Amplifier"
tags: [concept, microelectronics, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*A circuit that increases the amplitude of an analog signal using active components like transistors or op-amps.*

## Core Intuition
An amplifier takes a weak signal (like from a microphone) and makes it stronger (like for a speaker). The key insight is that the amplification doesn't come from nowhere — a power supply provides the extra energy, and the active component (transistor) controls how that energy is shaped to match the input signal. The transistor acts as a valve, not a generator.

## Formal Definition / Statement
An analog amplifier increases the voltage, current, or power of an analog signal.

**Basic configurations (BJT common-emitter, MOSFET common-source):**
- Voltage gain: A_v = -g_m × R_out (inverting for CE/CS)
- Transconductance: g_m = dI_C/dV_BE (BJT) or dI_D/dV_GS (MOSFET)
- Input impedance: varies by configuration
- Output impedance: affects load driving capability

**Key parameters:**
- Gain (A_v, A_i, A_p): voltage, current, power gain
- Bandwidth (BW): frequency range where gain is within 3dB of maximum
- Gain-bandwidth product (GBW): A_v × BW = constant for a given amplifier
- Linearity: how faithfully the output reproduces the input waveform
- Distortion: deviation from linear amplification (THD)
- Noise figure (NF): degradation of signal-to-noise ratio

**Types:**
- Small-signal amplifier: operates in linear region, small input signals
- Power amplifier: delivers significant power to a load (Class A, B, AB, D)
- Operational amplifier: high-gain differential amplifier with feedback
- Instrumentation amplifier: high CMRR for precise measurements

## Key Properties / Complexity
- Active devices (transistors) provide power gain; passive components (resistors, capacitors) shape the response
- Negative feedback trades gain for linearity, bandwidth, and stability
- Amplifier classes (A, B, AB, D) trade efficiency for linearity
- Frequency response: coupling/bypass capacitors set low-frequency cutoff; transistor parasitics set high-frequency cutoff
- Thermal stability: biasing must be temperature-independent for reliable operation

## Worked Example
Common-emitter BJT amplifier design:
1. Bias point: V_CC = 12V, I_C = 1mA, V_CE = 6V
2. g_m = I_C/V_T = 1mA/26mV = 38.5 mS
3. Load resistor R_C = 6kΩ
4. Voltage gain: A_v = -g_m × R_C = -38.5mS × 6kΩ = -231
5. Input signal: 10mV peak
6. Output signal: 10mV × 231 = 2.31V peak (inverted)
7. Bandwidth: with parasitic capacitances, f_3dB ≈ 10MHz
8. GBW = 231 × 10MHz = 2.31GHz

## Common Pitfalls
- **Biasing is critical**: Wrong bias point → clipping, distortion, or thermal runaway
- **Gain vs bandwidth tradeoff**: Higher gain means lower bandwidth (Miller effect)
- **Loading effects**: Connecting a load reduces the effective gain
- **Stability**: High-gain amplifiers can oscillate without proper compensation
- **Power supply rejection**: Noise on the power supply appears at the output

## Connections
- [[mosfet]] — MOSFET as the active device in CMOS amplifiers
- [[common-source-amplifier]] — MOSFET common-source configuration
- [[cmos-inverter]] — CMOS inverter as an amplifier
- [[capacitor]] — Coupling and bypass capacitors in amplifier circuits
- [[power-supply]] — Amplifier requires a DC power supply
- [[diode]] — Diode biasing and temperature compensation in amplifier circuits

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
