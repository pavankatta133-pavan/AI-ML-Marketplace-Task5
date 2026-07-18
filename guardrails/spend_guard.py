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
print("SPEND QUALITY GUARDRAIL")
print("=" * 60)

for _, student in students.iterrows():

    print(f"\nStudent: {student['name']}")

    for _, job in jobs.iterrows():

        score = 0

        for skill in skills:
            score += min(student[skill], job[skill])

        if student["Experience"] >= job["Experience"]:
            score += 50

        if student["Location"] == job["Location"]:
            score += 30

        if score >= 450:
            status = "Safe to Apply"
        elif score >= 350:
            status = "Apply Carefully"
        else:
            status = "Low Fit Warning"

        print(
            f"{job['company']} | {job['role']} | "
            f"Score: {score} | {status}"
        )