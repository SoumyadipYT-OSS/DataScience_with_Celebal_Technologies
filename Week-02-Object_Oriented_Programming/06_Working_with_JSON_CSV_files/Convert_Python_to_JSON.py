from json import dumps

# a Python object (dict)
x = {
    "Automobile-factory": {
        "robots-machine": {
            "id": "RM-001",
            "displayName": "Robot Machine 1",
            "status": "Running"
        },
        "painting-machine": {
            "id": "PM-001",
            "displayName": "Painting Machine 1",
            "status": "Running"
        },
        "welding-machine": {
            "id": "WM-001",
            "displayName": "Welding Machine 1",
            "status": "Running"
        }
    }
}


# dumps() function is used to convert python object to json
# convert into JSON:
y = dumps(x)

# the result is a JSON string
print(y)

# method to display proper json format
print(dumps(x, indent=4))   # indent=4 is used to display proper json format it means 4 spaces will be used for indentation
