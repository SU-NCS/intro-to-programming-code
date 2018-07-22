# A string with underlying JSON format can be turned into a dictionary
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
# 1. Given a string convert to a dict using json.loads and print the type 
# the json, and the dictionary - What's different between a dictionary and json
str = '{"name": "Maria", "age": 20, "occupation": "programmer"}'
j = json.loads(str)
print (j)
print(str)
print ("j is a ",type_test(j))

# 2. Given a string with an a list in it load to json and  print the type 
# the json, and the dictionary - What's different between a dictionary and json
str = '[1,2,3]'
j = json.loads(str)
print (j)
print(str)
print ("j is a ",type_test(j))

#3. Given a string with a list of dictionaries in it  load to json and  print the type 
# the json, and the dictionary - What's different between a dictionary and json
cities = '[{"name":"Seattle"},{"name":"Portland"},{"name":"San Francisco"}]'
j = json.loads(str)
print (j)
print(str)
print ("j is a ",type_test(j))