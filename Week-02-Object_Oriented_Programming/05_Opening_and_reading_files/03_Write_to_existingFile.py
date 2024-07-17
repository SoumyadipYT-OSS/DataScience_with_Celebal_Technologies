'''

    To write to an existing file, you must add a parameter to the open() function:

    "a" - Append - will append to the end of the file
    "w" - Write - will overwrite any existing content

'''

f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demo2.txt", "a")
f.write("Now the file has more content!")
f.close()


f1 = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demo2.txt", "r")
print(f1.read())
f1.close()


# the "w" method will overwrite the entire file.
f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demo3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demo3.txt", "r")
print(f.read())
f.close()
