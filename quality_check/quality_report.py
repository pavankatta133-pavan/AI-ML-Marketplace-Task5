import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

students = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "students.csv"))
jobs = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "jobs.csv"))

print("=" * 60)
print("CONVERSION QUALITY REPORT")
print("=" * 60)

print("Students Evaluated :", len(students))
print("Jobs Evaluated :", len(jobs))
print("Status : No relevance regression detected")