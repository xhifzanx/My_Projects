MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
money=0

working = True
while working == True:
    order = input("What would you like (espresso/latte/cappuccino):").lower()
    if order == "report":
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\ncoffee: {resources['coffee']}\nMoney: ${money}")
    elif order == "espresso":
        print("Please insert the coins.")
        quarter = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))
        total_charge = 0.25*quarter+0.1*dimes+0.05*nickels+0.01*pennies
        if resources['water'] < MENU["espresso"]["ingredients"]["water"]:
            print("Insufficient water.")
        elif resources['coffee'] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Insufficient coffee.")
        elif total_charge >= MENU["espresso"]["cost"]:
            charge = total_charge-MENU["espresso"]["cost"]
            charge = float(charge)
            charge = round(charge, 2)
            money += MENU["espresso"]["cost"]
            print(f"Here is ${charge} in change.")
            resources['water'] = resources['water']-MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"]-MENU["espresso"]["ingredients"]["coffee"]
            print("Here is your espresso ☕️. Enjoy!")
        else:
            print("Sorry there's not enough money, money refunded.")
    elif order == "latte":
        print("Please insert the coins.")
        quarter = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))
        total_charge = 0.25 * quarter + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        if resources['water'] < MENU["latte"]["ingredients"]["water"]:
            print("Insufficient water.")
        elif resources['milk'] < MENU["latte"]["ingredients"]["milk"]:
            print("Insufficient milk.")
        elif resources['coffee'] < MENU["latte"]["ingredients"]["coffee"]:
            print("Insufficient coffee.")
        elif total_charge >= MENU["latte"]["cost"]:
            charge = total_charge - MENU["latte"]["cost"]
            charge = float(charge)
            charge = round(charge, 2)
            money += MENU["latte"]["cost"]
            print(f"Here is ${charge} in change.")
            resources['water'] = resources['water'] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            print("Here is your latte ☕️. Enjoy!")
        else:
            print("Sorry there's not enough money, money refunded.")
    elif order == "cappuccino":
        print("Please insert the coins.")
        quarter = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickels = int(input("how many nickels?: "))
        pennies = int(input("how many pennies?: "))
        total_charge = 0.25 * quarter + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
        if resources['water'] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Insufficient water.")
        elif resources['milk'] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Insufficient milk.")
        elif resources['coffee'] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Insufficient coffee.")
        elif total_charge >= MENU["cappuccino"]["cost"]:
            charge = total_charge - MENU["cappuccino"]["cost"]
            charge = float(charge)
            charge = round(charge, 2)
            money += MENU["cappuccino"]["cost"]
            print(f"Here is ${charge} in change.")
            resources['water'] = resources['water'] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            print("Here is your cappuccino ☕️. Enjoy!")
        else:
            print("Sorry there's not enough money, money refunded.")
    elif order == "off":
        working = False
    else:
        print("invalid!")