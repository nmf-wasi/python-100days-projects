import random
from turtle import *
colormode(255)
# or
# import turtle
# turtle.colormode(255)

colors = [
    "aquamarine",
    "coral",
    "medium slate blue",
    "hot pink",
    "dark blue",
    "cyan",
    "dim gray",
    "light sky blue",
]
turn = [0, 90, 180, 270]
tartar = Turtle()
tartar.pensize(5)
tartar.speed("fastest")

for i in range(2000):
    tartar.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # tartar.color(       r,                     g,                    b    )
    tartar.forward(30)
    tartar.right(random.choice(turn))

screen = Screen()
screen.exitonclick()
# changing colormode of Turtle module is needed to add random colors with rgb. therefore, we need to modify the Turtle module not the turtle object
