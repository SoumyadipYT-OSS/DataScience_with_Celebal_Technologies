from json import loads

# some JSON
x = '{ "machine": { "id": 1, "displayName": "Machine 1", "status": "Running" } }'

y = loads(x)
print(y)
print(y["machine"])
print(y["machine"]["displayName"])
print(y["machine"]["status"])