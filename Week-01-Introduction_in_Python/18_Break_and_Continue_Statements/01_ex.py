nums = [1, 2, 3, 4, 5]

print("Break statement")
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)


print("\n")

print("Continue statement")
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)