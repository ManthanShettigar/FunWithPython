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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 2:Report of Resources left.
def show_report():
    print(f'Water : {resources["water"]}ml')
    print(f'Milk :  {resources["milk"]}ml')
    print(f'Coffee :{resources["coffee"]}g')
    print(f'Money : {profit}$')

def is_resources_sufficient(orderd_ingredients):
    for item in  orderd_ingredients:
        if orderd_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {orderd_ingredients[item]}")
            return False
    return True

def process_coins():
    print("Please Insert Coins")
    total = int(input("How many quarters"))* .25
    total += int(input("How many dimes"))* .10
    total += int(input("How many nickles"))* .05
    total += int(input("How many pennies"))* .01
    return total
# TODO 6 :
def is_transaction_succesful(money_received,drink_cost):
    if money_received>=drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is your ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO 7:Deduct resources from the menu of userschoice. 

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

#TODO 1:Prompt user by asking “​What would you like? (espresso/latte/cappuccino):
    
is_on = True
while is_on:
    choice=input("“​What would you like? (espresso/latte/cappuccino):").lower()
    if choice =='report':
        show_report()
    elif choice=='off':
        is_on=False
    elif choice =='latte'  or choice =='espresso' or choice=='cappuccino':
        drink=MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment =process_coins()
            if is_transaction_succesful(payment,drink['cost']):
                make_coffee(choice, drink["ingredients"])
    else:
        pass

#