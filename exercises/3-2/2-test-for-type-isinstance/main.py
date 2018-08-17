# in code you can test for the type of a variable using 

# 1. given a variable find out if its a list
myvar = [1,2,3]
print (isinstance(myvar,list))

# 2. given a variable find out if its a dictionary
myvar = {1:"a",2:"b",3:"c"}
print (isinstance(myvar,dict))

# 3. given a variable find out if its a string
myvar = "test"
print (isinstance(myvar,str))

# 4. given a variable find out if its an integer
myvar = 1
print (isinstance(myvar,int))

# 5. given a variable find out if its a boolean
myvar = True
print (isinstance(myvar,bool))

# 6. write a function that takes a variable parameter and returns the type
# and if you can't figure out the type return "NA"
def type_test(test_var):
  if (isinstance(test_var,list)):
    return "list"
  elif (isinstance(test_var,dict)):
    return "dict"
  elif (isinstance(test_var,str)):
    return "string" 
  elif (isinstance(test_var,int)):
    return "integer"
  elif (isinstance(test_var,bool)):
    return "boolean"
  else:
    return "NA" 

#test function
myvar = [1,2,3]
print ("myvar is a",type_test(myvar))

myvar = "hello"
print ("")