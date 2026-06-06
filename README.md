# Airport SOC Monitoring Platform

## Overview

The Airport SOC Monitoring Platform is a cybersecurity monitoring solution designed for a simulated airport environment. The platform analyzes packet capture (PCAP) files, detects suspicious network activity, stores security alerts, and presents incidents through a Security Operations Center (SOC) dashboard.

The project demonstrates practical networking, cybersecurity, packet analysis, backend development, and security monitoring concepts.

---

## Features

### Network Traffic Analysis

* PCAP file parsing using Scapy
* TCP and ICMP traffic inspection
* Source and destination IP extraction
* Port analysis

### Detection Engine

* Reconnaissance Detection (MITRE ATT&CK T1595)
* Port Scan Detection (MITRE ATT&CK T1046)
* ICMP Echo Request filtering to reduce false positives

### Alert Management

* Alert generation
* SQLite alert storage
* Timestamped incidents
* REST API integration

### SOC Dashboard

* Alert visualization
* Timestamp display
* Severity classification
* Source IP tracking

---

## Architecture

PCAP File

↓

Scapy Packet Parser

↓

Detection Engine

↓

Alert Generation

↓

Node.js REST API

↓

SQLite Database

↓

Airport SOC Dashboard

---

## Technology Stack

### Networking

* Cisco Packet Tracer
* VLAN Concepts
* ACL Concepts
* DHCP Snooping
* Dynamic ARP Inspection

### Cybersecurity

* MITRE ATT&CK Framework
* Network Reconnaissance Detection
* Port Scan Detection
* SOC Monitoring Concepts

### Backend

* Node.js
* Express.js

### Database

* SQLite

### Packet Analysis

* Python
* Scapy

### Frontend

* HTML
* CSS
* JavaScript

---

## Detection Rules

### Reconnaissance Detection

MITRE ATT&CK: T1595

Detects excessive ICMP Echo Request activity generated during network reconnaissance.

### Port Scan Detection

MITRE ATT&CK: T1046

Detects hosts scanning multiple unique destination ports using TCP SYN packets.

---

## Example Alert

{
"id": 1,
"timestamp": "2026-06-06T09:27:15.921Z",
"type": "Reconnaissance",
"source_ip": "10.0.2.15",
"severity": "Medium"
}

---

## Screenshots


---

## Future Improvements

* ARP Poisoning Detection
* SSH Brute Force Detection
* Rogue DHCP Detection
* Dashboard Analytics
* MITRE ATT&CK Visualizations
* Threat Intelligence Integration
* Cloud Deployment

---

## Author

Priyan Acharya

Airport SOC Monitoring Platform 
