---
title: "IoT Security Exam Prep"
tags: [study, exam-prep, iot-security, semester-1]
course: "IoT Security"
exam_date: "2026-08-05"
status: current
last_updated: 2026-07-27
source_count: 14
---

# IoT Security Exam Prep

Dr. Nikolaos Athanasios Anagnostopoulos. University of Passau. Exam: 5 August 2026. Written, 60 to 90 minutes.

Read the source pages in the vault, do not rely on this sheet alone. This condenses what is likely to appear.

## Exam format

Three question types:

1. Definitions of core concepts. Own words fine, must be valid and precise.
2. Use-case scenarios. Given smart car / home / agriculture / healthcare. Identify assets, threats, attacks, countermeasures. Map to CIA triad. Comment on cost and expertise.
3. Explain how a security mechanism works. Examples: digital signatures, PUFs, TPM, OTA updates, lightweight crypto.

Sources: [[iot-security-exam-format]], [[courses/iot-security]].

## Topic coverage map

| # | Topic | Vault coverage | Likelihood |
|---|-------|----------------|------------|
| L1 | IoT definition, components, segments, connectivity, scale, IoT 2.0 | Strong | High for definitions |
| L2 | Applications, V-A-C cycle, attacker model, pen test intro | Strong | Medium |
| L3 | CIA triad + extensions, 9 attack categories, Mirai/KRACK/ZigBee, threat modelling, SDLC | Strong | Very high |
| L4 | DevOps, attack tree / fault tree, secure design goals, op-sec lifecycle, compliance | Strong | Very high |
| L5 | Miessler 15 attack surface classes (DefCon 2023) | Strong | High |
| L6 | Cryptography fundamentals, symmetric vs asymmetric, hashing, MAC, signatures, RNG, PUFs, TPM, ASCON | Strong | Very high |
| L7 | Identity lifecycle, bootstrapping, PKI, OAuth 2.0, privacy by design, GDPR | Good | Medium |
| L8 | Compliance monitoring, governmental attacks, IoT 2.0 architecture, defence-in-depth | Good | Medium |
| L9 | DRAM-PUF protocol (Anagnostopoulos paper) | Good | Medium, likely a mechanism question |

Gaps: weak recall of the 15 attack surface class names. Weak on the steps of the DRAM-PUF authentication protocol. Gaps on Privacy by Design 8 principles. The L9 protocol is the professor's own research. Assume it appears.

## Definitions block

These are the terms most likely to appear in question type 1. One line each. Say it back without notes.

| Term | Definition |
|------|------------|
| Internet of Things | Network of physical devices with sensors, software, and connectivity that exchange, process, and act on data, potentially without human intervention (Anagnostopoulos definition). |
| Sensor | Resource-constrained device that gathers data from the environment. |
| Actuator | Resource-constrained or single-task device that performs actions on commands from the processing segment. |
| Processing segment | High-end devices (servers) that decide actions based on data and rules. |
| IoT segments | Space, Maritime, Agriculture and Aquaculture, Smart Cities, Energy, Industry and Manufacturing. |
| IoT 2.0 | IoT integrated with 5G/6G, AI/ML, edge computing, Industry 4.0/5.0, blockchain, post-CMOS. |
| Confidentiality | Sensitive information stays secret and protected from disclosure. |
| Integrity | Information is not modified, accidentally or on purpose, without being detected. |
| Availability | Information and capabilities are available when needed. |
| Authentication | Source of data is from a known identity or endpoint. |
| Non-repudiation | An entity cannot later deny having performed an action. |
| Resilience | State awareness and accepted level of operational normalcy under disturbance. Four phases: Anticipate, Withstand, Recover, Evolve. |
| Safety | Not in threat of undergoing or causing hurt, injury, or loss. |
| Security by Design | Security integrated from the start, not bolted on. |
| Attack tree | Diagram modeling how an attacker reaches a goal, branching into sub-goals and methods. |
| Fault tree | Diagram modeling how system failures lead to a hazardous state. |
| Hazard analysis | Systematic identification of potential hazards and their causes. |
| Waterfall | Linear sequential SDLC, no iterations. Royce extended it with feedback. |
| Spiral | Iterative based on feedback. Issues found late force restart. |
| Agile | No fixed plan. Principles: individuals over processes, working software over docs, customer collaboration over contracts, responding to change over a plan. |
| DevOps | Blends development, QA, and operations. Rapid small-component deployment with continuous feedback. |
| PUF | Physical Unclonable Function. Hardware primitive exploiting manufacturing variations to make unique, unclonable device IDs or keys. |
| TPM | Trusted Platform Module. Dedicated tamper-resistant cryptoprocessor for key storage and crypto ops, measured boot via PCRs. |
| TRNG | True Random-Number Generator. Entropy from physical process (thermal noise, DRAM decay, rowhammer). Needed for keys and nonces. |
| MAC | Message Authentication Code. Symmetric tag giving integrity and data-origin authentication, no non-repudiation. |
| Digital signature | Asymmetric primitive. KeyGen, Sign, Verify. Gives integrity, authentication, and non-repudiation. |
| ASCON | NIST lightweight cryptography winner (Feb 2023). AEAD plus hash. 320-bit permutation, 128-bit key and tag. For constrained IoT. |
| OTA update | Over-The-Air firmware update. Must be authenticated and signed. |
| Mirai | 2016 botnet that exploited default passwords on IP cameras and routers, used for massive DDoS against DNS. |
| KRACK | Key Reinstallation Attack on WPA2 (Vanhoef, 2017). Forces reuse of a cryptographic key. A protocol-level flaw. |
| ZigBee pairing vuln | Protocol designed for easy setup lacked secure config. Pairing procedures leak network keys to sniffers. |

