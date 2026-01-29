import pandas as pd
from pathlib import Path

LOG_FILE = Path('../logs/metrics_log.csv')

def detect_incident(cpu, memory, latency, restarts):
    if cpu > 80:
        return "CPU Issue", 0.9
    elif memory > 80:
        return "Memory Issue", 0.9
    elif latency > 1000:
        return "Latency Issue", 0.9
    elif restarts >= 3:
        return "Pod Restart Issue", 0.8
    else:
        return "Normal", 0.0

def process_logs():
    if not LOG_FILE.exists():
        print("No metrics log found!")
        return
    df = pd.read_csv(LOG_FILE)
    for _, row in df.iterrows():
        incident, confidence = detect_incident(row['cpu'], row['memory'], row['latency'], row['restarts'])
        print(f"Detected: {incident} (Confidence={confidence})")

if __name__ == "__main__":
    process_logs()
