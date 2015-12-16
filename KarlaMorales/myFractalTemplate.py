# myFractalTemplate.py

import turtle

def makePow(myTurtle, side):
        myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
	myTurtle.right(130)
	myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
        myTurtle.right(130)
	myTurtle.forward(side)
        myTurtle.left(120)
        myTurtle.forward(side)
        myTurtle.right(130)

# make our turtle
squeak = turtle.Turtle()


length = 50
while length > 0:
        makePow(squeak, length)
# rotate and make the sides shorter
        squeak.right(5)
        length = length - 1

# wait to exit until I've clicked
turtle.exitonclick()

