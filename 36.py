import xmltodict

f = open("payments.xml").read()
data_dict = xmltodict.parse(f)
root = data_dict["employees"]
employees = root["employee"]

for i in employees:
    if int(i["age"]) <= 30:
        print(i)
