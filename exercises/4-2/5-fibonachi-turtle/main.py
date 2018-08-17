# http://www.openbookproject.net/thinkcs/archive/python/thinkcspy3e_abandoned/ch03.html
from turtle import *


setup(800, 600)
wn = Screen()
bgcolor("goldenrod")
wn.title("Golden Mean Turtle")

tess = Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                    # this is new
pa = 0
ma = 1
for i in range(60):
    tess.stamp()                # leave an impression on the canvas
    # size = size + 3
    child = ma + pa
    pa = ma
    ma = child
    if (child < -400 or child > 400):
      break
    print(child * 10)
    # size = new             # increase the size on every iteration
    tess.forward(child)          # move tess along
    tess.right(60)              # and turn her
wn.exitonclick()