# make sure you are in the directory of this code when you run 
# 1. open a file name "myfile.txt", write "myfile" to it and then close the file
# check to see that there is a file named "myfile.txt" in your directory
myfile = open("myfile.txt","w")
myfile.write("myfile")
myfile.close()

# 2. Open my file for read and test is see if file is closed using the ".closed" property
# If it's not closed then close it and test again
# Example output 
# myfile.txt open true
# myfile.txt open false
myfile = open("myfile.txt","w")
print (myfile.name,"open", myfile.closed)
myfile.close()
print (myfile.name, "open", myfile.closed)

# 3. Read data from file up-one-level.txt and then write it to a file 
# named copy.txt in the directory that the program is in
# don't forget to close both files
# refresh or list the files in your file system to see if there is a file
# named copy.txt
upone = open("../up-one-level.txt","r")
str = upone.read()
upone.close()
myfile = open("copy.txt","w")
myfile.write(str)
myfile.close()