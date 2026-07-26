recommendations = [
    {
        "company": "Google",
        "role": "ML Engineer",
        "score": 95
    },
    {
        "company": "Infosys",
        "role": "Python Developer",
        "score": 88
    },
    {
        "company": "Amazon",
        "role": "Data Analyst",
        "score": 82
    }
]

print("=" * 60)
print("RECOMMENDATION DASHBOARD")
print("=" * 60)

recommendations.sort(key=lambda x: x["score"], reverse=True)

for rec in recommendations:

    print(f"{rec['company']} - {rec['role']} ({rec['score']}%)")