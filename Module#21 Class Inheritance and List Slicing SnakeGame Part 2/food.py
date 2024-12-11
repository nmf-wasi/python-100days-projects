from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-280, 265), random.randint(-280, 265)) #keeping it below 265 in y axis because there's score board above 265
        #screen is 600*600 width=-300to300 and length=-300to300 if we keep the food too close to wall, it will crash, so minimizing the length