import json
str = '{"name": "Maria", "age": 20, "occupation": "programmer"}'
j = json.loads(str)
print (j)

str = '{"name": "Maria", "age": 20, "occupation": null}'
j = json.loads(str)
print (j)
print (isinstance(j,dict))
print ("age", j["age"])