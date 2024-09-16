import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)
flights = root.findall('flight')
william_flights = []

for i in flights:
    passengers_root = i.find("passengers")
    passengers = passengers_root.findall("passenger")
    for j in passengers:
        # print(j.find("name").text)
        if j.find("name").text == "William Thompson":
            william_flights.append(i)

for i in william_flights:
    print(i.find("flight_number").text)
    print(i.find("origin").text, end=" to ")
    print(i.find("destination").text)
    print("-" * 50)
