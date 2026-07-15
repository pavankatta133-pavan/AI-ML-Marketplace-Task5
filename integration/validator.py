import pandas as pd

students = pd.read_csv("../data/students.csv")
jobs = pd.read_csv("../data/jobs.csv")

skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine_Learning",
    "Communication"
]

def calculate_score(student, job):

    score = 0

    for skill in skills:
        score += min(student[skill], job[skill])

    if student["Experience"] >= job["Experience"]:
        score += 50

    if student["Location"] == job["Location"]:
        score += 30

    return score


student = students.iloc[0]

results = []

for _, job in jobs.iterrows():

    score = calculate_score(student, job)

    results.append({
        "company": job["company"],
        "role": job["role"],
        "score": score
    })

results = sorted(results, key=lambda x: x["score"], reverse=True)

print("=" * 60)
print("VALIDATED MATCHES")
print("=" * 60)

for result in results:
    print(result)