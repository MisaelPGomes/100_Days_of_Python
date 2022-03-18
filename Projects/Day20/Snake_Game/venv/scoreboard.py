from turtle import Turtle
ALIGMENT = "center"
FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write("Scoreboard: " + str(self.score), False, ALIGMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGMENT, FONT)

    def new_score(self):
        self.score +=1