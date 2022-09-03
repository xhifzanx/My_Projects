import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")

game_is_on = True
n = 0.1
while game_is_on:
    time.sleep(n)
    screen.update()
    cars.lots_of_cars()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            time.sleep(5)
            game_is_on = False
        if player.ycor() > 280:
            player.goto(0, -280)
            n *= 0.8
            score.score_refresh()





