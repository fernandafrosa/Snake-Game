from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def increseScore(self):
        self.score +=1
        self.clear()
        self.updateScore()
