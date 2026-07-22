import os
import json

BASE_DIR = os.path.dirname(__file__)

resume = os.path.join(BASE_DIR, "..", "data", "resume.txt")

skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine Learning",
    "Communication",
    "Git",
    "Docker"
]

with open(resume, "r") as f:
    text = f.read()

found = []

for skill in skills:
    if skill.lower() in text.lower():
        found.append(skill)

result = {
    "document": "Resume",
    "skills": found
}

print(json.dumps(result, indent=4))