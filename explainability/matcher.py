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

def calculate_match(student, job):

    score = 0

    for skill in skills:
        score += min(student[skill], job[skill])

    if student["Experience"] >= job["Experience"]:
        score += 50

    if student["Location"] == job["Location"]:
        score += 30

    return score


student = students.iloc[0]

print("="*60)
print("JOB MATCHES")
print("="*60)

for _, job in jobs.iterrows():

    score = calculate_match(student, job)

    print(f"{job['company']} - {job['role']} : {score}")