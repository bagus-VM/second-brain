# IoT Security Lectures — Comprehensive Extraction

Source: University of Passau, Dr. Nikolaos Athanasios Anagnostopoulos
Textbook: Russel & Van Duren: "Practical Internet of Things Security", 2nd edition, Packt Publishing, 2019

---

## LECTURE 1: Introduction to IoT Security

### Title
IoT Security: Security Solutions for the Internet of Things (Introduction)

### Main Topics
- Definition of the Internet of Things (IoT)
- Components and segments of the IoT
- Inherent diversity of IoT ecosystems
- Urgent need for security in the IoT

### Key Concepts with Definitions

1. **Internet of Things (IoT)** — A network of physical devices, vehicles, appliances, and other objects embedded with sensors, software, and network connectivity, allowing them to collect and share data (IBM definition). More broadly: devices that connect and exchange data over the Internet or other communications networks (Wikipedia). Most comprehensive: a network where data are exchanged, processed, and utilised by sensors, actuators, and other electronic devices, potentially leading to actions without direct human intervention, supervision, or control (Anagnostopoulos).

2. **Sensors and Data Aggregators** — Resource-constrained devices such as single-board computers and microprocessors that gather information and data from the environment.

3. **Actuators and Agents** — Potentially resource-constrained devices or ones focusing on a single task, based on COTS (Commercial Off-The-Shelf) hardware or dedicated hardware with limited functionality. They perform tasks based on commands from the processing segment.

4. **Processing Segment** — Most probably high-end devices (e.g., infrastructure servers) that decide on actions to be taken based on data and sets of (potentially predefined) rules.

5. **IoT Segments/Domains** — Space, Maritime, Agriculture & Aquaculture, Smart Cities, Energy/Power/Sustainability, Industry and Manufacturing (IEEE World Forum).

6. **Connectivity Solutions in IoT** — Wi-Fi, LoRaWAN, Bluetooth, Ethernet, Serial, Analog I/O Pins, CAN (Controller Area Network), ZigBee. Huge diversity leads to incompatibility and lack of standardization.

7. **Scale of IoT** — ~17 billion connected devices today, projected ~30 billion by 2030.

8. **IoT 2.0** — Next-generation IoT concept connecting to 5G/6G, machine learning and AI, edge computing, Industry 4.0, and the blockchain.

9. **Security vs. Cost Balance** — The relationship between security investment and the cost of damages, ease of use, user experience, and risk assessment. Leads to determining an "acceptable level of security."

10. **Systems of Systems** — IoT essentially requires securing systems of systems of increasing complexity and vast networks of networks.

### Important Scenarios
- Smart car automatically opens smart garage door → if car is stolen, attacker gains home access
- IoT deployed in open field, totally unsupervised → physical attack surface
- Connection to critical infrastructures (space segment, smart grids) → cascading failures

### Cross-references
- → IoT 2.0 (revisited in later lectures)
- → Security by Design (Lecture 3)
- → Attack Surface Analysis (Lecture 5)
- → Lightweight Cryptography (future lectures)

---

## LECTURE 2: IoT Applications and Vulnerability Introduction

### Title
IoT Applications and Introduction to Vulnerabilities, Attacks, and Countermeasures

### Main Topics
- Real-world IoT application scenarios
- Introduction to vulnerabilities, attacks, and countermeasures

### Key Concepts with Definitions

1. **IoT Application Scenarios:**
   - **Smart Home Coordination** — Car/satellite/navigation/fridge/oven/TV/video recorder coordination for seamless user experience
   - **Emergency Response (Forest Fire)** — Space segment IoT detecting fires, on-location agricultural IoT confirming, highway infrastructure notifying vehicles, fire department deploying autonomous systems. Involves: satellite / on-site IoT / highway traffic infrastructure / cars / fire trucks / UAVs / cellphones
   - **Internet of Lights** — All smart lights in a space connected by digital networks, able to communicate with each other, servers/gateways, and nearby sensors/controls
   - **LiFi** — Wireless communication technology utilizing light to transmit data and position between devices
   - **Internet of Sounds (IoS)** — Emerging research field at intersection of IoT and Sound and Music Computing