## CIA triad mapping

The examiner will give you a scenario, you must identify two each of assets, threats, attacks, and countermeasures, then map to CIA. Memorise this skeleton.

Example scenario: smart home with smart lock, camera, voice assistant, cloud backend.

| Asset | Threat | Attack | Countermeasure | CIA property |
|-------|--------|--------|----------------|--------------|
| Door lock credentials | Unauthorized unlock | Default password replay (Mirai-style) | Force password change on first boot, rate limit | Confidentiality, Availability |
| Firmware image | Tampered firmware | MITM on OTA update server | Signed firmware with ECDSA, verify in TPM | Integrity |
| Video stream | Eavesdropping | Sniffing unencrypted RTSP | TLS in transit, AES at rest | Confidentiality |
| Lock availability | Lock bricked | DoS via cloud outage | Local fallback, gateway caching | Availability |
| Voice data | Privacy leak | Cloud raw-audio retention | On-device wake-word DSP, no raw audio to cloud | Confidentiality (privacy) |
| Lock motor | Unauthorized actuation | Replay of old open command | Nonce + MAC on each command | Integrity, Authentication |

Example scenario: industrial IoT, PLC controlling water valves.

| Asset | Threat | Attack | Countermeasure | CIA property |
|-------|--------|--------|----------------|--------------|
| PLC firmware | Malicious modification | Insider with USB | Secure boot, signed firmware | Integrity |
| Valve control channel | Spoofing | Modbus replay with no auth | Cryptographic auth, segmentation | Authentication |
| Sensor readings | Tampering | MITM on fieldbus | Integrity checks, MAC | Integrity |
| PLC availability | Process halt | DoS on controller | Redundancy, rate limit | Availability |
| Safety interlocks | Override | Privilege escalation | Least privilege, hardware e-stop | Safety |

Mention cost and expertise on every countermeasure. Examiners check whether you can reason about business tradeoffs, not just recite buzzwords. Example: a TPM per door lock is too expensive for a 20 euro consumer device. A signed firmware update is cheap (asymmetric signature, public key baked in) and should be standard.

## Attack case studies

These three come from Lecture 3. Expect at least one to appear, either as fact recall or as the basis for a scenario question.

### Mirai botnet (2016)

- Vector: default passwords on IP cameras and home routers. The most common ones were admin/admin, root/xc3511, and similar. Mirai's scanner targeted ports 23 and 2323 Telnet.
- Scale: hundreds of thousands to millions of enslaved devices.
- Impact: 2016 DDoS against Dyn DNS brought down Twitter, Reddit, Netflix, GitHub for hours.
- Cryptographic key reuse: Mirai itself was a clean attack. No fancy crypto. Default credentials plus scale equals a botnet.
- Countermeasures: force password change on first boot, unique per-device credentials, disable Telnet, network segmentation, egress filtering.

### KRACK (Vanhoef 2017)

