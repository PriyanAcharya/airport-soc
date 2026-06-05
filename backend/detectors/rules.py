def detect_port_scan(packets):
    scans = {}

    for packet in packets:
        if not packet.get("syn"):
            continue

        src = packet.get("src")
        dport = packet.get("dport")

        if not src or not dport:
            continue

        scans.setdefault(src, set()).add(dport)

    alerts = []

    for src, ports in scans.items():
        if len(ports) >= 5:
            alerts.append({
                "type": "Port Scan",
                "mitre": "T1046",
                "source_ip": src,
                "severity": "High",
                "ports_scanned": len(ports),
                "description": f"Scanned {len(ports)} unique ports"
            })

    return alerts


def detect_icmp_recon(packets):
    icmp_counts = {}

    for packet in packets:
        if packet.get("protocol") != "ICMP":
            continue

        src = packet.get("src")

        if not src:
            continue

        icmp_counts[src] = icmp_counts.get(src, 0) + 1

    alerts = []

    for src, count in icmp_counts.items():
        if count >= 3:
            alerts.append({
                "type": "Reconnaissance",
                "mitre": "T1595",
                "source_ip": src,
                "severity": "Medium",
                "icmp_packets": count,
                "description": f"Generated {count} ICMP packets"
            })

    return alerts
