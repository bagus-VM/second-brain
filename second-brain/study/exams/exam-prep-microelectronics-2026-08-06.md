---
title: "Introduction to Microelectronics Exam Prep — August 6, 2026"
tags: [exam-prep, microelectronics, semester-1]
course: "Introduction to Microelectronics"
status: current
last_updated: 2026-07-27
exam_date: 2026-08-06
exam_format: "Lecture-based, Slides 1-10 + textbook (Sedra/Smith/Carusone/Gaudet 2019)"
scope: "Lectures 1-10, topics 1-10 in syllabus"
lecturer: "Dr. Nikolaos Athanasious Anagnostopoulos"
---

# Introduction to Microelectronics — Exam Battle Plan

**Exam:** 06 August 2026. **Lecturer:** Dr. Nikolaos Athanasious Anagnostopoulos, University of Passau. **Textbook:** Sedra, Smith, Carusone, Gaudet, *Microelectronic Circuits*, OUP 2019. Companion text in slides: Razavi, *Fundamentals of Microelectronics*, 3rd ed., Wiley 2021.

This is a condensed, exam-focused review. It is not a textbook. Memorise the formulas boxed in [[#Key Formulas You Must Know]]. If you can answer the [[#Mock Exam Questions]] cold, you are ready. If you cannot, find the matching [[#Weak Spot Map]] row and re-read that lecture.

Vault sources synthesised here: [[microelectronics-lecture-1]] through [[microelectronics-lecture-9]], [[microelectronics]], [[electronics]], [[nanoelectronics]], and the ten `Microelectronics*_2026.pdf` slide decks in `raw/lectures/introduction_to_microelectronics/`.

---

## Topic Coverage Map

| # | Topic | Slides | Vault Pages | Priority |
|---|------|--------|-------------|----------|
| 1 | Basic concepts: electronics vs microelectronics vs nanoelectronics | L1 | [[electronics]] [[microelectronics]] [[nanoelectronics]] | Medium |
| 2 | Physics: semiconductors, doping, intrinsic/extrinsic | L1-L2 | [[microelectronics-lecture-1]] [[microelectronics-lecture-2]] | **HIGH** |
| 3 | P-N junction, diodes, breakdown | L3 | [[microelectronics-lecture-3]] [[diode]] [[p-n-junction]] | **CRITICAL** |
| 4 | Diode applications: rectifiers, clampers, limiters, Zener | L4 | [[microelectronics-lecture-4]] [[rectifier]] [[clamper-circuit]] [[limiter-circuit]] | **CRITICAL** |
| 5 | MOS transistors (nMOS/pMOS), MOS capacitor, regions | L5 | [[microelectronics-lecture-5]] [[mosfet]] [[mos-capacitor]] | **CRITICAL** |
| 6 | CMOS: inverter, NAND, NOR, XOR, arbitrary gates | L6 | [[microelectronics-lecture-6]] [[cmos-inverter]] [[cmos-logic-gates]] | **HIGH** |
| 7 | CMOS applications: flip-flops, memories, amplifiers, op-amp intro | L7 | [[microelectronics-lecture-7]] [[common-source-amplifier]] [[opamp-basics]] | **HIGH** |
| 8 | Op-amp: inverting, non-inverting, virtual short | L8 | [[microelectronics-lecture-8]] | **CRITICAL** |
| 9 | Op-amp: integrator, differentiator, adder, follower. Memories: SRAM/DRAM, Flash | L9 | [[microelectronics-lecture-9]] [[sram-cell]] [[dram-cell]] [[flash-memory]] | **CRITICAL** |
| 10 | Beyond silicon: graphene, CNTs, memristors. AI for circuit design | L10 | [[nanoelectronics]] | Low |

---

## Topic 1 — Basic Concepts

Three nested fields. Definitions are tight and examinable.

- **[[electronics]]:** scientific field that applies physics to devices manipulating electrons and charged particles. Subfields include microelectronics and nanoelectronics. Binary conducting/non-conducting states map to Boolean algebra; devices with >2 states enable unconventional computing (e.g. ternary).
- **[[microelectronics]]:** subfield of electronics. Components at the micrometre scale or smaller. Built on semiconductor wafers (mostly [[silicon]]). Fabrication: [[photolithography]], [[ion-implantation]], [[thermal-diffusion]]. Enables VLSI, billions of transistors per chip.
- **[[nanoelectronics]]:** subfield that exploits nanotechnology and quantum mechanical properties at the nanometre scale. Quantum tunnelling, discrete energy levels, wave-particle duality. Devices: quantum dots, single-electron transistors (SET), tunnel FETs, spintronics. Extends, does not replace, microelectronics. Many such devices need cryogenic temperatures.

Water analogies the lecturer uses and will lean on:
- Conductor = open canal. Insulator = canal dammed by rocks. Semiconductor = filled pool with a low wall.
- P-N junction = canal with a rock dam (depletion region). Forward bias removes rocks; reverse bias adds rocks; too much bias breaks the dam.

Memorise the distinction: **microelectronics = classical behaviour at micrometre scale; nanoelectronics = quantum behaviour at nanometre scale.** Anagnostopoulos uses these analogies in the slides, so a question framed in water terms is asking for the corresponding semiconductor concept.

---

## Topic 2 — Semiconductor Physics

### 2.1 Band structure classification

| Class | Bandgap E_g | Example | Carrier density |
|---|---|---|---|
| Conductor | overlapping / zero | Cu, Al | always free |
| Semiconductor | 0.1 eV < E_g < 4 eV | Si (1.12), Ge (0.66), GaAs (1.42) | thermally tunable |
| Insulator | E_g > 4 eV | SiO_2, diamond | essentially none |

- **Direct bandgap** (GaAs, InP): momentum-conserving transitions, efficient light emission (LEDs, lasers).
- **Indirect bandgap** (Si, Ge): photon emission needs a phonon, poor light emitters, excellent electronic material.
- Why [[silicon]] dominates: E_g = 1.12 eV ideal for room temperature; SiO_2 native oxide enables MOS; abundant; decades of CMOS infrastructure.

### 2.2 Intrinsic carrier concentration

$$n_i = \sqrt{N_c N_v}\, \exp\!\left(-\frac{E_g}{2kT}\right)$$

For Si at 300 K: n_i ≈ 1.5 × 10^10 cm^-3. As T rises, n_i rises exponentially. At very high T, intrinsic carriers overwhelm doping and the device fails. At very low T, freeze-out occurs.

Mobility (Si at 300 K): electrons ~1350 cm^2/Vs, holes ~480 cm^2/Vs. Conductivity:

$$\sigma = q(n\mu_n + p\mu_p)$$

### 2.3 Doping

[[doping]] deliberately introduces impurity atoms to control carrier concentration. Turns intrinsic Si into extrinsic Si.

| Dopant | Type | Group | Effect |
|---|---|---|---|
| P, As, Sb | n-type | V | donor, extra electron |
| B, Al, Ga | p-type | III | acceptor, creates hole |

**Mass-action law:** $n \cdot p = n_i^2$.

n-type (N_D >> n_i): $n \approx N_D$, $p = n_i^2 / N_D$.
p-type (N_A >> n_i): $p \approx N_A$, $n = n_i^2 / N_A$.
Compensation: $n - p = N_D - N_A$ with $np = n_i^2$.

Dopant ionisation (Si): donor level ~E_c - 0.045 eV, acceptor level ~E_v + 0.045 eV. Both shallow.

Doping ranges: light 10^14 to 10^16, moderate 10^16 to 10^18, heavy n+/p+ 10^18 to 10^21 cm^-3.

Fabrication methods:
1. **[[thermal-diffusion]]**: wafer at 900 to 1200 degC in dopant gas (PH_3, BCl_3). Gaussian or erfc profile. Older, less precise.
2. **[[ion-implantation]]**: ions accelerated to keV to MeV, shot into wafer. Precise dose (ions/cm^2), masked by photolithography. Lattice damage needs annealing. Modern standard.
3. In-situ doping during epitaxial growth.

Fermi level: more n-type doping shifts E_F toward E_c; more p-type toward E_v. Above ~10^19 the semiconductor becomes degenerate (metallic).

---

## Topic 3 — P-N Junction and Diode

A [[p-n-junction]] forms when p-type and n-type meet. Holes and electrons diffuse across, recombine, and leave fixed ionised dopants: positive donors on the n side, negative acceptors on the p side. This exposed charge is the [[depletion-region]]; its field produces the built-in potential.

**Built-in potential:**

$$V_{bi} = \frac{kT}{q}\,\ln\!\left(\frac{N_A N_D}{n_i^2}\right)$$

**Depletion width (zero bias):**

$$W = \sqrt{\frac{2\varepsilon_s V_{bi}}{q}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)}$$

The depletion region extends more into the lightly doped side.

**Ideal diode equation:**

$$I = I_s\left[\exp\!\left(\frac{qV}{nkT}\right)-1\right]$$

where I_s is reverse saturation current, n is ideality factor (1 to 2), V_T = kT/q ≈ 26 mV at 300 K.

### Bias conditions

| Condition | Barrier | Current | Depletion width |
|---|---|---|---|
| Zero bias | V_bi | zero net | W_0 |
| Forward (V > 0) | V_bi - V | exponential rise | narrows |
| Reverse (V < 0) | V_bi + |V| | ~ -I_s (tiny) | widens |

Forward voltage drop: ~0.7 V (Si), ~0.3 V (Ge), ~1.5 V (GaAs). The slides say built-in potential is 0.6 to 0.9 V for Si.

### Breakdown (two mechanisms, examinable contrast)

**[[avalanche-breakdown]]:** lightly doped, wide depletion. Carriers accelerate, impact-ionise, chain reaction. V_BR > 6 V for Si. **Positive** temperature coefficient.

**Zener breakdown:** heavily doped, narrow depletion. Field ~10^6 V/cm breaks covalent bonds by quantum tunnelling. V_BR < 5 V for Si. **Negative** temperature coefficient.

Sign of the tempco tells you which mechanism dominates. This is an exam-style distinguisher.

Practical effects: reverse leakage from minority carriers and generation in the depletion region; junction capacitance C_j = epsilon_s A / W (varactor effect); diffusion capacitance under forward bias from minority carrier storage.

---

## Topic 4 — Diode Applications

### 4.1 Rectifiers

**[[half-wave-rectifier]]:** one diode in series with load. Conducts only on positive half cycle. V_out = V_in - 0.7 V for V_in > 0.7 V, else 0.
- V_avg = V_peak / pi (~0.318 V_peak)
- Ripple frequency = input frequency
- Simple, poor efficiency, high ripple.

**[[full-wave-rectifier]] (center-tapped):** two diodes + center-tapped transformer. Both half cycles rectified (negative half inverted).
- V_avg = 2 V_peak / pi (~0.637 V_peak)
- Ripple frequency = 2 times input frequency.

**[[bridge-rectifier]]:** four diodes in a bridge. Both half cycles rectified, no center tap.
- V_avg = 2 V_peak / pi - 2(0.7 V) (two diode drops in the path)
- PIV per diode = V_peak (vs 2 V_peak for center-tapped).
- Most common full-wave topology.

**Smoothing:** filter capacitor C in parallel with the load reduces ripple. For full-wave:
$$V_{ripple} \approx \frac{I_{load}}{f \cdot C}$$
Larger C means less ripple.

### 4.2 Clampers ([[clamper-circuit]])

Shift the DC level of a waveform without changing its shape. Capacitor + diode + optional bias.

- **Positive clamper:** on the negative half cycle the diode conducts, charging the cap to V_peak - 0.7 V. On the positive half cycle the diode is off, so V_out = V_in + V_cap. Shifts the waveform upward so its minimum sits near 0 V.
- **Negative clamper:** reverse diode orientation. Shifts waveform downward so its maximum sits near 0 V.
- **Biased clamper:** add V_ref to shift the clamp level away from zero.

Slides L04 walk through six clamper variants: positive, positive with +V_R, positive with -V_R, negative, negative with +V_R, negative with -V_R. Know which diode orientation produces which direction of shift, and how the bias source moves the clamp point.

### 4.3 Limiters ([[limiter-circuit]])

Clip the waveform to a defined voltage range.

- **Series clipper:** diode in series with the signal path. Positive clipper = anode to ground, cathode to signal, clips positive half. Reversed = clips negative half.
- **Parallel (shunt) clipper:** diode in parallel with the output. When it conducts, it clamps output to ~0 V (or V_ref + 0.7 V with a bias source).
- **Biased clipper:** add V_ref in series with the diode. Clips at V_ref + 0.7 V instead of 0.7 V.
- **Double / window clipper:** two anti-parallel biased diodes. Clips both positive and negative peaks, confining the output to a window.

### 4.4 Zener voltage regulator

[[zener-diode]] operated in reverse breakdown across the load. For V_in > V_Z the Zener conducts and V_out stays near V_Z.
- Series resistor R sets current: I_R = (V_in - V_Z) / R.
- Load current: I_L = V_Z / R_L.
- Zener current: I_Z = I_R - I_L.
- Keep I_Z within [I_Z_min, I_Z_max]. Power dissipated in the Zener: P_Z = V_Z I_Z.

Exam trap: do not forget to check that I_Z stays positive and below the rated maximum. A Zener regulator question has two inequalities to satisfy, not one.

---

## Topic 5 — MOS Transistors

The [[mosfet]] is a voltage-controlled switch. A thin gate oxide separates the gate from the semiconductor body. Gate voltage creates a field through the oxide that forms or removes an inversion layer (channel) between source and drain. Because the oxide is insulating, gate current is essentially zero: the device has near-infinite input impedance.

### 5.1 MOS capacitor and threshold

$$C_{ox} = \frac{\varepsilon_{ox}}{t_{ox}}$$

For SiO_2, epsilon_ox ~ 3.9 epsilon_0. Modern gate oxides are 1 to 5 nm.

MOS capacitor regimes vs. gate-body voltage V_gb:

| V_gb | Surface |
|---|---|
| V_gb < V_FB | Accumulation (majority carriers pile up) |
| V_gb = V_FB | Flat band |
| V_FB < V_gb < V_th | Depletion |
| V_gb = V_th | Onset of inversion |
| V_gb > V_th | Strong inversion (channel forms) |

**Threshold voltage (nMOS):**

$$V_{th} = V_{FB} + 2\varphi_F + \frac{1}{C_{ox}}\sqrt{2\varepsilon_s q N_A (2\varphi_F)}$$

where $\varphi_F = (kT/q)\ln(N_A/n_i)$.

V_th is the minimum V_GS that creates a conducting path between source and drain. The slides phrase it exactly that way.

### 5.2 MOSFET I-V (long-channel model)

| Region | Condition | I_D |
|---|---|---|
| Cutoff | V_GS < V_th | 0 (leakage only) |
| Linear / triode | V_GS > V_th, V_DS < V_GS - V_th | $\mu_n C_{ox}\frac{W}{L}\left[(V_{GS}-V_{th})V_{DS} - \frac{V_{DS}^2}{2}\right]$ |
| Saturation | V_GS > V_th, V_DS >= V_dsat | $\frac{1}{2}\mu_n C_{ox}\frac{W}{L}(V_{GS}-V_{th})^2(1+\lambda V_{DS})$ |
| Breakdown | V_DS exceeds BV | avalanche, destructive |

V_dsat = V_GS - V_th is the saturation boundary. In saturation the channel pinches off at the drain end, and I_D is nearly independent of V_DS (lambda lumps channel-length modulation).

Why three regions matter for the exam:
- **Cutoff** is the OFF state in digital CMOS.
- **Triode** acts as a voltage-controlled resistor. Used in analog switches and pass transistors.
- **Saturation** is the amplification region. Common-source amplifiers bias here.

### 5.3 nMOS vs pMOS

| | nMOS | pMOS |
|---|---|---|
| Substrate | p-type | n-type |
| Source/Drain | n+ | p+ |
| Carriers | electrons | holes |
| V_th sign | positive (enhancement) | negative (enhancement) |
| Mobility | higher (~2 to 3x) | lower |
| Turn-on | positive V_GS | negative V_GS |

From L06: in standard cell layouts the bulk (body) electrode is not drawn; the substrate is common.

### 5.4 Short-channel effects (mentioned, low exam priority unless asked)

Velocity saturation, DIBL (drain-induced barrier lowering), channel-length modulation, subthreshold conduction, gate-oxide tunnelling. If a question asks "what happens when CMOS is scaled," mention mobility degradation, V_T variability from random dopant fluctuation, and rising leakage.

---

## Topic 6 — CMOS Logic Gates

**CMOS = complementary MOS.** Combine an nMOS pull-down network (PDN) to GND and a pMOS pull-up network (PUN) to V_DD on the same chip. The two networks are logical duals: exactly one conducts for any input combination. This is why CMOS gates have near-zero static power. One device is always OFF in steady state. Power is drawn only during the switching transient.

### 6.1 Construction rule

Given a Boolean function F(A, B, ...):
1. PDN (nMOS to GND): AND means series, OR means parallel. PDN conducts when F = 1.
2. PUN (pMOS to V_DD): implements NOT F. PUN conducts when F = 0.

Output = NOT F. The PDN is built from F; the gate is named after the function it pulls down. This naming is symmetric and trips people up.

### 6.2 Standard gates

| Gate | PDN (nMOS) | PUN (pMOS) | Output |
|---|---|---|---|
| Inverter (NOT) | 1 nMOS | 1 pMOS | NOT A |
| NAND | 2 nMOS in series | 2 pMOS in parallel | NOT(A AND B) |
| NOR | 2 nMOS in parallel | 2 pMOS in series | NOT(A OR B) |
| AND | NAND + inverter (2 stages) | | A AND B |
| OR | NOR + inverter (2 stages) | | A OR B |
| XOR | not constructible in a single static CMOS stage | | A XOR B |

**XOR is the gate that breaks the rule.** F = A XOR B = A NOT(B) + NOT(A) B has a PDN of two parallel series pairs, but no single pMOS network perfectly complements it while keeping the output always driven. Solutions:
- Transmission-gate XOR (6 to 12 transistors): pass B through a TG controlled by A, and NOT B through a TG controlled by NOT A.
- 6T static XOR with cross-coupled pMOS loads.
- Two-stage implementation from AND/OR/INV.

Exam phrase to answer: "Can you build XOR in standard CMOS?" Answer: no in one stage; yes with transmission gates.

### 6.3 CMOS metrics

Dynamic power per gate per transition:
$$P_{dyn} = \alpha \cdot C_L \cdot V_{DD}^2 \cdot f$$

Power scales with V^2, which is why every process generation reduces V_DD.

Propagation delay:
$$t_p \approx 0.69 \cdot R_{eq} \cdot C_L$$

Power-delay product PDP = P * t_p. Lower is better.

CMOS advantages you should be able to list: near-zero static power, full rail-to-rail output swing (large noise margins), high input impedance, scalable, ratio-less (output level does not depend on transistor sizing ratios, unlike pseudo-nMOS).

---

## Topic 7 — CMOS Applications: Memory and Amplifiers

### 7.1 Memory cells

**SRAM (Static RAM):** 6 transistors. Two cross-coupled CMOS inverters form a bistable latch, plus two access transistors. State persists as long as power is applied. No refresh. Fast (nanoseconds). Used for CPU caches (L1, L2, L3). Lower density (larger cell). Volatile.

**DRAM (Dynamic RAM):** 1 transistor + 1 capacitor. The bit is stored as charge on the capacitor; the transistor gates access during read and write. Higher density than SRAM. Needs periodic refresh (~every 64 ms) because charge leaks. Slower. Used for main memory. Volatile.

This 6T vs 1T1C contrast is examinable. Drills:
- "Which needs refresh?" DRAM.
- "Which is faster?" SRAM.
- "Which is denser?" DRAM.
- "How many transistors per bit in SRAM?" 6, plus two access transistors in the cell.

### 7.2 Flip-flop signals

phi (clock) synchronises state transitions. S (set) forces output to 1. R (reset) forces output to 0.

### 7.3 CMOS amplifier configurations

Named by the grounded terminal:

| Config | Grounded | Phase | Gain | Input Z | Use |
|---|---|---|---|---|---|
| Common Source | source | 180 deg | high | high | voltage amplifier |
| Common Gate | gate | 0 deg | moderate | low | current buffer |
| Common Drain (source follower) | drain at V_DD | 0 deg | ~1 | high | voltage buffer |

- Common Source is the most common voltage amplifier. Inverts.
- Common Gate is non-inverting, low input Z, useful with low-impedance sources.
- Common Drain gives unity voltage gain, used for impedance transformation, not voltage amplification.

A two-stage voltage amplifier is a differential pair (high input Z, common-mode rejection) followed by a common-source gain stage. Gain-bandwidth product is constant: doubling gain halves bandwidth.

### 7.4 Operational amplifier (intro)

Ideal op-amp:
- Infinite open-loop gain.
- Infinite input impedance (draws no input current).
- Zero output impedance.
- Infinite bandwidth.

Real op-amps approximate these closely enough for most circuits.

CMOS op-amp complexity (from L07):
- Basic: 8 transistors + 1 capacitor.
- Compensated: 8 transistors + 1 cap + 2 resistors (compensation for stability).
- Advanced: 22 transistors + 4 capacitors.

---

## Topic 8 — Op-Amp: Inverting and Non-Inverting

### 8.1 Virtual short circuit principle

With negative feedback, the op-amp drives its output to whatever voltage makes the inverting (-) input match the non-inverting (+) input. This is the **virtual short**: the two inputs sit at nearly the same potential, but no current flows between them. All analysis of these circuits starts from this principle.

The virtual short is an approximation, not a physical connection. It holds only while the op-amp has enough open-loop gain and is not slewing or saturated.

### 8.2 Inverting amplifier

Input through R1 to the (-) terminal. The (+) terminal is grounded. Feedback from output to (-) through R2.

$$\frac{V_{out}}{V_{in}} = -\frac{R_2}{R_1}$$

The negative sign means 180 degree phase shift. Input impedance = R1 (the input sees R1 to virtual ground). Derivation: the (-) terminal is at virtual ground (0 V), so the same current flows through R1 and R2: V_in/R1 = -V_out/R2.

### 8.3 Non-inverting amplifier

Input applied to the (+) terminal. Feedback from output to (-) through a voltage divider R2 (feedback) and R1 (to ground).

$$\frac{V_{out}}{V_{in}} = 1 + \frac{R_2}{R_1}$$

No phase inversion. Input impedance is very high (ideally infinite). The gain is always >= 1; you cannot attenuate with this topology.

Special case R2 = 0: gain = 1. This is the **voltage follower** (unity-gain buffer). Used for impedance matching, not voltage gain.

### 8.4 Comparison

| | Non-inverting | Inverting |
|---|---|---|
| Gain | 1 + R2/R1 | -R2/R1 |
| Phase | 0 deg | 180 deg |
| Input Z | very high (ideal: infinite) | R1 |
| Min gain magnitude | 1 | any (can be < 1) |
| Sign | always positive | negative |

Both gains depend only on the external resistor ratio, independent of the op-amp's internal open-loop gain (as long as that gain is large).

### 8.5 Worked example

Inverting amp, R1 = 10 kOhm, R2 = 100 kOhm, V_in = 50 mV.
Gain = -100/10 = -10. V_out = -500 mV. Current through R1 = 50 mV / 10 kOhm = 5 uA. Current through R2 = 500 mV / 100 kOhm = 5 uA. Same current, confirming the virtual short analysis.

Non-inverting with same resistors, V_in = 50 mV.
Gain = 1 + 10 = 11. V_out = 550 mV, in phase.

Same resistors, different topology, different gain and phase. The non-inverting adds 1.

---

## Topic 9 — Op-Amp Extensions and Memories

### 9.1 Integrator

Replace the feedback resistor R2 with a capacitor C. Z1 = R, Z2 = 1/(j omega C). Gain = -Z2/Z1.

Frequency domain: gain = -1/(j omega R C).
Time domain:
$$V_{out}(t) = -\frac{1}{RC}\int V_{in}(t)\,dt$$

Low-pass behaviour. At high frequencies the cap impedance drops and gain falls. At DC the cap is open and gain goes to infinity in theory; in practice DC offset accumulates and saturates the output.

Practical fix: add a large resistor R_f in parallel with the cap. This limits DC gain to -R_f/R and prevents saturation while preserving integrator behaviour in the band of interest.

Worked example: R = 10 kOhm, C = 100 nF, V_in = 1 V step. RC = 1 ms. V_out(t) = -t/1ms. At t = 5 ms, V_out = -5 V (a linear ramp). Without R_f the output eventually saturates at the negative rail.

### 9.2 Differentiator

Replace the input resistor R1 with a capacitor C. Z1 = 1/(j omega C), Z2 = R.

Frequency domain: gain = -j omega R C.
Time domain:
$$V_{out}(t) = -RC\,\frac{dV_{in}}{dt}$$

High-pass behaviour. At low frequencies the cap blocks the signal; at high frequencies gain rises without bound in theory.

Practical fix: add a small resistor R_s in series with the input cap. Limits high-frequency gain to -R/R_s and tames noise.

Worked example: same R and C, V_in(t) = 2t (ramp at 2 V/s). V_out = -RC * d(2t)/dt = -1e-3 * 2 = -2 mV (constant).

### 9.3 Non-inverting integrator and differentiator

Same impedance substitution applied to the non-inverting topology where gain = 1 + Z2/Z1:
- Non-inverting integrator: gain = 1 + 1/(j omega R C).
- Non-inverting differentiator: gain = 1 + j omega R C.

These keep the frequency-dependent behaviour but remove the phase inversion.

### 9.4 Voltage adder / weighted summer

Multiple input resistors R1, R2, ..., Rn to the (-) terminal. One feedback resistor R_f.

$$V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + \dots + \frac{V_n}{R_n}\right)$$

