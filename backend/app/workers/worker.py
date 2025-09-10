# backend/app/workers/worker.py
# Einfache Worker-Schleife placeholder
import time

class Worker:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            # Poll queue, process jobs
            time.sleep(1)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    w = Worker()
    try:
        w.start()
    except KeyboardInterrupt:
        w.stop()
