# 🛡️ Cyber Security Internship – Month 1 Project  

**Organization:** Arch Technologies  
**Intern Name:** Shumaila Arif  
**Domain:** Cyber Security  

---

## 📌 Overview  

This repository contains the work completed during the first month of my Cyber Security internship at **Arch Technologies**. The focus of this phase was to build practical tools for **network traffic analysis** and **host-based monitoring**.

The projects helped me understand how attackers intercept data and how defenders monitor systems to protect sensitive information.

---

## 🎯 Objectives  

- Understand real-time network packet flow.  
- Analyze protocols and IP communication.  
- Simulate host-based monitoring attacks ethically.  
- Learn defensive security techniques.  
- Improve Python scripting for cyber security.  

---

## 🛰️ Task 1: Network Traffic Sniffer  

### 🔍 Description  

A Python-based packet sniffer that captures and analyzes live network traffic. It extracts important details such as protocol types, source and destination IP addresses, and packet sizes.

### ⚙️ Features  

- Captures TCP and UDP packets.  
- Displays source and destination IPs.  
- Logs all traffic in `packet_log.txt`.  
- Helps analyze unencrypted network communication.  

### 🔐 Security Learning  

- Demonstrates how attackers intercept data.  
- Highlights the importance of HTTPS, SSL, and TLS.  
- Improves understanding of network monitoring.  

---

## ⌨️ Task 2: Keylogging Simulation  

### 🔍 Description  

A controlled simulation of a keylogger to understand how keystroke logging attacks work at the system level.

### ⚙️ Features  

- Captures keyboard events using Python.  
- Logs alphanumeric and special keys.  
- Stores data in `key_log.txt`.  

### 🛡️ Security Learning  

- Shows how credentials can be stolen.  
- Emphasizes the need for MFA.  
- Encourages use of anti-malware protection.  

---

## 📂 Repository Structure  

```text
├── sniffer.py
├── keylogger.py
├── packet_log.txt
├── key_log.txt
├── Submission_Screenshots.docx
└── README.md

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shumaila804/Cyber-Security-Internship-Arch-Tech.git

2️⃣ Install dependencies
pip install scapy pynput

3️⃣ Run the sniffer
python sniffer.py

4️⃣ Run the keylogger (for lab use only)
python keylogger.py

⚠️ Ethical Notice

These tools are developed strictly for educational and defensive security research purposes only.
Unauthorized use on systems or networks without permission is illegal and unethical.

🏁 Conclusion

This project strengthened my foundation in network security and host-based monitoring.

🌟 Author

Shumaila Arif
Cyber Security Intern – Arch Technologies
