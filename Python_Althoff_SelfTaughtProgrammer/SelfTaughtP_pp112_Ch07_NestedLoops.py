
# You can put loops inside of other loops, creating "outer" and "inner" loops.

for i in range(0, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)

# You can use nested loops to add each number in one list to all the
# numbers in another list.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []

for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

# You can nest a for-loop inside a while-loop and vice versa.

while input("y or n") != "n":
    for i in range(1, 6):
        print(i)
