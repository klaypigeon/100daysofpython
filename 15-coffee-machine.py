# Completed 5/18/23 as part of Udemy Class 100 days Python


supplies = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}


def get_order():
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        exit()
    if order not in ["espresso", "latte", "cappuccino", "report"]:
        print("Incorrect order")

    return order


def process_order(order):
    if order == "report":
        print_report()
    else:
        make_coffee(order)


def print_report():
    print(f"Water: {supplies['Water']}ml")
    print(f"Milk:: {supplies['Milk']}ml")
    print(f"Coffee: {supplies['Coffee']}g")
    print(f"Money: ${supplies['Money']}")


def make_coffee(coffee_type):
    has_resources, resource = check_resources(coffee_type)
    if not has_resources:
        print(f"There is not enough {resource}")
        return
    has_money = check_money(coffee_type)
    if not has_money:
        print("Sorry that's not enough money. Money refunded.")
        return
    deduct_resources(coffee_type)
    print(f"Here is your {coffee_type}. Enjoy!")

def deduct_resources(type):
    supplies['Water'] -= menu[type]["ingredients"]["water"]
    supplies['Milk'] -= menu[type]["ingredients"]["milk"]
    supplies['Coffee'] -= menu[type]["ingredients"]["coffee"]



def check_money(type):
    cost = menu[type]['cost']
    print(f"Your {type} will cost: ${cost}")
    qs = int(input("How many Quarters?"))
    ds = int(input("How many Dimes?"))
    ns = int(input("How many Nickles?"))
    ps = int(input("How many Pennies?"))
    money_total = qs*.25 + ds*.10 + ns*.05 + ps*.01

    if money_total < cost:
        return False
    else:
        if money_total > cost:
            print(f"Here is your ${'{:.2f}'.format(money_total - cost)} dollars in change.")
        supplies["Money"] += cost
        return True


def check_resources(type):
    if menu[type]["ingredients"]["water"] > supplies['Water']:
        return False, "Water"

    elif menu[type]["ingredients"]["milk"] > supplies['Milk']:
        return False, "Milk"

    elif menu[type]["ingredients"]["coffee"] > supplies['Coffee']:
        return False, "Coffee"

    else:
        return True, "all"


while 1:
    order = get_order()
    process_order(order)