Each input is weighted by R_f/R_i. Equal resistors give the simple sum:
$$V_{out} = -(V_1 + V_2 + \dots + V_n)$$

The inverting topology always inverts. Do not forget the negative sign.

Worked example: R_f = 10 kOhm, R1 = 10 kOhm, R2 = 20 kOhm, V1 = 1 V, V2 = 2 V.
V_out = -10k * (1/10k + 2/20k) = -10k * (0.1 mA + 0.1 mA) = -2 V.

### 9.5 Voltage follower / buffer

Non-inverting topology with R2 = 0 and R1 removed (open). Gain = 1. V_out = V_in.

Purpose: impedance transformation. High input Z draws negligible current from the source. Low output Z drives a load without voltage drop. It isolates stages and prevents loading. It is not pointless just because the gain is 1.

### 9.6 Digital memory details

SRAM cell organisation: two cross-coupled CMOS inverters + two access transistors. Read and write via word and bit lines. Fast because the cross-coupled inverters actively drive the bit lines.

DRAM organisation: array of cells in rows and columns, accessed via word lines and bit lines. The cell capacitor is tiny (femtofarads), so the bit line voltage change during a read is millivolts.

**Sense amplifiers:** detect and amplify the small voltage difference on the bit lines during a read. Equalisation precharges the bit lines to a reference voltage before the read. The sense amp compares the bit line voltage to the reference and latches the result. Critical for speed and reliability. DRAM needs them more than SRAM because the cell signal is so small.

