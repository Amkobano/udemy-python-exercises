from art import logo

print(logo)


def report(resources):
    print("Water: " + str(resources[0]) + "ml")
    print("Milk: " + str(resources[1]) + "ml")
    print("Coffee: " + str(resources[2]) + "g")
    print("Cash Money Records: $" + str(resources[3]))


def make_coffee(coffeetype):
    if coffeetype == "espresso":
        coffeewater = 50
        coffeecoffee = 18
        coffeemilk = 0
        coffeeprice = 1.5

    elif coffeetype == "latte":
        coffeewater = 200
        coffeecoffee = 24
        coffeemilk = 150
        coffeeprice = 2.5

    elif coffeetype == "cappuccino":
        coffeewater = 250
        coffeecoffee = 24
        coffeemilk = 100
        coffeeprice = 3.00

    else:
        print("Error")

    return coffeewater, coffeemilk, coffeecoffee, coffeeprice


def check_transaction(priceofcoffee, usersmoney):
    if usersmoney < priceofcoffee:
        print("You don't have enough money")
        return False
    else:
        print("Transaction approved")
        return True


def process_payment():
    # penny = 1cent, dime = 10cent, nickel = 5cent, quarter = 25cent
    amount_quarters = int(input("How many quarters?"))
    amount_dimes = int(input("How many dimes?"))
    amount_nickel = int(input("How many nickel?"))
    amount_pennies = int(input("How many pennies?"))

    wallet = round(amount_pennies * 0.01 + amount_nickel * 0.05 + amount_dimes * 0.1 + amount_quarters * 0.25, 2)

    return wallet


def check_resources(current_resources, userswish):
    if current_resources[0] < userswish[0]:
        print("There is not enough water")
        return False
    elif current_resources[1] < userswish[1]:
        print("There is not enough milk")
        return False
    elif current_resources[2] < userswish[2]:
        print("There is not enough coffee")
        return False
    else:
        return True


def main():
    # resources = [water, milk, coffee, money]
    resources = [1000, 500, 500, 0]
    check = True

    while check:
        userinput = input("What would you like? (espresso/latte/cappuccino)\n")

        if userinput == "off":
            check = False

        elif userinput == "report":
            report(resources)
        else:
            # usercoffee[water, coffee, milk, price]
            usercoffee = make_coffee(userinput)
            inserted_money = process_payment()
            while inserted_money < usercoffee[-1]:
                print(inserted_money)
                print("Enter more money")
                inserted_money += process_payment()

            if inserted_money > usercoffee[-1]:
                change = round(inserted_money - usercoffee[-1], 2)
                print("Here is your change: $" + str(change))

            check = check_resources(resources, usercoffee)

            if not check:
                exit()
            else:
                resources[0] -= usercoffee[0]
                resources[1] -= usercoffee[1]
                resources[2] -= usercoffee[2]
                resources[3] += usercoffee[3]


if __name__ == '__main__':
    main()




# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








