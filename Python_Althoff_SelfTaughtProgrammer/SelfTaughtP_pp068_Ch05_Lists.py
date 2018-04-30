 
# A list is a container that stores objects in a specific order.

# There are two ways to create a list:
fruit = list() # Way 1
fruit = []     # Way 2
fruit = ["Apple", "Orange", "Pear"] # Creating/populating a list.
print(fruit)

# Use the "append" method to add items to end of list.
fruit.append("Banana") 
print(fruit)
fruit.append("Peach")
print(fruit)

# Lists can contain any/multiple data types.
random = [] 
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

# You can access specific items from a list using its index location.
print(random[3])
print(random[1])
# print(random[5]) # Trying to use a nonexistent index creates an error.

# Lists are mutable, which means you can add, remove, and modify objects.
fruit[2] = "Red" # Replaces the current [2] with "Red"
print(fruit)

# You can use the method .pop() to remove an item from the end of a list.
colors = ["blue", "green", "yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)

# You can concatenate lists.
colors1 = ["red", "orange"]
colors2 = ["yellow", "green"]
colors3 = colors1 + colors2
print(colors3)

# You can check whether an item is in a list with the boolean keyword "in".
print("yellow" in colors3)

# Adding the keyword "not" allows us to check if an item is not in the list.
print("yellow" not in colors3)

# The "len()" function returns the number of items in a list.
print(len(colors3))

# Here's an example of how you might use a list.
colors = ["purple", "orange", "green"]
guess = input("Guess a color: ")
guess = guess.lower()
if guess in colors:
    print("You guessed correctly!")
else:
    print("You have FAILED, you moron!")