### 9.7 ROM and Flash

- **ROM:** programmed at manufacture, non-volatile.
- **PROM:** one-time programmable, via fuses.
- **EPROM:** UV-erasable through a quartz window.
- **EEPROM:** electrically erasable, byte-level access.
- **Flash:** block-erasable EEPROM. Dominant non-volatile storage.
  - **NOR flash:** random access, used for code storage (firmware).
  - **NAND flash:** sequential access, higher density, used for SSDs and USB drives.
  - **Floating gate transistor:** trapped charge changes the threshold voltage. This is the storage mechanism.

Flash erases in blocks, EEPROM erases byte by byte. The block structure is what enables Flash's higher density.

---

## Topic 10 — Beyond Silicon and AI for Circuit Design

Low exam weight, but Anagnostopoulos devoted a full lecture to it. Expect at most one short question.

### 10.1 Beyond-silicon devices

**Graphene:** single sheet of carbon atoms in a honeycomb lattice. Graphene transistors have been demonstrated but the zero bandgap makes them hard to switch off.

**Carbon nanotubes (CNTs):** nanoscale hollow tubes of carbon atoms, single-walled or multi-walled. **Chirality** (the internal orientation) determines the bandgap, so different chiralities give different electrical properties. CNT transistors are a candidate to replace silicon at the scaling limit.

