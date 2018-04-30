
# 1) Define a class called "Apple" with four instance variables that represent
#    four attributes of an apple.

class Apple():
    def __init__(self, c, t, w, d):
        self.color = c
        self.taste = t
        self.weight = w
        self.diameter = d

apple1 = Apple("green", "tart", "0.5lb", "3 inches")
print(apple1.color, apple1.taste, apple1.weight, apple1.diameter)

# 2) Create a "Circle" class with a method called "area" that calculates and
#    returns its area. Then create a "Circle" object, call "area" on it, and
#    print the result. Use Python's "pi" function in the built-in "math" module.

import math

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        p = math.pi
        a = p * (self.radius**2)
        return a

cir1 = Circle(2)
print(cir1.area())

# 3) Create a "Triangle" class with a method called "area" that calculates and
#    returns its area. Then create a "Triangle" object, call area on it, and
#    print the result.

class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        a = (self.base * self.height)/2
        return a

tri1 = Triangle(4, 4)
print(tri1.area())

# 4) Make a "Hexagon" class with a method called "calculate_perimeter" that
#    calculates and returns its perimeter. Then create a "Hexagon" object, call
#    "calculate_perimeter" on it, and print the result.

class Hexagon():
    def __init__(self, sl):
        self.sideLen = sl

    def calculate_perimeter(self):
        p = self.sideLen * 6
        return p

hex1 = Hexagon(2)
print(hex1.calculate_perimeter())

