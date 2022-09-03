from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Uroob", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.no_of_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.no_of_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.no_of_score > self.high_score:
            self.high_score = self.no_of_score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")

        self.no_of_score = 0
        self.update()

    def score_refresh(self):
        self.no_of_score += 1
        self.clear()
        self.update()


