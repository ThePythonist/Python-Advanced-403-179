import csv

data = [
    ['name', 'field', 'grade'],
    ['ahmad', 'computer engineering', '17.5'],
    ['setayesh', 'electrical engineering', '16.45'],
    ['peyman', 'computer engineering', '18.36'],
    ['kiana', 'civil engineering', '19.6'],
]

with open("students.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Done")
