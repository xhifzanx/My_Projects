from turtle import Turtle
import random
COLOR = ["red", "black", "green", "blue", "purple", "brown", "dark red"]
class Names(Turtle):
    def __init__(self):
        super(Names, self).__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR))



