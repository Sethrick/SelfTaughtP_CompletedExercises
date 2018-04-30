
# 1. -------------------------------------
def square():
    """
    Takes a number as input and returns that number squared.
    :param a: int.
    :returns: int.
    """
    a = int(input("Type an integer number, then press \"enter\": "))
    b = a**2
    return(b)

print(square())

# 2. -------------------------------------
def strPrint(a):
    """
    Accepts a string as a parameter and prints it.
    :param a: str.
    :return: str.
    """
    print(a)

strPrint(3)

# 3. -------------------------------------
def paramDemo(a, b, c, d=3, e=4):
    """
    Takes three required & two optional parameter, adds, and prints them.
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :returns: int.
    """
    f = a + b + c + d + e
    print(f)

paramDemo(1, 2, 3, 4)

# 4. -------------------------------------
def divideBy2(x):
    """
    Divides an integer parameter by 2.
    :param x: int.
    :returns: int or float.
    """
    y = x / 2
    return(y)

def multiplyBy4(a):
    """
    Multiplies an int/float parameter by 4.
    :param a: int/float.
    :returns: int/float.
    """
    b = a * 4
    return(b)

result = divideBy2(8)
print(multiplyBy4(result))

# 5. -------------------------------------
def convert():
    """
    Converts a string to a float, catching exceptions.
    :param x: str.
    :returns: float.
    """
    try:
        x = input("Type an integer number and press \"enter\": ")
        x = float(x)
        print(x)
    except ValueError:
        print("Invalid input. Please reboot user and try again.")

convert()

# 6. -------------------------------------
"""
Add a docstring to challenges 1-5... completed.
"""

