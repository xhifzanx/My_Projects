from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score()

game_on = True
while game_on:
   
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    screen.listen()
    screen.onkey(fun=r_paddle.up, key="Up")
    screen.onkey(fun=r_paddle.down, key="Down")
    screen.onkey(fun=l_paddle.up, key="w")
    screen.onkey(fun=l_paddle.down, key="s")
    #Detection with collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detection with Collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        score_board.l_point()

    if ball.xcor() < -400:
        ball.reset()
        score_board.r_point()

screen.exitonclick()
