import time
import turtle 

def drawPara(myTurtle):
	count = 0 
	while count < 1:
		shawn.fillcolor("blue")
   		shawn.begin_fill()
   		myTurtle.right(90)
   		myTurtle.forward(20)
   		myTurtle.left(120)
   		myTurtle.forward(20)
   		myTurtle.left(60)
		myTurtle.forward(20) 
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.end_fill()
 		count = count + 1 

def drawSidePara(myTurtle):
	count = 0
	while count < 1:
		myTurtle.left(90)
                myTurtle.forward(20)
                myTurtle.right(120)
                myTurtle.forward(20)
                myTurtle.right(60)
                myTurtle.forward(20)
                myTurtle.right(120)
                myTurtle.forward(20)
                count = count + 1

def drawBothPara(myTurtle):
	count = 0 
	while count < 1:
		drawPara(myTurtle)
		myTurtle.right(30)
		drawSidePara(myTurtle)
		count = count + 1 

def drawTopPara(myTurtle):
	count = 0 
	while count < 2:
		shawn.fillcolor('light blue')
		shawn.begin_fill() 
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.left(120)
		myTurtle.forward(20)
		myTurtle.end_fill()
		count = count + 1 

def drawAllPara(myTurtle):
	count = 0 
	while count < 1:
		drawBothPara(myTurtle)
		drawTopPara(myTurtle)
		count = count + 1

def drawNewPlaceCube(myTurtle):
		#drawBothPara(myTurtle)
               # drawTopPara(myTurtle)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.right(60)
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.left(30)
		myTurtle.pendown()

def drawAnothaOne(myTurtle):
		drawBothPara(myTurtle)
		drawTopPara(myTurtle)
		drawNewPlaceCube(myTurtle)
                drawBothPara(myTurtle)
                drawTopPara(myTurtle)
		drawNewPlaceCube(myTurtle)		
		drawBothPara(myTurtle)
                drawTopPara(myTurtle)
		drawNewPlaceCube(myTurtle)
                drawBothPara(myTurtle)
                drawTopPara(myTurtle)
		drawNewPlaceCube(myTurtle)
                drawBothPara(myTurtle)
                drawTopPara(myTurtle)

def drawGoBack(myTurtle):
	count = 0 
	while count < 4:
		drawAnothaOne(myTurtle)
		myTurtle.right(180)
		myTurtle.penup()
                myTurtle.forward(20)
                myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.right(60)

                myTurtle.forward(20)
		myTurtle.left(60)
                myTurtle.forward(20)
		myTurtle.right(60)

                myTurtle.forward(20)
		myTurtle.left(60)
		myTurtle.forward(20)
		myTurtle.right(60)
		myTurtle.forward(20)

		print("should be back at the start now")
                time.sleep(2)

		myTurtle.left(60)
		myTurtle.pendown()
		myTurtle.forward(20)
		myTurtle.left(90)
		myTurtle.left(60)
		myTurtle.forward(20)

		count = count + 1
			
shawn = turtle.Turtle()
shawn.speed(1)
drawGoBack(shawn)
turtle.exitonclick()