2. **Vulnerability-Attack-Countermeasure Cycle:**
   - Identify use cases (application, context, framework, environment)
   - Define attacker model
   - Identify realistic (and unrealistic) threats
   - Identify intrinsic vulnerabilities
   - Perform penetration testing
   - Identify attacks
   - Implement countermeasures (evaluate quality/performance)
   - Cycle: Attack → countermeasure → new attack → new countermeasure → …

### Cross-references
- → Threat Modelling (Lecture 3)
- → Attack Surface Classes (Lecture 5)
- → Penetration Testing (Lecture 4, Operational Security Life Cycle)

---

## LECTURE 3: Information Assurance, Attacks, and Secure Development

### Title
Information Assurance, Common Attacks Against the IoT, and Secure Development Life Cycle

### Main Topics
- Information Assurance (CIA triad + extensions)
- Common attacks against the IoT
- Evaluation factors for attacks
- Attack examples (Mirai, KRACK, ZigBee)
- Threat modelling an IoT system
- Security approaches for the IoT
- Secure Development Life Cycle (SDLC) models

### Key Concepts with Definitions

#### Information Assurance

1. **Confidentiality** — Keeping sensitive information secret and protected from disclosure.

2. **Integrity** — Ensuring that information is not modified, accidentally or purposefully, without being detected.

3. **Availability** — Ensuring that information and capabilities are available when needed.

4. **Authentication** — Ensuring that the source of data is from a known identity or endpoint (generally follows identification).

5. **Non-repudiation** — Ensuring that an individual or system cannot later deny having performed an action.

6. **Resilience** — Maintaining state awareness and an accepted level of operational normalcy in response to disturbances, including threats of an unexpected and malicious nature.

7. **Safety** — Not being in threat of undergoing or causing hurt, injury, or loss.

#### Common Attacks Against the IoT

8. **Wired and Wireless Scanning and Mapping Attacks** — Network reconnaissance to discover IoT devices, subnets, ports, and protocols. Example: drone with ZigBee protocol scanner identifying device beacon requests (Praetorian, Austin TX).

9. **Protocol Attacks** — Exploiting weaknesses in communication protocols. Example: ZigBee vulnerable device pairing procedures allowing sniffing of network keys during pairing.

10. **Eavesdropping Attacks** — Passive interception of communications leading to loss of confidentiality.

11. **Cryptographic Algorithm and Key Management Attacks** — Attacking weaknesses in cryptographic implementations or key lifecycle. Example: KRACK (Key Reinstallation Attack) against WPA2 — attacker forces device to reuse a cryptographic key (discovered by Mathy Vanhoef, 2017). See https://www.krackattacks.com/

12. **Spoofing and Masquerading (Authentication Attacks)** — Impersonating a legitimate device or user. Example: Mirai Botnet (2016) exploited IP cameras and internet routers using default passwords.

13. **Operating System and Application Integrity Attacks** — Compromising the software running on IoT devices. Application endpoints and application code running on the device can be directly targeted.

14. **Denial of Service (DoS) and Jamming** — Making devices or networks unavailable. Example: Mirai Botnet scaled to millions of devices launching DDoS attacks against DNS infrastructure.

15. **Physical Security Attacks** — Tampering with physical devices, interface exposures. Example: accessing JTAG interface to read memory, sensitive key material, passwords, configuration data.

16. **Access Control Attacks (Privilege Escalation)** — Gaining unauthorized elevated access to device resources.

#### Evaluation Factors for an Attack

17. **Attacker Capabilities** — Technical ability, notice ability (stealth), and cost of the attack.

18. **Attack Behaviours and Probabilities** — How the attack would be conducted and the likelihood of success.

19. **Impact of the Attack** — Consequences to the victim. Note: low impacts for individual aspects may aggregate to enormous final impact.

20. **Benefits to the Attacker** — Motivating impacts (what the attacker gains).

21. **Detriments to the Attacker** — Demotivators for the attack (risk, cost, effort).

#### Attack Case Studies

22. **Mirai Botnet (2016)** — Formed by exploiting default passwords on IP cameras and internet routers. Simple authentication attack vector scaled to a botnet of millions of devices used for DDoS against DNS.

23. **KRACK Attack (2017)** — Key Reinstallation Attack against WPA2 protocol. Attacker forces device to reuse cryptographic key, exploiting the standardized protocol itself.

24. **ZigBee Pairing Vulnerability** — Protocol designed for easy setup lacked security configuration possibilities. Vulnerable device pairing procedures allow external parties to sniff network keys during pairing.

