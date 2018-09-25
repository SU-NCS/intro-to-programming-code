#read from api
import requests, json

data = requests.get("http://numbersapi.com/19?json")
mydict = json.loads(data.content) #data in the form of a dictionary
print(type(mydict))
print(mydict)
print(mydict["text"])
mystr = json.dumps(mydict) #convert to string


#write to file
#write
outfile = open("mydict.json","w")
outfile.write(json.dumps(mydict))
outfile.close()
print (outfile.name, "is closed?", outfile.closed)

#read from FileExistsError
print('#================#')
with open('mydict.json') as f:
  indata = f.read()
print(type(indata))
print(indata)
newdict = json.loads(indata)  #string to dict
print(type(newdict))
print(newdict["text"])