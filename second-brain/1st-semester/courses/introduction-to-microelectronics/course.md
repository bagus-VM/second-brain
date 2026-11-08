---
title: "Introduction to Microelectronics"
tags: [course, microelectronics, electronics, semester-1]
university: "University of Passau"
professor: "Dr. Nikolaos Athanasios Anagnostopoulos"
semester: "SS 2026"
exam_date: "2026-08-06"
textbook: "Sedra, Smith, Carusone & Gaudet, Microelectronic Circuits, OUP 2019"
status: current
last_updated: 2026-06-02
---

## One-line Summary
A foundational course covering semiconductor physics, diodes, MOS transistors, and their applications in modern electronic circuits.

## Course Information

- **Professor:** Dr. Nikolaos Athanasios Anagnostopoulos
- **University:** University of Passau
- **Semester:** SS 2026
- **Exam Date:** August 06, 2026
- **Textbook:** Sedra, Smith, Carusone & Gaudet, *Microelectronic Circuits*, Oxford University Press, 2019

## Course Topic Roadmap (10 Topics)

1. **Basic concepts of microelectronics** — examples of electronic systems, electronics vs. microelectronics vs. nanoelectronics
2. **Physics of microelectronics** — charge carriers, pn junction, conductors, semiconductors, [[silicon]]
3. **Diodes and their applications** — [[diode]], [[rectifier]], [[clamper-circuit]], [[limiter-circuit]]
4. **MOS transistors** — [[pmtransistor]], [[nmos-transistor]], [[mosfet]], CMOS, principles of operation
5. **CMOS amplifiers** — amplifier design using complementary MOS pairs
6. **Operational amplifiers** — noninverting, inverting, integrator, differentiator, voltage adder
7. **Design principles of simple computer components** — memory cells, registers, logical gates
8. **Basic digital circuits and practical applications**
9. **Circuit design/correction/testing using AI**
10. **Microelectronics beyond silicon** — [[nanoelectronics]] and post-CMOS technologies

## Lecture Index

### Lecture 1: Basic Concepts of Electronics & Semiconductors
- [[electronics]] vs. [[microelectronics]] vs. [[nanoelectronics]]
- [[semiconductor]] physics: [[silicon]], [[bandgap]], [[valence-band]], [[conduction-band]]
- [[intrinsic-semiconductor]] vs. extrinsic ([[doping]])
- [[p-n-junction]] introduction

### Lecture 2: Reverse Breakdown, Zener Diodes & Rectifier Applications
- [[zener-breakdown]] and [[avalanche-breakdown]]
- [[zener-diode]] operation
- [[half-wave-rectifier]], [[full-wave-rectifier]], [[bridge-rectifier]]

### Lecture 3: Clampers, Limiters & Zener Diode Applications
- [[clamper-circuit]] (positive and negative, with/without reference voltage)
- [[limiter-circuit]] (series, parallel, dual-diode)
- Zener diode overvoltage protection

### Lecture 4: Transistors & MOS Transistor Fundamentals
- [[transistor]] concept (three-terminal devices)
- [[mosfet]] structure: [[mos-capacitor]], [[threshold-voltage]]
- [[nmos-transistor]] and [[pmtransistor]] basics
- [[mosfet-operating-regions]]: cutoff, linear, saturation

### Lecture 5: nMOS & pMOS Operating Characteristics
- Detailed [[mosfet-operating-regions]] analysis
- I-V characteristics of [[nmos-transistor]] and [[pmtransistor]]

## Key Topics (Linked)

| Topic | Key Concepts |
|---|---|
| [[semiconductor-physics]] | [[silicon]], [[bandgap]], [[valence-band]], [[conduction-band]] |
| [[doping-and-extrinsic-semiconductors]] | [[n-type-semiconductor]], [[p-type-semiconductor]], [[ion-implantation]], [[thermal-diffusion]] |
| [[p-n-junction-overview]] | [[depletion-region]], [[diode]], forward/reverse bias |
| [[diode-applications]] | [[rectifier]], [[clamper-circuit]], [[limiter-circuit]], [[zener-diode]] |
| [[mos-transistors]] | [[mosfet]], [[mos-capacitor]], [[threshold-voltage]], [[nmos-transistor]], [[pmtransistor]] |

## Textbook Reference

Sedra, Smith, Carusone & Gaudet: *Microelectronic Circuits*, Oxford University Press, 2019.

## Connections

This course builds the foundation for:
- [[digital-circuit-design]] — using MOS transistors as switches
- [[vlsi-design]] — large-scale integration of microelectronic circuits
- [[nanoelectronics]] — post-CMOS technologies beyond silicon

## Open Questions

- How does CMOS scaling affect threshold voltage and power dissipation?
- What are the practical limits of silicon-based microelectronics?
- How do post-CMOS technologies (e.g., tunnel FETs, spintronics) compare?