- Against WPA2, a ratified standard. The flaw is in the 4-way handshake when the client installs the pairwise transient key.
- Mechanism: the attacker forces nonce reuse by replaying message 3 of the 4-way handshake, resetting the key counter. The client encrypts multiple frames with the same key and nonce.
- Result: for AES-CCMP this lets the attacker decrypt frames and forge a few. For TKIP it gets worse. HTTPS on top still protects, but many IoT clients do not enforce HTTPS.
- Protocol-level flaw, not an implementation bug. Fix required patching every client device.
- Countermeasures: key reinstallation protections, disable TKIP, patch clients, prefer WPA3.

### ZigBee pairing vulnerability

- ZigBee is a low-power wireless protocols for smart home sensors. Easy setup was prioritised over secure config.
- During join, a joining device receives the network key. Some implementations transmit it in the clear or with a weak link-key wrapper that can be force-reset.
- Attack path: force a ZigBee device to factory reset (physical tamper or power cycling), capture the insecure rejoin, extract the network key, then control the whole ZigBee network.
- Countermeasures: install-only mode for pairing, pre-configured link keys, restrict rejoin windows, physical tamper detection on devices, segment ZigBee networks from critical systems.

## The 15 attack surface classes (Miessler, DefCon 2023)

Know the names cold and give one line on each. This is a likely definition list or scenario input.

1. Access control: authentication, session management, trust between components, secure enrolment and decommissioning, lost-credential handling.
2. Device memory: clear-text usernames, passwords, third-party credentials, and keys readable from flash or RAM.
3. Physical interfaces: JTAG, UART, SPI, USB. Firmware extraction, CLI exposure, reset to insecure state.
4. Device web interface: SQLi, XSS, username enumeration, weak passwords, no lockout, known default credentials.
5. Device firmware: hardcoded passwords, sensitive URL disclosure, hardcoded crypto keys.
6. Device network services: information disclosure, network CLI exposure, injection, DoS.
7. Administrative web interface: same web vulnerabilities but on the admin panel, often with elevated trust.
8. Local data storage: unencrypted data, encrypted data with recoverable keys, no integrity checks.
9. Cloud web interface: same web issues, cloud-side, plus broken OAuth or tenant isolation.
10. Third-party back-end APIs: unencrypted PII, leaked device metadata or location.
11. Update mechanism: updates sent unencrypted, not signed, update source writable by attacker.
12. Mobile application: trusted implicitly by device and cloud, hardcoded credentials, insecure local storage, no transport encryption.
13. Vendor back-end API: inherent trust of cloud or mobile, weak auth, weak access control, injection.
14. Ecosystem communications: abuse of health checks, heartbeats, ecosystem commands, decommissioning, update pushes.
15. Network traffic: LAN, LAN-to-internet, non-standard protocols, short-range Bluetooth, ZigBee, NFC.

## SDLC models and DevOps

| Model | Characteristic | Pitfall |
|-------|----------------|---------|
| Waterfall (Royce) | Linear, sequential. No iterations unless extended. | Late discovery is expensive. Requires restart. |
| Spiral | Iterative with feedback loops. | Still mostly one-way. Late issues force restart. |
| Agile (Manifesto) | Iterative, no fixed plan. Individuals and interactions over processes; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan. | Chaotic without supervision and deadline discipline. |
| DevOps | Blends development, QA, operations. Small components, rapid feedback. | Requires continuous collaboration and vigilance or it breaks down. |

DevOps principles, in order: automate, blend operations and QA and development, instrument and provide continuous feedback, be transparent, be vigilant.

## Secure design goals (Lecture 4)

The six goals to recite in order, from the slide list:

1. Mitigate automated attack risks. Resist unsupervised, scripted attacks.
2. Secure points of integration. Subsystem integration is designed with security in mind, not assumed.
3. Protect confidentiality and integrity. Apply cryptography to data at rest and in motion. Enable data lifecycle visibility. Implement secure OTA.
4. Design for safety. IoT must not cause harm. Hazard and fault tree analysis.
5. Hardware protection. Add secure hardware components. Anti-tamper that reports or reacts to physical compromise.
6. Design for availability. Cloud availability, guard against equipment failure, load balancing.
7. Design for resilience. Jamming protection, redundancy, gateway caching, clustering, rate limiting, congestion control, flexible policy, integrity-protected logging fed to cloud.
8. Design for compliance. US IoT Cybersecurity Improvement Act, ENISA, DHS, FDA.

Note: "Design for safety" and "Design for availability" are sometimes combined with resilience. Know the slide split as the professor intends it.

## Resilience phases

From Lecture 3 and Lecture 4:

