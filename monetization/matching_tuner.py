import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

students = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "students.csv"))
jobs = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "jobs.csv"))

skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine_Learning",
    "Communication"
]

print("=" * 60)
print("MATCHING TUNER")
print("=" * 60)

for _, student in students.iterrows():

    recommendations = []

    for _, job in jobs.iterrows():

        skill_score = 0

        for skill in skills:
            skill_score += min(student[skill], job[skill])

        experience_bonus = 50 if student["Experience"] >= job["Experience"] else 0
        location_bonus = 30 if student["Location"] == job["Location"] else 0

        total_score = skill_score + experience_bonus + location_bonus

        recommendations.append({
            "company": job["company"],
            "role": job["role"],
            "score": total_score
        })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["score"],
        reverse=True
    )

    print(f"\nStudent: {student['name']}")

    for r in recommendations[:3]:
        print(f"{r['company']} | {r['role']} | Score: {r['score']}")