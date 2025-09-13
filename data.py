import sqlite3
import pandas as pd
import os

DB_PATH = "cattle.db"

# Mapping of table names to their expected CSV file
TABLES = {
    "User": "./data/user.csv",
    "Cattle_Info": "./data/cattle_info.csv",
    "Milk_Yield": "./data/milk_yield.csv",
    "Feed_Data": "./data/feed_data.csv",
    "Health_Data": "./data/health_data.csv",
    "Activity_Data": "./data/activity_data.csv",
}

def import_csv_to_sqlite(table_name, csv_file, db_path=DB_PATH):
    """Import a CSV into SQLite table"""
    if not os.path.exists(csv_file):
        print(f"⚠️ Skipping {table_name} (CSV not found: {csv_file})")
        return

    df = pd.read_csv(csv_file)

    with sqlite3.connect(db_path) as conn:
        try:
            df.to_sql(table_name, conn, if_exists="append", index=False)
            print(f"✅ Inserted {len(df)} rows into {table_name} from {csv_file}")
        except Exception as e:
            print(f"❌ Error inserting into {table_name}: {e}")

def main():
    for table, csv_file in TABLES.items():
        import_csv_to_sqlite(table, csv_file)

if __name__ == "__main__":
    main()
