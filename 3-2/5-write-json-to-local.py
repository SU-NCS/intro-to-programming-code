#write
import json
myfile = open("local.json","w")
myfile.write(json.dumps({'name': 'Maria', 'age': 20, 'occupation': 'programmer'}))
myfile.close()
print (myfile.name, "is open?", myfile.closed)