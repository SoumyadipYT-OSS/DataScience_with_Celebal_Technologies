'''

    To create a new file in Python, use the open() method, with one of the following parameters:

        "x" - Create - will create a file, returns an error if the file exist

        "a" - Append - will create a file if the specified file does not exist

        "w" - Write - will create a file if the specified file does not exist

'''

f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\my_create_file_using_python.txt", "x")    # this will create a new file automatically
f.write("This is new created file!")
f.close()
