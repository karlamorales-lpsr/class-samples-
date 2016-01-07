import turtle

def drawTri(myTurtle):
        side_count = 0
        while side_count < 3:
                myTurtle.forward(10)
                myTurtle.right(120)
                side_count = side_count + 1
def drawMoreTri(myTurtle):
	side_count = 0
	while side_count < 7:
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.pendown()
		drawTri(shawn)
		side_count = side_count + 1 	 

shawn = turtle.Turtle()
drawMoreTri(shawn)

turtle.exitonclick()	
