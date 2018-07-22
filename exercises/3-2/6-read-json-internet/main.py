import requests, json

# When working on the internet we make requests and we get reponses.  The data is
# usually in a json format or we ask for it that way. 
# The other format you see is XML
# Notice we get help from two libaries "requests" and "json"
# Reading data from the internet through API's; Application Programming Interface

# 1. Read the numbers API with number 7. What did you find out? What if you run it again?
# What is the value of "type" in the response?
data = requests.get("http://numbersapi.com/7?json")
dictionary = json.loads(data.content)
print(dictionary)

print ("The type of the object  returned from the internet is", type(data))
print ("The type of the content returned from the internet is", type(data.content))
print ("The type of the data that the json.loads command creates is ", type(dictionary))

print("The interesting thing about 7 is: ", dictionary["text"])

# 2. Call the trivia API with random and report the question and the answer
# In many apis even if only 1 item is returned, it's put into an list, so to look 
# at a single item in the list you have to reference the item in the list
data = requests.get("http://jservice.io/api/random")
response = json.loads(data.content)
print(response)

print ("The type of the object  returned from the internet is", type(response))
print ("The type of the content returned from the internet is", type(response))
print ("The type of the data that the json.loads command creates is ", type(response))

print("The question is: ", response[0]["question"])
print("The answer is: ", response[0]["answer"])


# messing around with curl and ascii art
# Some API's allow you to provide parameters
# Internet parameter lists start with ? after main request URL and
# are always <parameter>=<value>.  If there is more than one they are 
# separated by an ampersand "&".  If there's a space in your value replace it 
# with a "+" plus sign
# http://artii.herokuapp.com/make?text=becky+peltz&font=caligraphy
# http://artii.herokuapp.com/fonts_list
# Use the ascii art api to translate text into ascii art. Call the api
# with text = your+name
# conda install -c ulmo urllib3
#import urllib.request
# req = urllib.request.Request('http://artii.herokuapp.com/make?text=becky+peltz')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read('http://artii.herokuapp.com/make?text=becky+peltz')
#    print(the_page)
#data = urllib.request.urlopen("http://artii.herokuapp.com/make?text=becky+peltz").read()
#print (data)
#


#req = urllib.request.Request('http://www.voidspace.org.uk')
#with urllib.request.urlopen(req) as response:
   #the_page = response.read()
   #print(the_page)
# req = urllib.request.Request('https://xkcd.com/2022/')
# with urllib.request.urlopen(req) as response:
#   the_page = response.read()
#   print(the_page)