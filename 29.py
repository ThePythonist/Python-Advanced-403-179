import json

f = open("states.json")
root = json.load(f)  # converts json into python dictionary
states = root["states"]

for i in states:
    print(i["name"])
