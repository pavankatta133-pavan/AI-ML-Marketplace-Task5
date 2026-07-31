# fairness_audit.py

recommendations = [
    {
        "student": "Rahul",
        "gender": "Male",
        "company": "Google",
        "score": 95
    },
    {
        "student": "Anjali",
        "gender": "Female",
        "company": "Google",
        "score": 92
    },
    {
        "student": "Arun",
        "gender": "Male",
        "company": "Infosys",
        "score": 84
    },
    {
        "student": "Priya",
        "gender": "Female",
        "company": "Amazon",
        "score": 89
    }
]

print("=" * 60)
print("FAIRNESS & BIAS AUDIT")
print("=" * 60)

male = 0
female = 0

for rec in recommendations:

    print(f"Student : {rec['student']}")
    print(f"Gender : {rec['gender']}")
    print(f"Company : {rec['company']}")
    print(f"Score : {rec['score']}")
    print("-" * 40)

    if rec["gender"] == "Male":
        male += 1
    else:
        female += 1

print("\nAudit Summary")
print("Male Recommendations :", male)
print("Female Recommendations :", female)

if male == female:
    print("Fairness Status : Balanced")
else:
    print("Fairness Status : Needs Review")