from turtle import *

ninjaTurtle = Turtle()

ninjaTurtle.shape("turtle")
ninjaTurtle.pencolor("red")

ninjaTurtle.forward(100)
ninjaTurtle.right(45)
ninjaTurtle.forward(100)
ninjaTurtle.left(45)
ninjaTurtle.forward(100)
# these 2 shoudl stay at the bottom of the file
screen = Screen()
screen.exitonclick()
