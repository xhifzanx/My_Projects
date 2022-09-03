MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def machine(ordered, money):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    used_water = MENU[ordered]["ingredients"]["water"]
    used_milk = MENU[ordered]["ingredients"]["milk"]
    used_coffee = MENU[ordered]["ingredients"]["coffee"]
    cost = MENU[ordered]["cost"]

    print("Please insert the coins.")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total_charge = 0.25 * quarter + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    if water < used_water:
        return print("Sorry there's not enough water.")
    elif milk < used_milk:
        return print("Sorry there's not enough milk.")
    if coffee < used_coffee:
        return print("Sorry there's not enough coffee.")
    elif total_charge >= cost:
        charge = total_charge - cost
        charge = float(charge)
        charge = round(charge, 2)
        money += cost
        print(f"Here is ${charge} in change.")
        water = water - used_water
        milk = milk - used_milk
        coffee = coffee - used_coffee
        print("Here is your latte ☕️. Enjoy!")
        return money
    else:
        return print("Sorry there's not enough money, money refunded.")


working = True
while working == True:
    order = input("What would you like (espresso/latte/cappuccino):").lower()
    if order == "report":
        if order == "report":
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\ncoffee: {resources['coffee']}\nMoney: ${money}")
    elif order == "cappuccino":
        machine(ordered = 'cappuccino', money = money)

    elif order == "latte":
        machine(ordered = 'latte', money = money)
    elif order == "off":
        working = False
    else:
        print("Invalid Input!")