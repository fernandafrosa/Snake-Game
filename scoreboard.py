from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        #self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.clear()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font= FONT)

    def increseScore(self):
        self.score +=1
        self.updateScore()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.updateScore()