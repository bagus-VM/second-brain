---
title: "Alternating Current Basics"
tags: [concept, energy-informatics, semester-2, alternating-current]
course: "Energy Informatics I"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[power-grid-fundamentals]]"]
---

## One-line Summary
AC is a sinusoid; its descriptive numbers are amplitude, period and frequency, and the value that matters for power and for the 230 V socket is the RMS value, peak/√2.

## Core Intuition
A DC circuit has one number per quantity; an AC circuit has a *shape*. The voltage rises to a peak, falls through zero, reaches the opposite peak and returns — fifty times a second in Europe. Because a full sine averages to zero, "the voltage" must mean the peak (what insulation withstands) or the RMS value (what heats like a DC source). The 230 V on a German socket is the second, so the peak is about 325 V.

## Formal Definition / Statement

**(a) As a function of time.** For a sinusoidal source:

```
v(t) = V_peak · sin(ωt + φ)        i(t) = I_peak · sin(ωt + φ − ψ)
ω = 2πf = 2π/T
```

`V_peak` is the amplitude, `ω = 2πf` the angular frequency, `φ` a phase offset, `ψ` the current/voltage phase shift. The lecture's qualitative version: AC periodically changes current direction, is typically a sine wave, and is operated as a three-phase system.

**(b) The three terms.** *Amplitude* — the maximum absolute value in a cycle, touched twice per period. *Period `T`* — the time for one complete cycle, the smallest `T` with `v(t + T) = v(t)`. *Frequency `f`* — cycles per second, `f = 1/T`, in hertz; Europe runs at 50 Hz, the US at 60 Hz.

**(c) Graphical representation.** One cycle of `v(t) = V_peak sin(ωt)`:

```
 v
▲
│        ╱╲
│      ╱    ╲
│    ╱        ╲
┼──╱────────────╲──────────╱──▶ t
│ 0    T/4   T/2  ╲      ╱  T
│                   ╲    ╱
│                     ╲╱
```

Zero at 0, `T/2`, `T`; peaks at `T/4` and `3T/4`.

**(d) RMS derivation.** RMS is the square root of the mean of the square over one period:

```
V_rms = sqrt( (1/T) · ∫₀ᵀ v(t)² dt )
```

Step 1 — substitute: `V_rms² = (V_peak²/T) · ∫₀ᵀ sin²(ωt) dt`.

Step 2 — linearise with `sin²θ = (1 − cos 2θ)/2`: the integral becomes `∫₀ᵀ ½ dt` minus `½∫₀ᵀ cos(2ωt) dt`.

Step 3 — the first part gives `T/2`; the second vanishes, since `∫cos(2ωt)dt = sin(2ωt)/(2ω)` and `sin(4π) = sin(0) = 0`.

Step 4 — so `V_rms² = V_peak²/2`, and

```
V_rms = V_peak / √2 ≈ 0.7071 · V_peak
```

**(e) German residential values.** With `V_rms = 230 V` and `f = 50 Hz`:

```
V_peak = √2 · 230 V = 325.27 V ≈ 325 V
T = 1/50 s = 20 ms
```

*Sourcing note:* 50 Hz and the sine/three-phase description are on the slides. The integration, `sin²` identity, `ω = 2πf`, the RMS-as-heating reading and the 230 V / 325 V numbers are **standard background** — the tutorial asks for them (Task 1); the slides do not derive them.

## Key Properties
- RMS survives averaging, which is why nameplate voltages are RMS.
- RMS is the DC-equivalent: a 230 V RMS sine heats a resistor as 230 V DC would (standard background).
- Peak and RMS differ by √2, so insulation and semiconductor ratings follow the peak.

## Worked Example
A German socket: 230 V RMS at 50 Hz. Peak = 230 × 1.4142 = 325.3 V, so the swing is about 650 V. One cycle takes 20 ms, zero crossings at 0, 10 and 20 ms. A device drawing 1 A RMS dissipates the same power as on 230 V DC — the 325 V peak is not the number for `P = V·I`. That 20 ms reference is also what makes frequency a usable control signal ([[power-grid-fundamentals]]).

## Common Pitfalls
- **Using the peak in power formulas.** `P = V_rms · I_rms · cos φ`; substituting 325 V overstates power by a factor of two.
- **Confusing amplitude with peak-to-peak.** 325 V is the amplitude; the swing is 650 V.
- **Forgetting the √2 is sinusoid-specific.** It follows from `sin²` averaging to ½; other waveforms have a different crest factor.

## Connections
- [[power-grid-fundamentals]] — 50 Hz, frequency-as-indicator and the AC/DC distinction.

## Open Questions
- The lecture says AC is three-phase but never develops the line-to-line versus line-to-neutral ratio; √2 covers one phase.
- The derivation assumes a pure sinusoid; distribution grids carry harmonics. At what distortion level does `V_peak/√2` stop being safe for metering?
