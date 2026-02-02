# PHYLAX: Sovereign Identity Protocol
### Project SENTINEL | Offline Volatile Memory Verification

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: Prototype](https://img.shields.io/badge/Status-Research_Prototype-blue.svg)
![Architecture: Sovereign](https://img.shields.io/badge/Architecture-Offline%20%2F%20Air--Gapped-green.svg)
![Compliance: GDPR](https://img.shields.io/badge/Compliance-GDPR%20Privacy%20By%20Design-orange.svg)

## 🛡️ Executive Summary
**Phylax Cybernetics** presents **Project SENTINEL**: an offline-first biometric verification framework designed for zero-trust maritime environments. 

Unlike traditional cloud-tethered systems, this protocol utilizes **Volatile Memory (RAM)** processing to ensure that sensitive biometric data is never written to a permanent drive. It allows sovereign entities to perform identity checks against a cryptographically hashed watchlist without maintaining a mass surveillance database.

> **Note:** This repository contains **Public Domain** academic research code. It is designed to be compatible with European Sovereign Supply Chains (STMicroelectronics STM32N6 / RISC-V).

## ⚡ Key Architecture
* **Air-Gapped Operation:** Functions with 0% internet connectivity.
* **Volatile Memory Defense:** Data exists only in RAM. Power loss = Data destruction.
* **Salted Hash Logic:** Uses daily-rotating cryptographic salts to prevent "Rainbow Table" attacks on the watchlist.
* **Audit-Ready:** Pseudonymous logging tracks the *Officer* without tracking the *Subject*.

## 🛠️ System Flow
```mermaid
graph LR
    A[Camera Input] -->|Raw Frame| B(Volatile RAM)
    B -->|Vectorize| C{Secure NPU}
    C -->|Add Daily Salt| D[Hashed Vector]
    D -->|Compare| E[Watchlist Database]
    E -->|Result| F[Audit Log]
    B -.->|Immediate Wipe| G[Null Data]
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#f66,stroke-width:2px
