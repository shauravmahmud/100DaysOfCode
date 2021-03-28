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

profit = 0

def enough_resources(order_ingredients):
    """"True or False if enough ingredients"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return True

def coins():
    print("Please insert your coins.")
    """Total value of coins"""
    total = int(input("How many quarters?")) * 0.25
    total = total + int(input("How many dimes?")) * 0.1
    total = total + int(input("How many nickles?")) * 0.05
    total = total + int(input("How many pennies?")) * 0.01
    return total


def transaction(money_in, drink_cost):
    """"True when payment is enough, or False when not enough"""
    if money_in >= drink_cost:
        change = round((money_in - drink_cost), 2)  # 2 decimal places
        print(f'your change is £{change}')
        global profit #Global scope needed
        profit = profit + drink_cost
        return True
    else:
        print("That's not enough money!")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

# Ask what drink the user would like.
switched_on = True
profit = 0

while switched_on:  # While True keep running this statement
    choice = input(f"What drink would you like? espresso,latte or cappuccino?\n")
    if choice == "report":
        """Generate report"""
        water = int(resources["water"])
        milk = int(resources["milk"])
        coffee = int(resources["coffee"])
        print(f' Water left: {water}ml')
        print(f' Milk left: {milk}ml')
        print(f' Coffee left: {coffee}grams')
        print(f' profit: £{profit}')
    elif choice == "off".lower():
        switched_on = False  # Turn off the Coffee Machine by entering off to the prompt.

    # Check resources are sufficient
    else:
        drink = MENU[choice]
        #print(drink)  # This is a dictionary of the components of the drink which will be passed in the function
        if enough_resources(drink["ingredients"]):
            payment = coins()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
