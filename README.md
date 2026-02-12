# 🛡️ PHYLAX Hardware-Root-of-Trust (RoT)
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
**Compliance Note:** This architecture satisfies the "Supply Chain Auditability" and "Operational Resilience" mandates of the **UK Cyber Security and Resilience Bill 2026**.
