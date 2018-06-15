import requests, json

data = requests.get("http://numbersapi.com/19?json")
dict = json.loads(data.content)
print(dict)

print ("The type of the object  returned from the internet is", type(data))
print ("The type of the content returned from the internet is", type(data.content))
print ("The type of the data that the json.loads command creates is ", type(dict))

print("The interesting thing about 19 is: ", dict["text"])