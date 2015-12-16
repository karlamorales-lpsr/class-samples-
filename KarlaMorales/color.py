import turtle 

def my_Star(myTurtle, x, y, side):
        star.color("blue") 
	myTurtle.penup()
        myTurtle.goto(x,y)
        myTurtle.pendown()
        side_count = 0
        while side_count < 50:
                myTurtle.forward(side)
                myTurtle.left(30)
                myTurtle.left(40)
                myTurtle.left(40)
                myTurtle.left(30)
		side_count = side_count + 1

star = turtle.Turtle()
my_Star(star,90,-8,49)
turtle.exitonclick()
