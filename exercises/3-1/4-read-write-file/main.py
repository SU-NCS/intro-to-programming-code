# make sure you are in the directory of this code when you run 
# 1. open a file name "myfile.txt", write "myfile" to it and then close the file
# check to see that there is a file named "myfile.txt" in your directory
myfile = open("myfile.txt","w")
myfile.write("myfile")
myfile.close()

# 2. open the file "myfile.txt" that you created above in read, write mode
# read the contents of the file and print to the screen
# next write the word "hello" to the file
# next close the file and reopen 
# next read the file and print to the screen
# close the file
myfile= open("myfile.txt","r+")
str = myfile.read()
print ("before write",str)
myfile.write("hello")
myfile.close()
myfile = open("myfile.txt","r+")
str = myfile.read()
print("after write",str)
myfile.close()

# 3. Append data to a file
# write hello to a file and close
# append how are you to the file and close
# open file for print and print contents
myfile= open("append.txt","w")
myfile.write("hello")
myfile.close()
myfile = open("append.txt", "a")
myfile.write("how are you")
myfile.close()
myfile = open("append.txt","r")
print (myfile.read())
myfile.close()

# 4. Add "newline" character to a file
number_file = open("number_file.txt","w")
for number in range(10):
  number_file.write("{}\n".format(number))
number_file.close() 
number_file = open("number_file.txt","r")
for line in number_file:
  print(line)

# 5. dump file contents on screen
big_file = open("big_file.txt","r")
print(big_file.readlines())
big_file.close()

# or

big_file = open("big_file.txt","r")
for line in big_file:
  print(line)
big_file.close()
