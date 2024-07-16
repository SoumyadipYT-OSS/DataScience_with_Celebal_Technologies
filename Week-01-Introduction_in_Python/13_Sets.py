# Sets 
# unordered
# unindexed
# cannot contain duplicate values
# set objects are mutable

cs_courses = {'Statistics', 'Math', 'Physics', 'CompSci', 'Math', 'Databases'}
print(cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}
print(art_courses)


# 'intersection method' returns the common elements between two sets
print(cs_courses.intersection(art_courses))

# 'union method' combines the two sets and removes any duplicates
print(cs_courses.union(art_courses))