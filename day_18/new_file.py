from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed(10)
direction = ["left", "right"]



def random_color():
    colors = ["red", "green", "blue", "purple", "yellow", "black", "brown", "violet", "cyan"]
    color = random.choice(colors)
    return tim.color(color)


def walk():
    if random.choice(direction)=="right":
        tim.right(90)
        tim.forward(10)
    else:
        tim.left(90)
        tim.forward(10)


walking = True
while walking == True:
    walk()
    random_color()



screen = Screen()
screen.exitonclick()


