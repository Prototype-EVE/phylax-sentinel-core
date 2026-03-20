![Status: Sovereign Pilot Ready](https://img.shields.io/badge/Status-Sovereign_Pilot_Ready-green)
![Compliance: UK Cyber Bill 2026](https://img.shields.io/badge/Compliance-UK_Cyber_Bill_2026-blue)
![Architecture: RISC--V](https://img.shields.io/badge/Architecture-RISC--V-orange)

## 🛡️ PHYLAX Hardware-Root-of-Trust (RoT)

## 🏛️ Purpose
This directory contains the low-level logic that bridges the PHYLAX software to the physical silicon. By rooting our security in the hardware, we eliminate the "Sovereignty Gap" created by foreign-managed cloud dependencies and opaque "Black Box" chips.

## 🔑 Core Technical Protocols

### 1. RISC-V Open-Standard Auditability
Unlike proprietary x86 or ARM architectures, our use of RISC-V allows the UK Government (NCSC) to perform a full **RTL (Register Transfer Level) Inspection**. 
* **Zero Backdoors:** We can mathematically prove that no hidden foreign "kill switches" exist in the silicon.

### 2. TPM 2.0 Measured Boot
Utilizing the **Trusted Platform Module (TPM)**, every stage of the device's startup is measured. 
* **Immutable Chain of Trust:** If a device is physically tampered with or the OS is altered, the hardware-rooted "Locker" refuses to open, protecting sensitive watchlist data.

### 3. Physical Memory Protection (PMP)
We utilize RISC-V's PMP to "fence off" the identity matching protocol. 
* **Isolation:** Even if a network-connected component is compromised, the attacker is physically blocked from accessing the biometric memory space.

## 📂 Directory Contents
* `volatile_wipe.c`: The "Verify & Discard" logic that purges RAM in <0.5s.
* `tpm_attestation.c`: Generates signed "Cryptographic Quotes" to prove system integrity.
* `pmp_config.h`: Header files defining the physical boundaries for memory isolation.
## 📊 Fiscal Displacement: Inquiry vs. Integrity
Project PHYLAX represents a transition from **sunk operational expenses** to a **permanent national security asset**. By investing in sovereign infrastructure, the UK can displace the catastrophic costs of reactive data failures and public inquiries.

| Category | Current Reactive Model (Sunk Cost) | PHYLAX Sovereign Solution (Asset) |
| :--- | :--- | :--- |
| **Annual Budget Impact** | **£2.9 Billion+** (Asylum Management) | **£550,000** (Full Pilot Phase)|
| **Primary Unit Cost** | ~£150 per person / day | ~£1,800 per device (One-time) |
| **Integrity Assurance** | Reactive Public Inquiries (£10M - £150M+) |**Immutable Audit** (Hardware-Rooted) |
| **Data Residency** | Foreign Cloud (US CLOUD Act Vulnerability)|**Offline-First** (100% UK Autonomy)  |
| **Hardware Trust** | Opaque / Non-Sovereign "Black Box" | **Auditable RISC-V** (NCSC RTL Verified)|
| **Privacy Compliance** | Permanent "Intelligence Collection" Risk | **"Verify & Discard"** (GDPR by Design)|

## 💡 The Sovereign Shield Value Proposition
Fiscal Efficiency: For the cost of housing roughly **10 migrants for one year**, the government can fund a full-scale Sovereign Pilot.
Resilience by Design: While cloud-based systems fail during network blackouts or cable cuts, PHYLAX's Offline-First architecture ensures the border remains functional under total isolation.

Zero Hackable Target: By processing biometrics in volatile memory and deleting non-matches in <0.5 seconds, we eliminate the massive strategic target for foreign state-sponsored hackers.

---

**Compliance Note:** This architecture satisfies the Supply Chain Auditability and "Operational Resilience" mandates of the **UK Cyber Security and Resilience Bill 2026**.
---

## ⚠️ Technical Architecture Disclaimer: Cloud Independence

### **The "Zero-Cloud" Mandate**
Project SENTINEL intentionally avoids the integration of any US-based Cloud APIs (including but not limited to OpenAI, Anthropic, Google Cloud, or AWS) for core biometric processing and decision-making. 

### **Rationale: Mitigation of Jurisdictional Risk**
This architecture is a response to the following identified security threats:

1. **Regulatory Capture & Data Seizure:** US-based entities are subject to the **Foreign Intelligence Surveillance Act (FISA)** and the **CLOUD Act**. These legal frameworks allow for the silent seizure of data and the forced implementation of "backdoors" under National Security Letters (NSLs) that carry gag orders.
2. **Operational Continuity:** Reliance on third-party APIs introduces a **Central Point of Failure**. If a provider terminates a service due to shifting political or corporate policies, the security infrastructure of Project SENTINEL remains unaffected.
3. **Supply Chain Integrity:** By executing on **Local Silicon (Apple M-Series Secure Enclave)**, the attack surface is reduced to the physical hardware in the user's possession, eliminating "Man-in-the-Middle" risks inherent in cloud-based inference.



### **Statement of Intent**
Project PHYLAX is developed as a **Sovereign Security Tool**. Our commitment to **Privacy-by-Design** dictates that "Intelligence" must never come at the cost of "Anonymity." We do not "rent" our logic; we own it.

---
##Manufacturing Readiness Level (MRL)
