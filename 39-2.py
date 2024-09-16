import xmltodict

xml_data = open("flights.xml").read()
data = xmltodict.parse(xml_data)
root = data["flights"]
flights = root["flight"]
william_flights = []

for i in flights:
    for j in i["passengers"]["passenger"]:
        if j["name"] == "William Thompson":
            william_flights.append(i)

wrapped_data = {"flights": {"flight": william_flights}}
xml_string = xmltodict.unparse(wrapped_data, pretty=True)
open("william_flights.xml", "w").write(xml_string)
