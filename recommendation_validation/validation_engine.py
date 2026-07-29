recommendations = [
    {
        "student": "Rahul",
        "company": "Google",
        "score": 95
    },
    {
        "student": "Rahul",
        "company": "Infosys",
        "score": 87
    },
    {
        "student": "Rahul",
        "company": "Amazon",
        "score": 72
    }
]

print("=" * 60)
print("RECOMMENDATION VALIDATION")
print("=" * 60)

for rec in recommendations:

    if rec["score"] >= 90:
        status = "Highly Recommended"

    elif rec["score"] >= 75:
        status = "Recommended"

    else:
        status = "Needs Review"

    print(f"\nStudent : {rec['student']}")
    print(f"Company : {rec['company']}")
    print(f"Score : {rec['score']}")
    print(f"Validation : {status}")