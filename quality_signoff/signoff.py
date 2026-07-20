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
print("QUALITY SIGN-OFF")
print("=" * 60)

for _, student in students.iterrows():

    best_job = None
    best_score = 0

    for _, job in jobs.iterrows():

        score = 0

        for skill in skills:
            score += min(student[skill], job[skill])

        if student["Experience"] >= job["Experience"]:
            score += 50

        if student["Location"] == job["Location"]:
            score += 30

        if score > best_score:
            best_score = score
            best_job = job

    print(f"\nStudent : {student['name']}")
    print(f"Best Match : {best_job['company']}")
    print(f"Role : {best_job['role']}")
    print(f"Score : {best_score}")

print("\nQUALITY SIGN-OFF COMPLETED")