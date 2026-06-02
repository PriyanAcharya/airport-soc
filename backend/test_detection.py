from parsers.pcap_parser import read_capture
from detectors.rules import detect_port_scan

packets = read_capture(
    "../scans/captures/attack_recon.pcapng"
)

alerts = detect_port_scan(packets)

print("\n=== ALERTS ===\n")

for alert in alerts:
    print(alert)
