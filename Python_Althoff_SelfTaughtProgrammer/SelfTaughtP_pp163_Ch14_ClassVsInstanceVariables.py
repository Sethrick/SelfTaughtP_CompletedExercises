
# Each class in Python is technically an object of class "type".

class Square:
    pass

print(Square)

# Classes have two types of variables: class variables and instance variables.

# The variables we've seen so far have been instance variables, defined by the
# syntax "self" (referring to the particular objects which instantiate them).

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

my_rectangle = Rectangle(3, 4)
my_rectangle.print_size()

# Class variables, on the other hand, belong to the original class (which is an
# object of the class "type"). This means that if an instance of a class you
# create changes a class variable, it is changed for all members of the class.
# This is similar to a global variable, but only within the class. You use the
# "self" prefix to access class variables just like for instance variables.

class Rectangle():
    recs = [] # defined outside of the method that initializes objects.

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len)) # use "self" prefix to access

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

r1 = Rectangle(3, 4)
r2 = Rectangle(4, 5)
r3 = Rectangle(5, 6)

print(Rectangle.recs)
print(r1.recs)
