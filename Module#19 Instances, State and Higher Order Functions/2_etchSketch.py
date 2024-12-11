# W=forward
# S=backwards
# A=CounterCLockwise
# D=ClockWise
# C=ClearDrawing

from turtle import *

tartar = Turtle()
screen = Screen()


def moveForward():
    tartar.forward(10)


def moveBackward():
    tartar.backward(10)


def turnLeft():
    tartar.left(10)


def turnRight():
    tartar.right(10)
def clear():
    tartar.penup()
    tartar.clear()#clears the screen
    tartar.home()#bring at the middle of the screen
    tartar.pendown()
tartar.speed("fastest")
screen.listen()
screen.onkey(moveForward, "w")
screen.onkey(moveBackward, "s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight, "d")
screen.onkey(clear, "c")
screen.exitonclick()
