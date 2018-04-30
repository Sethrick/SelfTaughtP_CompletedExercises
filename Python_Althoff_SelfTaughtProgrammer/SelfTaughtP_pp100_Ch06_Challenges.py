
# 1) Print every character in the string "Camus"
print("Camus"[:])

# 2) Write a program that collects two strings from a user, inserts them into
#    the string "Yesterday I wrote a [response_one]. I sent it to
#    [response_two]!" and prints a new string.
response_one = "letter"
# response_one = input("Please enter a type of written document: ")
response_two = "Mars"
# response_two = input("Please enter a location: ")

print("""Yesterday I wrote a {}. \
I sent it to {}!""".format(response_one, response_two))

# 3) Use a method to make the string "aldous Huxley was born in 1894."
#    grammatically correct by capitalizing the first letter in the sentence.
sentence1 = "aldous Huxley was born in 1894."
sentence2 = sentence1.capitalize()
print(sentence2)

# 4) Take the string "Where now? Who now? When now?" and call a method that
#    returns a list that looks like: ["Where now?", "Who now?", "When now?"]
questions = "Where now? Who now? When now?"
q_list = questions.split("?")
print(q_list)

# 5) Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and
#    turn it into a grammatically correct string. There should be a space
#    between each word, but no space between "fence" and the period that
#    follows it. (Don't forget, you learned a method that turns a list of
#    strings into a single string.)
list1 = ["The", "fox", "jumped", "over", "the", "fence", "."]
list2 = " ".join(list1)
list3 = list2[0:-2] + "."
print(list3)

# 6) Replace every instance of "s" in "A screaming comes across the sky." with
#    a dollar sign.
g_rainbow = "A screaming comes across the sky.".replace("s", "$")
print(g_rainbow)

# 7) Use a method to find the first index of the character "m" in the string
#    "Hemingway".
poet = "Hemingway"
m_index = poet.index("m")
print(m_index)

# 8) Find dialogue in your favorite book (containing quotes) and turn it
#    into a string.
lotr_string = """\"A very nice well-spoken gentlehobbit is Mr. Bilbo, as I've
always said,\" the Gaffer declared. With perfect truth: for Bilbo was very
polite to him, calling him \"Master Hamfast\", and consulting him constantly
upon the growing of vegetables - in the matter of \"roots\", especially
potatoes, the Gaffer was recognized as the leading authority by all in the
neighbourhood (including himself)."""
print(lotr_string)

# 9) Create the string "three three three" using concatenation, and then again
#    using multiplication.
three1 = "three " + "three " + "three "
print(three1)
three2 = "three " * 3
print(three2)

# 10) Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only include the characters before the comma.
str1 = "It was a bright cold day in April, and the clocks were striking thirteen."
str2 = str1[0:33]
print(str2)
