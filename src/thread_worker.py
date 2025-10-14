import threading
import time

class Worker:
    def __init__(self):
        for _ in range(5):
            t = threading.Thread(target=self.run_task)
            t.start()  

    def run_task(self):
        time.sleep(2)  