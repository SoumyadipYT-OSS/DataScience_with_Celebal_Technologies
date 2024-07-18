from json import loads

# target the file location to fetch the json file and use loads to convert it to python
with open('D:\\GitHub repo connections\\DataScience_with_Celebal_Technologies\\Week-02-Object_Oriented_Programming\\06_Working_with_JSON_CSV_files\\warehouse.json', 'r') as file:
    data = loads(file.read())
    print(data)