# import turtle
# timmy = turtle.Turtle()
#
# print(timmy)
# timmy.color("Darkred")
# timmy.shape("turtle")
# timmy.forward(100)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "squartle", "charmandar"])
table.add_column("Type", ["electric", "water", "fire"])
table.align
print(table)