li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li)

li.sort()
print('Original Variable:\t', li)   # Original list is sorted

s_li = sorted(li, reverse=True)
print('Sorted Variable:\t', s_li)   # Original list is sorted in reverse order

li.sort(reverse=True)
print('Original Variable:\t', li)   # Original list is sorted in reverse order


#-------------Example 2----------------
print("\n__Example 2__")
li2 = [-6, -5, -4, 1, 2, 3]
s_li2 = sorted(li2, key=abs)   # Sorts the list based on the absolute value
print('Sorted Variable:\t', s_li2)