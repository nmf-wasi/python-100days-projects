import random
from turtle import *

colormode(255)

tartar = Turtle()
tartar.speed("fastest")
# for i in range(300):
#     tartar.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tartar.circle(100)
#     tartar.setheading(tartar.heading() + 10)
# this one would not stop even after the spirograph is drawn. To stop this thing, we need to set a margin to stop it when it completely draws spirograph once
# spirograph would be 360 degree and there will be a gap
# 360/gap=the number of times we need to draw it to cover the whole area once


def drawSpirograph(gap):
    for i in range(int(360 / gap)):  # the deafault division ans from python is float, so we need to convert it to int
        tartar.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tartar.circle(100)
        tartar.setheading(tartar.heading() + gap)


drawSpirograph(10)
screen = Screen()
screen.exitonclick()
