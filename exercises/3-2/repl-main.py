myName = "Eloise"
print("Hi, My name is %s, " % myName)
yourName = input("what's yours?")
print ("Hi %s, nice to meet you? Let's play!" % yourName)
num1 = input("Enter an integer:")
num2 = input("Enter another integer:")
sum = int(num1) + int(num2)
print("The sum of the 2 numbers is: %d" % sum)
#print("How old are you %s?" % yourName)

# age guessing trick

pickANumber = input("Hey %s choose a number between 2 and 9:" % yourName)
print ("Ok, now mulitply that number by 2")
print (int(pickANumber)*2)
print ("Now add 5 to the number")
print ((int(pickANumber) * 2 + 5))
print ("Now multiply that number by 50")
print (((int(pickANumber) * 2 + 5)*50))

magicNumber = 1768 #for 2018
alreadyCelebratedBirthday = input("Did you already celebrate your birthday this year[y/n]?")
almostThere = 0
if alreadyCelebratedBirthday == 'y':
  print ("Add %d" % magicNumber)
  almostThere = ((int(pickANumber) * 2 + 5)*50) + magicNumber
  # print ((((int(pickANumber) * 2 + 5)*50) + magicNumber))
else:
  print ("Add %d" % (magicNumber-1))
  almostThere = ((int(pickANumber) * 2 + 5)*50) + (magicNumber - 1)
  # print ((((int(pickANumber) * 2 + 5)*50) + (magicNumber - 1)))

yearBorn = input("Almost there, what year were you born?")
print ("Subtract the year you were born")
print ("%d" % (almostThere - int(yearBorn)))

age = str(almostThere - int(yearBorn))[1:]
print ("%s are you %s years old?" % (yourName, age) )