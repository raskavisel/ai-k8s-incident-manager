import joblib
from pathlib import Path

MODEL_FILE = Path('../models/classifier.joblib')
clf = joblib.load(MODEL_FILE)

def decide_action(cpu, memory, latency, restarts):
    sample = [[cpu, memory, latency, restarts]]
    pred = clf.predict(sample)[0]
    prob = clf.predict_proba(sample).max()
    
    if prob >= 0.8:
        action_type = "Auto-Fix"
    elif prob >= 0.5:
        action_type = "Suggest Fix"
    else:
        action_type = "Alert Human"
    
    return pred, prob, action_type

if __name__ == "__main__":
    # Test with sample metrics
    incident, confidence, action = decide_action(85, 40, 120, 0)
    print(f"Incident={incident}, Confidence={confidence:.2f}, Action={action}")
