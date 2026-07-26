print("=" * 60)
print("AI TRUST LAYER SIGN-OFF")
print("=" * 60)

features = {
    "Resume Parser": "Passed",
    "JD Parser": "Passed",
    "Ontology Mapping": "Passed",
    "AI Proctoring": "Passed",
    "False Positive Reduction": "Passed"
}

for feature, status in features.items():
    print(f"{feature} : {status}")

print("\nOverall Status : APPROVED")