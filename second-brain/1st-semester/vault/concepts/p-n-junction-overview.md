---
title: "P-N Junction Overview"
tags: [concept, microelectronics, physics, semiconductor, diode, semester-1]
course: "Introduction to Microelectronics"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites:
  - semiconductor-physics
  - doping-and-extrinsic-semiconductors
  - electron-hole
---

## One-line Summary
*A p-n junction is where p-type and n-type semiconductors meet — the built-in electric field at this boundary creates a one-way gate for current, which is the basis of every diode and transistor.*

## Core Intuition
When you bring p-type and n-type material together, something remarkable happens without any external voltage. Electrons from the n-side diffuse across the junction and recombine with holes on the p-side. This leaves behind fixed positive donor ions on the n-side and fixed negative acceptor ions on the p-side, creating a built-in electric field that opposes further diffusion. This is the depletion region — a narrow zone depleted of mobile carriers. The junction reaches equilibrium when diffusion is balanced by the field. Apply a forward voltage and the barrier shrinks (current flows); apply a reverse voltage and it grows (current blocks). This asymmetry is the diode.

## Formal Definition / Statement
A p-n junction is the metallurgical boundary formed when p-type and n-type semiconductor regions are in intimate contact (typically fabricated from a single crystal by doping different regions differently).

**Built-in potential:**
- V_bi = (kT/q) × ln(N_A × N_D / n_i²)
- For silicon with N_A = N_D = 10¹⁶: V_bi ≈ 0.697 V at 300K

**Depletion region:**
- Width: W = x_n + x_p = √(2ε_s V_bi / q × (1/N_A + 1/N_D))
- Charge neutrality: q × N_A × x_p = q × N_D × x_n
- Electric field maximum at junction: E_max = q × N_A × x_p / ε_s

**Current-voltage relationship (Shockley equation):**
- I = I_s × [exp(qV/nkT) - 1]
- I_s = reverse saturation current (typically 10⁻¹² to 10⁻¹⁵ A)
- n = ideality factor (1 for diffusion current, 2 for recombination current)
- Forward bias (V > 0): exponential current increase
- Reverse bias (V < 0): current ≈ -I_s (tiny, nearly constant)

**Breakdown mechanisms:**
- [[zener-breakdown]]: quantum tunnelling of electrons through thin depletion region (heavily doped, <5V)
- [[avalanche-breakdown]]: impact ionisation creates carrier avalanche (lightly doped, >5V)
- Both are reversible if current is limited

## Key Properties / Complexity
- Depletion width scales with √(V_bi + |V_R|): wider under reverse bias, narrower under forward bias
- The junction acts as a voltage-dependent capacitor (junction capacitance: C_j = ε_s A / W)
- Forward voltage drop is ~0.7V for silicon diodes (conventional design target)
- Reverse leakage current doubles approximately every 10°C
- At high forward injection, the ideality factor approaches 1 (diffusion-limited)
- Breakdown voltage is set by doping: lighter doping → wider depletion → higher breakdown voltage
- Diffusion capacitance dominates under forward bias (minority carrier storage)

## Worked Example
**Silicon p-n junction with N_A = 10¹⁶ cm⁻³, N_D = 10¹⁷ cm⁻³ at 300K:**

Step 1: Built-in potential
  V_bi = 0.0259 × ln(10¹⁶ × 10¹⁷ / (1.5×10¹⁰)²)
       = 0.0259 × ln(10³³ / 2.25×10²⁰)
       = 0.0259 × ln(4.44×10¹²)
       = 0.0259 × 29.12
       = 0.754 V

Step 2: Depletion width at zero bias
  W = √(2 × 11.7 × 8.85×10⁻¹⁴ × 0.754 / 1.6×10⁻¹⁹ × (1/10¹⁶ + 1/10¹⁷))
    = √(1.554×10⁻¹¹ / 1.6×10⁻¹⁹ × 1.1×10⁻¹⁶)
    = √(1.554×10⁻¹¹ × 6.875×10¹⁵)
    = √(1.068×10⁵ × 10⁻⁸)
    = √(1.068×10⁻³) ≈ 0.327 μm = 327 nm

Step 3: Depletion width under 5V reverse bias
  W = √(2ε_s(V_bi + 5)/q × (1/N_A + 1/N_D))
    = 327nm × √(5.754/0.754) = 327 × 2.76 = 903 nm

Step 4: Maximum electric field at zero bias
  E_max = q × N_D × x_n / ε_s ≈ 4.6 × 10⁴ V/cm

## Common Pitfalls
- **"No current in reverse bias"**: There is always a small reverse saturation current from minority carriers. It's tiny but not zero.
- **Forward voltage is always 0.7V**: It's approximately 0.7V at typical operating currents, but varies with current, temperature, and doping. The Shockley equation is exponential, not a fixed threshold.
- **Depletion region has no charge**: It has no mobile carriers, but it has fixed ionized dopant charges — this is what creates the electric field.
- **Zener and avalanche are the same**: They're different mechanisms. Zener is tunnelling (high doping), avalanche is impact ionisation (low doping). "Zener diode" often uses avalanche in practice.
- **The junction exists at zero bias**: The built-in field and depletion region form spontaneously — no external voltage is needed.

## Connections
- [[p-n-junction]] — The fundamental structure; all diodes and transistors contain at least one
- [[depletion-region]] — The carrier-free zone with built-in electric field
- [[diode]] — A two-terminal device based on a single p-n junction
- [[zener-diode]] — A diode designed to operate in reverse breakdown for voltage regulation
- [[zener-breakdown]] — Quantum tunnelling breakdown mechanism in heavily doped junctions
- [[avalanche-breakdown]] — Impact ionisation breakdown in lightly doped junctions
- [[doping-and-extrinsic-semiconductors]] — The p and n regions are created by selective doping
- [[mosfet]] — Contains two p-n junctions (source-body and drain-body)

## Open Questions
- How does the depletion approximation break down at very low doping or very small junction dimensions?
- What determines the ideality factor n in practice, and when does it deviate from 1 or 2?
- How does trap-assisted recombination in the depletion region affect the I-V characteristics?