- Anticipate: proactively identify and prepare for potential threats.
- Withstand: maintain operations during a threat event.
- Recover: restore normal operations after a disruption.
- Evolve: learn and improve from incidents.

## Operational security lifecycle (Lecture 4)

Four phases. Examiners like the names and one-line justification.

1. Define: define system security policies and system roles.
2. Implement / Integrate: configure gateways and network security, bootstrap and securely configure devices, set up threat intelligence and vulnerability monitoring, set up deception mechanisms, train stakeholders.
3. Operate and Maintain: manage assets, manage credentials, manage firmware and patches, monitor the system, run penetration tests, manage incidents.
4. Dispose: secure disposal, data purging, inventory removal, data archival or records maintenance.

Best security practices from the same slide block: lifecycle enforcement; software authorization and authentication; device network authentication on boot; IoT firewalling (needed because devices are resource-constrained); authenticated updates that consume minimal bandwidth.

## Cryptography fundamentals (Lecture 6)

### Security services to mechanism map

| Service | Mechanism |
|---------|-----------|
| Confidentiality | Encryption (symmetric or asymmetric) |
| Integrity | Digital signature or MAC |
| Authentication | Digital signature or MAC |
| Non-repudiation | Digital signature (asymmetric only) |

Know why MAC cannot give non-repudiation: both sender and receiver share the key, so either could have produced the tag. The signer can deny it.

### Symmetric vs asymmetric

| Property | Symmetric | Asymmetric |
|----------|-----------|------------|
| Keys | One shared secret | Public plus private pair |
| Speed | Fast, MB/s to GB/s | Slow, about 1000 times slower |
| Key distribution | Hard, needs out-of-band | Easy, publish public key |
| Non-repudiation | No | Yes |
| Examples | AES, ChaCha20, 3DES, Blowfish | RSA, ECC, ECDSA, Ed25519 |
| Typical use | Bulk encryption | Key exchange, signatures, certificates |

### Hashing properties

A cryptographic hash H maps arbitrary input to a fixed n-bit digest with pre-image resistance, second pre-image resistance, and collision resistance. Examples: SHA-256, SHA-3, BLAKE2. MD5 and SHA-1 are broken, known collisions.

### Digital signature steps

KeyGen produces (pk, sk). Sign produces signature sigma on message with sk. Verify accepts or rejects sigma against pk and message. Security goal: EUF-CMA, existential unforgeability under chosen-message attack.

Examples: RSA with PKCS#1 or PSS padding, DSA, ECDSA, Ed25519.

### Hash vs MAC vs signature

Hash: one-way, no key, integrity check only.
MAC: keyed, symmetric, integrity and data-origin authentication, no non-repudiation. HMAC-SHA256 and AES-CMAC are the common ones.
Signature: keyed, asymmetric, integrity, authentication, and non-repudiation.

### RNGs

PRNG: deterministic from a seed. Fine for non-secret randomness like salts and padding. Never for keys.
TRNG: physical source. Thermal noise, radioactive decay, DRAM start-up values, rowhammer. Output is unpredictable but biased. Needs entropy distillation. Von Neumann debiasing eats half the bits but gives uniform output.

## Hardware security primitives

### PUF classes

- SRAM PUF: power-up state of SRAM cells.
- DRAM PUF variants: start-up values, decay-based, data remanence, rowhammer disturbance, reduced read-write latency.
- Flash PUF: program disturbance in unaccessed cells.

All satisfy instance-unique, persistent over time, hard to imitate. The trick is the primitive lives in a component the device already has, no extra silicon. PUFs need a fuzzy extractor or helper-data algorithm because responses are noisy.

### TPM

Dedicated tamper-resistant cryptoprocessor. Stores keys, performs crypto in isolation, implements measured boot via platform configuration registers. Communicates over I2C, SPI, or LPC. TPM 2.0 supports RSA, ECC, SHA-256, HMAC. Costs money, area, and power. Found in gateways, high-end IoT, and laptops. Rarely in coin-cell sensors.

### Security co-processor and crypto library

Security co-processor offloads crypto operations from a constrained main CPU. Cryptographic library is software-only, the lightest option, no tamper resistance.

## ASCON (Lecture 6)

The NIST Lightweight Cryptography standardisation winner, announced February 2023. Built on a 320-bit permutation with a 64-bit S-box. Properties:

