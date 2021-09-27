import os
import data


def count_coins(quarters, dimes, nickles, pennies):
    sum = quarters * 0.25
    sum += dimes * 0.1
    sum += nickles * 0.05
    sum += pennies * 0.01
    return sum


def report(resource):
    print(f"Water: {resource['water']}ml\nMilk: {resource['milk']}ml\nCoffee: {resource['coffee']}g\nMoney: ${resource['money']}")


def check_resources(order_ingredients):
    missing_ingredients = []
    for item in order_ingredients:
        if order_ingredients[item] > data.resources[item]:
            missing_ingredients.append(item)
    return missing_ingredients 


def decrease_resources(order_ingredients):
    for item in order_ingredients:
        data.resources[item] -= order_ingredients[item]


should_continue = True
while should_continue:
    # Ask what the user would like
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        should_continue = False
    elif user_choice == "report":
        report(data.resources)
    elif user_choice in (data.MENU):
        if len(check_resources(data.MENU[user_choice]["ingredients"])) != 0:
            print(f"Sorry, there is not enough {check_resources(user_choice)}") 

        # Ask for coins
        print("Please, insert coins.")
        num_of_quarters = int(input("How many quarters?: "))    # $0.25
        num_of_dimes = int(input("How many dimes?: "))          # $0.10
        num_of_nickles = int(input("How many nickles?: "))      # $0.05
        num_of_pennies = int(input("How many pennies?: "))      # $0.01

        amount_paid = count_coins(num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies)

        # Check if entered coins is enough
        if data.MENU[user_choice]['cost'] > amount_paid:
            print("Sorry that's not enough money. Money refunded.")
        else:
            amount_change = round(amount_paid - data.MENU[user_choice]['cost'], 2)
            if amount_change > 0: 
                print(f"Here is ${amount_change} in change.")

            data.resources["money"] += amount_paid - amount_change
            decrease_resources(data.MENU[user_choice]["ingredients"])

            print(f"Here is your {user_choice}. Enjoy!")
    else:
        print("Invalid entry, try again.")

        

