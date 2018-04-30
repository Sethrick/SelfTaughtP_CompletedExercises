
# Another way to automatically close the file you're using is to encapsulate
# your code in a "with-statement", a compound statement with an  action that
# automatically occurs when Python leaves it.

import os

write_path = os.path.join("/", "media", "seth", "Anglachel_1", "Seth_Documents",
                         "Documents_Current", "Technomancy",
                         "Python_Althoff_SelfTaughtProgrammer", "Testing_Sandbox",
                         "Write_Testing.py")

my_list = list()

with open(write_path, "w") as wp:
    wp.write("This is a test of the write and read functions!")

with open(write_path, "r") as wp:
    my_list.append(wp.read())

print(my_list)

    
