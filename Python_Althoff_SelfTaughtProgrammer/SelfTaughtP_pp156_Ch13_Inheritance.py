
# Inheritance in programming is like genetic inheritance. The "child" class
# inherits methods and variables from the "parent" class. Changes you make
# to the child class will not affect the parent class. If you define a method
# in a child class with the same name as a method in the parent class, the
# method defined in the child class will "overrride" the inherited class
# when you call the method.

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

shape1 = Shape(2, 3)
shape1.print_size()

class Square(Shape):
    def area(self): # method unique to child class
        return self.width * self.len

    def print_size(self): # overrides inherited "print_size" method
        print("I am {} by {}".format(self.width, self.len))

square1 = Square(3, 3)
print(square1.area())
square1.print_size()
