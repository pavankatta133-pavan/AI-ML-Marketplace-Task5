# drift_detector.py

historical_scores = [92, 90, 91, 93, 89]
current_scores = [82, 80, 79, 81, 78]

historical_avg = sum(historical_scores) / len(historical_scores)
current_avg = sum(current_scores) / len(current_scores)

drift = historical_avg - current_avg

print("=" * 60)
print("MODEL DRIFT MONITOR")
print("=" * 60)

print(f"Historical Average : {historical_avg:.2f}")
print(f"Current Average    : {current_avg:.2f}")
print(f"Drift Value        : {drift:.2f}")

if drift > 5:
    print("\nStatus : Drift Detected")
else:
    print("\nStatus : Model Stable")