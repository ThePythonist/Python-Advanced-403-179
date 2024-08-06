import time


class SedanCar:
    def __init__(self, name, color, year, hp, delay):  # Constructor Method
        self.name = name
        self.color = color
        self.year = year
        self.horsepower = hp
        self.delay = delay
        self.engine = False
        self.speed = 0

    def startengine(self):
        print(f"{self.name} Started Engine")
        self.engine = True

    def accelerate(self, value):
        if self.engine == True:
            for i in range(value):
                time.sleep(self.delay)
                self.speed += 10
                print(self.speed)

    def horn(self):
        print("Beep")

    def brk(self):
        print("Breaking")


# Creating Instances ( Objects )

persia = SedanCar("Persia", "Sefid", 1399, "115", 3)
runna = SedanCar("Runna", "Ghermez", 1402, "110", 4)
dena = SedanCar("Dena", "Meshki", 1401, "120", 2)

# Using ( Calling Methods )
persia.startengine()
persia.accelerate(4)
