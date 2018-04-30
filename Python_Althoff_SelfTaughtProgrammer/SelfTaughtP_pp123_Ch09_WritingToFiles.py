
# Use the "os" module to let your operating system format your file path.

import os

quad_path = os.path.join("/", "mnt", "Anglachel_1", "Seth_Documents", "Documents_Current", "Technomancy", "Python_Althoff_SelfTaughtProgrammer", "Testing_Sandbox", "Quadratic_Formula.py")

qf = open(quad_path, "r")

print(qf.read())

qf.close()
