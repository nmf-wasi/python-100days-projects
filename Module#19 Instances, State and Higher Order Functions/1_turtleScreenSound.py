from turtle import *
tartar=Turtle()
screen=Screen()
# A higher order function is a function that takes one or more functions as arguments, or returns a function as its result

def move_forward():
    tartar.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)

# screen.onkey(key="a key", fun=afunctionName)
#when we are passing a func into another func, we dont need to add the ()




screen.exitonclick()