from turtle import  Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segment = []
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    #Collision with the food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.score_refresh()
        snake.extend()
    #Collision with the wall
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 \
            or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:
        score.reset()
        snake.reset()
    #Detect collision with the tail
    for segment in snake.segment[1:]:
      if snake.segment[0].distance(segment) < 10:
            score.reset()
            snake.reset()








screen.exitonclick()