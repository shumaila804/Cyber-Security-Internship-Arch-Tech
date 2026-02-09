# ***🛡️ CYBER SECURITY INTERNSHIP: MONTH 1 PROJECT***
**🏢 Organization:** Arch Technologies
**👤 Intern Name:** Shumaila Arif
**💻 Domain:** Cyber Security
---

## 📌 Overview  

Welcome to the documentation of my first month as a Cyber Security Intern at Arch Technologies. This phase was dedicated to bridging the gap between theoretical security concepts and practical implementation.

The core focus was twofold:

**Network Visibility**: Developing a robust traffic sniffer to analyze live data packets and identify security gaps in network protocols.

**Host-level Monitoring:** Simulating system-level security threats (Keylogging) to understand how malware evades detection and how to implement effective countermeasures.

Through these projects, I have transitioned from understanding what a threat is to actively simulating and analyzing how these threats operate in a controlled, ethical environment.

---

## 🎯 Objectives  


Real-Time Traffic Analysis: Gain hands-on experience in capturing and dissecting live network packet flows to understand data transmission.

Protocol & IP Intelligence: Develop the ability to analyze core networking protocols and map source-to-destination communication patterns.

Ethical Threat Simulation: Conduct controlled simulations of host-based monitoring (Keylogging) to understand attacker methodologies within an ethical framework.

Defensive Strategy Development: Evaluate and learn proactive security measures, such as encryption and multi-factor authentication, to mitigate identified risks.

Security Automation: Enhance Python scripting skills to build custom, automated tools for continuous security monitoring and data logging. 

---

## 🛰️ Task 1: Network Traffic Sniffer  

### 🔍 Description  

A Python-based packet sniffer that captures and analyzes live network traffic. It extracts important details such as protocol types, source and destination IP addresses, and packet sizes.

### ⚙️ Features  

- Multi-Protocol Inspection: Engineered to intercept and parse both TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) traffic, providing a comprehensive view of network activity.

- Granular IP Tracking: Extracts and displays real-time Source and Destination IP addresses, enabling precise monitoring of data origin and endpoints.

- Automated Data Persistence: Features a dedicated logging mechanism that exports captured packet metadata into packet_log.txt for detailed forensic analysis.

- Protocol Analysis: Specifically designed to identify and analyze unencrypted (clear-text) communication, highlighting vulnerabilities in non-secure network channels.

- Payload Insight: Allows for the observation of packet sizes and headers to understand network overhead and traffic patterns.

### 🔐 Security Learning  

- Vulnerability Analysis: Demonstrated how clear-text protocols (like HTTP, FTP, or Telnet) allow attackers to perform eavesdropping and intercept sensitive data through packet sniffing.

- Cryptographic Importance: Validated the necessity of HTTPS (SSL/TLS) by observing how encryption masks data, making it unreadable to unauthorized sniffers and preventing Man-in-the-Middle (MITM) attacks.

- Network Visibility: Improved practical understanding of Network Intrusion Detection, learning how defenders use traffic patterns to identify suspicious behavior or unauthorized data exfiltration.

Packet Forensics: Gained hands-on experience in deconstructing network headers, which is a fundamental skill for investigating security breaches and network troubleshooting.
---

## ⌨️ Task 2: Keylogging Simulation  

### 🔍 Description  

This task involved the development of a system-level monitoring tool designed to simulate how keystroke logging (Keylogging) operates within a host environment. The primary goal was to study the vulnerability of user input and understand the lifecycle of a credential theft attack—from initial interception to local data storage.

Developed in a strictly controlled and ethical environment, this simulation provides a practical look at how malicious actors can bypass standard input methods to capture sensitive information like passwords, PII, and command-line interactions.

### ⚙️ Features  

- Low-Level Event Hooking: Utilizes Python's pynput library to create a listener that hooks into system keyboard events in real-time.

- Comprehensive Input Logging: Specifically designed to capture and sanitize alphanumeric characters, whitespace, and critical special keys (e.g., Shift, Enter, Backspace) for a readable log.

- Persistent Local Storage: Implements automated file handling to securely write and append intercepted keystrokes into key_log.txt for post-simulation analysis.

- Invisible Execution: Built as a background process to simulate how stealthy monitoring tools operate within a host system.

### 🛡️ Security Learning  

- Data Vulnerability: Demonstrated how sensitive information (like passwords and PII) can be intercepted at the source before encryption is even applied.

- The Power of MFA: Highlighted that even if a password is stolen via a keylogger, Multi-Factor Authentication (MFA) acts as a crucial second line of defense to prevent unauthorized access.

- Endpoint Protection: Emphasized the importance of using robust Anti-Malware and EDR (Endpoint Detection and Response) solutions that can detect and block unauthorized keyboard hooks.

- User Awareness: Underscored that social engineering and malicious attachments are common delivery methods for such scripts, making user education vital.  

---

## 📂 Repository Structure  

```text
├── sniffer.py
├── keylogger.py
├── packet_log.txt
├── key_log.txt
├── Submission_Screenshots.docx
└── README.md

```
## 🚀 How to Run  

### 1. Clone the repository  
```bash
git clone https://github.com/shumaila804/Cyber-Security-Internship-Arch-Tech.git
```

### 2. Install dependencies
```bash
pip install scapy pynput
```


### 3. Run the Sniffer
```bash
python sniffer.py
```


### Run the keylogger
```bash
python keylogger.py
```

## **⚠️ Ethical Notice**
These tools are developed strictly for educational and defensive security research purposes only.

Unauthorized use on systems or networks without permission is illegal and unethical.

---

## **🏁 Conclusion**
This internship project was a deep dive into the practical side of Cyber Security. Through the development of these tools, I achieved the following:

**Network Security:** I gained hands-on experience with Packet Sniffing and understood how data travels across a network. It highlighted the critical need for encryption (HTTPS/TLS) to prevent Man-in-the-Middle (MITM) attacks.

**Host Monitoring**: Building the Keylogger simulation taught me how malware operates at the system level and why Endpoint Security and Multi-Factor Authentication (MFA) are non-negotiable for modern businesses.

**Python for Security**: I improved my ability to use specialized libraries like Scapy (for packet manipulation) and Pynput (for system event monitoring).

**Ethical Mindset:** Most importantly, I learned the importance of the Ethical Hacker's Code—using these skills only in controlled environments to build stronger defenses, not for harm.

---


## **🌟 Author**
Shumaila Arif

Cyber Security Intern – Arch Technologies

---
