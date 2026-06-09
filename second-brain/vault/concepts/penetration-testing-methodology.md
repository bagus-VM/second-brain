---
title: "Penetration Testing Methodology"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: ["[[threat-modeling]]", "[[attack-surface-analysis]]"]
---

## One-line Summary
IoT penetration testing methodology covers the phases — reconnaissance, enumeration, exploitation, and reporting — applied specifically to embedded devices, wireless protocols, and IoT ecosystems.

## Core Intuition
Threat modeling tells you what could go wrong. Penetration testing proves it. IoT pentesting is different from web or network pentesting because the attack surface spans hardware (JTAG, UART), wireless protocols (BLE, Zigbee), firmware, cloud APIs, and mobile apps — all in one engagement. A comprehensive IoT pentest must cover every component and every interface.

## Formal Definition / Statement
IoT penetration testing follows a structured methodology adapted from traditional pentesting for the unique characteristics of IoT systems:

**Phase 1: Reconnaissance**
- **Passive**: Identify device manufacturer, model, firmware version from public sources (FCC filings, product manuals, Shodan, Censys)
- **Active**: Network scanning (Nmap, Masscan), wireless discovery (Kismet, Wireshark), Bluetooth scanning (hcitool, nRF Connect)
- **Firmware discovery**: Download firmware from vendor website, FTP, or update servers
- **Documentation review**: Analyze FCC internal photos, patent filings, open-source components

**Phase 2: Enumeration and Analysis**
- **Network enumeration**: Port scanning, service identification, banner grabbing
- **Wireless enumeration**: BLE service discovery (GATT), Zigbee network discovery (KillerBee), Wi-Fi probe analysis
- **Firmware analysis**: Extract with binwalk, analyze filesystem, search for hardcoded credentials (strings, regex), identify libraries and versions
- **Hardware enumeration**: Identify ICs on PCB, locate debug interfaces (JTAG, UART, SPI), probe test points
- **Cloud/mobile enumeration**: API endpoint discovery, mobile app reverse engineering (jadx, Frida), cloud service mapping

**Phase 3: Vulnerability Analysis**
- **Static analysis**: Source code review (if available), binary analysis (Ghidra, IDA Pro), firmware emulation (QEMU)
- **Dynamic analysis**: Runtime debugging (GDB with JTAG), network traffic analysis (Wireshark), API fuzzing (AFL, libFuzzer)
- **Configuration review**: Default credentials, open ports, weak TLS, permissive ACLs
- **Known vulnerability mapping**: CVE matching against identified software components

**Phase 4: Exploitation**
- **Network exploitation**: Default credential attacks, protocol exploitation (MQTT without auth, Zigbee key sniffing), MITM attacks
- **Firmware exploitation**: Hardcoded credential extraction, buffer overflow exploitation, firmware modification and reflashing
- **Hardware exploitation**: JTAG/UART shell access, flash memory dumping, side-channel key extraction, fault injection
- **Cloud/mobile exploitation**: API abuse, authentication bypass, insecure data storage, mobile app hooking (Frida)
- **Wireless exploitation**: BLE pairing attacks, Zigbee network key extraction, Wi-Fi deauthentication

**Phase 5: Post-Exploitation**
- **Lateral movement**: Using compromised device as pivot to attack other devices or cloud services
- **Persistence**: Installing backdoors, modifying firmware, adding SSH keys
- **Data exfiltration**: Extracting credentials, sensor data, encryption keys
- **Impact demonstration**: Controlling actuators, modifying sensor readings, disrupting service

**Phase 6: Reporting**
- **Executive summary**: Business impact, risk ratings, key findings
- **Technical findings**: Detailed vulnerability descriptions with proof-of-concept
- **Attack narrative**: Step-by-step walkthrough of successful attack chains
- **Remediation guidance**: Specific, actionable recommendations
- **Evidence**: Screenshots, packet captures, extracted credentials, firmware analysis results

## Key Properties / Complexity

- **IoT pentests require diverse skill sets**: hardware (oscilloscopes, logic analyzers), wireless (SDR, protocol analyzers), software (reverse engineering), cloud (API testing), and mobile (app analysis)
- **Specialized hardware needed**: JTAG debugger (J-Link), SDR (HackRF, RTL-SDR), BLE sniffer (Ubertooth, nRF52), Zigbee sniffer (KillerBee), logic analyzer, oscilloscope
- **Physical access changes everything**: Many IoT vulnerabilities are only exploitable with physical device access
- **Firmware analysis is often the highest-value activity**: A single hardcoded credential can compromise an entire product line
- **Scope must cover the full ecosystem**: device + gateway + cloud + mobile app + communication channels
- **Legal considerations**: Wireless testing may be regulated (FCC, ETSI); some attacks may violate computer fraud laws

## Worked Example

**IoT pentest of a smart thermostat:**
1. **Recon**: Identify model (Nest-like), download firmware from vendor site, FCC filing shows PCB layout
2. **Network scan**: Nmap reveals ports 80 (HTTP), 443 (HTTPS), 8883 (MQTT), 22 (SSH)
3. **Firmware analysis**: binwalk extracts filesystem; `grep -r "password"` finds hardcoded MQTT credentials; `strings` reveals AWS IoT endpoint
4. **Hardware**: UART pins identified on PCB (labeled TX/RX); connect with USB-TTL adapter; bootloader shell access obtained
5. **Wireless**: BLE scan reveals GATT services; pairing uses Just Works (no MITM protection)
6. **Exploitation**: Use hardcoded MQTT credentials to connect to broker; subscribe to `#` wildcard; receive data from ALL thermostats of this model
7. **Impact**: Publish false temperature to any thermostat, control HVAC remotely, infer occupancy from temperature patterns
8. **Reporting**: Critical finding — hardcoded MQTT credentials compromise entire product fleet

## Common Pitfalls

- Not having proper legal authorization (written scope and rules of engagement)
- Testing only the network layer and ignoring firmware, hardware, and wireless
- Not testing the full ecosystem (device alone is insufficient)
- Using automated scanners without manual analysis (IoT vulnerabilities are often logic flaws)
- Not documenting the attack chain (individual vulns may be low severity, but chains are critical)
- Bricking devices during testing without having recovery mechanisms
- Not considering the impact of testing on production IoT systems

## Connections

- [[threat-modeling]] — Threat models define what to test
- [[attack-surface-analysis]] — Miessler's 15 classes as test scope
- [[firmware-security]] — Firmware analysis as a pentest phase
- [[side-channel-attacks]] — Hardware-level exploitation techniques
- [[owasp-iot-top-10]] — Common vulnerability checklist for testing
- [[iot-lecture-2]] — Attack types to replicate during testing
- [[iot-lecture-3]] — Attack surfaces to target during testing

## Open Questions
- How should pentesting adapt to devices with no debug interfaces and secure boot enabled?
- Can automated firmware analysis tools replace manual pentesting for known vulnerability discovery?
- What ethical frameworks should govern IoT security research, especially for medical and industrial devices?
