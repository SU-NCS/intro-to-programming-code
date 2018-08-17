from turtle import *
def draw_shape():
  begin_fill()
  # while True:
  for i in range(10):
    forward(200)
    left(170)
    # if abs(pos()) < 1:
        # break
  end_fill()

def draw_square():
  begin_fill()
  for i in range(4):
    forward(200)
    left(90)
  end_fill()
  

color('red', 'yellow')
bgcolor('black')
speed(10)
print(position())
draw_square()
for i in range(4):
  pu()
  goto (-i*100,i*100)
  pd()
  print(position())
  print(abs(pos()))
  # draw_shape()
  draw_square()
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
done()