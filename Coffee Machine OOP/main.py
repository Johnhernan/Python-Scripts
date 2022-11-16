from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == '__main__':
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    app_running = True
    while app_running:

        print("What would you like? " + menu.get_items())

        user_choice = input()

        if user_choice == 'report':
            coffee_maker.report()

        elif user_choice != 'exit':
            drink = menu.find_drink(user_choice)

            if drink:
                payment_successful = money_machine.make_payment(drink.cost)

                if payment_successful:
                    enough_resources = coffee_maker.is_resource_sufficient(drink)

                    if enough_resources:
                        coffee_maker.make_coffee(drink)

        elif user_choice == 'exit':
            app_running = False
