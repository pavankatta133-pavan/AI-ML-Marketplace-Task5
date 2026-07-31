# bias_checker.py

recommendations = [
    ("Rahul", "Male", 95),
    ("Anjali", "Female", 92),
    ("Arun", "Male", 84),
    ("Priya", "Female", 89)
]

print("=" * 60)
print("BIAS CHECKER")
print("=" * 60)

male = 0
female = 0

for _, gender, _ in recommendations:

    if gender == "Male":
        male += 1
    else:
        female += 1

print("Male Count :", male)
print("Female Count :", female)

if abs(male - female) <= 1:
    print("Bias Status : No Significant Bias")
else:
    print("Bias Status : Potential Bias Detected")