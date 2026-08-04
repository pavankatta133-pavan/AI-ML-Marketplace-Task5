# fairness_signoff.py

audit_results = [
    {
        "category": "Gender",
        "status": "Passed"
    },
    {
        "category": "Location",
        "status": "Passed"
    },
    {
        "category": "Experience",
        "status": "Passed"
    }
]

print("=" * 60)
print("FAIRNESS AUDIT SIGN-OFF")
print("=" * 60)

passed = True

for item in audit_results:

    print(f"Category : {item['category']}")
    print(f"Status   : {item['status']}")
    print("-" * 40)

    if item["status"] != "Passed":
        passed = False

if passed:
    print("\nFinal Fairness Status : APPROVED")
else:
    print("\nFinal Fairness Status : REVIEW REQUIRED")