#write
myfile = open("myfile.txt","w")
myfile.write("hello")
myfile.close()
print (myfile.name, "is open?", myfile.closed)

