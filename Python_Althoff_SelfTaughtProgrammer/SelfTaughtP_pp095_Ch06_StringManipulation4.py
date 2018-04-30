
# The "index" method finds a character's first occurrence in a string.
poppins = "Mary Poppins"
i_poppins = poppins.index("i")
print(i_poppins)

# If you aren't sure if a character is used, employ exception handling.
try:
    martin = "I am that is"
    matthias = martin.index("z")
    print(matthias)
except:
    print("Letter not found")

# Use keywords "in" and "not in" to see if a string is in another string.
survival = "Who survives the game of thrones? Jon Snow does"
jonSnow = "Snow" in survival
jonArryn = "Arryn" in "Who survives the game of thrones? Jon Snow does"
jonConnington = "Connington" not in survival
print(jonSnow, jonArryn, jonConnington)

# Use "\" as an escape character in Python.
# For example, the first one doesn't work, and the second one does:
# print("Yup, she's "special" alright!")
print("She said, \"surely\"")
print("She said, 'surely'")
print('She said, "surely"')

# Use "\n" to create a new line.
print("Line1\nLine2\nLine3")

