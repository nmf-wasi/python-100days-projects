from turtle import *

screen = Screen()
# screen.bgcolor("black")
tartar = Turtle()
tartar.shape("arrow")
tartar.color("red")
tartar.forward(10)

for i in range(11):
    tartar.forward(10)
    tartar.color("red")
    tartar.forward(10)
    tartar.color("black")
    # this will create a dasj lone

tartar.color("black")
for i in range(11):
    tartar.forward(10)
    tartar.penup()
    tartar.forward(10)
    tartar.pendown()
    # this will create a dashed line with bigger dash
screen.exitonclick()