- Authenticated encryption plus hashing in one lightweight permutation.
- 128-bit key, 128-bit tag, recommended security level.
- Ciphertext length equals plaintext length, minimal overhead.
- Single-pass, online, nonce-based, inverse-free.
- No table lookups and no integer additions, so timing-resistant.
- S-box is masking-friendly for side-channel resistance.

Family: ASCON-128 and ASCON-128a (AEAD), ASCON-80pq (post-quantum), ASCON-Hash, ASCON-XOF.

The Passau group has published on ASCON. Assume an ASCON-specific question.

### Worked example: signed firmware update

Manufacturer generates ECDSA key pair. Device stores the public key in its TPM or certificate at provisioning. Manufacturer signs the SHA-256 digest of the firmware with its private key. Device receives firmware plus signature. Device recomputes the digest and verifies with the stored public key. Accept or reject. This combines hashing for efficiency, asymmetric crypto for the signature, and a TPM for trust anchor storage.

### Worked example: ASCON-128 AEAD

Inputs: 128-bit key, 128-bit nonce, associated data AD, plaintext. Output: ciphertext plus 128-bit tag. Ciphertext length equals plaintext length. Receiver recomputes the tag over ciphertext plus AD and accepts only if it matches. Any bit flip in ciphertext, key, nonce, or AD invalidates the tag.

Pitfall: reusing a nonce with the same key in any AEAD construction leaks the authentication key or the plaintext. The most common real-world crypto bug in IoT firmware.

## Identity lifecycle and privacy (Lecture 7)

Know the structure, do not memorise every credential type.

### Identity attributes

Manufacturer, device type, serial number, deployment date, location.

### Bootstrapping approaches

Factory provisioning (most secure, needs trusted factory). Pre-shared key bootstrap (device ships with a symmetric key, exchanges it for long-term credentials). Certificate-based bootstrap (device ships with a manufacturer certificate, pulls operational credentials from a registration authority). Out-of-band channel (QR code, NFC tap, physical button).

### Account lifecycle

Provisioned, Active, Monitored, Updated, Suspended, Deactivated or Deleted. The deactivation step must be irreversible and verifiable.

### Authorization frameworks

- X.509: PKI standard. CA signature binds public key to identity. Chain of trust: root CA, intermediate CA, end-entity. CRLs and OCSP for revocation.
- IEEE 1609.2 for vehicular networks. Implicit certificates, smaller than X.509. Pseudonymous for driver privacy.
- OAuth 2.0 (RFC 6749): delegated authorization. Four roles: resource owner, client, authorization server, resource server. The Device Authorization Grant (RFC 8628) is the one to know for IoT, it is the "enter this code on your phone" flow for input-constrained devices.

### IAM infrastructure

- 802.1X: port-based network access control. Supplicant, authenticator, authentication server (RADIUS). EAP methods include EAP-TLS.
- PKI for IoT: hierarchical root CA offline, intermediate CAs issue at scale. Automated enrollment protocols: EST (RFC 7030) and CMP (RFC 4210).
- Trusted storage: keys in tamper-resistant hardware, not software-only.
- Revocation: CRLs (bandwidth-heavy at scale), OCSP (privacy concern, server learns who connects to whom), OCSP stapling, short-lived certificates (avoid revocation by short expiry of hours or days).

### Privacy by Design, 8 principles (Cavoukian, extended)

1. Proactive not reactive.
2. Privacy as default setting.
3. Privacy embedded into design.
4. Full functionality, positive-sum not zero-sum.
5. End-to-end security, full lifecycle protection.
6. Visibility and transparency.
7. Respect for user privacy.
8. Privacy throughout the organization and supply chain.

Principle 8 is the extension added in the lecture. The seven original are Cavoukian's.

### Privacy-preserving techniques

Pseudonymity, anonymity, short-lived certificates, batch certificates, location obscurer proxy (LOP).

### Privacy Impact Assessment

Five steps under GDPR: Describe the data flows, Identify privacy risks, Assess likelihood and severity, Mitigate, Document and review periodically. Mandatory for high-risk processing.

## Compliance and IoT 2.0 (Lecture 8)

### Compliance monitoring program

Executive oversight (policies, training, testing). Internal monitoring is a cycle: install or update sensors, automated flaw search, collect results, triage, fix bugs, progress reports, system design updates, system implementation.

### Periodic risk assessments

Black-box testing with no internal knowledge: physical security, update process, interface analysis, wireless, configuration, mobile, cloud.

