import pandas as pd

jobs = pd.read_csv("../data/jobs.csv")

print("=" * 60)
print("COMPANY PORTAL")
print("=" * 60)

for _, job in jobs.iterrows():

    print(f"""
Company : {job['company']}
Role    : {job['role']}
Location: {job['Location']}
Experience Required : {job['Experience']} years
""")