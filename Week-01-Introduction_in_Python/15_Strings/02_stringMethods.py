sentence = "Python is used in Data Science"

print("String capitalize Method")
str_capitalize = sentence.capitalize()
print(str_capitalize)

print("\n String Casefold Method")
str_casefold = sentence.casefold()
print(str_casefold)

print("\n String Center Method")
str_center = sentence.center(50)    # 50 is the width of the string, default is space; takes character as an argument
print(str_center)

print("\n String Count Method")
str_count = sentence.count('i')    # counts the number of times a character appears in the string
print(str_count)
# count a word in a sentence
str_count = sentence.count('Python')
print(str_count)
# count using three arguments (start, end, substring)
str_count = sentence.count('i', 1, 20)
print(str_count)


# string encode method is used for encoding the string
print("\n String Decode Method")
str_encode = sentence.encode()
print(str_encode)
# using two arguments
str_encode = sentence.encode(encoding='utf-8', errors='strict')   # utf-8 is the default encoding and 'strict' is the default error
print(str_encode)
#to decode the string
str_decode = str_encode.decode()
print(str_decode)


