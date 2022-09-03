
color_list = [(246, 242, 233), (249, 240, 245), (239, 247, 241), (239, 242, 248), (198, 165, 118), (144, 80, 55),
              (221, 202, 136), (60, 95, 122), (168, 151, 50), (135, 162, 181), (133, 33, 21), (51, 120, 87),
              (74, 37, 29), (193, 95, 80), (145, 177, 150), (105, 74, 78), (166, 146, 156), (19, 92, 69),
              (27, 59, 77), (227, 176, 166), (59, 43, 46), (138, 27, 33), (180, 203, 178), (26, 84, 89),
              (86, 148, 129), (12, 70, 58), (43, 64, 89), (180, 97, 102)]
import random
from turtle import Turtle, Screen
tim = Turtle()
Screen().colormode(255)
tim.hideturtle()
tim.penup()
tim.back(100)
tim.left(90)
tim.back(100)
tim.right(90)

for _ in range(5):
    for i in range(10):
        color = random.choice(color_list)
        print(color)

        tim.forward(30)
        tim.dot(10, color)
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.back(30)
    for i in range(10):
        color = random.choice(color_list)
        print(color)
        tim.forward(30)
        tim.dot(10, color)
    tim.right(90)
    tim.forward(30)
    tim.right(90)
    tim.back(30)


screen = Screen()
screen.exitonclick()