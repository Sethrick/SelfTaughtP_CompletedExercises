

# The word "syntax" refers to the rules for sentence structure in a language.
# The following program executes because it follows Python syntax.

myString = "Hello World!"
print(myString)

# The following program will not work, because it contains a syntax error.
"""
print("Hello World!)
SyntaxError: EOL while scanning string literal
"""

# In Python, an error that is not a "syntax error" is called an "exception".
# Example - ZeroDivisionError:
"""
x = 6/0
print(x)

Traceback (most recent call last):
  File "/home/seth/Documents/SelfTaughtP_pp024_SyntaxRules_ErrorsExceptions.py", line 17, in <module>
    x = 6/0
ZeroDivisionError: division by zero
"""

# A syntax error is always fatal. An exception isn't always fatal.
# Example - IndentationError:
"""
y = 2
    x = 4

SyntaxError: unexpected indent
"""
