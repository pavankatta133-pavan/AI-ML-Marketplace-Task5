baseline = 7
improved = 1

reduction = ((baseline - improved) / baseline) * 100

print("=" * 60)
print("BASELINE COMPARISON")
print("=" * 60)

print("Baseline :", baseline)
print("Improved :", improved)
print(f"Reduction : {reduction:.2f}%")