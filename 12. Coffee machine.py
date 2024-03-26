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
def is_resources_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry! there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
def is_transaction_successful(payment_received,cost):
    global profit
    if payment_received>cost:
        change=round(payment_received-cost,2)
        print(f"Here is your {change}$ change.")
        profit+=cost
        return True
    elif payment_received==cost:
        profit += cost
        return True
    else:
        print("That's not enough money. Money Refunded!")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on == True:
    choice=input("\nEspresso - 1.5$\nLatte - 2.5$\nCappuccino - 3.0$\nWhat would you like?: ").lower()
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: {profit}$")
    else:
        drink=MENU[choice]
        if is_resources_available(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])



