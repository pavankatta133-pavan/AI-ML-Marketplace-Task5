students = [
    {
        "student_id": 1,
        "name": "Rahul",
        "skills": ["Python", "SQL", "Machine Learning", "Flask"]
    }
]

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
print("PLACEMENT DASHBOARD")
print("=" * 60)

student = students[0]

print("Student:", student["name"])
print()

for job in jobs:

    matched = list(set(student["skills"]).intersection(job["skills"]))

    score = len(matched)

    print("Company :", job["company"])
    print("Role :", job["role"])
    print("Matched Skills :", matched)
    print("Recommendation Score :", score)
    print("-" * 40)