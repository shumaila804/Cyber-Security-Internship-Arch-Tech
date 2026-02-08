from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

LOG_FILE = "packet_log.txt"

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"
            src_port = "-"
            dst_port = "-"

        else:
            src_port = "-"
            dst_port = "-"

        packet_size = len(packet)
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output = (
            f"[{time_stamp}] "
            f"Protocol: {protocol} | "
           f"Source: {src_ip}:{src_port} -> "
f"Destination: {dst_ip}:{dst_port} | "

            f"Size: {packet_size} bytes"
        )

        print(output)

        with open(LOG_FILE, "a") as log:
            log.write(output + "\n")

print("🔍 Advanced Network Sniffer Started...")
print("📌 Press CTRL + C to stop\n")

sniff(prn=analyze_packet, store=False)
