🛡️ Cyber Security Internship - Month 1 Project Report

Organization: Arch-Technologies Intern Name: Shumaila Arif Domain: Cyber Security 

📌 Project Overview
This repository contains the technical tasks completed during the first month of my Cyber Security internship at Arch Technologies. The focus of this month was on developing tools for network traffic analysis and understanding the mechanics of host-based monitoring through keystroke logging.

🛰️ Task 1: Network Traffic Sniffer
Objective
The goal of this project was to build a network sniffer in Python capable of capturing and analyzing real-time network traffic. This tool helps in understanding how data flows across a network and how packets are structured.


Technical Implementation

Language: Developed using Python.


Functionality: The script captures live packets and extracts critical information, including protocol types (TCP, UDP), source and destination IP addresses, and packet sizes.


Data Logging: All captured traffic is automatically logged into packet_log.txt for forensic and security analysis.

Security Insights
Through this task, I analyzed how unencrypted data can be intercepted by unauthorized parties. This highlights the critical importance of using encrypted protocols like HTTPS, SSL, and TLS to protect data integrity.

⌨️ Task 2: Keylogging Simulation
Objective
This task involved simulating a basic keylogger in a controlled and safe environment to understand the mechanism of keystroke logging attacks.

Technical Implementation

Method: Used Python scripts to capture and monitor local keyboard events.


Storage: Captured keys are securely logged into a local file named key_log.txt.


Analysis: The script is designed to handle both alphanumeric characters and special keys (such as Space, Enter, and Shift) to provide a comprehensive log of user activity.

Risk Assessment & Mitigation
Keyloggers represent a significant threat, often used for credential theft. By simulating this attack, I evaluated the risks associated with such malware and the necessity of implementing defensive measures, such as:


Anti-keylogging software.


Multi-Factor Authentication (MFA) to prevent unauthorized access even if passwords are compromised.

📂 Repository Structure
sniffer.py: The main script for network packet sniffing.

keylogger.py: The script for keystroke logging simulation.

packet_log.txt: Log file containing captured network traffic data.

key_log.txt: Log file containing recorded keystrokes.

Submission_Screenshots.docx: Detailed report with visual evidence of the tasks.

🏁 Conclusion
The completion of these tasks has provided a solid foundation in network monitoring and host-based security analysis. All source code and logs have been compiled according to the submission requirements of Arch-Technologies
