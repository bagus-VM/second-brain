---
title: "IoT Common Attacks"
tags: [concept, iot-security, attacks, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*A taxonomy of the most frequently observed attack types targeting IoT devices, networks, and ecosystems.*

## Core Intuition
Knowing what attacks exist is the first step to defending against them. IoT devices face a unique combination of attacks: some inherited from traditional IT (SQL injection, XSS), some adapted for constrained environments (jamming, side-channel), and some unique to IoT (firmware extraction via physical access, supply chain tampering). Understanding the attack landscape helps prioritize defenses.

## Formal Definition / Statement
Common IoT attacks organized by target layer:

**Device/Physical Layer:**
- Firmware extraction via JTAG/UART/SPI flash dumping
- Side-channel attacks (power analysis, electromagnetic emanation)
- Fault injection (voltage glitching, laser fault injection)
- Physical tampering and reverse engineering
- Bus sniffing (I2C, SPI, UART interception)

**Network/Communication Layer:**
- Man-in-the-middle (MITM) on unencrypted protocols
- Replay attacks on authentication sequences
- Jamming and interference (DoS at the physical layer)
- Protocol-specific attacks (MQTT unauthorized publish, CoAP amplification)
- Zigbee key sniffing during insecure join
- BLE eavesdropping on weak pairing modes

**Application/Cloud Layer:**
- Credential stuffing (default/weak passwords)
- API abuse (broken authentication, excessive data exposure)
- SQL/NoSQL injection in cloud backends
- Insecure direct object references (IDOR)
- Firmware update manipulation (MITM on OTA)

**Supply Chain:**
- Counterfeit components with backdoors
- Malicious firmware modifications during transit
- Compromised third-party libraries
- Hardware trojans in chip fabrication

**Ecosystem:**
- Lateral movement from compromised IoT to enterprise network
- Botnet recruitment (Mirai, Mozi, Ripple20)
- Data exfiltration through covert channels
- Ransomware targeting IoT devices (e.g., bricking smart locks)

## Key Properties / Complexity
- Mirai botnet (2016) remains the template for large-scale IoT attacks
- Default credentials are the #1 attack vector for consumer IoT
- Physical attacks require proximity; network attacks can be remote
- Many IoT protocols (MQTT, CoAP) were designed for efficiency, not security
- Supply chain attacks are the hardest to detect and prevent
- Lateral movement from IoT to IT networks is an increasing concern

## Worked Example
Attack chain against a smart home camera:
1. **Reconnaissance**: Shodan scan finds the camera's web interface exposed on port 80
2. **Credential attack**: Try default credentials (admin:admin) — success
3. **Firmware extraction**: Download firmware update from manufacturer website, extract with binwalk
4. **Vulnerability analysis**: Find buffer overflow in RTSP handler (CVE-2023-XXXX)
5. **Exploitation**: Send crafted RTSP payload, gain root shell
6. **Lateral movement**: Camera is on the same network as the home NAS — pivot to access stored files
7. **Botnet enrollment**: Install Mirai variant, camera becomes part of DDoS botnet
8. **Persistence**: Modify firmware to survive factory reset

## Common Pitfalls
- **Attack taxonomy overlap**: Categories overlap (MITM is both network and application layer)
- **Evolving landscape**: New attack vectors emerge as IoT adoption grows
- **Incomplete coverage**: Any taxonomy will miss novel attack techniques
- **Context matters**: The same vulnerability has different severity in consumer vs industrial IoT
- **Defence vs offence**: Knowing attacks doesn't automatically tell you how to defend

## Connections
- [[iot-attack-taxonomy]] — Broader taxonomy including Miessler's 15 attack surface classes
- [[owasp-iot-top-10]] — Vulnerability-focused complement to attack-focused taxonomy
- [[mirai-botnet]] — Case study of the most impactful IoT botnet
- [[side-channel-attacks]] — Detailed treatment of physical-layer attacks
- [[penetration-testing-methodology]] — Structured approach to discovering these attacks
- [[iot-secure-design]] — Defensive counterpart: how to design systems resistant to these attacks

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
