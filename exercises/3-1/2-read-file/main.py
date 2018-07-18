# make sure you are in the directory of this code when you run 
# 1. open and read oneline.txt and print what you read and then close the file
myfile = open("oneline.txt","r")
str = myfile.read()
print ("contents of ",myfile.name,": ",str)
myfile.close()

# 2. open and read twoline.txt and print what you read and then close the file
myfile = open("twoline.txt","r")
str = myfile.read()
print ("contents of ",myfile.name,": ",str)
myfile.close()

# 3. open and read up-one-level.txt and print what you read and then close the file
# remember that a file in this directory would be accessed as "uponelevel.txt" but
# if it was in a directory above the program it would be access as "../up-one-level.txt"
myfile = open("../up-one-level.txt","r")
str = myfile.read()
print ("contents of ",myfile.name,": ",str)
myfile.close()