from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.turtlesize(1)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor()+self.x_move
        y_pos = self.ycor()+self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1




