# live_monitor.py

models = [
    {
        "model": "Recommendation_Model_V1",
        "status": "Running",
        "requests": 1250,
        "latency_ms": 48
    },
    {
        "model": "Recommendation_Model_V2",
        "status": "Standby",
        "requests": 0,
        "latency_ms": 0
    }
]

print("=" * 60)
print("LIVE MODEL MONITOR")
print("=" * 60)

for model in models:
    print(f"Model      : {model['model']}")
    print(f"Status     : {model['status']}")
    print(f"Requests   : {model['requests']}")
    print(f"Latency(ms): {model['latency_ms']}")
    print("-" * 40)