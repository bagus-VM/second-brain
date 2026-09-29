---
title: "IoT Common Attacks"
tags: [topic, iot-security, semester-1]
course: "IoT Security"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-lecture-1]]", "[[networking-fundamentals]]"]
---

## One-line Summary
A comprehensive taxonomy of attack types targeting IoT systems, organized into nine categories spanning reconnaissance, protocol exploitation, cryptographic weaknesses, spoofing, integrity violations, denial-of-service, physical tampering, and access control bypass.

## Core Intuition
IoT attacks exploit the same fundamental weaknesses as traditional IT attacks — unpatched software, weak credentials, cleartext protocols — but with amplified impact because IoT devices bridge the digital and physical worlds. A compromised thermostat is not just a data breach; it can disable heating in winter. The attack taxonomy below shows that attackers exploit every layer: from radio signals to cloud APIs, from physical board access to supply chain infiltration.

## Formal Definition / Statement

### 1. Scanning and Mapping Attacks
Active reconnaissance to discover IoT devices and enumerate services.

- **Network Scanning**: Tools like Shodan, Censys, and Nmap identify exposed IoT devices on the internet. Shodan indexes banners, default credentials, and service fingerprints. Masscan can sweep entire IP ranges in minutes.
- **Service Enumeration**: Probing open ports ([[mqtt-security]] on 1883, [[coap-security]] on 5683, HTTP on 80/443) to identify running services and their versions.
- **Fingerprinting**: Identifying device models, firmware versions, and OS through banner grabbing, TCP/IP stack behavior (p0f), or HTTP headers.
- **Wireless Discovery**: Scanning for [[zigbee-security-model]], Z-Wave, [[ble-security]], or LoRaWAN networks using SDR (Software Defined Radio) tools or dedicated hardware like KillerBee for Zigbee.

**Impact**: Provides attackers with a target map. All subsequent attacks depend on reconnaissance data.

### 2. Protocol Attacks
Exploiting weaknesses in IoT communication protocols.

