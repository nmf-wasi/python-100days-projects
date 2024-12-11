# make a bet, who will win the race? red, orange, blue, violet, green, yellow

from turtle import *
import random

raceOn = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "SpringGreen", "RoyalBlue1", "SlateBlue1"]
allTurtles = []
yPosition = [-100, -60, -20, 20, 60, 100]
# turtle object is 40*40 size
# width is from -250 to 250
# so when a turtle crosses 230, it's finished!


for t in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[t])
    newTurtle.penup()
    newTurtle.goto(x=-220, y=yPosition[t])
    allTurtles.append(newTurtle)
# newTurtle.shape("turtle")


userBet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color(red/orange/yellow/green/blue/purple : ",
)

if userBet:
    raceOn = True
while raceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 210:
            # print(turtle.color())
            raceOn = False
            winningColor = turtle.pencolor()
            if winningColor == "SpringGreen":
                winningColor = "green"
            elif winningColor == "RoyalBlue1":
                winningColor = "blue"
            elif winningColor == "SlateBlue1":
                winningColor = "purple"
            if winningColor == userBet:
                print(f"You have won! The {winningColor} turtle is the winner!")
            else:
                print(f"You have lost! The {winningColor} turtle is the winner!")
            # turtle.write("GeeksForGeeks")

        randomDistance = random.randint(0, 10)
        turtle.forward(randomDistance)


screen.exitonclick()
