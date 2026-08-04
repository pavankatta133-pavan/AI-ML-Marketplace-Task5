# model_registry.py

models = [
    {
        "model_name": "Recommendation_Model_V1",
        "version": "1.0",
        "status": "Production"
    },
    {
        "model_name": "Recommendation_Model_V2",
        "version": "2.0",
        "status": "Staging"
    }
]

print("=" * 60)
print("MODEL REGISTRY")
print("=" * 60)

for model in models:
    print(f"Model Name : {model['model_name']}")
    print(f"Version    : {model['version']}")
    print(f"Status     : {model['status']}")
    print("-" * 40)