recommendations = [
    ("Google",95),
    ("Infosys",87),
    ("Amazon",72)
]

print("="*60)
print("RECOMMENDATION QUALITY CHECK")
print("="*60)

for company,score in recommendations:

    if score >= 75:
        print(f"{company} : PASS")
    else:
        print(f"{company} : REVIEW REQUIRED")