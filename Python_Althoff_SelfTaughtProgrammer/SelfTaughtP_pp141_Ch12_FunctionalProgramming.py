
# Functional programming doesn't use global variables.
# It only uses parameters which are passed to functions.

# Definition of Functional Programming:
#   "Functional code is characterized by one thing: the absence of side effects.
#   It doesn't rely on data outside the current function, and it doesn't change
#   data that exists outside the current function.

# Example of a function that has side-effects:
a = 0
def increment():
    global a
    a += 1

# Example of a function with no side-effects:
def increment(a):
    return a + 1

