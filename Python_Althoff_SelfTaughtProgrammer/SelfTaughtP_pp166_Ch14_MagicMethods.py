
# All classes in Python INHERIT from the parent class called "Object". This
# is different from the fact that all classes in Python are an INSTANCE of the
# class called "type". Python uses the "magic" methods inherited from "Object"
# in several ways.

class Lion():
    def __init__(self, name):
        self.name = name

my_lion = Lion("Aslan")
print(my_lion)

# If you print a class, Python calls the magic "__repr__" method and prints
# whatever it returns. Normally, this prints something like:

# "<__main__.Lion object at 0x7f23690ba320>".

# However, you can override the inherited "__repr__" method to change that.

class Lion():
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name
    
this_lion = Lion("Dilbert")
print(this_lion)

# Any operand in an expression has to have a magic method telling it what to do.
# Here, we override the "__add__" method included in each integer object.

class AbsValueAdd():
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

av1 = AbsValueAdd(4)
av2 = AbsValueAdd(-10)

print(av1 + av2)

