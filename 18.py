from math import pi


class Circle:
    def __init__(self, radius):
        self.r = radius

    def perimeter(self):
        return self.r * 2 * pi

    def area(self):
        return self.r * self.r * pi


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


# ---------------- Polymorphic methods ----------------

def calculate_area(shape):
    print(shape.area())


def calculate_perimeter(shape):
    print(shape.perimeter())


shape1 = Rectangle(5, 6)
shape2 = Circle(4)

print("Polymorphic method for shape1 :")
calculate_area(shape1)
calculate_perimeter(shape1)
print("-"*50)
print("Polymorphic method for shape2 :")
calculate_area(shape2)
calculate_perimeter(shape2)
