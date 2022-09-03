from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money = MoneyMachine()
coffee = CoffeeMaker()

menu = Menu()

activated = True
while activated == True:
    order = input(f"Enter the name? {menu.get_items()} ")
    if order == "off":
        activated = False
    elif order == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(order)

        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                print(drink)
                coffee.make_coffee(drink)






