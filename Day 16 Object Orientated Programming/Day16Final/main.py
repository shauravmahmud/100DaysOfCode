from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): \n")
    if choice == "off": #Command to turn off
        machine_on = False #then turn off
    elif choice == "report": #Check the reports from the coffee and money machine
        coffee.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee.is_resource_sufficient(drink)
        is_payment_successful = machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee.make_coffee(drink)
