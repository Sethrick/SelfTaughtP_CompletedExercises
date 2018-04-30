
# 1) Add a "square_list" class variable to a class called "Square" so that
#    every time you create a new "Square" object, the new object gets added
#    to the list.

class Square():
    square_list = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.dimensions = str(self.width) + " x " + str(self.len)
        self.sides = "{} by {} by {} by {}".format(self.width, # Chal 2
                                                   self.width,
                                                   self.len,
                                                   self.len)
        self.square_list.append(self.dimensions)
        
    def __repr__(self):
        return self.sides
    
sq1 = Square(1, 2)
sq2 = Square(2, 3)
sq3 = Square(3, 4)
print(Square.square_list)

# 2) Change the "Square class so that when you print a "Square" object, a
#    message prints that tells you the length of each of the 4 sides of the
#    shape.

print(sq1)

# 3) Write a function that takes two objects as parameters and returns "True"
#    if they are the same object, and "False" if not.

def same(x, y):
    print(x is y)

same(3, 3)
same(2, 3)

