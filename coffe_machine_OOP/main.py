from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem('latte', 200, 100, 24, 2.5)
cappuccino = MenuItem('cappuccino', 250, 150, 24, 3.0)
espresso = MenuItem('espresso', 50, 0, 18, 1.5)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
should_continue = True
while(should_continue):
    order = input(f"what would you like: ({menu.get_items()}): ")
    drink = menu.find_drink(order)
    if menu.find_drink(order):
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif order == 'off':
        should_continue = False
    elif order == 'report':
        print(money_machine.report())
        print(coffee_maker.report())    


