---
title: "Industrial IoT Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-device-fundamentals]]", "[[network-security-fundamentals]]"]
---
## One-line Summary
Industrial IoT (IIoT) security covers SCADA systems, PLCs, and operational technology networks where cyber attacks can cause physical destruction, environmental disasters, and loss of life — governed by IEC 62443.

## Core Intuition
Industrial IoT is the convergence of IT (information technology) and OT (operational technology). OT networks were historically air-gapped — physically isolated from the internet. Now, Industry 4.0 connects them to enterprise IT and cloud platforms for monitoring, analytics, and remote management. This creates the "IT/OT convergence" problem: OT protocols (Modbus, DNP3, OPC-UA) designed decades ago with no security features are now exposed to the internet. A cyber attack on industrial IoT doesn't just steal data — it can cause explosions, contaminate water supplies, or shut down power grids.

## Formal Definition / Statement
Industrial IoT encompasses connected devices in manufacturing, energy, water, oil & gas, and transportation sectors:

**Key Systems:**
- **SCADA (Supervisory Control and Data Acquisition)**: Centralized monitoring and control of geographically distributed assets
- **PLCs (Programmable Logic Controllers)**: Industrial computers controlling physical processes (motors, valves, pumps)
- **RTUs (Remote Terminal Units)**: Field devices connecting sensors/actuators to SCADA
- **HMIs (Human-Machine Interfaces)**: Operator panels for process visualization and control
- **DCS (Distributed Control Systems)**: Process control systems for continuous manufacturing (chemical plants, refineries)

**Industrial Protocols:**
- **Modbus (1979)**: Serial/TCP protocol. No authentication, no encryption, no integrity checking. Commands are cleartext. Still widely deployed.
- **DNP3 (Distributed Network Protocol)**: Used in utilities. Supports Secure Authentication (SA) v5 but often not enabled.
- **OPC-UA (Open Platform Communications Unified Architecture)**: Modern protocol with built-in security (X.509 certificates, encryption, authentication). Becoming the standard.
- **EtherNet/IP**: Industrial Ethernet using CIP (Common Industrial Protocol). Security depends on network segmentation.
- **PROFINET**: Siemens industrial Ethernet. Security via network segmentation and access control.

**IEC 62443 Framework:**
- Defines security levels (SL 1-4) for industrial automation
- SL 1: Protection against casual violation
- SL 2: Protection against intentional violation using simple means
- SL 3: Protection against sophisticated attack with moderate resources
- SL 4: Protection against state-sponsored attack
- Roles: Component manufacturer, system integrator, asset owner
- Zones and conduits model for network segmentation

## Key Properties / Complexity

- **Availability is paramount**: Industrial processes cannot tolerate downtime for security patches. A refinery shutdown for patching costs millions per day.
- **Legacy systems**: PLCs and RTUs have 15-30 year lifespans, often running firmware that cannot be updated
- **Safety-critical**: Security failures have physical consequences (Stuxnet destroyed centrifuges, Triton targeted safety systems)
- **Deterministic timing**: Industrial processes require real-time response; security overhead must not introduce latency
- **IT/OT convergence risk**: Connecting OT to IT exposes industrial systems to commodity malware and internet-based attacks
- **Protocol insecurity**: Modbus and DNP3 were designed for serial communication with implicit trust — no auth, no encryption
- **Physical access**: Industrial sites often have limited physical security for field devices (PLCs in open cabinets)
- **Skilled workforce shortage**: OT security requires both cybersecurity and industrial process expertise

## Worked Example

**Stuxnet-style attack on a water treatment plant:**
1. Attacker gains access to corporate IT network via phishing
2. Pivots to OT network through poorly segmented IT/OT boundary
3. Discovers Modbus-connected PLC controlling chemical dosing
4. Modbus has no authentication — attacker sends commands directly to PLC
5. Increases chlorine dosing to dangerous levels
6. HMI shows normal readings (attacker modified HMI feedback)
7. Physical consequence: contaminated water supply

**Mitigation with IEC 62443:**
1. Network segmentation: OT network in separate zone with firewall-controlled conduit
2. PLC firmware integrity verified by secure boot
3. Modbus commands restricted by application-layer firewall (only allow expected function codes from known hosts)
4. HMI and SCADA on separate network segments
5. Intrusion detection system monitoring OT network for anomalous Modbus traffic
6. Physical access controls on PLC cabinets

## Common Pitfalls

- Connecting SCADA/PLC directly to the internet without firewall or VPN
- Using Modbus/DNP3 without security extensions on IP-connected networks
- Not segmenting IT and OT networks (flat network from office to factory floor)
- Ignoring physical security of field devices (PLCs, RTUs)
- Assuming "security through obscurity" (proprietary protocols are not secure just because they're undocumented)
- Not having an OT-specific incident response plan
- Patching OT systems during production (causes downtime) and therefore never patching

## Connections

- [[healthcare-iot-security]] — Both are safety-critical IoT domains
- [[iec-62443]] — Deep dive into the industrial security standard
- [[smart-city-infrastructure]] — Critical infrastructure overlaps
- [[network-security-fundamentals]] — Network segmentation, firewalls, IDS
- [[zero-trust-architecture]] — Applying zero-trust to OT networks
- [[threat-modeling]] — Industrial-specific threat modelling
- [[risk-assessment-frameworks]] — IEC 62443 risk assessment
- [[iot-firewalling]] — Industrial network segmentation and traffic filtering
- [[iot-lecture-1]] — Industrial IoT in the application domain overview
- [[mirai-botnet]] — Botnets can target internet-exposed industrial devices

## Open Questions
- How can industrial systems be patched without production downtime?
- Will OPC-UA fully replace insecure legacy protocols (Modbus, DNP3) in existing installations?
- How should liability be assigned when a cyber attack causes physical harm through industrial IoT?
