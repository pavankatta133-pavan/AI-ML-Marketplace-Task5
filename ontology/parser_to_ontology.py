parsed_skills = [
    "Python",
    "SQL",
    "Flask",
    "Machine Learning",
    "Communication",
    "Git"
]

ontology = {
    "Programming": ["Python", "SQL"],
    "Framework": ["Flask"],
    "Artificial Intelligence": ["Machine Learning"],
    "Soft Skills": ["Communication"],
    "Tools": ["Git", "Docker"]
}

print("=" * 60)
print("PARSER TO ONTOLOGY")
print("=" * 60)

for category, skills in ontology.items():

    matched = []

    for skill in parsed_skills:

        if skill in skills:
            matched.append(skill)

    print(category, ":", matched)