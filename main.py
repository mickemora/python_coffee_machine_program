import pyinputplus as pyip

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


required_resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}


coffee_machine_on = True
resources["money"] = 0

def print_report():
    for items in resources:
        print(f"{items}: {resources[items]}")
    return


def check_resources(user_order):
    if MENU[user_order].get('ingredients').get('water') is not None:
        required_water = MENU[user_order].get('ingredients').get('water')
        required_resources["water"] = required_water
    else:
        required_water = 0
    if MENU[user_order].get('ingredients').get('milk') is not None:
        required_milk = MENU[user_order].get('ingredients').get('milk')
        required_resources["milk"] = required_milk
    else:
        required_milk = 0
    if MENU[user_order].get('ingredients').get('coffee') is not None:
        required_coffee = MENU[user_order].get('ingredients').get('coffee')
        required_resources["coffee"] = required_coffee
    else:
        required_coffee = 0

    if resources['water'] < required_water:
        print("Sorry there is not enough water")
        return False
    elif resources['milk'] < required_milk:
        print("Sorry there is not enough water")
        return False
    elif resources['coffee'] < required_coffee:
        print("Sorry there is not enough coffee")
        return False
    return MENU[user_order].get('cost')


def adjust_resources(cost):
    resources["water"] = resources["water"] - required_resources["water"]
    resources["milk"] = resources["milk"] - required_resources["milk"]
    resources["coffee"] = resources["coffee"] - required_resources["coffee"]
    return


def process_coins(cost):
    print("Please insert coins:")
    quarters = float(pyip.inputNum("How many quarters?: "))
    dimes = float(pyip.inputNum("How many dimes?: "))
    nickles = float(pyip.inputNum("How many nickles?: "))
    pennies = float(pyip.inputNum("How many pennies?: "))
    money_from_customer = ((quarters*25)+(dimes*10)+(nickles*5)+(pennies))/100
    if money_from_customer < cost:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif money_from_customer > cost:
        change = round(money_from_customer - cost,2)
        print(f"Thank you for your payment of: ${money_from_customer}")
        print(f"Here is ${change} in change")
        resources["money"] += money_from_customer
        resources["money"] -= change
    elif money_from_customer == cost:
        print(f"Thank you for your payment of: ${money_from_customer}")
    return money_from_customer


def process_order(user_order, cost):
    print(f"Processing order...{user_order} for a cost of ${cost}")
    payment_from_customer = process_coins(cost)
    if payment_from_customer > 0:
        adjust_resources(cost)
        print(f"Here's your {user_order}")
    return


def init_resources():
    required_resources["water"] = 0
    required_resources["milk"] = 0
    required_resources["coffee"] = 0
    return


while coffee_machine_on:
    init_resources()
    user_order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if user_order == "report":
        print_report()
    elif user_order == "off":
        coffee_machine_on = False
        print("Turning machine off...")
    elif user_order == "espresso" or user_order == "latte" or user_order == "cappuccino":
        enough_resources = check_resources(user_order)
        if enough_resources > 0:
            #print("There are enough resources for this beverage.")
            process_order(user_order, enough_resources)
    else:
        print("PLease select a valid option for your order.")