White-box assessments with full knowledge: staff interviews, reverse engineering, hardware analysis, code analysis, design and config reviews, attack tree and fault tree analysis.

Fuzz testing: power sequences, protocol fields, headers, data validation.

### Governmental-level attacks

Performed by state or tech-giant agencies with vast resources, time, and effort. Practically impossible to avoid completely. Resilience and prevention together are required. Defence-in-depth is mandatory. Assume breach, design for recovery.

### Defence in depth

Multiple layers: physical, device (secure boot, firmware signing), network (encryption, segmentation), application (input validation), cloud (access control), data (encryption at rest and transit), operational (patching, monitoring, incident response). Attacker must breach every layer.

### IoT 2.0

A concept connecting IoT to 5G or 6G, AI and ML, edge computing, Industry 4.0 and 5.0, blockchain, post-CMOS technologies, with a focus on user-friendliness, sustainability, interoperability, scalability, and security. Cites Zhou et al. 2021 in IEEE Access.

Architecture evolves from conventional device-to-gateway-to-cloud toward layered architectures with edge or fog computing, AI layers, and blockchain for trust.

## DRAM-PUF authentication protocol (Lecture 9)

This is the professor's own research. Expect a mechanism question.

### Setup

PUF primitive: DRAM retention decay as a physical unclonable function. Cells lose charge at a rate that depends on temperature and the cell's physical characteristics. The rate is unique per chip.

### Enrollment phase (once, in a secure environment)

Server records, for one device: challenges c, responses R, decay times t, temperatures T. Server computes helper data HD and key k and stores them server-side. The physical hardware is then delivered to the IoT device.

### Authentication phase (repeatable)

1. IoT sends an auth request to the server.
2. Server picks a challenge c and decay time t and sends them to the device.
3. Device powers DRAM, waits decay time t at temperature T, reads PUF response R prime equals PUF sub t of c. Device reports T to the server.
4. Server looks up the helper data HD for the (c, t, T) triple and sends HD to the device.
5. Device computes key k equals HD XOR R prime. Uses k to encrypt measurement data m.
6. Device sends ciphertext to the server.
7. Server derives the same k from HD and the stored values for (c, t, T), decrypts m, recovers the measurement.

Key properties:
- No stored key on the device. Key is re-derived from physics and helper data each session.
- Replay-resistant. Each session the server picks a fresh (t, c).
- Temperature-dependent. T is required; HD is temperature-specific.
- Helper data HD is not secret. Without the physical PUF response R prime, an attacker cannot reconstruct k.
- Enrollment is the trust anchor. Compromise enrollment and the whole protocol fails.

Pitfalls students hit:
- Forgetting that T is an input and changes the helper data selection.
- Thinking HD is secret. It is not, it is key reconciliation data.
- Confusing this with a generic PUF. This protocol is specific to DRAM retention PUFs, not SRAM start-up or arbiter PUFs.
- Believing the key is transmitted. It is derived on both sides, never crosses the wire.

## Compliance frameworks

| Framework | Jurisdiction | Scope |
|-----------|--------------|-------|
| US IoT Cybersecurity Improvement Act of 2020 | US federal | Minimum security standards for IoT used by federal agencies. Vulnerability, patch, and configuration management. |
| ENISA Baseline Security Recommendations | EU | Baseline security recommendations for IoT, covers secure development, deployment, operation. |
| US DHS Guiding Principles for Secure IoT | US | Principles for securing IoT across critical infrastructure. |
| US FDA Guidance on IoT Medical Devices | US | Pre-market and post-market cybersecurity requirements for medical IoT. |

Common requirements across all: secure development, vulnerability disclosure and management, authentication and access control, encryption at rest and in transit, patch and update mechanisms, logging and monitoring.

## Mock exam questions

### Type 1: Definitions

1. Define the Internet of Things. Give two examples of segments where IoT security has direct safety implications.
   - Answer: An IoT is a network of physical devices with sensors, software, and connectivity that exchange, process, and act on data, potentially without human intervention. Segments with safety impact: healthcare IoMT (insulin pump dosing, pacemakers) and industrial IoT (PLC-controlled valves in a water plant).
2. Define non-repudiation and give one cryptographic mechanism that provides it.
   - Non-repudiation is the property that an entity cannot later deny having performed an action. Only an asymmetric digital signature provides it, because only the holder of the private key could have produced the signature.
