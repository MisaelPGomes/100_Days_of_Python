from turtle import Turtle

FONT = ("Courier", 20, "normal")
point = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-100, 250)
        self.point = point
        self.write(f"Level: {self.point}", False, align="right", font= FONT)

    def pointmaker(self):
        self.point += 1
        self.clear()
        self.write(f"scoreboard: {self.point}", False, align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font= FONT)
