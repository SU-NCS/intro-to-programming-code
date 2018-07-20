import os
# 1. rename a file int the directory
if os.path.isfile("new_myfile.txt"):
  os.rename( "new_myfile.txt", "old_myfile.txt")
  print("renamed new to old")
os.rename( "old_myfile.txt", "new_myfile.txt")
print("renamed old to new")

# 2. create a new file and then rename it
myfile = open("new.txt","w")
print (myfile.name)
myfile.close()
os.rename("new.txt", "rename.txt")
