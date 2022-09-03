
from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
NEW_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for n in STARTING_POSITION:
            self.add_segment(n)

    def add_segment(self, n):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(n)
        self.segment.append(turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x=new_x, y=new_y)
        self.segment[0].forward(NEW_DISTANCE)

    def up(self):
        if self.segment[0].heading() != DOWN:
           self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)