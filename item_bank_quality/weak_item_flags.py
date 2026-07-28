questions = [
    {"id": 1, "status": "Healthy"},
    {"id": 2, "status": "Weak Item"},
    {"id": 3, "status": "Healthy"},
    {"id": 4, "status": "Weak Item"}
]

print("=" * 60)
print("WEAK ITEM FLAGS")
print("=" * 60)

for q in questions:

    if q["status"] == "Weak Item":
        print(f"Question {q['id']} flagged for Admin Review")