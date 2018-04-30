
# You can import built-in Python modules and use them in your code.

import math # Note: always import all modules at the top of the file.

cubed = math.pow(2,3) # Raises 2 to the power of 3.

print(cubed)

# Another useful built-in module is called "random".

import random

num = random.randint(0, 100) # Returns a random integer between the parameters.

print(num)

# The "statistics" module can calculate mean, median, and mode.

import statistics

numbers = [2, 5, 6, 3, 6, 4, 3, 6, 42,]
print(statistics.mean(numbers)) # average
print(statistics.median(numbers)) # middle number
print(statistics.mode(numbers))# most common number
