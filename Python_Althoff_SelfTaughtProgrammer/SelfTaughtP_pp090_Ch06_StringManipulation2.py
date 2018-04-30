# You can change some or all of the characters in a string to
# upper or lower case by employing the ".upper()" and ".lower()" methods.
case = "Change CASE Example"
print(case)
case = case.upper()
print(case)
case = "Change Case EXample".lower()
print(case)
case = case.capitalize()
print(case)

# The "format" method allows you to pass in strings or variables
# using curly brackets as placeholders.
formMeth = "My first use of the {} method.".format("format")
print(formMeth)
myVar = "best and most awesomest"
formMeth = "My first use of the {} method.".format(myVar)
print(formMeth)
quote = "I {} that {}".format("am", "is")
print(quote)

# You can use the "format" method to create customized strings
# based on user input.
"""
n2 = input("Enter a noun: ")
adj = input("Enter an adjective: ")
n1 = input("Enter another noun: ")
v = input("Enter a verb: ")

r = "The {} {} the {} {}.".format(n1,
           v,
           adj,
           n2)

print(r)
"""

