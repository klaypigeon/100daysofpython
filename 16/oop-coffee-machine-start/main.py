from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Define menu items

my_cm = CoffeeMaker()
my_menu = Menu()
my_mm = MoneyMachine()

def get_order():
    order = input(f"What would you like? ({my_menu.get_items()}):")
    if order == "off":
        exit()
    elif order == "report":
        my_cm.report()
        my_mm.report()
        return False
        
    elif order not in my_menu.get_items():
        print("Incorrect order")
        return
    
    else:
        return order

def make_coffee(order):
    drink = my_menu.find_drink(order)
    has_money = check_money(drink)
    if not my_cm.is_resource_sufficient(drink):
        return
    if not has_money:
        return
    else:
        my_cm.make_coffee(drink)

def check_money(mydrink):
    cost = mydrink.cost
    print(f"Your {mydrink.name} will cost: ${cost}")
    if my_mm.make_payment(cost):
        return True
    else:
        return False


while True:
    myorder = get_order()
    if myorder:
        make_coffee(myorder)




