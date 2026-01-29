import random
import time
import pandas as pd
from pathlib import Path

LOG_FILE = Path('../logs/metrics_log.csv')
LOG_FILE.parent.mkdir(exist_ok=True, parents=True)

def generate_metrics():
    cpu = random.randint(20, 95)       # CPU usage %
    memory = random.randint(20, 95)    # Memory usage %
    latency = random.randint(50, 2000) # Response time in ms
    restarts = random.randint(0, 5)    # Pod restarts
    return cpu, memory, latency, restarts

def save_metrics():
    cpu, memory, latency, restarts = generate_metrics()
    df = pd.DataFrame([[cpu, memory, latency, restarts]], 
                      columns=['cpu', 'memory', 'latency', 'restarts'])
    if LOG_FILE.exists():
        df.to_csv(LOG_FILE, mode='a', index=False, header=False)
    else:
        df.to_csv(LOG_FILE, index=False)
    print(f"Saved: CPU={cpu}%, Memory={memory}%, Latency={latency}ms, Restarts={restarts}")

if __name__ == "__main__":
    while True:
        save_metrics()
        time.sleep(5)
