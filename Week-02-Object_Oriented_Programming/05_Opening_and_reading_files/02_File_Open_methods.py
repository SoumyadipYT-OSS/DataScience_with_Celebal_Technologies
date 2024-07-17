f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\testfile.txt", "r")
print(f.read())
f.close()

print("\n")

f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\testfile.txt", "r")
print(f.read(18)) # returns the 5 characters of the file
f.close()

print("\n")
# Read Lines
f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demofile.txt", "r")
print(f.readline())
f.close()
f1 = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\testfile.txt", "r")
print(f1.readline())
f1.close()


# Looping through the file
f = open("D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\05_Opening_and_reading_files\\demofile.txt", "r")
for x in f:
    print(x)

f.close()
