import os
import time
import json
import threading
import logging
import random

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("task_scheduler")

# Constants
TASK_FILE = "tasks.json"
LOG_FILE = "scheduler.log"
DEFAULT_TASKS = {"tasks": [{"name": "job1", "interval": 2}]}

def load_tasks():
    """Load tasks from a JSON file. Creates a default task file if it doesn't exist."""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump(DEFAULT_TASKS, f, indent=2)

    with open(TASK_FILE, "r") as f:
        data = json.load(f)
    return data.get("tasks", [])

def write_log(message):
    """Append a message to the log file with a timestamp."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.asctime()}: {message}\n")

def execute_task(task):
    """Simulate task execution with random results and possible failure."""
    try:
        for _ in range(3):
            result = random.randint(0, 100)
            msg = f"Executing {task['name']} | Result: {result}"
            write_log(msg)
            logger.info(msg)

            if result > 90:
                raise Exception("Random execution failure")

            time.sleep(task.get("interval", 1))
    except Exception as e:
        logger.warning(f"Task {task['name']} failed: {e}")
        write_log(f"Task {task['name']} failed: {e}")

def background_scheduler(tasks):
    """Start each task in a separate background thread."""
    def run():
        for t in tasks:
            threading.Thread(target=execute_task, args=(t,), daemon=True).start()
        # Uncomment the line below to simulate a crash
        # raise RuntimeError("Simulated scheduler crash")

    threading.Thread(target=run, daemon=True).start()

def main():
    tasks = load_tasks()
    background_scheduler(tasks)
    logger.info("Task scheduler started")
    time.sleep(5)  # Allow background tasks to run briefly
    logger.info("Main process completed")

if __name__ == "__main__":
    main()
