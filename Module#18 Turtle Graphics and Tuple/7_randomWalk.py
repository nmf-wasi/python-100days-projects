import random
from turtle import *

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
turn = [90, 180, 270]
tartar = Turtle()
tartar.pensize(5)
tartar.speed(10)

for i in range(200):
    tartar.color(random.choice(colors))
    tartar.forward(30)
    tartar.right(random.choice(turn))

screen = Screen()
screen.exitonclick()
