import sqlite3

conn = sqlite3.connect("cattle.db")
conn.execute("PRAGMA foreign_keys = ON;")
cur = conn.cursor()

# 1. User Table
cur.execute("""
CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_no TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

# 2. Cattle_Info
cur.execute("""
CREATE TABLE IF NOT EXISTS Cattle_Info (
    cattle_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    breed TEXT NOT NULL,
    age INTEGER,
    weight REAL,
    lactation_stage TEXT,
    parity INTEGER,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES User(user_id) ON DELETE CASCADE
)
""")

# 3. Milk_Yield
cur.execute("""
CREATE TABLE IF NOT EXISTS Milk_Yield (
    milk_yield_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    milk_yield REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

# 4. Feed_Data
cur.execute("""
CREATE TABLE IF NOT EXISTS Feed_Data (
    feed_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    feed_type TEXT,
    quantity REAL,
    feeding_time TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

# 5. Health_Data
cur.execute("""
CREATE TABLE IF NOT EXISTS Health_Data (
    health_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    body_temp REAL,
    heart_rate REAL,
    disease TEXT,
    vaccination_history TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

# 6. Activity_Data
cur.execute("""
CREATE TABLE IF NOT EXISTS Activity_Data (
    activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    walking_distance REAL,
    grazing_duration REAL,
    resting_hours REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

# 7. Alerts
cur.execute("""
CREATE TABLE IF NOT EXISTS Alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    alert_type TEXT,
    message TEXT,
    resolved INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

# 8. Reports
cur.execute("""
CREATE TABLE IF NOT EXISTS Reports (
    report_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    report_type TEXT,
    file_path TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES User(user_id) ON DELETE CASCADE
)
""")

# 9. DB_Update_Log
cur.execute("""
CREATE TABLE IF NOT EXISTS DB_Update_Log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT NOT NULL,
    field_changed TEXT NOT NULL,
    old_value TEXT,
    new_value TEXT,
    updated_by INTEGER,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(updated_by) REFERENCES User(user_id) ON DELETE SET NULL
)
""")

# 10. ML_Prediction_Log
cur.execute("""
CREATE TABLE IF NOT EXISTS ML_Prediction_Log (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cattle_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    milk_yield_pred REAL,
    disease_pred TEXT,
    model_version TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(cattle_id) REFERENCES Cattle_Info(cattle_id) ON DELETE CASCADE
)
""")

conn.commit()
conn.close()
print("Database and all tables created successfully!")