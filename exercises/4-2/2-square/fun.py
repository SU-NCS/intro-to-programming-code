# experiment with forward/backward and left/right

from turtle import *



def draw_it(t,pen_dir,dir_num,angle_dir,angle_num):
  if pen_dir == "forward":
    t.forward(dir_num)
  else:
    t.backward(dir_num)
  if angle_dir == "right":
    t.right(angle_num)
  else:
    t.left(angle_num)



bgcolor('black')
bob = Turtle() # create a turtle named bob
bob.color('red', 'yellow') # define pen and fill colors
bob.begin_fill()
for i in range(4):
  draw_it(bob,"forward",100,"left",90)
bob.end_fill()

done() #screen will stay open until you close it
