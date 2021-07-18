from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


machine_on = True

while machine_on:
    print(menu.table())
    drink_name = input(f"What would you like to have?: ")
    if drink_name == "off":
        machine_on = False
    elif drink_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_name)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

