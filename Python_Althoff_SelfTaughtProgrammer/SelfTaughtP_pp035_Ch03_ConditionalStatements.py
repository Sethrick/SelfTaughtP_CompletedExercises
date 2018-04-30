
# Making decisions with control structures/conditional statements.

# Pseudocode:
#   If (expression) Then
#       (code_area1)
#   Else
#       (code_area2)

# Basic if/else control structure
home = "America"

if home == "America":
    print("Hello America")
else:
    print("Hello World")
    
# Multiple if statements
x = 2

if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")
    
# Nested if statements
x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)

# Else-If statements
home = "Thailand"

if home == "Japan":
    print("Hello, Japan")
elif home == "Thailand":
    print("Hello, Thailand")
elif home == "India":
    print("Hello, India")
elif home == "China":
    print("Hello, China")
else:
    print("Hello, World")

# Combining conditional statements
x = 100

if x == 10:
    print("x = 10")
elif x == 20:
    print("x = 20")
else:
    print("I don't know")

if x == 100:
    print("x = 100")

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
