
# You can use a "continue-statement" to stop the current iteration of a loop
# and skip to the next iteration.

for i in range(1, 4):
    if i == 2:
        continue
    print(i)

# You can do the same thing with a while-loop.

i = 5
while i > 0:
    if i == 4:
        i -= 1
        continue
    if i == 2:
        i -= 1
        continue
    print(i)
    i -= 1
