questions = [
    {
        "id": 1,
        "question": "What is Python?",
        "usage": 120,
        "accuracy": 92
    },
    {
        "id": 2,
        "question": "Explain AI.",
        "usage": 8,
        "accuracy": 45
    },
    {
        "id": 3,
        "question": "Define Machine Learning.",
        "usage": 65,
        "accuracy": 81
    },
    {
        "id": 4,
        "question": "Explain Flask.",
        "usage": 5,
        "accuracy": 38
    }
]

print("=" * 60)
print("ITEM BANK QUALITY CHECK")
print("=" * 60)

for q in questions:

    if q["usage"] < 10 or q["accuracy"] < 50:
        status = "Weak Item"
    else:
        status = "Healthy"

    print(f"Question ID : {q['id']}")
    print(f"Question : {q['question']}")
    print(f"Usage : {q['usage']}")
    print(f"Accuracy : {q['accuracy']}%")
    print(f"Status : {status}")
    print("-" * 50)