import turtle
from Tkinter import *

def square(myTurtle):
	side_count = 0
`	while side_count < 4:
		myTurtle.forward(90)
		myTurtle.left(90)
		side_count = side_count + 1

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
squarebutton = Button(frame, text='squarebutton', command=lambda: square(shawn))
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
squarebutton.pack(side=LEFT)
frame.pack()

turtle.exitonclick()
