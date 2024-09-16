import json

file = open("payments.json")
root = json.load(file)
employees = root["employees"]
salaries = []

for i in employees:
    for j in i["monthly_payment"].values():
        salaries.append(j)

print("Average Salary of Last Year :", sum(salaries) / len(salaries))
