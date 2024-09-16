import json
from colorama import Fore, Back, Style

file = open("payments.json")
root = json.load(file)
employees = root["employees"]
salaries = {}

for i in employees:
    avg = sum(i["monthly_payment"].values()) / len(i["monthly_payment"].values())
    salaries.update({i["name"]: avg})

print(salaries)

max_salary = max(salaries.values())

for k, v in salaries.items():
    if v == max_salary:
        print(Fore.MAGENTA + "Most Paid Employee :", k, ":", v)

print(Style.RESET_ALL, end='')
print("Back to normal")