**Memristors:** "memory resistor." Resistive switching device. When a voltage threshold is exceeded, resistance drops abruptly to the **Low Resistive State (LRS)**. Applying reverse polarity raises resistance again to the **High Resistive State (HRS)**. The device remembers its resistance state after power is removed. Memristors are candidates for non-volatile memory and neuromorphic computing.

**Future of silicon transistors:** scaling continues toward 3 nm and below. Architectural shifts: FinFET, gate-all-around (GAA), 3D stacking. Limits: quantum tunnelling through the gate, subthreshold swing floor of 60 mV/decade at room temperature, random dopant fluctuation causing V_T variability.

### 10.2 AI for circuit design (topic 9 in the syllabus)

Lecture 10 mentions specific tools. If asked, name one or two, do not write a survey.

- **SnapMagic Copilot** (formerly SnapEDA): generative AI for PCB design. Auto-completes circuits (drops decoupling caps automatically), takes natural language design requests ("non-inverting amplifier with gain 2"), suggests reference designs, optimises BOM by cost, recommends alternatives for low-stock parts.
- **Autodesk AI / AutoCAD:** generative design tools.
- **NVIDIA Metropolis:** visual data + AI for operational efficiency and safety.
- Companies building AI for hardware/PCB: JITX (USA), Celus (Germany), Flux AI, CADY (schematic inspection), Circuit Tree (India), CircuitMind (UK), Zuken (Japan), InstaDeep (UK), Gumstix Geppetto (USA).

