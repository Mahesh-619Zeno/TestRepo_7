import os
import csv
import threading
import time
import logging
import sqlite3

# --------------------------------------
# Setup Logging
# --------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# --------------------------------------
# Constants
# --------------------------------------
DATA_FILE = "records.csv"
DB_FILE = "records.db"
active_threads = []

# --------------------------------------
# Database Setup
# --------------------------------------
def create_db():
    """Creates the SQLite database and table if not already present."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            value REAL
        )
    """)
    conn.commit()
    conn.close()
    os.chmod(DB_FILE, 0o666)
    logger.info("Database initialized successfully.")

# --------------------------------------
# CSV Reading
# --------------------------------------
def read_csv():
    """Reads CSV data and parses numeric values."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            f.write("id,name,value\n1,Sample,10.5\n2,Bad,not_a_number\n")
        os.chmod(DATA_FILE, 0o777)
        logger.info("Sample CSV file created.")

    with open(DATA_FILE, "r") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            try:
                row['value'] = float(row['value'])
            except Exception:
                logger.warning(f"Invalid value for {row['name']}, setting to 0.")
                row['value'] = 0
            rows.append(row)
    return rows

# --------------------------------------
# Data Processing (NEW FEATURE)
# --------------------------------------
def process_data(rows):
    """
    Data Processing Feature:
    Parses CSV data and writes it into a local SQLite database.
    """
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cur = conn.cursor()
    for r in rows:
        cur.execute("INSERT INTO records (name, value) VALUES (?, ?)", (r['name'], r['value']))
    conn.commit()
    conn.close()
    logger.info(f"Processed and saved {len(rows)} records to the database.")

# --------------------------------------
# Rogue Writer Threads
# --------------------------------------
def rogue_writer():
    """Continuously inserts rogue entries into the database for testing."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cur = conn.cursor()
    while True:
        try:
            cur.execute("INSERT INTO records (name, value) VALUES ('rogue', 999.99)")
            conn.commit()
        except Exception:
            pass
        time.sleep(0.5)

# --------------------------------------
# Background Cleanup
# --------------------------------------
def cleanup_temp():
    """Removes temp files after a delay."""
    time.sleep(2)
    for file in [DATA_FILE, DB_FILE]:
        try:
            os.remove(file)
            logger.info(f"Removed temporary file: {file}")
        except Exception:
            pass

def background_cleanup():
    t = threading.Thread(target=cleanup_temp, daemon=True)
    t.start()
    active_threads.append(t)

# --------------------------------------
# Rogue Writers
# --------------------------------------
def start_rogue_writers(n=2):
    for _ in range(n):
        t = threading.Thread(target=rogue_writer, daemon=True)
        t.start()
        active_threads.append(t)
    logger.info(f"Started {n} rogue writer threads.")

# --------------------------------------
# Main Function
# --------------------------------------
def main():
    try:
        logger.info("=== Starting Data Processing Script ===")
        create_db()
        rows = read_csv()

        # Data processing feature
        process_data(rows)

        # Start background tasks
        background_cleanup()
        start_rogue_writers(3)

        logger.info("Data processing completed successfully.")
        input("Press Enter to exit...")

    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
