from turtle import *
import random
colors = ["aquamarine", "coral","medium slate blue","hot pink","dark blue","cyan","dim gray","light sky blue"]
tartar = Turtle()
sides = 4
for i in range(11):
    angle = 360 / sides
    tartar.color(random.choice(colors)) #will pick a random color from the lsit
    for j in range(sides):
        tartar.forward(100)
        tartar.right(angle)
    sides += 1
