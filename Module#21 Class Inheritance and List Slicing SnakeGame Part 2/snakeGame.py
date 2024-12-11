from turtle import *
import time
from snake import *
from food import *
from scoreboard import *

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")

# //when we open the turtle graphics, we see 3 blocks creating and then moving. we need to stop that animation
screen.tracer(0)
screen.title("My Snake Game")

segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

gameOn = True
# while gameOn:
#     screen.update()
#     time.sleep(0.1)
# gameOn=False


screen.listen()  # will take input from screen
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect colison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        gameOn = False
        scoreboard.gameOver()
    # detect colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < -20:
            gameOn = False
            scoreboard.gameOver()


screen.exitonclick()
