from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP, ICMP


def read_capture(file_path):
    packets = rdpcap(file_path)

    results = []

    for packet in packets:
        entry = {
            "src": None,
            "dst": None,
            "protocol": None,
            "sport": None,
            "dport": None,
            "syn": False
        }

        if packet.haslayer(IP):
            entry["src"] = packet[IP].src
            entry["dst"] = packet[IP].dst

        if packet.haslayer(TCP):
            entry["protocol"] = "TCP"
            entry["sport"] = packet[TCP].sport
            entry["dport"] = packet[TCP].dport

            flags = packet[TCP].flags
            entry["syn"] = bool(flags & 0x02)

        if packet.haslayer(ICMP):
            entry["protocol"] = "ICMP"

        results.append(entry)

    return results


