
# Encapsulation in object oriented programming means that both variables
# (state) and methods (for altering state or doing calculations) are grouped
# together in "objects".

class Rectangle():
    def __init__(self, w, l):
        self.width = w # Variables (state)
        self.len = l

    def area(self): # Method which makes a calculation based on state
        return self.width * self.len

rec1 = Rectangle(4, 5)
print(rec1.area())

# Encapsulation also refers to hiding a class's internal data to prevent the
# code outside of the object (the "client") from reading it.

class Data():
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data0 = Data()
print(data0.nums) # Changing a variable by accessing it directly.
data0.nums[0] = 8
print(data0.nums)

data1 = Data()
print(data1.nums)
data1.change_data(1, 9) # Changing a variable via the "change_data" method.
print(data1.nums)

# Some programming languages have "private variables" that can only be accessed
# by objects of the class in which they are contained. Python does not, using
# naming conventions instead. A Python method that starts with an underscore
# ("_") is not supposed to be accessed by any code outside of its class
# (client code).

class PublicPrivateExample():
    def __init__(self):
        self.public = "safe"
        self.private = "unsafe"

    def public_method(self):
        # clients can use this.
        print(self.public)

    def private_method(self):
        # clients should not use this.
        print(self.private)
        
ppe = PublicPrivateExample()
ppe.public_method()
ppe.private_method()

