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
