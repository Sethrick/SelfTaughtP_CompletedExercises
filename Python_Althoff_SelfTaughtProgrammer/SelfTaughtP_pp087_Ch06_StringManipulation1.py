
# Triple Strings are used when you need a string to span more than one line:
"""Line 1
Line 2
Line 3"""

# Strings are iterable, and you can access their contents by index:
author = "Kafka"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])
# print(author[5]) # This won't work, because the index doesn't exist.

# A "negative index" can be used to look up a location from right to left.
print(author[-1])
print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])
# print(author[-6]) # This won't work, because the index doesn't exist.

# Strings are immutable, you can't change them directly.
# Instead, you have to overwrite them with a new string of the same name.
ff = "F. Fitzgerald"
ff = "F. Scott Fitzgerald"
print(ff)

# String concatenation means adding strings together end-to-end to make a
# new, longer combined string.
cih = "The " + "Cat " + "in " + "the " + "Hat"
print(cih)

# String multiplication appends a string to itself a given number of times.
mult = "Cat" * 8
print(mult)

