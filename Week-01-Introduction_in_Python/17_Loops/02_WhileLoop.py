# While Loop
# While loop is used to execute a block of statements repeatedly until a given condition is satisfied.

x = 0
while x < 10:
    print(x)
    x += 1


print("\n While loop with break statement")
x = 0
while True:
    if x == 5:
        break   # here break 
    print(x)
    x += 1