COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_COORDINATE = [-60, -20, 20, 60, 100]
import random
from turtle import Turtle


class CarManager:

    def __init__(self):
        self.all_cars = []

    def lots_of_cars(self):
        rand_chance = random.randint(0, 6)
        if rand_chance == 1:
            self.turtle = Turtle("square")
            self.turtle.penup()
            self.turtle.shapesize(stretch_len=2, stretch_wid=1)
            self.turtle.color(random.choice(COLORS))
            self.turtle.seth(180)
            rand_y = random.randint(-250, 250)
            self.turtle.goto(300, rand_y)
            self.all_cars.append(self.turtle)

    def move(self):
        for car in self.all_cars:
            x_move = car.xcor() - MOVE_INCREMENT
            y_move = car.ycor()
            car.goto(x_move, y_move)





