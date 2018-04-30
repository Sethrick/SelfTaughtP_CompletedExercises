# Quadratic Formula (not from book, just an idea):
from math import sqrt

# a = 1
a = int(input("Please enter the coefficient for \"a\": "))
# b = -6
b = int(input("Please enter the coefficient for \"b\": "))
# c = -2
c = int(input("Please enter the coefficient for \"c\": "))
x_add = (-b+(sqrt((b**2)-(4*a*c))))/2*a
x_sub = (-b-(sqrt((b**2)-(4*a*c))))/2*a
x = "{} or {}".format(x_add, x_sub)
print(x)
#print(3+(sqrt(11)))
#print(3-(sqrt(11)))

