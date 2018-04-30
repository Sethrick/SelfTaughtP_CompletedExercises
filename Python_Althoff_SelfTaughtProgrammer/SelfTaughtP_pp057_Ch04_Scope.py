 
# Faulty user input can cause errors, such as "divide by zero":
"""
a = input("Type a number: ")
b = input("Type another: ")
a = int(a)
b = int(b)
print(a/b) # if "b" is zero, the program breaks
"""

# ZeroDivisionError Example:
"""
a = input("Type a number: ")
b = input("Type another: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero")
"""

# Add ValueError:
try:
    a = input("Type a number: ")
    b = input("Type another: ")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Invalid Input. Please replace user and try again.")

# NOTE: Don't use variables defined in a "try" statement in the "except" clause.
# An error might occur before they are ever defined. For example:
"""
try:
    10/0
    c = "I will never be defined."
except ZeroDivisionError:
    print(c)
"""
