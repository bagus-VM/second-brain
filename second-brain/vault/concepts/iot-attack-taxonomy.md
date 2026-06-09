---
title: "IoT Attack Taxonomy"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[cia-triad]]", "[[internet-of-things]]"]
---

## One-line Summary
IoT attacks span nine major categories — from scanning and eavesdropping to physical tampering and privilege escalation — each exploiting different layers of the IoT architecture.

## Core Intuition
Attackers don't just hack software. In IoT, they can intercept wireless signals, tamper with physical devices, exploit default passwords, jam communications, or extract firmware. The attack surface is everywhere — digital AND physical.

## Formal Definition / Statement
Common attacks against the IoT (from Lecture 3):

1. **Wired and Wireless Scanning and Mapping** — Network reconnaissance to discover IoT devices, subnets, ports, and protocols
2. **Protocol Attacks** — Exploiting weaknesses in communication protocols (e.g., ZigBee pairing)
3. **Eavesdropping** — Passive interception of communications → loss of confidentiality
4. **Cryptographic Algorithm and Key Management Attacks** — Attacking crypto implementations or key lifecycle (e.g., KRACK)
5. **Spoofing and Masquerading** — Impersonating a legitimate device or user (e.g., Mirai using default passwords)
6. **OS and Application Integrity Attacks** — Compromising software running on devices
7. **Denial of Service (DoS) and Jamming** — Making devices or networks unavailable
8. **Physical Security Attacks** — Tampering with devices, accessing JTAG interfaces
9. **Access Control / Privilege Escalation** — Gaining unauthorized elevated access

## Key Properties / Complexity

### Evaluation Factors for an Attack
- **Attacker Capabilities** — Technical ability, stealth, cost
- **Attack Behaviours and Probabilities** — How conducted, likelihood of success
- **Impact** — Consequences to victim (low individual impacts may aggregate to enormous final impact)
- **Benefits to Attacker** — Motivating gains
- **Detriments to Attacker** — Demotivators (risk, cost, effort)

### The V-A-C Cycle
Vulnerability → Attack → Countermeasure → New Attack → New Countermeasure → …
This is an endless cycle; security is never "done."

## Worked Example
**Scanning Attack (Praetorian, Austin TX):** A drone equipped with a ZigBee protocol scanner flew over a neighbourhood, identifying device beacon requests. This passive reconnaissance mapped all ZigBee devices in the area — a precursor to targeted attacks.

**Physical Attack via JTAG:** An attacker with physical access to an IoT device connects to the JTAG debug interface and reads out memory contents, including sensitive key material, passwords, and configuration data. This bypasses all software-level security.

## Common Pitfalls
- Focusing only on software/network attacks and ignoring physical attack vectors
- Underestimating the impact of "low-severity" attacks when aggregated
- Treating the V-A-C cycle as linear rather than cyclical
- Not considering that attacker motivations differ across IoT domains (nation-state vs. script kiddie vs. insider)

## Connections
- [[mirai-botnet]] — Spoofing/authentication attack case study
- [[krack-attack]] — Cryptographic key management attack case study
- [[zigbee-pairing-vulnerability]] — Protocol attack case study
- [[attack-surface-analysis]] — Miessler's 15 detailed attack surface classes
- [[iot-common-attacks]] — Topic page grouping all attack types
- [[threat-modeling]] — Systematic approach to identifying threats
- [[information-assurance]] — IA properties violated by each attack type

## Open Questions
- How do we prioritize defense against 9+ attack categories with limited resources?
- What new attack categories will emerge with IoT 2.0 (5G, AI, blockchain)?
- How do we share threat intelligence across IoT domains?
