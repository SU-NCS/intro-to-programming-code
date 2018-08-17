from turtle import Turtle, Screen

def jump(turtle,x, y):
  turtle.pu(); 
  turtle.goto(x,y); 
  turtle.pd()

turtle = Turtle()
screen = Screen()
turtle.ondrag(goto)

screen.click(jump)
turtle.shape("circle")
turtle.pensize(3)
for n in "0123456789":
  turtle.onkey(lambda c=int(n):
  pensize(2*c+1), n)
screen.listen()
turtle.speed(1)
turtle.pencolor("blue")

mainloop()
# input("press to contine")