from parsers.pcap_parser import read_capture
from detectors.rules import detect_port_scan
import requests

packets = read_capture(
    "../scans/captures/portscan_attack.pcap"
)

alerts = detect_port_scan(packets)

print("\n=== ALERTS ===\n")

for alert in alerts:
    print(alert)

    response = requests.post(
        "http://localhost:3000/alerts",
        json=alert
    )

    print("Status Code:", response.status_code)
