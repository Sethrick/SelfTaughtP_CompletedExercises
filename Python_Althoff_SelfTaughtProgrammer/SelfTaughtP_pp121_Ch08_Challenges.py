
# 1) Call a different function from the statistics module.

import statistics

sample_list = [253, 53, 743, 446, 777, 777, 564, 557, 473, 552, 47574]

print(statistics.mean(sample_list))
print(statistics.median(sample_list))
print(statistics.mode(sample_list))

# 2) Create a module named "cubed" with a function that takes a number as a parameter, and returns the number cubed. Import and call the function from another module.

import SelfTaughtP_pp121_Ch8_Challenges2

cubeA = SelfTaughtP_pp121_Ch8_Challenges2.cubed(3)

print(cubeA)
