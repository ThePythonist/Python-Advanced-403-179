import xml.etree.ElementTree as ET

# XML data
xml_data = open("flights.xml").read()

# Parse XML
root = ET.fromstring(xml_data)

# Find flights with destination "Paris"
paris_flights = []

# Looping through flights and selecting
for flight in root.findall("flight"):
    destination = flight.find("destination")
    if destination.text.lower() == "paris":
        print(flight.find("flight_number").text)
