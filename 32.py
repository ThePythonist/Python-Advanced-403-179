import json

# with open("payments.json") as file:
#     root = json.load(file)
#     employees = root["employees"]
#
#     for i in employees:
#         print(f"{i["name"]} : {i["job_title"]}")


# ========================================================

file = open("payments.json")
root = json.load(file)
employees = root["employees"]

for i in employees:
    print(f"{i["name"]} : {i["job_title"]}")
