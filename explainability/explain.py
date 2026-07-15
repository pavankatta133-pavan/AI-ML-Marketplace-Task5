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

student = students.iloc[0]

job = jobs.iloc[0]

print("="*60)
print("MATCH EXPLANATION")
print("="*60)

for skill in skills:

    if student[skill] >= job[skill]:

        print(f"✔ {skill} matched ({student[skill]}/{job[skill]})")

    else:

        print(f"✖ {skill} below requirement ({student[skill]}/{job[skill]})")

if student["Experience"] >= job["Experience"]:
    print("✔ Experience requirement satisfied")
else:
    print("✖ Experience requirement not satisfied")

if student["Location"] == job["Location"]:
    print("✔ Location matched")
else:
    print("✖ Location different")