- **MQTT Exploitation**: Open MQTT brokers without authentication allow subscription to all topics (# wildcard), leaking sensor data and enabling command injection. Malicious publishing can inject false data or trigger actuator commands.
- **CoAP Exploitation**: CoAP's UDP-based design enables IP spoofing and amplification attacks. Weak or absent DTLS configurations expose plaintext communications.
- **Zigbee Attacks**: Zigbee's trust center model has known weaknesses. The Zigbee 1.2 standard uses a well-known trust center link key (ZigBeeAlliance09) that can be sniffed to decrypt network traffic. Key enumeration and replay attacks are possible.
- **BLE Exploitation**: BLE pairing can be intercepted (KNOB attack, downgrade to weak key length). GATT profile manipulation can alter device behavior. BLE MAC address tracking enables physical surveillance.
- **Thread/Matter Attacks**: Newer protocols with stronger security, but implementation bugs in early stacks (e.g., OpenThread) may allow routing attacks or commissioning abuse.

**Impact**: Traffic interception, data manipulation, unauthorized device control, lateral movement within mesh networks.

### 3. Eavesdropping and Traffic Interception
Passive monitoring of IoT communications.

- **Packet Sniffing**: Capturing unencrypted MQTT, HTTP, or CoAP traffic using Wireshark or tcpdump. Many legacy IoT devices transmit sensor readings, credentials, and commands in cleartext.
- **Wireless Sniffing**: Using SDR hardware (HackRF, RTL-SDR) or protocol-specific tools (Ubertooth for BLE, KillerBee for Zigbee) to capture over-the-air transmissions.
- **Side-Channel Traffic Analysis**: Even encrypted traffic can reveal information through packet size, timing, and frequency patterns (e.g., inferring occupancy from smart meter data patterns).
- **Man-in-the-Middle (MitM)**: Intercepting and optionally modifying traffic between device and cloud by ARP spoofing, DNS hijacking, or rogue access points. Particularly effective against devices that don't validate TLS certificates.

**Impact**: Privacy violations, credential theft, data manipulation, surveillance.

### 4. Cryptographic and Key Management Attacks
Targeting weaknesses in cryptographic implementations.

- **Weak/Default Keys**: Devices shipped with default encryption keys or hardcoded credentials. Some Zigbee devices use the well-known trust center link key.
- **Key Extraction**: Side-channel attacks (power analysis, electromagnetic analysis) to extract keys from constrained devices. Fault injection to bypass crypto operations.
- **Algorithm Downgrade**: Forcing devices to use weaker cipher suites (e.g., BLE KNOB attack reduces encryption key length to 1 byte).
- **Certificate Mismanagement**: Self-signed certificates, expired certificates, or failure to validate certificate chains. Devices that accept any TLS certificate are trivially MitM'd.
- **Insufficient Entropy**: Constrained devices with poor random number generators produce predictable keys, nonces, or IVs, enabling replay and cryptographic attacks.

**Impact**: Complete compromise of confidentiality and integrity guarantees. Enables all other attack types once crypto is broken.

### 5. Spoofing and Masquerading Attacks
Impersonating legitimate devices, users, or services.

- **Device Impersonation**: Cloning MAC addresses, Zigbee IEEE addresses, or BLE addresses to impersonate trusted devices. Without mutual authentication, a rogue sensor can feed false data.
- **ARP/DNS Spoofing**: Redirecting traffic within local networks to attacker-controlled endpoints.
- **Rogue Access Points**: Setting up fake Wi-Fi access points with the same SSID as legitimate networks to intercept IoT device connections.
- **Replay Attacks**: Capturing and retransmitting valid authentication tokens, commands, or protocol messages. Effective against protocols without sequence numbers or timestamps.
- **Sybil Attacks**: In mesh networks, a single attacker creates multiple fake identities to influence routing, voting, or consensus mechanisms.

**Impact**: Unauthorized access, data injection, command injection, network disruption.

### 6. OS and Application Integrity Attacks
Compromising firmware, operating systems, or application software.

- **Firmware Extraction and Modification**: Dumping flash memory via JTAG/SPI/UART interfaces, modifying firmware to insert backdoors, and reflashing. Tools like binwalk enable firmware analysis and repacking.
- **Buffer Overflow / Memory Corruption**: Exploiting vulnerabilities in embedded C code (stack overflows, heap overflows, use-after-free) to achieve code execution on the device.
- **Rootkit Installation**: Persistent malware that survives reboots by modifying bootloaders or kernel modules. Difficult to detect without external attestation.
- **Supply Chain Attacks**: Compromised firmware or libraries injected during manufacturing or distribution. Hardware trojans embedded in chips during fabrication.
- **Insecure Deserialization**: Parsing untrusted data (JSON, XML, CBOR) without validation, enabling code execution through crafted payloads.

**Impact**: Persistent device compromise, botnet enrollment, data exfiltration, physical damage via actuator manipulation.

### 7. Denial-of-Service and Jamming Attacks
Rendering devices or networks unavailable.

- **Volumetric DoS**: Flooding devices with traffic (SYN floods, UDP floods). Constrained devices have minimal capacity to handle even modest traffic volumes.
- **Protocol-Specific DoS**: MQTT subscription flooding, CoAP amplification (small request, large response), Zigbee battery exhaustion attacks.
- **Wireless Jamming**: Transmitting interference on the same frequency band. Constant jamming, random jamming, reactive jamming (transmit only when legitimate traffic detected), and intelligent jamming targeting specific protocols.
- **Resource Exhaustion**: Draining device batteries through repeated wake-up triggers (BLE advertisements, Zigbee rejoin requests) or forcing expensive cryptographic operations.
- **Application-Layer DoS**: Sending malformed but syntactically valid requests that trigger expensive parsing or processing (XML bombs, algorithmic complexity attacks).
- **Sleep Deprivation Attacks**: Preventing battery-powered devices from entering low-power states by maintaining active communication, rapidly depleting batteries.

**Impact**: Service unavailability, safety hazards (critical monitoring disabled), financial loss, battery replacement costs.

### 8. Physical Attacks
Direct access to hardware components.

- **Tampering**: Opening device enclosures, modifying circuits, attaching probes. Many IoT devices lack tamper-evident seals or tamper-resistant enclosures.
- **Side-Channel Analysis**: Measuring power consumption, electromagnetic emissions, or timing to extract cryptographic keys or internal state.
- **Fault Injection**: Glitching voltage or clock signals to skip security checks, cause misexecution of instructions, or bypass authentication. Laser fault injection for more precise targeting.
- **Hardware Reverse Engineering**: Decapsulating ICs, using electron microscopy to read chip layouts, identifying custom logic or hidden debug interfaces.
- **Debug Interface Exploitation**: Accessing JTAG, SWD, UART, SPI, or I2C interfaces to dump memory, inject code, or bypass boot security. These interfaces are often left enabled in production devices.

**Impact**: Complete device compromise, key extraction, firmware extraction/cloning, physical safety hazards.

### 9. Access Control Attacks
Bypassing authentication and authorization mechanisms.

- **Default Credential Exploitation**: Using factory-default usernames and passwords (admin/admin, root/root). The [[mirai-botnet]] famously leveraged a table of 61 default credential pairs to compromise hundreds of thousands of devices.
- **Brute Force / Credential Stuffing**: Automated password guessing against devices with exposed login interfaces. Many IoT devices lack account lockout mechanisms.
- **Broken Access Control**: Web interfaces with insecure direct object references (IDOR), missing authorization checks on API endpoints, or privilege escalation through parameter manipulation.
- **Token/Session Hijacking**: Stealing session cookies or API tokens through XSS in web interfaces, network sniffing, or predictable token generation.
- **Insufficient Authentication**: Devices that rely solely on MAC address filtering, shared secrets, or no authentication at all. Single-factor authentication for administrative interfaces.

**Impact**: Unauthorized device control, data access, configuration changes, lateral movement.

## Key Properties / Complexity

- **Attack Chain Complexity**: Most real-world IoT compromises chain multiple attack types (reconnaissance → exploit → persist → pivot).
- **Automation Potential**: Tools like Mirai demonstrate that IoT attacks can be fully automated and scaled to millions of devices.
- **Cross-Layer Exploitation**: Effective attacks often span multiple OSI layers simultaneously (physical jamming + application-layer credential stuffing).
- **Asymmetric Effort**: Defenders must secure every attack surface; attackers need only find one weakness.
- **Physical-Digital Bridge**: IoT is unique in that cyber attacks can cause physical consequences (overheating, mechanical damage, safety hazards).

## Connections

### Case Studies
- [[mirai-botnet]] — The canonical IoT botnet exploiting default credentials and known vulnerabilities across millions of devices
- [[krack-attack]] — WPA2 key reinstallation attack (CVE-2017-13077-13088) affecting virtually all Wi-Fi-enabled IoT devices
- [[zigbee-pairing-vulnerability]] — Exploitation of Zigbee's trust center link key during device pairing

### Attack Surface Mapping
- [[iot-lecture-3]] — Miessler's 15 attack surface classes that these attacks target
- [[attack-surface-analysis]] — Systematic methodology for identifying and prioritizing attack surfaces

### Defense Strategies
- [[iot-lecture-4]] — Design principles that mitigate the attacks described above
- [[security-by-design]] — Proactive security integration from the earliest design stages
- [[iot-lecture-5]] — Hardware-level protections (TPMs, PUFs) that resist physical and cryptographic attacks

### Protocol Security
- [[mqtt-security]] — Hardening MQTT deployments against protocol attacks
- [[coap-security]] — DTLS configuration and CoAP-specific attack mitigations
- [[zigbee-security-model]] — Zigbee trust center, key hierarchy, and known weaknesses
- [[ble-security]] — BLE pairing modes, known vulnerabilities, and mitigations

### Foundational References
- [[iot-lecture-1]] — Overview connecting all IoT security domains
- [[information-assurance]] — CIA triad and how each attack violates assurance properties
- [[network-security-fundamentals]] — Classical network attacks that also apply to IoT

## Open Questions
- How can automated vulnerability discovery be applied to the long tail of proprietary IoT firmware?
- What lightweight intrusion detection approaches work on devices with <64KB RAM?
- How do we establish reliable device identity in networks with billions of heterogeneous devices?
- Can formal verification of embedded firmware scale to real-world IoT products?
- How should incident response differ when IoT compromises cause physical harm?
