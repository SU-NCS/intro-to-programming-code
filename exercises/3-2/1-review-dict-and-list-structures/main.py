# review data structures 

# 1. given a list find it's 3rd element
mylist = [1,2,3]
print (mylist[2])

mylist = ["a","b","c"]
print(mylist[2])

mylist = [True, False, True]
print(mylist[2])

# 2. given a list print it out to console
mylist = ["a","b","c"]
for item in mylist:
  print(item)

# 3. given a dictionary find the value associated with the key "q"
mydict = {"p":1, "q":2, "r":3}
print(mydict["q"])

# 4. given a dictionary print it out to the console showing <key value>
mydict = {"p":1, "q":2, "r":3}
for key in mydict:
  print(key, mydict[key])

# 5. given a list of dictionary items print the value of name for each item in the list
cities = [{"name":"Seattle"},{"name":"Portland"},{"name":"San Francisco"}]
for city in cities:
  print(city["name"])