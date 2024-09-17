import csv

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Access values using column names
        if float(row["grade"]) >= 17:
            print(row)
