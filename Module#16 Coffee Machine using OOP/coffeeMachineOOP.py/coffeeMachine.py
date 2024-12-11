from coffeemaker import *
from menu import *
from moneyMachine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# print(money_machine.report())
# print(coffee_maker.report())

coffeeOn = True
while coffeeOn:
    option = menu.get_items()
    selection = input(f"What would you like? {option} Type the name of the drink ")
    if selection == "off":
        coffeeOn = False
    elif selection == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if drink is None:
            continue
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
