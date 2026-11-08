---
title: "IoT Attack Surfaces"
tags: [concept, iot-security, attacks, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*Systematic enumeration of all points where an IoT system can be attacked, from physical interfaces to cloud APIs.*

## Core Intuition
You can't defend what you don't know about. An IoT device has dozens of potential entry points — some obvious (the web interface), some subtle (the debug header on the PCB, the Bluetooth pairing protocol, the firmware update server). Attack surface enumeration is the process of systematically listing every possible point of attack so you can prioritize defenses.

## Formal Definition / Statement
Miessler's 15 IoT Attack Surface Classes (DefCon 2023):

**Device-Level:**
1. **Physical interfaces** — JTAG, UART, SPI, I2C, USB ports on the PCB
2. **Device memory** — Flash, EEPROM, RAM contents (firmware, keys, credentials)
3. **Device firmware** — Extractable firmware images, bootloader vulnerabilities
4. **Local data stores** — On-device databases, configuration files, logs
5. **Network services** — Open ports, running services (HTTP, SSH, Telnet)

**Network-Level:**
6. **Network communication** — Unencrypted protocols, weak TLS implementations
7. **Authentication/authorization** — Default credentials, weak access control
8. **Encryption** — Weak algorithms, hardcoded keys, improper certificate validation
9. **Third-party components** — Vulnerable libraries, outdated dependencies

**Cloud/Application-Level:**
10. **Cloud APIs** — Broken authentication, injection, excessive data exposure
11. **Web interface** — XSS, CSRF, insecure session management
12. **Mobile application** — Insecure storage, certificate pinning bypass
13. **Vendor backend infrastructure** — Server vulnerabilities, data breaches

**Ecosystem-Level:**
14. **Ecosystem communications** — Device-to-device, device-to-gateway protocols
15. **Update mechanism** — Unsigned updates, MITM on update channel, no rollback protection

**Additional considerations:**
- **Supply chain** — Counterfeit components, compromised manufacturing
- **Administrative interfaces** — Management consoles, SNMP, proprietary protocols
- **Side channels** — Power consumption, electromagnetic emanation, timing

## Key Properties / Complexity
- Attack surface grows with each connected component and protocol
- Consumer IoT typically has 10-15 distinct attack surfaces
- Industrial IoT may have 20+ including legacy protocol surfaces
- Physical attack surfaces require proximity; network surfaces are remote
- The update mechanism (class 15) is paradoxically both a defence and an attack surface
- Attack surface reduction is often the most cost-effective security measure

## Worked Example
Attack surface assessment of a smart doorbell:

1. **Physical**: USB-C port for power (can inject data?), reset button (factory reset bypasses auth?)
2. **Memory**: eMMC chip on PCB (can be desoldered and read?)
3. **Firmware**: Downloadable from vendor website (binwalk analysis reveals hardcoded AWS keys)
4. **Network**: HTTP server on port 80 (no HTTPS), mDNS broadcasting device type
5. **Auth**: Default pairing code '1234' (unchanged by 80% of users)
6. **Encryption**: TLS 1.0 supported (downgrade attack possible)
7. **Components**: BusyBox 1.22.1 (12 known CVEs)
8. **Cloud API**: REST API accepts any Origin header (CORS misconfiguration)
9. **Web**: Stored XSS in doorbell name field
10. **Mobile**: App stores auth token in plaintext SharedPreferences
11. **Vendor**: Manufacturer's cloud runs outdated Apache Struts
12. **Ecosystem**: Doorbell communicates with smart lock over BLE (no encryption)
13. **Update**: Firmware update over HTTP (no signature verification)

**Result**: 13 distinct attack surfaces identified. Top 3 priorities: firmware signing, TLS upgrade, default password enforcement.

## Common Pitfalls
- **Incomplete enumeration**: It's easy to miss attack surfaces, especially in complex supply chains
- **Static assessment**: Attack surfaces change with firmware updates and new features
- **Prioritization paralysis**: Listing 20 attack surfaces without prioritizing leads to inaction
- **Interconnected risks**: Attack surfaces are often chained (physical access → firmware extraction → credential theft → cloud access)
- **Vendor cooperation**: Full attack surface assessment requires vendor documentation that may not be available

## Connections
- [[iot-common-attacks]] — Attacks that exploit these surfaces
- [[owasp-iot-top-10]] — Top vulnerability categories across these surfaces
- [[penetration-testing-methodology]] — Structured approach to testing attack surfaces
- [[iot-secure-design]] — Designing to minimise attack surfaces
- [[threat-modeling]] — Using attack surfaces as input to threat models
- [[side-channel-attacks]] — Physical attack surfaces requiring specialized analysis

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
