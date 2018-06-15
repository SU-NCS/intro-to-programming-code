#read
myfile = open("myfile.txt","r")
str = myfile.read()
print ("contents of ",myfile.name,": ",str)
myfile.close()