from parsers.pcap_parser import read_capture
from detectors.rules import detect_icmp_recon
import requests

packets = read_capture(
    "../scans/captures/attack_recon.pcapng"
)

alerts = detect_icmp_recon(packets)

print("\n=== ALERTS ===\n")

for alert in alerts:
    print(alert)

    response = requests.post(
        "http://localhost:3000/alerts",
        json=alert
    )

    print("Status Code:", response.status_code)
