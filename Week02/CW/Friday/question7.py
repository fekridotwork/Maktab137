import csv

students = [
    {"name": "Ali", "age": 18, "score": 12},
    {"name": "Sara", "age": 19, "score": 17},
    {"name": "Reza", "age": 20, "score": 14},
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "score"])
    writer.writeheader()
    writer.writerows(students)