#### Threat Modelling

25. **Threat Modelling Process:**
   - Identify assets and use cases (components, architecture, application, context, framework, environment)
   - Identify realistic (and unrealistic) threats
   - Rate threats on perceived probability

#### Security Approaches

26. **Security by Design** — Integrating security from the very beginning of system design rather than adding it later.

27. **Lowest Common Denominator Approach** — If the security solution fits and works on a sensor or very small (pico) board, it can fit and work on all other devices and subsystems. Trade-off: effectiveness vs. cost.

28. **Physical Unclonable Functions (PUFs)** — Hardware security primitives that exploit manufacturing variations to create unique device identifiers. (To be covered in detail in future lectures.)

29. **Trusted Platform Module (TPM)** — Dedicated security hardware for cryptographic operations and secure key storage. (To be covered in detail.)

30. **Security Co-processor** — Dedicated hardware component for offloading security operations.

31. **Cryptographic Library** — Software-based collection of cryptographic algorithms.

32. **System Approach** — Need for holistic security across the entire IoT system, not just individual components.

#### Secure Development Life Cycle (SDLC)

33. **Secure Development Life Cycle (SDLC)** — Development of security from scratch in the framework of a system, essentially the same as software development from scratch.

34. **Waterfall Development Model** — Linear sequential design process with no iterations or feedback. Can be extended with feedback (Royce's iterative waterfall).

35. **Spiral Development Model** — Addresses the iteration issue and is based on feedback. Still mostly one-way regarding progress — issues discovered late require a restart.

36. **Agile Development Model** — Not based on an exact plan. Principles: individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan. Very efficient if supervised and deadlines met, otherwise chaotic.

### Cross-references
- → CIA Triad is foundational to all security discussions
- → PUFs, TPMs, TRNGs (future lecture on lightweight security primitives)
- → Lightweight Cryptography (future lecture)
- → Authentication Protocols (future lecture)
- → Attack Surface Classes (Lecture 5)
- → DevOps and Operational Security Life Cycle (Lecture 4)

---

## LECTURE 4: DevOps, Security Practices, and Secure Design Goals

### Title
DevOps, Security Best Practices, and Secure Design Goals for the IoT

### Main Topics
- DevOps methodology and principles
- Required security properties (Security, Safety, Resilience)
- Basic/Best security practices for IoT
- Concerns in IoT security
- Consumer convenience vs. security
- Secure design goals
- Operational security life cycle

### Key Concepts with Definitions

1. **DevOps** — Blends the processes of development, quality assurance, and production. Steady collaboration between systems engineers, developers, testers, system administrators, and product owners, organized by scrum masters, focused on deploying small components of functionality rapidly. Embeds system administrators and other stakeholders into development. Developers need to understand production environment. Provides framework for rapid feedback on software quality in the field. Requires harmonic collaboration and frequent supervision.

2. **DevOps Principles:**
   - Automate
   - Blend operations, Quality Assurance, and development
   - Instrument and provide continuous feedback
   - Be transparent
   - Be vigilant

3. **Security (Required Property):**
   - Threat modelling
   - Attack tree
   - Automated security analysis

4. **Safety (Required Property):**
   - Hazard analysis
   - Fault tree

5. **Resilience (Required Property):**
   - Anticipate — Proactively identify and prepare for potential threats
   - Withstand — Maintain operations during a threat event
   - Recover — Restore normal operations after a disruption
   - Evolve — Learn and improve from incidents

6. **Attack Tree** — A structured diagram modeling how an attacker could achieve a specific goal, branching into sub-goals and methods.

7. **Fault Tree** — A structured diagram modeling how system failures can lead to a hazardous state.

8. **Hazard Analysis** — Systematic process for identifying potential hazards and their causes in a system.

#### Basic / Best Security Practices

9. **Lifecycle Security Enforcement** — Security should be enforced in IoT throughout the development and operational lifecycle of all IoT devices and hubs.

10. **Software Authorization and Authentication** — The software running on all IoT devices should be authorized and authenticated.

11. **Device Network Authentication** — When an IoT device is turned on, it should first authenticate itself into the network before collecting or sending data.

12. **IoT Firewalling** — IoT devices have limited computation and memory capabilities; firewalling is necessary in IoT networks to filter packets directed to devices.

13. **Authenticated Updates** — Updates and patches on the device should be installed without consuming additional bandwidth and should be authenticated.

#### Concerns

14. **Speed to Market** — Market pressure to ship products quickly, often at the expense of security.

15. **Attack Deluge** — Internet-connected devices face a deluge of attacks.

16. **Privacy Threats** — IoT introduces new threats to user privacy.

17. **Physical Compromise** — IoT products and systems can be physically compromised.

18. **Consumer Convenience (UX)** — Easy installation, Plug'n'Play, no complaints/returns, but often combined with: poor customer knowledge, poor installation, poor technology understanding.

19. **Security Talent Shortage** — Skilled security engineers are hard to find and retain.

#### Secure Design Goals

20. **Mitigate Automated Attack Risks** — Design IoT systems to resist automated/unsupervised attacks.

21. **Secure Points of Integration** — Design integration points between subsystems with security in mind.

22. **Protect Confidentiality and Integrity:**
    - Apply cryptography to secure data at rest and in motion
    - Enable visibility into the data life cycle and protect data from manipulation
    - Implement secure over-the-air (OTA) updates

23. **Design for Safety** — Ensure IoT systems do not cause harm.

24. **Hardware Protection Measures:**
    - Introduce secure hardware components within IoT system
    - Incorporate anti-tamper mechanisms that report and/or react to attempted physical compromise

25. **Design for Availability:**
    - Cloud availability
    - Guard against unplanned equipment failure
    - Load balancing

26. **Design for Resilience:**
    - Protecting against jamming attacks
    - Device redundancy
    - Gateway caching
    - Digital configurations
    - Gateway clustering
    - Rate limiting
    - Congestion control
    - Flexible policy and security management features for administrators
    - Logging mechanisms with integrity-protected logs fed to cloud for safe storage

27. **Design for Compliance:**
    - US IoT Cybersecurity Improvement Act of 2020
    - ENISA baseline security recommendations
    - US DHS guiding principles for secure IoT
    - US FDA guidance on IoT medical devices

#### Operational Security Life Cycle

28. **Define Phase:**
    - Define system security policies
    - Define system roles

29. **Implement/Integrate Phase:**
    - Configure gateways and network security
    - Bootstrap and securely configure devices
    - Set up threat intelligence and vulnerability monitoring
    - Set up deception mechanisms
    - Train stakeholders

30. **Operate and Maintain Phase:**
    - Manage assets
    - Manage credentials
    - Manage firmware and patch updates
    - Monitor the system
    - Perform penetration testing
    - Manage incidents

31. **Dispose Phase:**
    - Secure disposal
    - Data purging
    - Inventory removal
    - Data archival/records maintenance

### Cross-references
- → Secure Development Life Cycle models (Lecture 3)
- → Information Assurance (CIA triad) (Lecture 3)
- → Resilience concept (Lecture 3)
- → Attack Surface Classes (Lecture 5)
- → ENISA Reports (mentioned, referenced to files)
- → PUFs, TPMs (Lecture 3 intro, future lectures)
- → Compliance frameworks → US IoT Cybersecurity Improvement Act, ENISA, DHS, FDA

---

## LECTURE 5: Attack Surface Analysis

### Title
Attack Surface Classes for IoT (Daniel Miessler, DefCon 2023)

### Main Topics
- Comprehensive attack surface classification for IoT
- Connection to operational security life cycle

### Key Concepts with Definitions

#### Attack Surface Classes (by Daniel Miessler, DefCon 2023)

1. **Access Control Attack Surface:**
   - Authentication — Verifying identity of users/devices
   - Session management — Managing authenticated sessions securely
   - Implicit trust between components — Unvalidated trust relationships
   - Enrolment secure processes — Secure device onboarding
   - Decommissioning secure processes — Secure device retirement
   - Lost access-processes — Handling lost credentials/access

2. **Device Memory Attack Surface:**
   - Clear text username — Usernames stored without encryption
   - Clear text passwords — Passwords stored without encryption
   - Third-party credentials — Credentials for external services stored insecurely
   - Encryption keys — Cryptographic keys stored in accessible memory

3. **Physical Interface Assessment:**
   - Firmware extraction — Dumping firmware via physical access
   - User CLI — User-level command-line interfaces exposed
   - Admin CLI — Administrative command-line interfaces exposed
   - Privilege escalation — Gaining higher access through physical interfaces
   - Reset to insecure state — Factory reset leaving device in vulnerable state

4. **Device Web Interface:**
   - SQL Injection — Malicious SQL queries through web interface
   - Cross-site scripting (XSS) — Injecting malicious scripts into web pages
   - Username enumeration — Discovering valid usernames
   - Weak passwords — Insufficient password complexity requirements
   - Account lock out — Absence of brute-force protection
   - Known credentials — Default or publicly known credentials

5. **Device Firmware:**
   - Hardcoded passwords — Passwords embedded in firmware
   - Sensitive URL disclosure — Internal URLs exposed in firmware
   - Encryption keys — Cryptographic keys hardcoded in firmware

6. **Device Network Services:**
   - Information disclosure — Leaking system information through network services
   - User CLI — Network-accessible user interfaces
   - Admin CLI — Network-accessible admin interfaces
   - Injection — Command/code injection through network services
   - Denial of Service — Making network services unavailable

7. **Administrative Web Interface:**
   - SQL injection, Cross-site scripting, Username enumeration, Weak passwords, Account lock out, Known credentials (same vulnerability classes as device web interface but for admin panel)

8. **Local Data Storage:**
   - Unencrypted data — Sensitive data stored without encryption
   - Data encrypted with recovered keys — Encryption useless if keys are recoverable
   - Lack of data integrity checks — No verification that stored data hasn't been tampered with

9. **Cloud Web Interface:**
   - SQL injection, Cross-site scripting, Username enumeration, Weak passwords, Account lock out, Known credentials (same vulnerability classes, cloud-side)

10. **Third-Party Back-End APIs:**
    - Unencrypted PII sent — Personally Identifiable Information transmitted in clear text
    - Encrypted PII sent — Even encrypted PII can be problematic if keys are compromised
    - Device information leaked — Metadata about devices exposed
    - Location leaked — User/device location data exposed

11. **Update Mechanism:**
    - Updates sent unencrypted — Firmware updates transmitted without encryption
    - Updates not hash signed — No integrity verification for updates
    - Source location writable — Update server/location can be modified by attacker

12. **Mobile Application:**
    - Implicitly trusted by device and cloud — Mobile app treated as trusted without verification
    - Known credentials — Hardcoded or default credentials in app
    - Insecure data storage — Sensitive data stored insecurely on mobile device
    - Lack of transport encryption — Communications not encrypted

13. **Vendor Back-End API:**
    - Inherent trust of cloud or mobile application — Unconditional trust in client applications
    - Weak authentication — Insufficient authentication mechanisms
    - Weak access control — Insufficient authorization checks
    - Injection attacks — SQL/command injection through API parameters

14. **Ecosystem Communications:**
    - Health checks — Exploiting device health monitoring mechanisms
    - Heartbeats — Exploiting keep-alive/heartbeat signals
    - Ecosystem commands — Exploiting command channels between ecosystem components
    - Decommissioning — Exploiting device retirement processes
    - Update pushes — Exploiting push update mechanisms

15. **Network Traffic:**
    - LAN traffic — Local network communications interception/manipulation
    - LAN to Internet — Traffic between local network and cloud/internet
    - Non-standard — Non-standard protocol communications
    - Short-range — Bluetooth, ZigBee, NFC, and other short-range communications

### Cross-references
- → All attack types introduced in Lecture 3
- → Physical Security Attacks (Lecture 3)
- → Authentication Attacks / Mirai (Lecture 3)
- → Operational Security Life Cycle (Lecture 4)
- → Secure Design Goals (Lecture 4)
- → Cryptographic Algorithm and Key Management (Lecture 3)

---

## MASTER CONCEPT INDEX

### Definitions (Alphabetical)
- **Actuator** — Device that performs physical actions based on commands (L1)
- **Agile Development** — Iterative, flexible SDLC model (L3)
- **Attack Tree** — Diagram modeling attacker paths to a goal (L4)
- **Authentication** — Verifying identity of data source (L3)
- **Availability** — Information/capabilities available when needed (L3)
- **CAN** — Controller Area Network, IoT connectivity protocol (L1)
- **CIA Triad** — Confidentiality, Integrity, Availability (L3)
- **Confidentiality** — Keeping sensitive information secret (L3)
- **COTS** — Commercial Off-The-Shelf hardware (L2)
- **DDoS** — Distributed Denial of Service (L3)
- **Decommissioning** — Secure retirement of IoT devices (L5)
- **DevOps** — Blending development, QA, and operations (L4)
- **Edge Computing** — Processing data near the source (L1)
- **ENISA** — European Union Agency for Cybersecurity (L4)
- **Fault Tree** — Diagram modeling failure paths to hazardous state (L4)
- **Hazard Analysis** — Systematic identification of potential hazards (L4)
- **Integrity** — Information not modified without detection (L3)
- **IoT** — Internet of Things (L1)
- **IoT 2.0** — Next-gen IoT with 5G/6G, AI, blockchain (L1)
- **IoS** — Internet of Sounds (L2)
- **JTAG** — Hardware debug interface, physical attack vector (L3)
- **KRACK** — Key Reinstallation Attack against WPA2 (L3)
- **LiFi** — Light-based wireless communication (L2)
- **LoRaWAN** — Long Range Wide Area Network protocol (L1)
- **Mirai Botnet** — 2016 botnet exploiting default passwords (L3)
- **Non-repudiation** — Cannot deny having performed an action (L3)
- **OTA Updates** — Over-The-Air firmware updates (L4)
- **PII** — Personally Identifiable Information (L5)
- **PUF** — Physical Unclonable Function, hardware security primitive (L3)
- **Resilience** — Maintaining operational normalcy under disturbance (L3)
- **Safety** — Not causing or undergoing hurt/injury/loss (L3)
- **SDLC** — Secure Development Life Cycle (L3)
- **Sensor** — Device that gathers environmental data (L1)
- **SQL Injection** — Malicious SQL through input fields (L5)
- **TPM** — Trusted Platform Module, dedicated security hardware (L3)
- **TRNG** — True Random-Number Generator (L1)
- **Waterfall Development** — Linear sequential SDLC model (L3)
- **WPA2** — Wi-Fi Protected Access 2 protocol (L3)
- **XSS** — Cross-Site Scripting (L5)
- **ZigBee** — Low-power wireless protocol for IoT (L1, L3)

### Attack Types (Comprehensive List)
1. Wired and wireless scanning and mapping (L3)
2. Protocol attacks (L3)
3. Eavesdropping (L3)
4. Cryptographic algorithm and key management attacks (L3)
5. Spoofing and masquerading (L3)
6. OS and application integrity attacks (L3)
7. Denial of Service and jamming (L3)
8. Physical security attacks / tampering (L3)
9. Access control / privilege escalation (L3)
10. SQL Injection (L5)
11. Cross-site scripting (L5)
12. Username enumeration (L5)
13. Hardcoded credentials (L5)
14. Firmware extraction (L5)
15. Unencrypted data storage/transmission (L5)
16. Key reinstallation attacks (L3)
17. Default password exploitation (L3)

### Security Mechanisms (Comprehensive List)
1. Security by Design (L3)
2. Physical Unclonable Functions (PUFs) (L3)
3. Trusted Platform Module (TPM) (L3)
4. Security co-processor (L3)
5. Cryptographic library (L3)
6. Lowest common denominator approach (L3)
7. IoT firewalling (L4)
8. Anti-tamper mechanisms (L4)
9. Device redundancy (L4)
10. Gateway caching and clustering (L4)
11. Rate limiting and congestion control (L4)
12. Integrity-protected logging (L4)
13. Authenticated updates (L4)
14. Deception mechanisms (L4)
15. Threat intelligence and vulnerability monitoring (L4)
16. Penetration testing (L4)
17. Secure disposal and data purging (L4)

### Standards and Regulations
- US IoT Cybersecurity Improvement Act of 2020 (L4)
- ENISA baseline security recommendations (L4)
- US DHS guiding principles for secure IoT (L4)
- US FDA guidance on IoT medical devices (L4)

### Development Models
- Waterfall (L3)
- Spiral (L3)
- Agile (L3)
- DevOps (L4)

---

## RECOMMENDED VAULT PAGES TO CREATE

### Topic Pages
1. [[IoT Security]] — Main hub page
2. [[Internet of Things (IoT)]] — Definition, components, segments, diversity
3. [[IoT 2.0]] — 5G/6G, AI/ML, edge computing, Industry 4.0, blockchain integration
4. [[Information Assurance]] — CIA triad + authentication + non-repudiation + resilience + safety
5. [[IoT Attack Surface]] — Comprehensive attack surface classes (Miessler/DefCon 2023)
6. [[Common IoT Attacks]] — All attack types indexed
7. [[Secure Development for IoT]] — SDLC models, security by design
8. [[DevOps]] — Principles, blending dev/ops/QA
9. [[IoT Security Best Practices]] — Lifecycle enforcement, authenticated software, firewalling
10. [[Secure Design Goals for IoT]] — All design goals from Lecture 4
11. [[Operational Security Life Cycle]] — Define, Implement, Operate, Dispose
12. [[Threat Modelling for IoT]] — Process, assets, threat identification, rating
13. [[IoT Applications]] — Smart home, emergency response, Internet of Lights, Internet of Sounds, LiFi

### Concept Pages
14. [[Confidentiality]]
15. [[Integrity]]
16. [[Availability]]
17. [[Authentication]]
18. [[Non-repudiation]]
19. [[Resilience]]
20. [[Safety]]
21. [[Security by Design]]
22. [[Lowest Common Denominator Approach]]
23. [[Attack Tree]]
24. [[Fault Tree]]
25. [[Hazard Analysis]]

### Protocol/Standard Pages
26. [[Wi-Fi]]
27. [[LoRaWAN]]
28. [[Bluetooth]]
29. [[ZigBee]]
30. [[CAN Bus]]
31. [[WPA2]]
32. [[JTAG]]

### Attack Pages
33. [[Mirai Botnet]]
34. [[KRACK Attack]]
35. [[ZigBee Pairing Vulnerability]]
36. [[SQL Injection]]
37. [[Cross-Site Scripting (XSS)]]
38. [[Denial of Service (DoS)]]
39. [[Eavesdropping]]
40. [[Spoofing and Masquerading]]
41. [[Privilege Escalation]]

### Hardware Security Pages
42. [[Physical Unclonable Functions (PUFs)]]
43. [[Trusted Platform Module (TPM)]]
44. [[True Random-Number Generators (TRNGs)]]
45. [[Security Co-processor]]

### Regulation/Framework Pages
46. [[US IoT Cybersecurity Improvement Act 2020]]
47. [[ENISA IoT Security Guidelines]]
48. [[DHS IoT Security Principles]]
49. [[FDA IoT Medical Device Guidance]]

### Development Model Pages
50. [[Waterfall Development Model]]
51. [[Spiral Development Model]]
52. [[Agile Development Model]]
53. [[DevOps]]

---

## PREREQUISITE CHAINS

```
IoT Definition (L1)
  ├── IoT Components (L1)
  ├── IoT Segments (L1)
  ├── IoT Connectivity (L1) → ZigBee, LoRaWAN, Bluetooth, Wi-Fi, CAN
  └── IoT Applications (L2)
       └── Vulnerabilities, Attacks, Countermeasures cycle (L2)
            ├── Information Assurance / CIA Triad (L3) ← FOUNDATIONAL
            │    ├── Confidentiality
            │    ├── Integrity
            │    ├── Availability
            │    ├── Authentication
            │    └── Non-repudiation
            ├── Resilience (L3) → Design for Resilience (L4)
            ├── Safety (L3) → Design for Safety (L4)
            ├── Common IoT Attacks (L3)
            │    ├── Authentication Attacks → Mirai Botnet
            │    ├── Protocol Attacks → ZigBee Pairing Vulnerability
            │    ├── Crypto/Key Mgmt Attacks → KRACK Attack
            │    ├── Physical Security Attacks → JTAG
            │    ├── DoS/Jamming → Mirai DDoS
            │    └── → Attack Surface Classes (L5) [detailed breakdown]
            ├── Threat Modelling (L3) → Attack Tree (L4)
            ├── Security by Design (L3) → Secure Design Goals (L4)
            │    ├── PUFs
            │    ├── TPM
            │    ├── Security Co-processor
            │    └── Cryptographic Library
            ├── SDLC Models (L3)
            │    ├── Waterfall
            │    ├── Spiral
            │    ├── Agile
            │    └── → DevOps (L4)
            └── Operational Security Life Cycle (L4)
                 ├── Define
                 ├── Implement/Integrate
                 ├── Operate and Maintain
                 └── Dispose
```
