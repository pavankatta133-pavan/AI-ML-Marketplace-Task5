students = {
    "student_id": 1,
    "name": "Rahul",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning",
        "Flask"
    ]
}

jobs = [
    {
        "company": "Google",
        "role": "ML Engineer",
        "skills": [
            "Python",
            "Machine Learning",
            "SQL"
        ]
    },
    {
        "company": "Infosys",
        "role": "Python Developer",
        "skills": [
            "Python",
            "Flask",
            "Git"
        ]
    },
    {
        "company": "Amazon",
        "role": "Data Analyst",
        "skills": [
            "SQL",
            "Python",
            "Excel"
        ]
    }
]

print("=" * 60)
print("RECOMMENDATION ENGINE V1")
print("=" * 60)

for job in jobs:

    matched = list(
        set(students["skills"]).intersection(job["skills"])
    )

    score = len(matched)

    print(f"\nCompany : {job['company']}")
    print(f"Role : {job['role']}")
    print(f"Matched Skills : {matched}")
    print(f"Score : {score}")