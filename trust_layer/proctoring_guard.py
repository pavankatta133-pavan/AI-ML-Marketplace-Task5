import random
import time

print("=" * 60)
print("AI TRUST LAYER - PROCTORING HARDENING")
print("=" * 60)

events = [
    "Face Detected",
    "Looking Away",
    "Face Missing",
    "Looking Away",
    "Face Detected",
    "Looking Down",
    "Face Detected",
    "Face Missing",
    "Face Detected"
]

warning_count = 0

for event in events:

    print("Event :", event)

    if event in ["Looking Away", "Face Missing", "Looking Down"]:
        warning_count += 1
    else:
        warning_count = 0

    if warning_count >= 3:
        print("Violation Confirmed")
    else:
        print("False Positive Ignored")

    time.sleep(0.5)

print("\nTrust Layer Completed")