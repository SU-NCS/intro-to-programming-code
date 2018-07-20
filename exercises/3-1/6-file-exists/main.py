# 1. Test if main.py exists
import os.path
print("this file exists?",os.path.isfile("main.py") )

# 2. Write a file and test if it exists
myfile = open("myfile.txt","w")
myfile.close()
print("this file exists?",os.path.isfile("myfile.txt") )

# 3. Write a file, delete it and test if it exists
myfile = open("myfile.txt","w")
myfile.close()
try:
  os.remove("myfile.txt")
  print("file deleted")
except Exception:
  print("error deleting")
print("this file exists?",os.path.isfile("myfile.txt") )

# 4. Test if file exists and open as r+ if it does and a if it doesn't
# write your name to the file
# Show contents of file
if os.path.isfile("myfile.txt"):
  myfile = open("myfile.txt","r+")
else:
  myfile = open("myfile.txt","w")
myfile.write("Becky\nsays hi")
myfile.close()
myfile = open("myfile.txt","r")
print(myfile.readlines())
myfile.close()

