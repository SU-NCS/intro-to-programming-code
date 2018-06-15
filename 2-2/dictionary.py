dict =  {'name': 'Maria', 'age': 20, 'occupation': 'programmer'}
print (dict['name'], 'is a ', dict['age'], " year old ", dict["occupation"],".")

print ("Value : %s" %  dict.keys())

for key, value in dict.items():
    print (key, value)

list = [{'one':1}, {"two":2}, {'three':3} ]
for item in list:
    for key, value in item.items():
        print (key, value)