
# The keyword "is" returns "True" if two objects are the same object, and
# "False" if not.

class Person():
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# The first expression above evaluates to "True" because "bob" and "same_bob"
# variables both point to the same "Person" object. The variable "another_bob"
# points to a different "Person" object.

# Use the "is" keyword to check if a variable is "None".

class IsTester():
    def __init__(self, x):
        self.x = x

    def if_else(self):
        if self.x is None:
            print("x is None :( ")
        else:
            print("x is not None")

test1 = IsTester(10)
test1.if_else()
test1.x = None
test1.if_else()