---

## Key Formulas You Must Know

Memorise these. They are the backbone of any numerical question.

| Formula | Meaning |
|---|---|
| $n_i = \sqrt{N_c N_v}\exp(-E_g/2kT)$ | Intrinsic carrier concentration |
| $\sigma = q(n\mu_n + p\mu_p)$ | Conductivity |
| $np = n_i^2$ | Mass-action law |
| $V_{bi} = (kT/q)\ln(N_A N_D / n_i^2)$ | Built-in potential |
| $W = \sqrt{2\varepsilon_s V_{bi}(1/N_A + 1/N_D)/q}$ | Depletion width |
| $I = I_s[\exp(qV/nkT) - 1]$ | Diode equation |
| $C_{ox} = \varepsilon_{ox}/t_{ox}$ | MOS oxide capacitance per area |
| $V_{th} = V_{FB} + 2\varphi_F + (1/C_{ox})\sqrt{2\varepsilon_s q N_A (2\varphi_F)}$ | Threshold voltage |
| $I_D = \mu_n C_{ox}(W/L)[(V_{GS}-V_{th})V_{DS} - V_{DS}^2/2]$ | MOSFET triode |
| $I_D = (1/2)\mu_n C_{ox}(W/L)(V_{GS}-V_{th})^2(1+\lambda V_{DS})$ | MOSFET saturation |
| $V_{dsat} = V_{GS} - V_{th}$ | Saturation boundary |
| $V_{avg} = V_{peak}/\pi$ | Half-wave rectifier average |
| $V_{avg} = 2V_{peak}/\pi$ | Full-wave rectifier average |
| $V_{ripple} \approx I_{load}/(f C)$ | Full-wave ripple |
| $V_{out}/V_{in} = -R_2/R_1$ | Inverting amplifier |
| $V_{out}/V_{in} = 1 + R_2/R_1$ | Non-inverting amplifier |
| $V_{out} = -(1/RC)\int V_{in}\,dt$ | Integrator (time domain) |
| $V_{out} = -RC\,dV_{in}/dt$ | Differentiator (time domain) |
| $V_{out} = -R_f\sum_i(V_i/R_i)$ | Weighted summer |
| $P_{dyn} = \alpha C_L V_{DD}^2 f$ | CMOS dynamic power |
| $t_p \approx 0.69 R_{eq} C_L$ | Propagation delay |

