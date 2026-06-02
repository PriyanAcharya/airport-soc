from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Airport SOC API",
    description="Security Operations Center backend for airport network monitoring",
    version="1.0.0"
)

class Alert(BaseModel):
    id: int
    alert_type: str
    source_ip: str
    severity: str
    description: str

alerts_db = [
    Alert(
        id=1,
        alert_type="Reconnaissance",
        source_ip="10.0.2.15",
        severity="Medium",
        description="Nmap scan detected against target host"
    ),
    Alert(
        id=2,
        alert_type="ICMP Activity",
        source_ip="10.0.2.15",
        severity="Low",
        description="Multiple ICMP echo requests observed"
    )
]

@app.get("/")
def root():
    return {
        "message": "Airport SOC API Running",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "airport-soc"
    }

@app.get("/alerts", response_model=List[Alert])
def get_alerts():
    return alerts_db

@app.get("/alerts/{alert_id}")
def get_alert(alert_id: int):
    for alert in alerts_db:
        if alert.id == alert_id:
            return alert

    return {"error": "Alert not found"}

@app.get("/stats")
def stats():
    return {
        "total_alerts": len(alerts_db),
        "high": len([a for a in alerts_db if a.severity == "High"]),
        "medium": len([a for a in alerts_db if a.severity == "Medium"]),
        "low": len([a for a in alerts_db if a.severity == "Low"])
    }
