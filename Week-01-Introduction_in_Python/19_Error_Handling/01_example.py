# Error Handling in Python

try:
    f = open('D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-01-Introduction_in_Python\\19_Error_Handling\\test_file.txt', 'r')
    print(f)
except FileNotFoundError as e:
    print(e) 
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()  # If we don't use f.close() then it will not close the file and it will be in open state.
finally:
    print("Executing Finally...")



try:
    f = open('D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-01-Introduction_in_Python\\19_Error_Handling\\corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")