Constants to remember: V_T = kT/q ~ 26 mV at 300 K; Si forward drop ~ 0.7 V; Si bandgap 1.12 eV; Ge 0.66 eV; GaAs 1.42 eV; electron mobility in Si ~ 1350 cm^2/Vs; hole mobility ~ 480 cm^2/Vs.

---

## Common Pitfalls and Exam-Style Tricks

1. **Sign of the inverting amp.** The gain is -R2/R1, not R2/R1. Forgetting the negative sign is the single most common error. The sign means 180 degree phase shift.
2. **Non-inverting minimum gain is 1.** You cannot attenuate with a non-inverting amplifier. If you need gain < 1, use the inverting topology with R2 < R1. The "+1" in 1 + R2/R1 comes from the direct path from input to output; do not write R2/R1 by mistake.
3. **Inverting input impedance is R1, not infinity.** This differs from the non-inverting case and matters when the source has non-negligible output Z. A common exam question asks you to compare the two topologies on this point.
4. **Virtual ground is not real ground.** The (-) terminal of the inverting amp sits at ~0 V but cannot sink or source current to ground. All current through R1 flows through R2 to the output.
5. **Integrator DC offset.** Without a parallel resistor, any tiny input offset ramps the output to saturation. The fix is a large R_f in parallel with the cap.
6. **Differentiator noise.** A raw differentiator amplifies high-frequency noise without bound. The fix is a small series resistor R_s.
7. **Zener regulator has two inequalities.** Check both I_Z > I_Z_min (Zener stays in breakdown) and I_Z < I_Z_max (Zener does not burn out). A question that gives you R, V_in range, and R_L is asking you to verify both bounds.
8. **Bridge rectifier has two diode drops.** The conduction path goes through two diodes, so V_avg = 2V_peak/pi - 2(0.7 V). Forgetting the second diode drop is a numerical error.
9. **NAND series nMOS, parallel pMOS.** NOR is the reverse. The pattern is: the function the PDN implements uses series for AND, parallel for OR; the PUN is the dual. Mixing these up is a structural error in any "draw the CMOS gate" question.
10. **AND and OR are not single-stage CMOS gates.** They are NAND/NOR followed by an inverter. If asked to implement AND in static CMOS, the answer is two stages.
11. **XOR is not a single-stage static CMOS gate.** Answer "no" and propose a transmission-gate or multi-stage solution.
12. **SRAM is 6T, DRAM is 1T + 1C.** DRAM needs refresh, SRAM does not. Swapping these two facts is a classic mistake.
13. **Common Source inverts, Common Gate and Common Drain do not.** If you identify an amplifier from a schematic and forget the phase, you lose the follow-up questions.
14. **Common Drain gain is ~1, not 0.** It is a buffer. Calling it "useless" miss is wrong; its purpose is impedance transformation.
15. **Threshold-voltage formula direction.** More n-type doping shifts E_F toward E_c and raises V_th in magnitude. More p-type doping shifts E_F toward E_v.
16. **Breakdown temperature coefficient distinguishes the mechanism.** Avalanche has positive tempco, Zener has negative. If a question gives a Zener with V_BR that drops as T rises, that's quantum tunnelling, not avalanche.

