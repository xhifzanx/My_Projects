from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height= 400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim", "tom", "joe", "jim", "kay", "kim"]
turtles =[]
n=0
for trtle in names:
    trtle = Turtle(shape="turtle")
    trtle.color(colors[n])
    n+=1
    trtle.penup()
    trtle.goto(-230, -130+n*40)
    turtles.append(trtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()