import turtle
a = turtle.Turtle()      #instantiate a new turtle object called 'a'
a.hideturtle()           #make the turtle invisible
a.penup()                #don't draw when turtle moves
a.goto(-200, -200)       #move the turtle to a location
a.showturtle()           #make the turtle visible
a.pendown()              #draw when the turtle moves
a.goto(50, 50)           #move the turtle to a new location

a.speed (10)
for n in range(4):
	a.forward (50)
	a.left (90)
input("press any key to continue")
print(a.pos())
# from turtle import Turtle, Screen

# SQUARE_SIZE = 100

# screen = Screen()

# square = Turtle(shape="square", visible=False)
# square.penup()
# square.goto(SQUARE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - SQUARE_SIZE/2)
# square.pendown()
# square.showturtle()

# # square.pendown()
# Turtle.speed (10)
# for i in range(4):
# 	square.forward (50)


# screen.mainloop()
# # input("press any key to continue")