---
title: "MOS Transistors"
tags: [topic, microelectronics, semester-1]
course: "Introduction to Microelectronics"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[microelectronics-lecture-3]]", "[[microelectronics-lecture-1]]"]
---

## One-line Summary
The [[mosfet]] (Metal-Oxide-Semiconductor Field-Effect Transistor) uses a gate-controlled electric field through a thin oxide to modulate the conductivity of a semiconductor channel — the [[mos-capacitor]] effect — enabling [[transistor]] switching and amplification that powers all modern digital and analog electronics.

## Core Intuition
The [[mosfet]] is essentially a voltage-controlled switch. A thin gate oxide separates a metal (or polysilicon) gate from the silicon body. When voltage is applied to the gate, an electric field penetrates the oxide and attracts or repels carriers at the silicon surface. For an [[nmos-transistor]] (built in p-type substrate), applying a positive gate voltage above the [[threshold-voltage]] V_th attracts electrons to the surface, forming an n-type inversion layer (channel) between the n+ source and n+ drain. This channel conducts current. No gate current flows (oxide is insulating), so the device has essentially infinite input impedance. A [[pmtransistor]] works complementarily with negative V_gs on an n-type substrate.

## Formal Definition / Statement
The [[mos-capacitor]] is the heart of the [[mosfet]]. The gate-body structure forms a capacitor with capacitance per unit area:

    C_ox = ε_ox / t_ox

where ε_ox is the oxide permittivity (≈ 3.9 × ε_0 for SiO_2) and t_ox is the oxide thickness.

**[[threshold-voltage]] (for nMOS):**

    V_th = V_FB + 2φ_F + (1/C_ox) × sqrt(2ε_s q N_A (2φ_F))

where V_FB is the flat-band voltage, φ_F = (kT/q) ln(N_A/n_i) is the Fermi potential, and N_A is the substrate doping.

**MOSFET Drain Current (long-channel model):**

*Cutoff region:* V_gs < V_th → I_D = 0

*Linear (triode) region:* V_gs > V_th and V_ds < V_gs − V_th:

    I_D = μ_n C_ox (W/L) [(V_gs − V_th) V_ds − V_ds^2 / 2]

*Saturation region:* V_gs > V_th and V_ds ≥ V_gs − V_th:

    I_D = (1/2) μ_n C_ox (W/L) (V_gs − V_th)^2 (1 + λV_ds)

where μ_n is electron mobility, W/L is the width-to-length ratio, and λ is the channel-length modulation parameter.

## Key Properties / Complexity

**MOS Structure Layers (bottom to top):**
1. Silicon substrate (p-type for nMOS, n-type for pMOS).
2. Thin gate oxide (SiO_2 or high-κ dielectric) — typically 1–5 nm in modern processes.
3. Gate electrode (polysilicon or metal).
4. Source and drain regions (heavily doped, opposite type to substrate).

**[[mos-capacitor]] Operating Regimes:**
| Gate Voltage (V_gb) | Surface Condition | Carrier Behavior |
|---|---|---|
| V_gb < V_FB | Accumulation | Majority carriers accumulate at surface |
| V_gb = V_FB | Flat band | No band bending |
| V_FB < V_gb < V_th | Depletion | Majority carriers repelled, depleted surface |
| V_gb = V_th | Onset of inversion | Minority carriers = intrinsic concentration at surface |
| V_gb > V_th | Strong inversion | Minority carrier inversion layer forms channel |

**[[mosfet-operating-regions]]:**

1. **Cutoff:** V_gs < V_th. No channel. I_D ≈ 0 (only leakage). Transistor is OFF.

2. **Linear (Triode):** V_gs > V_th, V_ds < V_dsat. Channel exists from source to drain. Acts as a voltage-controlled resistor. I_D increases roughly linearly with V_ds. Used in analog switches and pass transistors.

3. **Saturation:** V_gs > V_th, V_ds ≥ V_dsat = V_gs − V_th. Channel pinches off at drain end. I_D is relatively independent of V_ds (modulated by λ). Used for amplification and digital switching. Maximum gain region.

4. **Breakdown:** V_ds exceeds breakdown voltage. Avalanche in drain depletion region. Destructive if sustained.

**nMOS vs pMOS ([[nmos-transistor]] vs [[pmtransistor]]):**

| Property | nMOS | pMOS |
|---|---|---|
| Substrate | p-type | n-type |
| Source/Drain | n+ (phosphorus/arsenic) | p+ (boron) |
| Channel carriers | Electrons | Holes |
| V_th | Positive (enhancement) | Negative (enhancement) |
| Mobility (μ) | Higher (~2-3×) | Lower |
| Symbol arrow | Into gate | Out of gate |
| Gate voltage | Positive to turn ON | Negative to turn ON |

**CMOS (Complementary MOS):**
- Combines nMOS and pMOS on the same chip.
- Near-zero static power dissipation (one device always OFF in steady state).
- Basis of all modern digital logic (processors, memory, FPGAs).

**Short-Channel Effects (modern scaled MOSFETs):**
- Velocity saturation: carriers reach maximum velocity before pinch-off.
- Drain-induced barrier lowering (DIBL): V_ds reduces effective V_th.
- Channel-length modulation: I_D continues to increase slightly in saturation.
- Subthreshold conduction: exponential leakage below V_th.
- Gate leakage: quantum tunneling through ultra-thin oxides.

## Connections

- [[mosfet]] — The transistor device built on the MOS capacitor principle.
- [[mos-capacitor]] — The gate-oxide-substrate structure that forms the channel.
- [[threshold-voltage]] — The gate voltage at which the inversion layer forms.
- [[nmos-transistor]] — MOSFET with n-type source/drain in p-type substrate; electron channel.
- [[pmtransistor]] — MOSFET with p-type source/drain in n-type substrate; hole channel.
- [[mosfet-operating-regions]] — Cutoff, linear, saturation, and breakdown regimes.
- [[transistor]] — The general class of three-terminal semiconductor devices.
- [[microelectronics-lecture-3]] — Source-body and drain-body junctions are p-n junctions.
- [[microelectronics-lecture-2]] — How source, drain, channel, and substrate are doped.
- [[microelectronics-lecture-1]] — Band structure and carrier statistics underlying MOS operation.

## Open Questions
- How far can gate length scaling go before quantum effects dominate completely?
- Can FinFET and Gate-All-Around (GAA) structures sustain Moore's Law?
- What are the fundamental limits of subthreshold swing (60 mV/dec at room temp)?
- How do ferroelectric and negative-capacitance gates modify the threshold voltage model?
