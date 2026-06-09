---
title: "IoT Security: Security Solutions for the Internet of Things"
tags: [course, iot-security, semester-1]
semester: "SS 2026"
university: "University of Passau"
professor: "Dr. Nikolaos Athanasios Anagnostopoulos"
exam_date: "2026-08-05"
textbook: "Russel & Van Duren, Practical Internet of Things Security, 2nd ed., Packt 2019"
status: current
last_updated: 2026-06-02
---

## Course Overview

This course covers security solutions for the Internet of Things (IoT), spanning from foundational concepts and threat modelling to hardware security primitives and comprehensive attack surface analysis. Taught by Dr. Nikolaos Athanasios Anagnostopoulos at the University of Passau.

## Lectures

### [[Lecture 1 — Introduction to IoT Security]]
- Definition of IoT (IBM, Wikipedia, Anagnostopoulos definitions)
- IoT components: [[sensors]], [[actuators]], processing segment
- IoT segments: Space, Maritime, Agriculture, Smart Cities, Energy, Industry
- [[iot-connectivity-protocols|Connectivity solutions]]: Wi-Fi, LoRaWAN, Bluetooth, Ethernet, CAN, ZigBee
- Scale: ~17B devices today, ~30B by 2030
- [[iot-2.0|IoT 2.0]]: 5G/6G, AI/ML, edge computing, Industry 4.0, blockchain
- Security vs. cost balance; "acceptable level of security"
- Systems of systems complexity

### [[Lecture 2 — IoT Applications and Vulnerability Introduction]]
- Application scenarios: smart home, emergency response, Internet of Lights, LiFi, Internet of Sounds
- Vulnerability-Attack-Countermeasure cycle
- Attacker model definition
- Penetration testing introduction

### [[Lecture 3 — Information Assurance, Attacks, and Secure Development]]
- [[cia-triad|CIA Triad]] + extensions: [[authentication]], [[non-repudiation]], [[resilience-iot|resilience]], safety
- Common attacks: scanning, protocol attacks, eavesdropping, crypto attacks, spoofing, DoS, physical attacks, privilege escalation
- Case studies: [[mirai-botnet|Mirai]], [[krack-attack|KRACK]], [[zigbee-pairing-vulnerability|ZigBee pairing]]
- [[threat-modeling|Threat modeling]] process
- [[security-by-design|Security by Design]]
- Hardware security: [[physical-unclonable-functions|PUFs]], [[trusted-platform-module|TPM]], security co-processors
- [[secure-development-lifecycle|SDLC models]]: Waterfall, Spiral, Agile

### [[Lecture 4 — DevOps, Security Practices, and Secure Design Goals]]
- [[devops-security|DevOps]] methodology and principles
- Required properties: Security ([[attack-tree|attack tree]]), Safety ([[fault-tree|fault tree]]), Resilience (anticipate/withstand/recover/evolve)
- Best practices: lifecycle enforcement, software auth, device network auth, [[iot-firewalling|IoT firewalling]], authenticated updates
- Secure design goals: mitigate automated attacks, protect C&I, hardware protection, availability, resilience, compliance
- [[operational-security-lifecycle|Operational security life cycle]]: Define → Implement → Operate → Dispose
- Compliance: US IoT Cybersecurity Improvement Act, ENISA, DHS, FDA

### [[Lecture 5 — Attack Surface Analysis]]
- Daniel Miessler's 15 [[attack-surface-analysis|attack surface classes]] (DefCon 2023)
- Access control, [[device-memory-attack-surface|device memory]], [[physical-interface-attack-surface|physical interfaces]], web interfaces, [[firmware-security|firmware]], network services, admin interfaces, local data storage, cloud interfaces, third-party APIs, [[ota-updates|update mechanism]], mobile apps, vendor APIs, [[ecosystem-communications-security|ecosystem communications]], network traffic

## Exam Information

- **Date:** August 05, 2026
- **Format:** TBD
- **Key topics:** CIA triad extensions, attack case studies (Mirai, KRACK, ZigBee), Miessler's 15 attack surface classes, operational security life cycle, secure design goals, SDLC models, threat modelling

## Key Concepts

- [[internet-of-things|Internet of Things]]
- [[information-assurance|Information Assurance]]
- [[iot-attack-taxonomy|IoT Attack Taxonomy]]
- [[threat-modeling|Threat Modeling]]
- [[security-by-design|Security by Design]]
- [[attack-surface-analysis|Attack Surface Analysis]]
- [[resilience-iot|Resilience in IoT]]
- [[iot-compliance-frameworks|Compliance Frameworks]]
