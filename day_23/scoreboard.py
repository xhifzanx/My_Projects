FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.no_of_score = 0
        self.hideturtle()
        self.goto(-240, 250)
        self.color("black")
        self.update()

    def update(self):
        self.write(f"Level: {self.no_of_score}", align="center", font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def score_refresh(self):
        self.no_of_score += 1
        self.clear()
        self.update()
