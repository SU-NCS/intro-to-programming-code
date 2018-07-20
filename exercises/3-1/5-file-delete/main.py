# 1. Try to delete a file that doesn't exist
# add try/except if there's an error
import os
try:
  os.remove("becky.txt")
  print("file deleted")
except Exception:
  print("error deleting")

# 2. write a file and delete it
myfile = open("myfile.txt","w")
myfile.close()
try:
  os.remove("myfile.txt")
  print("file deleted")
except Exception:
  print("error deleting")

# 