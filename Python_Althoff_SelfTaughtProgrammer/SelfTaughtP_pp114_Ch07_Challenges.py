
# 1) Print each item in the following list: ["The Walking Dead",
#    "Entourage", "The Sopranos", "The Vampire Diaries"].

showList = ["The Walking Dead",
            "Entourage",
            "The Sopranos",
            "The Vampire Diaries"]

for show in showList:
    print(show)

# 2) Print all the numbers from 25 to 30.

for i in range(25, 31):
    print(i)

# 3) Print each item in the list from the first challenge and their indexes.

showList = ["The Walking Dead",
            "Entourage",
            "The Sopranos",
            "The Vampire Diaries"]

for show in showList:
    print(showList.index(show), show)

# 4) Write a program with an infinite loop (with the option to type q to quit)
#    and a list of numbers. Each time through the loop ask the user to guess
#    a number on the list and tell them whether or not they guessed correctly.

numList = ["2", "4", "8"]
i = 1 # Must be set to zero for while-loop to run.

while i == 0:
    for num in numList:
        answer = input("Guess the number, or type \"q\" to quit: ")
        if answer == "q":
            print("You have chosen to quit the game. Goodbye!")
            i = 1
            break
        elif answer == num:
            print("You guessed correctly!")
        else:
            print("Wrong answer, you FAIL!")
        
# 5) Multiply all the numbers in the list [8, 19, 148, 4] with the numbers
#    in the list [9, 1, 33, 83], and append each result to a third list.

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
listMult = []

for i in list1:
    for j in list2:
        listMult.append(i * j)

print(listMult)



