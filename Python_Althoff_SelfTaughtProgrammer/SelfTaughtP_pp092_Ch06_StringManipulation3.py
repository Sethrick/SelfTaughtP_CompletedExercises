# The "split" method allows a string to be broken up into smaller parts.
# To do so, you pass in a string as a parameter to tell it where to divide.
# The result is a list of the sub-strings you've created.
whole = "This is a very long string. Don't you think so?".split(". ")
print(whole)
print(whole[0])
print(whole[1])

# The "join" method lets you add new characters between each
# character in a string.
ll = "llllllllllllllll"
lol = "o".join(ll)
print(lol)

# You can use the "join" method to turn a list into a single string by using
# the "join" method on an empty string and passing in a list as a parameter.
myList = ["The",
          "quick",
          "brown",
          "fox",
          "jumped..."]

fragment = "".join(myList)
print(fragment)

# To insert spaces into a joined list of strings, join on a single space string.
myOtherList = ["Eleven", "is", "a", "Jedi."]
sentence = " ".join(myOtherList)
print(sentence)

# The "strip" method is used on a string to strip leading/trailing white space.
myString = "     leading_trailing      "
myStrip = myString.strip()
print(myStrip)

# The "replace" method replaces every instance of string with another string.
gondor = "Aragorn is the king of Gondor. Let's make Gondor great again!"
arnor = gondor.replace("Gondor", "Arnor")
print(arnor)
