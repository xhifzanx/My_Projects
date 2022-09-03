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
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        random_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()