import turtle

# let shawn be the turtle
shawn = turtle.Turtle()

# set the color to purple 
shawn.color("purple")
shawn.shape("turtle")
shawn.stamp()
# line is equal to 0
line = 0

while line < 8:
        shawn.forward(100)
        shawn.backward(100)
        shawn.left(45)
        shawn.forward(80)
        line = line + 1
        shawn.stamp()
        shawn.shape("classic")
turtle.exitonclick()

