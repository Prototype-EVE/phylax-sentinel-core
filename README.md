![Status: Sovereign Pilot Ready](https://img.shields.io/badge/Status-Sovereign_Pilot_Ready-green)
![Compliance: UK Cyber Bill 2026](https://img.shields.io/badge/Compliance-UK_Cyber_Bill_2026-blue)
![Architecture: RISC--V](https://img.shields.io/badge/Architecture-RISC--V-orange)
#🛡️ PHYLAX Hardware-Root-of-Trust (RoT)
**Level:** Sovereign Tier 1 (Strategic Infrastructure)

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

---

🚀 Project Roadmap: PHYLAX Sentinel 2026
"The Digital Redoubt: Securing UK Sovereignty at the Edge"

Phase 1: Operational Validation (Q1 2026)
Goal: Finalize the "Sovereign Shield" baseline for maritime use.

Key Milestone: Deployment of 5 hardened units for the UK Border Force small-boat interception pilot.

Deliverables:

Completion of the NCSC RTL Audit on our RISC-V hardware logic.

Validation of the "Verify & Discard" sub-0.5s volatile memory purge protocol.

Integration of TPM 2.0 Measured Boot to prevent device interdiction.

Phase 2: Legislative Alignment (Q2 2026)
Goal: Formalize Project SENTINEL as a compliance standard for the 2026 Cyber Bill.

Key Milestone: Submission of the "Fiscal Displacement Study" to the Science, Innovation and Technology Committee (Julia Lopez's office).

Deliverables:

"Inquiry vs. Integrity" whitepaper showcasing the £31M cost-savings per avoided public inquiry.

Release of the Sovereign Supply Chain Registry, ensuring zero reliance on "Black Box" foreign silicon.

Phase 3: Tactical Expansion (Q3 2026)
Goal: Deploy the "Sovereign Sidecar" to other critical departments.

New Departments & Use Cases:

NCA (National Crime Agency): Deployment of encrypted mobile units for high-stakes undercover identity verification.

Metropolitan Police: Pilot program for Operator-Initiated Facial Recognition (OIFR) that uses the "Verify & Discard" logic to bypass current public privacy concerns (GDPR-compliant by default).

MoD (Ministry of Defence): Implementation of the PMP (Physical Memory Protection) logic in field-comms for high-threat environments.

Phase 4: Full UK National Deployment (Q4 2026)
Goal: Integration into the UK National Security Infrastructure.

Key Milestone: Project SENTINEL becomes the mandatory "Tactical Tier" for any department handling sensitive biometric data in zero-trust zones.

Final 2026 Deliverables:

Establishment of the UK Sovereign Tech Hub for the ongoing maintenance of the RISC-V codebase.

Transition from "Pilot" to "Primary Asset" for all UK maritime and coastal enforcement.
**Compliance Note:** This architecture satisfies the "Supply Chain Auditability" and "Operational Resilience" mandates of the **UK Cyber Security and Resilience Bill 2026**.
