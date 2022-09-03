from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move():
    tim.forward(10)
def left():
    tim.left(10)
def right():
    tim.right(10)
def down():
    tim.back(10)
def reset():
    tim.reset()
screen.listen()

screen.onkey(key="w", fun=move)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="s", fun=down)
screen.onkey(key="c", fun=reset)


screen.exitonclick()
