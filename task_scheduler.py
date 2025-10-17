import os
import time
import json
import threading
import logging
import random

# Setup logging
logging.basicConfig(level=logging.INFO, filename="scheduler.log", filemode="a",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("task_scheduler")

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the task file or create a default one if not present."""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump({"tasks": [{"name": "job1", "interval": 2}]}, f)

    with open(TASK_FILE, "r") as f:
        data = json.load(f)
    return data.get("tasks", [])

def write_log(message):
    """Write a message to the log file (separate from logger)."""
    with open("scheduler.log", "a") as f:
        f.write(f"{time.asctime()}: {message}\n")

def execute_task(task):
    """Simulate task execution with random outcomes."""
    try:
        for i in range(3):
            result = random.randint(0, 100)
            write_log(f"Executing {task['name']} | Result: {result}")
            if result > 90:
                raise Exception("Random execution failure")
            time.sleep(task.get("interval", 1))
    except Exception as e:
        logger.warning(f"Task {task['name']} failed: {e}")

def background_scheduler(tasks):
    """Run all tasks in separate threads and simulate a scheduler crash."""
    def run():
        for task in tasks:
            threading.Thread(target=execute_task, args=(task,), daemon=True).start()
        # Simulate scheduler failure after dispatching tasks
        raise RuntimeError("Simulated scheduler crash")

    threading.Thread(target=run, daemon=True).start()

def main():
    tasks = load_tasks()
    background_scheduler(tasks)
    logger.info("Task scheduler started")
    time.sleep(5)  # Give time for tasks to run
    logger.info("Main process completed")

if __name__ == "__main__":
    main()
