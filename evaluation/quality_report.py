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

scores = []

for _, student in students.iterrows():

    best = 0

    for _, job in jobs.iterrows():

        score = 0

        for skill in skills:
            score += min(student[skill], job[skill])

        if student["Experience"] >= job["Experience"]:
            score += 50

        if student["Location"] == job["Location"]:
            score += 30

        best = max(best, score)

    scores.append(best)

print("=" * 60)
print("QUALITY REPORT")
print("=" * 60)
print("Students Evaluated :", len(scores))
print("Average Match Score :", round(sum(scores) / len(scores), 2))
print("Highest Score :", max(scores))
print("Lowest Score :", min(scores))