
# Required parameters must be entered.
# Optional parameters use a default value if not replaced.

# For example:
def f(x=2):
    return x**x

print(f())
print(f(4))

# Please note that required parameters must be defined before optional ones
def add_it(x, y=10):
    return x + y

print(add_it(4))
print(add_it(5, 6))
