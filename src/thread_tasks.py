import threading
import time

def run_task():
    def worker():
        time.sleep(5)
        print("Task complete")

    for _ in range(5):
        t = threading.Thread(target=worker)
        t.start()
