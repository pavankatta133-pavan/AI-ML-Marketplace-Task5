ontology = {
    "Programming": [
        "Python",
        "SQL"
    ],
    "Framework": [
        "Flask"
    ],
    "Artificial Intelligence": [
        "Machine Learning"
    ],
    "Soft Skills": [
        "Communication"
    ],
    "Tools": [
        "Git",
        "Docker"
    ]
}

print("=" * 60)
print("SKILL ONTOLOGY")
print("=" * 60)

for category, skills in ontology.items():

    print(f"\n{category}")

    for skill in skills:
        print(f"   - {skill}")