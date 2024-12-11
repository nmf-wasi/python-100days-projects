# later i will add function to add resources and make a password preoection to acess resources with if else so that everyone can't change resources

menu = {
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
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def isPaymentSuccess(totalPay, cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if totalPay == cost:
        print(f"Payment success!")
        global profit
        profit += cost
        return True
    elif totalPay > cost:
        back = round(totalPay - cost, 2)
        print(f"You have paid ${round(totalPay,2)}, here's your change ${back}")
        # global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def makeCoffee(drink, ingredients):
    """Deduct the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")


def resourceCheck(ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


coffeeOn = True
while coffeeOn:
    selection = input(
        "What would you like? (espresso/latte/cappuccino). Press '1' for Espresso '2' for Latte and '3' for Cappuccino. If you want admin control, write password "
    )
    selection = selection.lower()
    if selection == "off":
        coffeeOn = False
        break
    elif selection == "admin":
        changeResource = input("Do you want to change resource? If yes, press 'Y'. ")
        if changeResource.lower() == "y":
            waterAdd = int(input("How much water do you want to add? "))
            milkAdd = int(input("How much milk do you want to add? "))
            coffeeAdd = int(input("How much coffee do you want to add? "))
            resources["water"] += waterAdd
            resources["milk"] += milkAdd
            resources["coffee"] += coffeeAdd
    elif selection == "report":
        print(f"Water : {resources["water"]}ml")
        print(f"Milk : {resources["milk"]}ml")
        print(f"Coffee : {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        if selection == "1":
            selection = "espresso"
        elif selection == "2":
            selection = "latte"
        elif selection == "3":
            selection = "cappuccino"
        drink = menu[selection]
        if resourceCheck(drink["ingredients"]):
            pay = coins()
            if isPaymentSuccess(pay, drink["cost"]):
                makeCoffee(selection, drink["ingredients"])


