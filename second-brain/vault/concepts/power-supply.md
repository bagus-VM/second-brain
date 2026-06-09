---
title: "Power Supply in Electronics"
tags: [concept, microelectronics, circuits, semester-1]
course: "Microelectronics"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The source of electrical energy that powers electronic circuits, converting AC mains or battery voltage to the regulated DC voltages needed by components.*

## Core Intuition
Every circuit needs power. A power supply converts raw energy (wall outlet, battery, solar panel) into the clean, stable DC voltage that transistors and ICs require. The quality of the power supply directly affects circuit performance — noisy power means noisy signals, unstable voltage means unreliable operation.

## Formal Definition / Statement
A power supply provides regulated DC voltage to electronic circuits.

**Types:**

1. **Linear regulators** (LDO):
   - Drop excess voltage as heat: P = (V_in - V_out) × I_load
   - Simple, low noise, fast transient response
   - Low efficiency when V_in >> V_out
   - Examples: LM7805 (fixed 5V), LM317 (adjustable)

2. **Switching regulators** (SMPS):
   - Use inductors/capacitors to store and transfer energy
   - High efficiency (85–95%) regardless of voltage ratio
   - Topologies: buck (step-down), boost (step-up), buck-boost
   - Generate switching noise (EMI)
   - More complex than linear regulators

3. **Battery:**
   - Primary (non-rechargeable): alkaline, lithium
   - Secondary (rechargeable): lithium-ion, lithium-polymer
   - Voltage decreases as battery discharges
   - Requires protection circuits (over-charge, over-discharge, over-current)

**Key specifications:**
- Output voltage (e.g., 3.3V, 5V, 12V)
- Output current capability
- Line regulation: ΔV_out / ΔV_in
- Load regulation: ΔV_out / ΔI_load
- Ripple: AC component on DC output
- Efficiency: P_out / P_in
- Transient response: speed of recovery after load change

## Key Properties / Complexity
- Linear regulators: simple, low noise, low efficiency
- Switching regulators: complex, high efficiency, noisy
- LDO (Low Dropout): linear regulator with small V_in - V_out minimum
- Power supply rejection ratio (PSRR): how well the supply rejects input noise
- Decoupling capacitors: local energy storage for fast transient demands
- Power sequencing: some ICs require specific power-on order

## Worked Example
Power supply for an IoT sensor node:
- Source: 3.7V lithium-ion battery (3.0–4.2V range)
- MCU requires 3.3V (±5%)
- LDO: MCP1700 (3.3V, 250mA, 178mV dropout)
  - At full charge (4.2V): efficiency = 3.3/4.2 = 78.6%
  - At low battery (3.5V): efficiency = 3.3/3.5 = 94.3%
  - Dropout: 3.3V + 0.178V = 3.478V minimum input
- Decoupling: 10μF electrolytic + 100nF ceramic at MCU VDD pins
- Sleep current: MCU draws 2μA in sleep, LDO quiescent current 1.6μA
- Battery life: 500mAh / (2μA + 1.6μA) = 138,889 hours ≈ 15.8 years (sleep only)

## Common Pitfalls
- **Insufficient decoupling**: Missing or wrong capacitors cause oscillation or noise
- **Thermal management**: Linear regulators dissipate (V_in - V_out) × I as heat
- **Ground loops**: Multiple ground paths can introduce noise
- **Input voltage range**: Exceeding V_in max destroys the regulator
- **Load transients**: Sudden current changes (radio TX) cause voltage dips
- **Efficiency at light load**: Switching regulators can be inefficient at very low currents

## Connections
- [[capacitor]] — Decoupling and filtering capacitors in power supplies
- [[diode]] — Rectifier diodes in AC-DC power supplies
- [[cmos-inverter]] — CMOS circuits require stable V_DD for proper operation
- [[electricity]] — Fundamental electrical concepts (voltage, current, power)
- [[analog-amplifier]] — Amplifiers require clean power supply for low noise
- [[mosfet]] — MOSFETs used in switching regulator circuits

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
