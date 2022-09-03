from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
Screen().colormode(255)
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return tim.color(color)

for i in range(75):
    tim.circle(100)
    i = i*5
    print(i)
    tim.seth(i)
    random_color()


screen = Screen()
screen.exitonclick()