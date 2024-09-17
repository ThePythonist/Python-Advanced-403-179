import csv


def write(filename, data):
    header = ["name", "field", "grade"]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print(f'{filename} has been created successfully.')


def read(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        computer_students = []
        for row in reader:
            if "computer" in row[1]:
                # print(row)
                computer_students.append(row)

        write("computer_students.csv", computer_students)


students = [
    ["arian", "chemical engineering", 16.5],
    ["mohammadali", "computer engineering", 18.5],
    ["sara", "literature ", 17.35],
    ["kiana", "law ", 14.78],
]

# write("students.csv",students)
read("students.csv")
