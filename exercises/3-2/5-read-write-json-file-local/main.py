#https://realpython.com/python-json
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

# 1. open the simple.json file and convert to json
with open('../simple.json', 'r') as f:
    dictionary = json.load(f) #deserialize
print(dictionary)

# 2. given a dictionary conver to json and write to myfile
cities = [{"name":"Seattle"},{"name":"Portland"},{"name":"San Francisco"}]
with open('cities.json', "w") as f:
    json.dump(cities,f)  #serialize
f.close()

# 3. read the cities.json file and load into a dictionary
myfile = open('cities.json','r')
dictionary = json.load(myfile) #deserialize
print("dictionary",dictionary)
print("dictionary is a ",type_test(dictionary))

# 4. experiment with dumps and loads where you are not writing to disk
# but serializing/deserializing in code - does the decoded = the original?
card_hand = ("A","K",10)
encoded_hand = json.dumps(card_hand)
decoded_hand = json.loads(encoded_hand)
print(decoded_hand)
print("original",type(card_hand))
print("encoded",type(encoded_hand))
print("decoded",type(decoded_hand))