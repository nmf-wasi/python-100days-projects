from turtle import *
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        # keep the pen up beofre going or it will draw a line
        self.penup()
        self.goto(0, 265)
        # if you change color and goto after your self.write, you won't see any change.texts will be same as before.
        #  You have to change color and position before start writing
        self.hideturtle()
        self.updateScoreBoard()


    def updateScoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font=FONT)
    def increaseScore(self):
        self.score+=1
        self.clear()
        self.updateScoreBoard()
