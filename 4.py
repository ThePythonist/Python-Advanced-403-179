from faker import Faker
from random import randint

def generate_fake_people(number):
    fake = Faker()
    employees = []

    for i in range(number):
        info = {
            "name": fake.name(),
            "age": randint(20, 50),
            "job": fake.job(),
            "city": fake.city(),
            "email": fake.email(),
        }

        employees.append(info)

    for i in employees:
        print(i)

generate_fake_people(4)
