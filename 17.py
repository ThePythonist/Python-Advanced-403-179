class Person:
    def __init__(self, name, age, ct, job, company):
        self.name = name
        self.age = age
        self.job = job
        self.company = company
        self.city = ct

    def talk(self):
        print(f"""
I'm {self.name} and I'm {self.age} years old
I live in {self.city} and I work as {self.job} at {self.company}.""")


person1 = Person("pedram", 25, "Shiraz", "Front-End Dev", "Irancell")

person1.talk()