---

## Mock Exam Questions

Treat these as closed-book. Answers in the collapsible block below each question.

### Q1 (MOSFET regions)
An nMOS has V_th = 0.7 V. V_GS = 2.0 V, V_DS = 0.5 V. Which region is it in? Sketch the I_D expression and compute the numerical value given mu_n C_ox (W/L) = 200 uA/V^2.

> **Answer.** V_GS - V_th = 1.3 V. V_DS = 0.5 V < 1.3 V, so the device is in the **triode (linear) region**.
> $$I_D = 200\times10^{-6}\,[(1.3)(0.5) - 0.5^2/2] = 200\times10^{-6}\,(0.65 - 0.125) = 200\times10^{-6}\times 0.525 = 105\,\mu A.$$

### Q2 (Rectifier)
A bridge rectifier is driven by a 12 V RMS, 50 Hz transformer secondary. The load draws 100 mA and the filter capacitor is 1000 uF. Estimate the ripple voltage and the average output voltage (neglect diode drops for the V_avg estimate, then include them).

> **Answer.** V_peak = sqrt(2) * 12 ~ 17.0 V. Full-wave ripple frequency = 100 Hz. V_ripple ~ I_load / (f C) = 0.1 / (100 * 1000e-6) = 1.0 V. Average output without diode drops = 2V_peak/pi ~ 10.8 V. With two diode drops: ~10.8 - 1.4 = 9.4 V.

### Q3 (Op-amp inverting)
Design an inverting amplifier with gain -20 and input impedance 10 kOhm. State R1 and R2.

> **Answer.** Input impedance = R1 = 10 kOhm. Gain = -R2/R1 = -20, so R2 = 200 kOhm.

### Q4 (Op-amp non-inverting)
A non-inverting amplifier has R1 = 2 kOhm and R2 = 18 kOhm. Compute the gain. If V_in = 0.3 V, what is V_out?

> **Answer.** Gain = 1 + R2/R1 = 1 + 9 = 10. V_out = 10 * 0.3 = 3.0 V.

### Q5 (CMOS gate design)
Draw the CMOS implementation of a 2-input NOR gate. State the PDN and PUN topology.

> **Answer.** PDN: 2 nMOS in **parallel** to GND. PUN: 2 pMOS in **series** to V_DD. Output = NOT(A OR B). When either A or B is high, the PDN conducts; the PUN only conducts when both A and B are low.

### Q6 (Zener regulator)
A 5.1 V Zener diode regulates a 12 V supply. The series resistor is 220 Ohm. The load draws 20 mA. The Zener needs at least 5 mA to stay in breakdown and can dissipate max 500 mW. Is the design valid?

> **Answer.** I_R = (12 - 5.1) / 220 = 31.4 mA. I_Z = I_R - I_L = 31.4 - 20 = 11.4 mA. This is above I_Z_min = 5 mA, so the Zener is in breakdown. P_Z = 5.1 * 11.4 mA = 58 mW < 500 mW. Both constraints satisfied, so the design is valid.

### Q7 (Integrator)
An integrator has R = 20 kOhm, C = 50 nF, and a 0.5 V DC input step at t = 0. Plot V_out(t) and state V_out at t = 2 ms. Assume no parallel resistor and ideal op-amp.

> **Answer.** RC = 20e3 * 50e-9 = 1 ms. V_out(t) = -(1/RC) integral Vin dt = -(1/0.001) * 0.5 * t = -500 t (volts, t in seconds). At t = 2 ms, V_out = -1.0 V. The output ramps down linearly at 500 V/s.

### Q8 (Voltage adder)
A weighted summer has R_f = 20 kOhm, R1 = 10 kOhm, R2 = 20 kOhm, R3 = 5 kOhm. V1 = 1 V, V2 = -2 V, V3 = 0.5 V. Compute V_out.

> **Answer.** V_out = -20k * (1/10k + (-2)/20k + 0.5/5k) = -20k * (0.1 - 0.1 + 0.1) mA = -20k * 0.1 mA = -2.0 V. The first two inputs cancel; only V3 contributes net current.

