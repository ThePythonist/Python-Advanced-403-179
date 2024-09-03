import json

f = open("states.json")
root = json.load(f)  # converts json into python dictionary
states = root["states"]

names = []
for i in states:
    names.append(i["name"])

# print(names)

f = open("state_names.json", "w")
json.dump(names, f, indent=2)
print("Done")
