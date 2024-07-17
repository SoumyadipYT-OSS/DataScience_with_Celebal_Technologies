nums = [1, 2, 3, 4, 5]

print("\n For loop")
for num in nums:
    print(num)

print("\n For loop with break statement")
for i in nums:
    if i == 3:
        print('Found!')
        break
    print(i)

print("\n For loop with continue statement")
for j in nums:
    if j == 3:
        print('Found!')
        continue    # continue will skip the rest of the loop and start over
    print(j)


print("\n For loop with nested for loop")
for k in nums:
    for l in 'abc':
        print(k, l)


print("\n For loop with range")
for i in range(10):
    print(i)

print("\n For loop with range starting from 1")
for i in range(1, 11):
    print(i)