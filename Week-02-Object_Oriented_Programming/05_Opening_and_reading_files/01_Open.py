'''

    The key function for working with files in Python is the open() function.

    The open() function takes two arguments: the name of the file (as a string), and the mode in which the file should be opened.

    There are four kinds of modes:

    "r" - Read mode (default)
    "a" - Append mode
    "w" - Write mode
    "x" - Create mode

    ---------------------------------------------
    In addition you can specify if the file should be handled in binary mode and if the file should be opened in a way that allows both reading and writing.

    The syntax for the open function is:

        open(filename, mode)
    ----------------------------------------------

    If the file should be handled as binary or text mode:

    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)

'''



f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demofile.txt")
print(f)
print(f.read())
f.close()   # this 'close()' method should be used, if it is not used it will run in the background.

f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demofile.txt", "rt")
print(f.read())     # It will gives the same output as above
f.close()  
