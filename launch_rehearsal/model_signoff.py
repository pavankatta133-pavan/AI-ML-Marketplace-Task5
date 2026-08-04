# model_signoff.py

models = [
    {
        "name": "Recommendation_Model_V1",
        "version": "1.0",
        "status": "Approved"
    },
    {
        "name": "Recommendation_Model_V2",
        "version": "2.0",
        "status": "Approved"
    }
]

print("=" * 60)
print("MODEL SIGN-OFF")
print("=" * 60)

for model in models:

    print(f"Model : {model['name']}")
    print(f"Version : {model['version']}")
    print(f"Approval : {model['status']}")
    print("-" * 40)

print("\nAll Models Ready For Production")