from turtle import Turtle, Screen

TURTLE_SIZE = 20

screen = Screen()

yertle = Turtle(shape="turtle", visible=False)
yertle.penup()
yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
yertle.pendown()
yertle.showturtle()

for i in range(5):
  yertle.penup()
  yertle.forward(20)
  yertle.right(90)
  yertle.pendown()
  yertle.showturtle()
  input("Press to continue")

screen.mainloop()