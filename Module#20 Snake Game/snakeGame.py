from turtle import *
import time
from snake import *
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")

# //when we onpen the turtle graphics, we see 3 blocks creating and then moving. we need to stop that animation
screen.tracer(0)
screen.title("My Snake Game")

segments = []

snake=Snake()

gameOn = True
# while gameOn:
#     screen.update()
#     time.sleep(0.1)
# gameOn=False


screen.listen()#will take input from screen
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    


screen.exitonclick()
