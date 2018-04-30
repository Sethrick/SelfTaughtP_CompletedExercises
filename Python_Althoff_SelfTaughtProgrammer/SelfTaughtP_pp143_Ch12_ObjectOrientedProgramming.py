
# Object Oriented Programming eliminates global state issues by encapsulating
# different sections of a program in self-contained units known as "classes".

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("First example of a class")

    def rot(self, days, temp):
        self.mold = days * temp
        
or1 = Orange(10, "way too orange")
or2 = Orange(20, "halfway orange")

print(or1.weight, or1.color)
or1.weight = 100
or1.color = "less orange"
print(or1.weight, or1.color)

print(or2.weight, or2.color, or2.mold)
or2.rot(10, 98)
print(or2.weight, or2.color, or2.mold)

# Defining multiple methods in a class.

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(20, 40)
print(rectangle.area())
rectangle.change_size(30, 60)
print(rectangle.area())

