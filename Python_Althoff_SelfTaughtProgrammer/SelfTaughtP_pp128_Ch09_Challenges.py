
# 1) Find a file on your computer and print its contents using Python.

import os

qf = os.path.join("/", "media", "seth", "Anglachel_1", "Seth_Documents",
             "Documents_Current", "Technomancy",
             "Python_Althoff_SelfTaughtProgrammer", "Testing_Sandbox",
             "Quadratic_Formula.py")

with open(qf, "r") as f:
    print(f.read())

# 2) Write a program that asks a user a question, and saves their answer
#    to a file.

with open("Testing_Sandbox/Input_Save.txt", "w") as f:
    f.write(input("Type a sentence to save in a file: "))

# 3) Take the items in this list of lists:
#       [["Top Gun", "Risky Business", "Minority Report",],
#       ["Titanic", "The Revenant", "Inception"],
#       ["Training Day", "Man on Fire", "Flight"]]
#    and write them to a CSV file. The data from each list should be a row in
#    the file, with each item in the list separated by a comma.

import csv

with open("Testing_Sandbox/Ch7Chal3.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["Top Gun", "Risky Business", "Minority Report",])
    w.writerow(["Titanic", "The Revenant", "Inception"])
    w.writerow(["Training Day", "Man on Fire", "Flight"])

with open("Testing_Sandbox/Ch7Chal3.csv", "r") as f:
    print(f.read())
