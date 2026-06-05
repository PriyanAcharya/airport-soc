const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./database/alerts.db", (err) => {
    if (err) {
        console.error("Database connection error:", err.message);
    } else {
        console.log("Connected to SQLite database");
    }
});

db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            source_ip TEXT,
            severity TEXT
        )
    `);
});

module.exports = db;
