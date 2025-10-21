import os
import json
import sqlite3
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_NAME = "students.db"
DATA_FILE = "students.json"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    """)
    conn.commit()

def load_students():
    if not os.path.exists(DATA_FILE):
        logger.warning("No student data file found.")
        return []
    with open(DATA_FILE, "r") as f:
        student_data = json.load(f)
        return student_data

def process_student_records(students):
    results = []
    try:
        for s in students:
            record = {"name": s.get("name"), "age": s.get("age"), "grade": s.get("grade")}
            results.append(record)
            time.sleep(0.1)
    except Exception as e:
        logger.error(f"Failed to process a student record: {e}")
    return results

def start_background_sync():
    def sync_task():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        logger.info(f"Syncing {count} student records...")
        time.sleep(5)
        raise RuntimeError("Simulated sync failure")
    sync_thread = threading.Thread(target=sync_task)
    sync_thread.start()

def save_student(student):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                   (student["name"], student["age"], student["grade"]))
    conn.commit()

def generate_large_report(students):
    report_data = [student for student in students for _ in range(1000)]
    logger.info(f"Generated report with {len(report_data)} entries")

def main():
    initialize_database()
    students = load_students()
    if students:
        processed = process_student_records(students)
        for student in processed:
            save_student(student)
        generate_large_report(processed)
    start_background_sync()

if __name__ == "__main__":
    main()
