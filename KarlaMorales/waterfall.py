import turtle 

def drawSquare(myTurtle):
	count = 0
        while count < 4:
                myTurtle.forward(20)
                myTurtle.left(90)
                count = count + 1 

def drawMultiSquare(myTurtle):
	colors = ['red','blue','yellow','green']
	count = 0
	while count < 4:
		myTurtle.right(90)
		myTurtle.color(colors[count])   
                myTurtle.pendown()
		drawSquare(myTurtle)
		count = count + 1

def drawAllSquare(myTurtle):
	count = 0 
	while count < 4:
		myTurtle.right(90)
		myTurtle.penup()
		myTurtle.forward(30)
		myTurtle.left(90)
		myTurtle.forward(30)
		myTurtle.pendown()
		drawMultiSquare(myTurtle)
		count = count + 1
		
shawn = turtle.Turtle()
drawAllSquare(shawn)

turtle.exitonclick()
