import json

file = open("payments.json")
root = json.load(file)
print(root)