3. Define a PUF and a TRNG. State the one-sentence difference.
   - A PUF is a hardware primitive exploiting manufacturing variations to produce unique per-device IDs or keys. A TRNG is a random-number generator sourced from a physical process. Difference: a PUF is keyed by identity, a TRNG produces fresh randomness.
4. Define ASCON and state two reasons it fits constrained IoT devices.
   - ASCON is the NIST Lightweight Cryptography standardization winner (2023), providing AEAD and hashing with one 320-bit permutation. It is small state and simple permutation, no table lookups, ciphertext length equals plaintext length, and single-pass online operation.
5. Define resilience. Name the four phases.
   - Resilience is the property of maintaining state awareness and an accepted level of operational normalcy under disturbance. The phases are Anticipate, Withstand, Recover, Evolve.

### Type 2: Use-case scenarios

1. A smart agriculture deployment has soil sensors, a cellular gateway, and a cloud analytics backend. Identify two assets, two threats, two attacks, two countermeasures. Map to CIA. Comment on cost.
   - Assets: sensor firmware; gateway credential store.
   - Threats: physical tampering of sensors (they sit unsupervised in a field); gateway account takeover.
   - Attacks: JTAG readout of sensor flash to extract the gateway pre-shared key; credential stuffing the cloud admin panel.
   - Countermeasures: fuse JTAG at manufacturing and use a memory-based PUF for per-device keys (low cost on constrained hardware); enforce MFA plus rate limit on the cloud admin login (low cost, pure software).
   - CIA mapping: tampering hits Integrity; credential stuffing hits Confidentiality and Availability of cloud; PUF-based keys provide Authentication; MFA provides Authentication and Non-repudiation via audit logs.
   - Cost note: a PUF sits on hardware the sensor already has, near-zero BOM cost. MFA is near-zero. The expensive options are TPMs and HSMs, which the sensors do not need.

2. A healthcare IoT device is an implantable insulin pump with a paired controller app. Identify two assets, two threats, two attacks, two countermeasures. Map to CIA. Comment on cost and on safety.
   - Assets: dose commands; patient monitoring data.
   - Threats: unauthorized dosing; privacy leak of patient data.
   - Attacks: replay of an old increase-dose command on the wireless link; unencrypted backend API leak of patient records.
   - Countermeasures: per-command nonce plus MAC, signed commands, short session keys via ECDH; TLS for backend, encrypted storage, short-lived access tokens via OAuth 2.0 device grant.
   - CIA mapping: dose command replay hits Integrity and Safety; privacy leak hits Confidentiality; MAC and signatures provide Integrity, Authentication; TLS provides Confidentiality.
   - Cost note: a TPM in an implant is expensive (power, board area) and often impractical. Lightweight cryptography like ASCON is the realistic choice. Safety override is mandatory, a hardware emergency stop or a hard floor on the dose.

3. A smart grid substation with IoT sensors reports to a regional control centre. Identify two assets, two threats, two attacks, two countermeasures.
   - Assets: sensor telemetry streams; breaker control channel.
   - Threats: false telemetry feeding wrong control decisions; DoS on the control channel.
   - Attacks: spoofed sensor data via MITM on an unencrypted protocol; DDoS against the regional gateway.
   - Countermeasures: MAC on every telemetry packet, signed control messages, firewalling and segmentation of SCADA from IT; redundancy on the gateway, rate limiting, fail-safe defaults.
   - CIA mapping: telemetry tampering hits Integrity and Safety; DoS hits Availability; MAC hits Integrity and Authentication; segmentation hits Availability.
   - Cost: medium. Substations already accept compute. Lightweight crypto plus segmentation is well within budget. TPM on the gateway is reasonable.

### Type 3: Mechanism explanations

1. Explain how a digital signature provides integrity, authentication, and non-repudiation. State why a MAC does not.
   - KeyGen produces a public-private pair. Sign with the private key. Verify with the public key. Inthasgrity comes from the binding between message and signature. Authentication comes from only-keyholdership of the private key. Non-repudiation comes from this same asymmetry: no one else could have produced the signature, so the signer cannot deny it. A MAC uses a shared symmetric key, so either party could have produced the tag. The signer can deny. No non-repudiation.

