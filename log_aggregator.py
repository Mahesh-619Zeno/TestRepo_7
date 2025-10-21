import os
import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("log_aggregator")

LOG_DIR = "app_logs"
AGGREGATED_FILE = "aggregated_logs.txt"

def create_sample_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    for i in range(3):
        with open(os.path.join(LOG_DIR, f"log_{i}.txt"), "w") as f:
            for j in range(5):
                f.write(f"{time.asctime()}: Event {random.randint(1,100)}\n")

def aggregate_logs():
    files = os.listdir(LOG_DIR)
    f_out = open(AGGREGATED_FILE, "w")
    for file in files:
        f_in = open(os.path.join(LOG_DIR, file), "r")
        f_out.write(f_in.read())
        f_in.close()
        time.sleep(1)
    f_out.close()
    logger.info("Logs aggregated")

def background_aggregator():
    def worker():
        while True:
            try:
                aggregate_logs()
                if random.random() > 0.7:
                    raise RuntimeError("Simulated aggregation failure")
                time.sleep(5)
            except Exception as e:
                logger.warning(f"Aggregation error: {e}")
                time.sleep(2)
    t = threading.Thread(target=worker)
    t.start()

def main():
    create_sample_logs()
    background_aggregator()
    logger.info("Log aggregator started")
    time.sleep(10)
    logger.info("Main thread exiting")

if __name__ == "__main__":
    main()