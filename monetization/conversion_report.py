import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

students = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "students.csv"))
jobs = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "jobs.csv"))

print("=" * 60)
print("CONVERSION REPORT")
print("=" * 60)

print("Students:", len(students))
print("Jobs:", len(jobs))
print("Top Recommendations Per Student: 3")
print("Ranking tuned for better paid conversion.")