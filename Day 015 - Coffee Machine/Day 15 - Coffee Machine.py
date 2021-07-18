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
    "coffee":  100,
}

machine_on = True
money = 0


def check_qunatity(drink_name):
    for key in MENU[drink_name]['ingredients']:
        if MENU[drink_name]['ingredients'][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def coins_operation():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + \
        (nickles * 0.05) + (pennies * 0.01)
    return total


def is_enough_money(total_received, drink_price):
    if total_received > drink_price:
        refund = round(total_received - drink_price, 2)
        print(f"Here is ${refund} in change.")
        global money
        money += drink_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def decrease_resources(drink_name):
    for ing in MENU[drink_name]['ingredients']:
        new_value = resources[ing] - MENU[drink_name]['ingredients'][ing]
        resources[ing] = new_value
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while machine_on:

    order = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        machine_on = False
    elif order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {money}")

    else:
        check_qunatity(order)
        total_payment = coins_operation()
        drink_price = MENU[order]['cost']
        if is_enough_money(total_payment, drink_price):
            decrease_resources(order)
