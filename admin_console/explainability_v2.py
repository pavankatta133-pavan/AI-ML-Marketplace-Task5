students = {
    "student_id": 1,
    "name": "Rahul",
    "skills": ["Python", "SQL", "Machine Learning", "Flask"]
}

jobs = [
    {
        "company": "Google",
        "role": "ML Engineer",
        "skills": ["Python", "Machine Learning", "SQL"]
    },
    {
        "company": "Infosys",
        "role": "Python Developer",
        "skills": ["Python", "Flask", "Git"]
    },
    {
        "company": "Amazon",
        "role": "Data Analyst",
        "skills": ["SQL", "Python", "Excel"]
    }
]

print("=" * 60)
print("RECOMMENDATION EXPLAINABILITY V2")
print("=" * 60)

for job in jobs:

    matched = list(set(students["skills"]).intersection(job["skills"]))
    missing = list(set(job["skills"]) - set(students["skills"]))

    score = len(matched)

    print(f"\nCompany : {job['company']}")
    print(f"Role : {job['role']}")
    print(f"Recommendation Score : {score}")
    print(f"Matched Skills : {matched}")
    print(f"Missing Skills : {missing}")

    if score >= 3:
        print("Explanation : Excellent match based on current skills.")
    elif score == 2:
        print("Explanation : Good match with minor skill gaps.")
    else:
        print("Explanation : Needs additional skill development.")