
# Abstraction mean reducing something to the bare, essential characteristics
# relevant to the problem at hand.

# Polymorphism is the ability use the same interface (function or method) to
# handle different underlying forms (data types) of input.

print("Hello World!")   # string as parameter
print(200)              # integer as a parameter
print(200.1)            # float as parameter

print(type("Hello World!"))   # returns: <class 'str'>
print(type(200))              # returns: <class 'int'>
print(type(200.1))            # returns: <class 'float'>

# Drawing shapes without polymorphism:
# shapes = [tr1, sq1, cr1]
# for a_shape in shapes:
#     if type(a_shape) == "Triangle":
#         a_shape.draw_triangle()
#     if type(a_shape) == "Square":
#         a_shape.draw_square()
#     if type(a_shape) == "Circle":
#         a_shape.draw_circle

# Drawing shapes with polymorphism:
# shapes = [tr1, sq1, cr1]
# for a_shape in shapes:
#     a_shape.draw()

