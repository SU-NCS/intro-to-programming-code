# draw a triangle
# use tri.forward(n) where n is the number of pixes
# use tri.right(d) or tri.left(d) where is the number of degress to rotate 
# what value of d work? what values of n work?
import turtle
wn = turtle.Screen()
tri=turtle.Turtle()

tri.speed (0) #0-10 with 0 fastest; 0 means no animation
tri.penup()  #pen up so nothing recorded on the screen
tri.left(90)  #rotate 90 degrees - a right angle
tri.forward(-100) #move forward 100 pixels
tri.right(90) #rotate 90 degrees
tri.pendown() # put the pen down
for x in range(3):  # 3 times do the following
	tri.forward(160) # record 60 pixels
	tri.right(240)  # rotate left 120 degrees
input("press any key to continue")
