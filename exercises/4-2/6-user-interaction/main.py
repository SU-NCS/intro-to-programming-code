from turtle import Turtle, mainloop

BUTTON_SIZE = 60
CURSOR_SIZE = 20
FONT_SIZE = 18
FONT = ('Arial', FONT_SIZE, 'bold')
STATES = (('red', 'OFF'), ('green', 'ON'))
INITIAL_STATE = STATES[0]

def toggle_power(x, y):
    color, state = STATES[button.fillcolor() == 'red']

    button.fillcolor(color)
    marker.undo()
    marker.write(state, align='center', font=FONT)

color, state = INITIAL_STATE

button = Turtle('circle')
button.shapesize(BUTTON_SIZE / CURSOR_SIZE, outline=2)
button.color('black', color)
button.penup()
# button.goto(-200, 200)  # move the button into position

marker = Turtle(visible=False)
marker.penup()
marker.goto(button.xcor(), button.ycor() - BUTTON_SIZE/2 - FONT_SIZE - 2)
marker.write(state, align='center', font=FONT)

button.onclick(toggle_power)

mainloop()