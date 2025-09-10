# worker/worker.py
# Separater asynchroner Worker-Prozess placeholder
import time

if __name__ == "__main__":
    print("Worker started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Worker stopped")
