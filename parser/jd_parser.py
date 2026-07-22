import os
import json

BASE_DIR = os.path.dirname(__file__)

jd = os.path.join(BASE_DIR, "..", "data", "job_description.txt")

skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine Learning",
    "Communication",
    "Git",
    "Docker"
]

with open(jd, "r") as f:
    text = f.read()

found = []

for skill in skills:
    if skill.lower() in text.lower():
        found.append(skill)

result = {
    "document": "Job Description",
    "skills": found
}

print(json.dumps(result, indent=4))