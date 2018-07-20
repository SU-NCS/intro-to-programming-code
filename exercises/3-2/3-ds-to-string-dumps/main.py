# lists and dictionaries may be turned in to JSON 
# if you want to send data out on the web you would turn it into JSON first
# in JSON every key must be quoted
def type_test(test_var):
  if (isinstance(test_var,list)):
    return "list"
  elif (isinstance(test_var,dict)):
    return "dict"
  elif (isinstance(test_var,str)):
    return "dict" 
  elif (isinstance(test_var,int)):
    return "dict"
  elif (isinstance(test_var,bool)):
    return "dict"
  else:
    return "NA" 

import json
# 1. Given a dictionary convert to JSON 
# print the json and print the original dict
mydict = {"p":1, "q":2, "r":3}
print("json",json.dumps(mydict))
print("dict",mydict)

mydict = {"p":"1", "q":"2", "r":"3"}
print(json.dumps(mydict))

# 2. Given a dictionary convert to JSON, test the type and print the type
mydict = {"p":1, "q":2, "r":3}
myjson = json.dumps(mydict)
print ("myjson is a",type_test(myjson))
print ("mydict is a", type_test(mydict))

# 3.  Given a list convert it to JSON, test the type and print the type, 
# print the list and print the json
mylist =  [1,2,3]
myjson = json.dumps(mylist)
print("mylist is a ",type_test(mylist))
print ("myjson is a ", type_test(myjson))
print(mylist)
print(myjson)

# 4. Given a list of dictionaries convert it to JSON, test the type and print
# the type, print the list and the json
cities = [{"name":"Seattle"},{"name":"Portland"},{"name":"San Francisco"}]
myjson = json.dumps(cities)
print("cities is a ",type_test(cities))
print("myjson is a ",type_test(myjson))
print(cities)
print(myjson)

