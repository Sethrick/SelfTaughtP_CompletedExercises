
# You can use a "break-statement" to terminate a loop.

for i in range(1, 5): # Without break statement
    print(i)

for i in range(11, 15): # With break statement
    print(i)
    break

# You can use a while loop with a break statement to create a program that
# keeps asking a user for input until they type "q" to quit.

queries = ["What's your name? ",
           "What is that? ",
           "Why are you such a muggle? "]

n = 0
while True:
    print("Type q to quit")
    a = input(queries[n])
    if a == "q":
        break
    n = (n + 1) % 3
