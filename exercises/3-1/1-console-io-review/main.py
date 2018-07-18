# use input and print to review console I/O

# 1. ask for a user name and respond with a hello greeting
# Example
# What is your name?
# Becky
# Hellow Becky
name = input("What is your name?")
print ("Hello ",name)

# 2. ask for favorite cookie and reply "yum"
# Example
# What is your favorite cookie?
# chocolate
# yum
cookie = input("What is your favorite cookie?")
print("yum")


# 3. ask for a user age and respond with the age user will be in 5 years
# Example
# How old are you?
# 16
# In five years you will be 21
age = input("How old are you?")
print ("In five years you will be ",int(age)+ 5)

# 4. ask for 2 numbers and return their sum
# Example
# Enter number: 1 
# 2
# Enter number: 2
# 3
# Sum 5
num1 = input("Enter number 1:")
num2 = input("Enter number 2:")
print ("Sum", int(num1) + int(num2))

# 4. print your favor color and then ask user to enter the color and report success/fail
# Example
# My favorite color is purple
# What is my favorite color?
# purple
# Yes
print("My favorite color is purple")
answer = input("What is my favorite color?")
if (answer == "purple"):
  print("Yes")
else:
  print("No")


