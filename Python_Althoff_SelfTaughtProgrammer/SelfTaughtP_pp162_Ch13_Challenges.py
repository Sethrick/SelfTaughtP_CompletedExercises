
# 1) Create "Rectangle" and "Square" classes with a method called
#    "calculate_perimeter" that calculates the perimeter of the shapes they
#    represent. Create "Rectangle" and "Square" objects and call the method on
#    both of them.

class Shape():
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, l, w):
        self.len = l
        self.width = w

    def calculate_perimeter(self):
        return (self.len * 2) + (self.width * 2)

class Square(Rectangle):
    def calculate_perimeter(self):
        if self.len != self.width:
            return "This is not a square."
        else:
            return self.len * 4

    def change_size(self, c): # Challenge 2
        self.change = c

        self.len = self.len + self.change
        self.width = self.width + self.change
        
rectan1 = Rectangle(2, 4)
print(rectan1.calculate_perimeter())

square1 = Square(2, 4)
print(square1.calculate_perimeter())

square2 = Square(4, 4)
print(square2.calculate_perimeter())

# 2) Define a method in your "Square" class called "change_size" that allows
#    you to pass in a number that increases or decreases (if the number is
#    negative) each side of a "Square" object by that number.

square3 = Square(3, 3)
print(square3.len, square3.width, square3.calculate_perimeter())
square3.change_size(-1)
print(square3.len, square3.width, square3.calculate_perimeter())

# 3) Create a class called "Shape". Define a method in it called "what_am_i"
#    that prints "I am a shape" whan called. Change your "Square" and
#    "Rectangle" objects, and call the new method on both of them.

rectan2 = Rectangle(3, 6)
print(rectan2.calculate_perimeter())
rectan2.what_am_i()

square4 = Square(2, 2)
print(square4.calculate_perimeter())
square4.what_am_i()

# 4) Create a class called "Horse" and a class called "Rider". Use composition
#    to model a horse that has a rider.

class Rider():
    def __init__(self, n):
        self.name = n
        
class Horse():
    def __init__(self, n, r):
        self.name = n
        self.rider = r

rider1 = Rider("Woody")
horse1 = Horse("Blaze", rider1)
print(horse1.rider.name)
