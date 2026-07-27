review_queue = [
    {
        "student": "Rahul",
        "company": "Google",
        "status": "Pending Review"
    },
    {
        "student": "Rahul",
        "company": "Infosys",
        "status": "Approved"
    },
    {
        "student": "Rahul",
        "company": "Amazon",
        "status": "Pending Review"
    }
]

print("=" * 60)
print("ADMIN REVIEW QUEUE")
print("=" * 60)

for item in review_queue:
    print(f"Student : {item['student']}")
    print(f"Company : {item['company']}")
    print(f"Status : {item['status']}")
    print("-" * 40)