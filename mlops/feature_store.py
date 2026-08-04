# feature_store.py

features = {
    "Python": 90,
    "SQL": 85,
    "Machine Learning": 88,
    "Communication": 80,
    "Experience": 2
}

print("=" * 60)
print("FEATURE STORE")
print("=" * 60)

for feature, value in features.items():
    print(f"{feature} : {value}")

print("\nFeature Store Status : Active")