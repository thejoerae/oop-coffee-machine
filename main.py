from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order_name = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    elif order_name == "off":
        break

    menu_item = menu.find_drink(order_name)
    if menu_item is not None:
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
