
# Dictionaries organize information by linking a "key" to a "value".
# This linking of two objects is called "mapping".
# The "key" can be used to look up the "value" but not vice versa.
# Dictionaries do not store information in a particular order.

# Dictionaries are represented by curly brackets.
my_dict = dict()
your_dict = {}
print(my_dict)
print(your_dict)

# Use a colon to separate the key from the value.
fruits = {"Apple":
          "Red",
          "Banana":
          "Yellow"}

# Note that the printed dictionary might not be in the original order.
print(fruits)

# The key is used with brackets like an index to retrieve the value.
print(fruits["Apple"])

# Add key-value pairs to a dictionary using the following syntax.
fruits["Blueberry"] = "Blue"

# For example:
facts = dict()

facts["code"] = "fun"
print(facts["code"])

facts["Bill"] = "Gates"
print(facts["Bill"])

facts["founded"] = "1776"
print(facts["founded"])

# Unlike a dictionary value, a dictionary key must be immutable.
# A string or a tuple can be a key, but not a list or dictionary.
# As with lists and tuples, "in" and "not" can be used to search.
# However, they can only be used to search keys, not values.
bill = dict({"Bill Gates":
             "charitable"})

print("Bill Gates" in bill)
print("Bill Gates" not in bill)

# If you try to access a nonexistent key, you'll raise an exception.
# print(bill["Bill Doors"])

# Use the "del" keyword to delete a key-value pair.
books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}

del books["The Trial"]

print(books)

# Here's one example of a program using a dictionary:
rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "hive"
          }

n = input("Type a number: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found :(")




