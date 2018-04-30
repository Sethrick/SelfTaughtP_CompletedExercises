"""
# Built-in functions are built into the programming language
# to accomplish common tasks.

# For example:
print(len("Monty"))
print(str(600)) # Can accept most objects
print(int("37")) # Only accepts numeric strings and floating point numbers
print(float(30)) # Only accepts numeric strings and integers

# For example:
print(int("110"))
print(int(20.54))
print(float("16.04"))
print(float(99))

# This will return an error:
print(int("Half-Blood Prince"))
"""

# The built-in function "input" collects information from a user:
age = input("Enter your age: ")
int_age = int(age)
if int_age < 21:
    print("You are young")
else:
    print("Wow, you are old!")


