class SedanCar:
    def __init__(self, color, year, hp):  # Constructor Method
        self.color = color
        self.year = year
        self.horsepower = hp

    def startengine(self):
        print("Started Engine")

    def accelerate(self):
        print("Accelerating")

    def horn(self):
        print("Beep")

    def brk(self):
        print("Breaking")


# Creating Instances ( Objects )

persia = SedanCar("Sefid", 1399, "115")
runna = SedanCar("Ghermez", 1402, "110")
dena = SedanCar("Meshki", 1401, "120")

# Using ( Calling Methods )

print(dena.horsepower)
print(persia.horsepower)
