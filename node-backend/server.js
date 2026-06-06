const db = require("./database/db");
const express = require("express");
const cors = require("cors");

const app = express();

app.use(express.static("public"));
app.use(cors());
app.use(express.json());

app.get("/alerts", (req, res) => {
    db.all("SELECT * FROM alerts", [], (err, rows) => {
        if (err) {
            return res.status(500).json({
                error: err.message
            });
        }

        res.json(rows);
    });
});

app.post("/alerts", (req, res) => {
    const { type, source_ip, severity } = req.body;

    db.run(
        `INSERT INTO alerts (type, source_ip, severity)
         VALUES (?, ?, ?)`,
        [type, source_ip, severity],
        function(err) {
            if (err) {
                return res.status(500).json({
                    error: err.message
                });
            }

            res.status(201).json({
                message: "Alert created",
                id: this.lastID
            });
        }
    );
});

app.get("/seed", (req, res) => {
    db.run(
        `INSERT INTO alerts (type, source_ip, severity)
         VALUES (?, ?, ?)`,
        ["Reconnaissance", "10.0.2.15", "Medium"],
        function(err) {
            if (err) {
                return res.status(500).json({
                    error: err.message
                });
            }

            res.json({
                message: "Alert inserted",
                id: this.lastID
            });
        }
    );
});

const PORT = 3000;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

