# 🛡️ Ransomware Tripwire (File Integrity Monitor - FIM)

## 📖 Project Description
A lightweight, high-performance security tool designed to simulate core functionalities of Endpoint Detection and Response (EDR) and File Integrity Monitoring (FIM) systems. 

This project operates as a cryptographic "tripwire" for sensitive directories. By leveraging advanced cryptographic hashing, it establishes a secure state baseline and detects unauthorized changes—such as file modifications, deletions, or new file injections—which are classic indicators of Ransomware attacks or unauthorized system tampering.

## ✨ Key Features
* **Cryptographic Baseline Generation:** Captures a point-in-time snapshot of a secure directory using the highly secure **SHA-512** algorithm.
* **3-Way Anomaly Detection Engine:**
  * `[ ! ] ALARM (MODIFIED):` Flags files whose cryptographic signatures have changed (even by a single character).
  * `[ - ] ALARM (DELETED):` Identifies critical files that have been removed from the system.
  * `[ + ] WARNING (NEW FILE):` Detects untracked, newly introduced files that could represent malicious payloads or webshells.
* **Memory-Optimized Processing:** Implements chunked binary file streaming (`8192 bytes` streams), allowing the tool to process extremely large files (e.g., databases, ISOs) smoothly without exhausting system RAM.
* **Structured State Persistence:** Saves and reads system states natively using structured `JSON` baselines, allowing for seamless integration with external SIEMs or alerting workflows.

## 🏗️ Architecture & Workflow

The solution is split into two distinct operational phases:
1. **Baseline Creation (`tripwire.py`):** Run on a known-clean system to generate `baseline.json`, which maps absolute file paths to their trusted SHA-512 hashes.
2. **Integrity Monitoring (`monitor.py`):** Executed periodically or on-demand to compare the current state of the directory against the trusted baseline and raise immediate security alerts upon discrepancy.

## 💼 Business & SOC Value
In a professional Security Operations Center (SOC), monitoring file integrity is vital for compliance (e.g., PCI-DSS, ISO 27001) and early breach detection. This tool automates the verification of critical system configurations and data folders, significantly cutting down the time to detect ransomware encryption processes before they spread across the network.

## 🛠️ Setup & Usage

### 1. Environment Requirements
* Python 3.x (Uses standard libraries: `os`, `hashlib`, `json`). No external dependencies required.

### 2. Deployment Steps
1. Clone the repository to your local machine.
2. Create a target directory to protect (e.g., `wazne_dane/`) and populate it with your critical files.
3. **Generate the trusted baseline:**