from turtle import *
STARTING_POSITION = [(-20, 0), (0, 0), (20, 0)]
# in python, constants are named in all capital and snake case
MOVE_DISTANCT=20
UP=90
DOWN=-90
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()  # creating 3 squares and keeping them one beside another to make them look like a snake
        self.head=self.segments[0] #if you write this line above createSnake, it will show error, because before creating the snake, the segments list was empty

    def createSnake(self):
        for i in STARTING_POSITION:
            newSegment = Turtle("square")
            newSegment.color("white")
            newSegment.penup()
            newSegment.goto(i)
            self.segments.append(newSegment)

    #     for segment in segments:
    #         segment.forward(20)
    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segNum - 1].xcor()
            newY = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newX, newY)
        self.segments[0].forward(MOVE_DISTANCT)

    def up(self):
        if self.head.heading()!=DOWN: #self.head->is the head part and self.head.heading->where to head is pointing (in angle)
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

# if we move forward, then when we turn, only the head will turn but the rest of the body will go other side
# Therefore, lets just replace the squares to their previous square's position instead of moving forward.
# Like Seg3 will go to the position of seg2 and seg2 will go to the postion of seg1 and then seg1 will go to a new postion
