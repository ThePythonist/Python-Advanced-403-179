import json

# ================= Deserializing =================

f = open("states.json", "r")
root = json.load(f)
states = root["states"]
selected_states = []
for i in states:
    if i["name"] in ["Alaska", "Florida", "New York"]:
        selected_states.append(i)

# print(state_names)

# ================= Seralizing =================

output = {
    "states": selected_states
}

f = open("selected_states.json", "w")
json.dump(output, f, indent=2)
