from turtle import Turtle
  
def jump(turtle, distance):
  turtle.pu()
  turtle.forward(distance)
  turtle.pd()
fred = Turtle()
fred.speed(1)
jump(fred, 100)
herb = Turtle()
herb.speed(1)
herb.left(180)
jump(herb, 100)