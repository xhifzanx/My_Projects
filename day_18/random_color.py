
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed("fastest")
Screen().colormode(255)
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return tim.color(color)


def walk():
        tim.seth(random.choice(direction))
        tim.forward(10)


walking = True
while walking == True:
    walk()
    random_color()



screen = Screen()
screen.exitonclick()