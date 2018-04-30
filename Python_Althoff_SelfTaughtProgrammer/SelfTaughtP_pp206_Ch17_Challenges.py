# 1) Write a regular expression that matches the word "Dutch" in "The Zen of Python"

cat SelfTaughtP_pp195_Ch17_RegularExpressionSetup.txt | grep Dutch

# 2) Come up with a regular expression that matches all the digits in the string:
#    "Arizona 479, 501, 870. California 209, 213, 650."

echo Arizona 479, 501, 870. California 209, 213, 650. | grep -o [[:digit:]] | sed ':a;N;$!ba;s/\n/ /g'

# 3) Create a regular expression that matches any word that starts with any character and is followed by two o's. 
#    Then use Python's "re" module to match "boo" and "loo" in the sentence: "The ghost that says boo haunts the loo."

seth@Anglachel:/media/seth/Anglachel_1/Seth_Documents/Documents_Current/Technomancy/Python_Althoff_SelfTaughtProgrammer$ python3
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> hl = "The ghost that says boo haunts the loo."
>>> match = re.findall(".oo", hl, re.IGNORECASE)
>>> print(match)
['boo', 'loo']
>>> exit()
seth@Anglachel:/media/seth/Anglachel_1/Seth_Documents/Documents_Current/Technomancy/Python_Althoff_SelfTaughtProgrammer$
