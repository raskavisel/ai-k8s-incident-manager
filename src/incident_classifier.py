import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from pathlib import Path

MODEL_FILE = Path('../models/classifier.joblib')
MODEL_FILE.parent.mkdir(exist_ok=True, parents=True)

# Load training data
data = pd.read_csv('../data/incident_data.csv')
X = data[['cpu_usage', 'memory_usage', 'latency', 'restarts']]
y = data['incident_type']

# Split for evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, MODEL_FILE)
print(f"Model saved at {MODEL_FILE}")

# Example prediction
sample = [[85, 40, 120, 0]]
pred = clf.predict(sample)
prob = clf.predict_proba(sample).max()
print(f"Sample prediction: Incident={pred[0]}, Confidence={prob:.2f}")
