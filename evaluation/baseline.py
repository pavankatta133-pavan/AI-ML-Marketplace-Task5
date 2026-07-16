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
print("MATCH QUALITY BASELINE")
print("=" * 60)

for _, student in students.iterrows():

    best_score = 0
    best_company = ""

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
            best_company = job["company"]

    print(f"{student['name']} -> {best_company} | Score: {best_score}")