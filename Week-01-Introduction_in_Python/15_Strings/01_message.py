# String

message = "Hey, Developer!"
print(message)

my_message = 'This is Python Programming'
print(my_message)

multiline_message = '''This is a multiline message.
        It spans multiple lines.'''
print(multiline_message)


# String Length
print(len(message)) # 13; because it also counts the space

# Accessing String Characters
print(message[0])

# Slicing Strings
print(message[0:4]) # from 0 to 3
print(message[:4]) # from 0 to 3
print(message[2:]) # from 2 to the end
print(message[-3:]) # last 3 characters
print(message[:-3]) # all but last 3 characters
print(message[2:-3]) # from 2 to last 3 characters
print(message[-1:-3]) # nothing
print(message[-3:-1]) # from last 3 to 1
print(message[-3:2]) # nothing
print(message[2:1]) # nothing
print(message[3:3]) # nothing
