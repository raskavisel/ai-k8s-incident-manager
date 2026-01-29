def remediation_action(incident):
    actions = {
        "CPU Issue": "Scale replicas",
        "Memory Issue": "Restart pod",
        "Latency Issue": "Rollback deployment",
        "Pod Restart Issue": "Check pod logs"
    }
    return actions.get(incident, "No action needed")

if __name__ == "__main__":
    # Test example
    incident = "CPU Issue"
    action = remediation_action(incident)
    print(f"For incident '{incident}', take action: {action}")
