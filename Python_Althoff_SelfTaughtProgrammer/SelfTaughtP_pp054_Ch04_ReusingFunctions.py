
# Functions can do more than just return values.
# They can also encapsulate functionality you want to reuse.

# For example:
def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(5)

# Take a look at the following two examples. One uses functions, one doesn't.

# Version 1:
print("\nVersion 1:")
n = input("Type a number: ")
n = int(n)
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

n = input("Type a number: ")
n = int(n)
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

n = input("Type a number: ")
n = int(n)
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

# Version 2:
print("\nVersion 2:")
def even_odd():
    n = input("Type a number: ")
    n = int(n)
    if n % 2 == 0:
        print("n is even")
    else:
        print("n is odd")

even_odd()
even_odd()
even_odd()
