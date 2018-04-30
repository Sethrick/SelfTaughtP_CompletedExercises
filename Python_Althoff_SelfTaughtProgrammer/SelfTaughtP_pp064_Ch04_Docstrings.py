
# Only create a variable if you're going to use it again.
# Don't create a variable just to print or otherwise use it once.

# Bad:
x = 100
print(x)

# Good:
print(100)

# Creating a variable forces the program to permanently store that value,
# which takes up space.
