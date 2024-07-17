# Comparisons:

# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object Identity:      is

# and
# or
# not


language = "Python"

# Example Equal '=='
if language == "JavaScript":
    print("Language is JavaScript")
elif language == "Python":
    print("Language is Python")
else:
    print("No match")

# Example Not Equal '!='
user = "Admin"
logged_in = True

if user == "Admin" and logged_in != False:
    print("Admin is logged in")
else:
    print("Bad Creds")


# Example Greater Than '>'
a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a > b)  # False because they are equal in length and also in values
print(id(a) == id(b))