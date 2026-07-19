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
print("RELEVANCE REGRESSION CHECK")
print("=" * 60)

for _, student in students.iterrows():

    best_score = 0

    for _, job in jobs.iterrows():

        score = 0

        for skill in skills:
            score += min(student[skill], job[skill])

        if student["Experience"] >= job["Experience"]:
            score += 50

        if student["Location"] == job["Location"]:
            score += 30

        best_score = max(best_score, score)

    if best_score >= 400:
        status = "No Relevance Regression"
    else:
        status = "Needs Review"

    print(f"{student['name']} -> Best Score: {best_score} -> {status}")