2. Explain the DRAM-PUF authentication protocol, step by step. Say where the key lives.
   - Two phases. Enrollment (once, secure): server records challenges c, responses R, decay times t, temperatures T, computes helper data HD and key k, ships thephysical PUF to the device. Authentication (repeatable): server sends (t, c) to the device, device reads PUF response R prime at temperature T and reports T, server replies with HD, device computes k equals HD XOR R prime and encrypts measurement data, server re-derives k from stored (HD, c, t, T) and decrypts. The key is not stored anywhere on the device. It is re-derived from physics plus helper data each session. HD is not secret. Each session uses a fresh (t, c) so it resists replay. Enrollment is the trust anchor.

3. Explain how ASCON provides authenticated encryption and why it fits IoT.
   - Inputs: 128-bit key, 128-bit nonce, associated data AD, plaintext. The permutation produces ciphertext plus 128-bit tag. Ciphertext length equals plaintext length. The receiver recomputes the tag over ciphertext plus AD and accepts only on match. Security rests on the permutation and the keyed finalisation. It fits IoT because the state is small (320 bits), there are no table lookups, no integer additions, it is single-pass and online, inverse-free, and the S-box is masking-friendly for side-channel resistance. The pitfall: nonce reuse with the same key is catastrophic, it leaks the plaintext and the authentication key.

4. Explain the role of a TPM in IoT and why it is not universal.
   - A TPM is a tamper-resistant cryptoprocessor. It stores keys in hardware, performs signing and encryption in isolation from the main CPU, and implements measured boot via platform configuration registers. It is the strongest practical root of trust for keys. It is not universal because it costs money, board area, and power. Coin-cell sensors and microcontrollers cannot afford it. It is realistic in gateways, high-end IoT, and PCs. Lower-tier devices substitute memory-based PUFs, secure elements if affordable, or signed firmware with a public key baked into ROM. The TPM cannot stop an attacker with physical access from reflashing the firmware, it is one layer, not a silver bullet.

5. Explain the operational security lifecycle. Why is the Dispose phase the one most often skipped?
   - Four phases. Define: policies and roles. Implement-integrate: gateways, network security, device bootstrapping, threat intelligence, deception, training. Operate-and-maintain: asset and credential management, patching, monitoring, pen-testing, incident response. Dispose: secure physical disposal, data purging, inventory removal, archived records. Dispose is skipped because it happens after the product's commercial life, after the engineering team is gone, and is invisible to current user experience. Skipping itleaks keys and credentials from discarded devices, which are then mined for attack. The Mirai default-password vector works partly because decommissioned devices went back on sale with their credentials intact.

## Weak spots

Topic areas where recall is weakest, sorted by likelihood of appearance times weakness.

1. The 15 attack surface class names. You can describe them but not list them in order. Drill this list.
2. The DRAM-PUF protocol step order. You remembered "something about decay and helper data." Walk through the seven steps until it is automatic.
3. Privacy by Design 8 principles. You can name 4. The full list matters because the 8th is the professor's extension.
4. Secure design goals. You have 4 of 8 and cannot put them in slide order.
5. ZigBee protocol details. "Easy pairing leaks keys" is enough for a definition, not enough for a mechanism question.
6. ASCON specifics. You know it is lightweight. You blank on the permutation size, the nonce length, the bit sizes, and the modes.
7. White-box vs black-box testing scope in compliance monitoring. You mix them up.
8. The deviations of SDLC models. Waterfall is not linear-period, Royce's version has feedback. Spiral still forces restarts on late issues. Agile is efficient only with supervision.

## Study priorities for the remaining days

1. Drill the 15 attack surface class names and one line each until recall is fast and stable. Five minutes per day, every day.
2. Walk through the DRAM-PUF protocol out loud. Speak the seven steps. Speak properties, pitfalls, and one attack on the enrollment phase. You will get a mechanism question on this.
3. Recite the secure design goals and the operational security lifecycle phases in slide order until they are automatic. Write them out without looking.
4. Memorize the asymmetric-symmetric, hash-MAC-signature relations, and the four services plus their mechanisms. Expand one mock firmware-signing example out loud.
5. Know the three case studies cold. For each: vector, mechanism, impact, countermeasure, one number. For Mirai: 2016, Dyn DNS, millions of devices, Telnet ports 23 and 2323. For KRACK: Vanhoef 2017, WPA2 4-way handshake, nonce reuse. For ZigBee: factory reset plus rejoin, network key in clear.
6. Take the mock questions above. Answer without notes. Then read the answer. Fix only what was wrong. Re-test the wrong ones tomorrow.
7. One pass over the Privacy by Design 8 principles and the GDPR DPIA steps. They are short, drillable.

End of prep. This is not a half-measure.