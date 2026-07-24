events = [
    "Face Detected",
    "Looking Away",
    "Looking Away",
    "Face Detected",
    "Face Missing",
    "Face Detected",
    "Looking Down",
    "Looking Away",
    "Face Detected",
    "Face Missing",
    "Face Missing",
    "Face Missing"
]

baseline_alerts = 0
improved_alerts = 0
consecutive = 0

print("=" * 60)
print("FALSE POSITIVE REDUCTION")
print("=" * 60)

for event in events:

    print("Event:", event)

    # Baseline system
    if event != "Face Detected":
        baseline_alerts += 1

    # Improved system
    if event != "Face Detected":
        consecutive += 1
    else:
        consecutive = 0

    if consecutive >= 3:
        improved_alerts += 1
        consecutive = 0

print("\nBaseline Alerts :", baseline_alerts)
print("Improved Alerts :", improved_alerts)

reduction = baseline_alerts - improved_alerts

print("False Positives Reduced :", reduction)