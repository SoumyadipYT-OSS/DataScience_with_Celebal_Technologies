from os import path, remove
if path.exists("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\my_create_file_using_python.txt"):
    remove("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\my_create_file_using_python.txt")
else:
    print("The file does not exist")


'''

    Delete a folder:

    from os import rmdir
    rmdir("__yourpath__\\folder_name")

    Note: You can only remove empty folders. You can't remove a folder that contains files.

'''
