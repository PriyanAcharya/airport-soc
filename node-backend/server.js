const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

const alerts = [
  {
    id: 1,
    type: "Reconnaissance",
    source_ip: "10.0.2.15",
    severity: "Medium"
  },
  {
    id: 2,
    type: "Port Scan",
    source_ip: "192.168.10.5",
    severity: "High"
  }
];

app.get("/", (req, res) => {
  res.json({
    message: "Airport SOC Backend Running",
    status: "online"
  });
});

app.get("/alerts", (req, res) => {
  res.json(alerts);
});

const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
