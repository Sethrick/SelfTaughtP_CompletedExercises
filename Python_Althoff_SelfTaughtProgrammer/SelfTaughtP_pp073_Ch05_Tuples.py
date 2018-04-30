
# Tuples are like lists, except they're immutable once they're created.
my_tuple = tuple() # One way to create a tuple.
your_tuple = () # Another way to create a tuple.
print(my_tuple)
print(your_tuple)

# To create a populated tuple, use the following syntax.
rndm = ("M. Jackson", 1958, True)
print(rndm)

# NOTE: A tuple with a single item still needs a comma after the item.
#       This ensures that Python knows the parentheses designate a tuple
#       and aren't part of a mathematical operation.

# This is a tuple.
st = ("Self-Taught", )
print(st)

# This is not a tuple.
nmbr = (9) + 1
print(nmbr)

# Immutability means that tuples can't be changed after they're created.
dys = ("1984", "Brave New World", "Fahrenheit 451")
# dys[1] = "Handmaid's Tale" # This returns an error.

# You can retrieve an item using it's index just like a list.
print(dys[1])

# You can also use the "in" keyword as with a list.
print("1984" in dys)

# The keyword "not" remains equally applicable.
print("1984" not in dys)

# Tuples are useful for unchanging values that you want to avoid corrupting.
# Tuples, unlike lists, can be used as keys in dictionaries.