### Q9 (P-N junction)
A silicon p-n junction at 300 K has N_A = 10^17, N_D = 10^16, n_i = 1.5e10. Compute V_bi. (Use V_T = 26 mV.)

> **Answer.** V_bi = V_T ln(N_A N_D / n_i^2) = 0.026 * ln(10^17 * 10^16 / (1.5e10)^2) = 0.026 * ln(10^33 / 2.25e20) = 0.026 * ln(4.44e12) = 0.026 * 29.1 ~ 0.757 V.

### Q10 (Conceptual)
Explain in two sentences why CMOS has near-zero static power dissipation, and why this breaks down at advanced process nodes.

> **Answer.** In steady state, exactly one of the PDN and PUN conducts, so there is no DC path from V_DD to GND and the only current is leakage. At advanced nodes, subthreshold leakage and gate-oxide tunnelling rise enough that "near-zero" becomes only approximate, and static power reappears as a design constraint solved by power gating, multi-V_t libraries, and reverse body bias.

---

## Weak Spot Map

Use this to triage remaining study time. Each row maps a symptom (what you get wrong) to the lecture and vault pages that fix it.

| Symptom (you miss questions on...) | Lecture | Re-read |
|---|---|---|
| Intrinsic vs extrinsic, mass-action law | L1, L2 | [[microelectronics-lecture-1]] [[microelectronics-lecture-2]] [[intrinsic-semiconductor]] [[doping]] |
| Built-in potential or depletion width numerics | L3 | [[microelectronics-lecture-3]] [[p-n-junction]] |
| Distinguishing avalanche vs Zener breakdown | L3 | [[microelectronics-lecture-3]] [[avalanche-breakdown]] |
| Rectifier V_avg, ripple, diode-drop count | L4 | [[microelectronics-lecture-4]] [[half-wave-rectifier]] [[full-wave-rectifier]] [[bridge-rectifier]] |
| Clamper direction (positive vs negative, biased) | L4 | [[microelectronics-lecture-4]] [[clamper-circuit]] |
| Limiter / clipper threshold, window clipper | L4 | [[microelectronics-lecture-4]] [[limiter-circuit]] |
| Zener regulator current limits | L4 | [[microelectronics-lecture-4]] [[diode-applications]] |
| MOS capacitor regimes (accumulation, depletion, inversion) | L5 | [[microelectronics-lecture-5]] [[mos-capacitor]] |
| V_th formula terms and what each means | L5 | [[microelectronics-lecture-5]] [[threshold-voltage]] |
| MOSFET region identification (cutoff/triode/sat) | L5 | [[microelectronics-lecture-5]] [[mosfet-operating-regions]] |
| nMOS vs pMOS substrate, V_th sign, mobility | L5, L6 | [[microelectronics-lecture-5]] [[microelectronics-lecture-6]] |
| PDN/PUN construction rule, series vs parallel | L6 | [[microelectronics-lecture-6]] [[cmos-logic-gates]] |
| XOR construction (transmission gate) | L6 | [[microelectronics-lecture-6]] [[cmos-xor-gate]] |
| CMOS dynamic power and delay formulas | L6 | [[microelectronics-lecture-6]] [[cmos-logic-gates]] |
| SRAM vs DRAM cell, refresh, transistor count | L7, L9 | [[microelectronics-lecture-7]] [[microelectronics-lecture-9]] [[sram-cell]] [[dram-cell]] |
| Amplifier configurations (CS, CG, CD) | L7 | [[microelectronics-lecture-7]] [[common-source-amplifier]] |
| Inverting vs non-inverting gain formula | L8 | [[microelectronics-lecture-8]] |
| Virtual short principle | L8 | [[microelectronics-lecture-8]] [[opamp-basics]] [[negative-feedback]] |
| Integrator / differentiator sign and behaviour | L9 | [[microelectronics-lecture-9]] [[opamp-integrator]] [[opamp-differentiator]] |
| Voltage adder weights and overall sign | L9 | [[microelectronics-lecture-9]] [[weighted-summer]] |
| Flash vs EEPROM, NOR vs NAND flash | L9 | [[microelectronics-lecture-9]] [[flash-memory]] |
| Beyond-silicon devices (graphene, CNT, memristor) | L10 | [[nanoelectronics]] |

---

## Final Readiness Checklist

Before the exam, confirm you can do all of these without notes:

- [ ] State the electronics / microelectronics / nanoelectronics hierarchy and the one-line distinction at each boundary.
- [ ] Derive n, p from N_D, N_A using the mass-action law.
- [ ] Compute V_bi and W from given doping values.
- [ ] Identify forward, reverse, and breakdown regions on a diode I-V curve and say which breakdown mechanism dominates from the tempco.
- [ ] Compute V_avg and V_ripple for half-wave, full-wave, and bridge rectifiers, including the diode-drop count.
- [ ] Determine the clamper direction from diode orientation and the shift from the bias source.
- [ ] Solve a Zener regulator for I_Z and verify both current bounds.
- [ ] Name the three MOSFET regions, give the condition and I_D expression for each, and identify the region from a given (V_GS, V_DS).
- [ ] Write V_th and C_ox formulas from memory.
- [ ] Draw the CMOS inverter, NAND, NOR. State PDN and PUN topology.
- [ ] Explain why XOR needs a transmission gate or multi-stage implementation.
- [ ] List the five op-amp configurations (inverting, non-inverting, integrator, differentiator, adder) with their gain formulas and signs.
- [ ] State and use the virtual short principle to derive inverting and non-inverting gains.
- [ ] Compare SRAM (6T, fast, no refresh, low density) vs DRAM (1T+1C, refresh, high density).
- [ ] Name two beyond-silicon devices and one AI-for-circuit-design tool.

If every box is checked, you are ready. If not, the Weak Spot Map points you to the exact lecture to re-read. Cook.