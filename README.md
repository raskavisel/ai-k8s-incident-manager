# AI-Driven Kubernetes Incident Detection & Auto-Remediation

## Overview
This project simulates a **production-grade AI system** that monitors Kubernetes clusters, detects incidents using **rule-based and ML methods**, and recommends or performs safe remediation actions.

It demonstrates:
- Metrics monitoring and logging
- Rule-based anomaly detection
- Machine learning classification of incidents
- Confidence-based decision engine
- Safe auto-remediation strategy

## Features
- Generates simulated Kubernetes metrics (CPU, Memory, Latency, Pod Restarts)
- Detects anomalies using simple rules
- Classifies incident type using a trained Random Forest model
- Decides whether to auto-fix, suggest fix, or alert human
- Maps incidents to safe remediation actions

## Repository Structure

ai-k8s-incident-manager/ │ ├── data/                  # Training dataset ├── logs/                  # Metrics logs ├── models/                # Saved ML model └── src/                   # Source code

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt

2. Run metrics generator:
python src/metrics_generator.py

3. Run rule-based detection:
python src/rule_detector.py

4. Train ML classifier:
python src/incident_classifier.py

5. Make ML-based decisions:
python src/decision_engine.py

6.Check recommended actions:
python src/remediation_actions.py

## Future Enhancements
- Connect to real Kubernetes cluster using Python kubernetes client
- Add web-based dashboard for real-time monitoring
- Extend ML model for multiple clusters & more incident types
