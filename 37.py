import xmltodict

f = open("payments.xml").read()  # string
data_dict = xmltodict.parse(f)

root = data_dict["employees"]
employees = root["employee"]
python_salaries = []

for i in employees:
    if "python" in i["job_title"].lower():
        for j in i["monthly_payment"].values():
            python_salaries.append(int(j))

avg = sum(python_salaries) / len(python_salaries)
print("Average python developer income per month :", avg)
print(avg * 12)
