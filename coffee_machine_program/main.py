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
should_continue = True
profit = 0
def is_enough_money(type, money):
            if type['cost'] > money:
                return False
            else:
                return True
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f'money: {profit}')
    elif choice == 'off':
        break
    else:
        type = MENU[choice]
        ingredients = type['ingredients']
        flag = True
        for key in ingredients:
            if ingredients[key] >= resources[key]:
                flag = False
                lack_of = key
            else:
                resources[key] -= ingredients[key]
        money = 0
        if flag:
            print("please insert coines.")
            quarters = float(input("enter how many quarters: ")) * 0.25
            dime = float(input("enter how many dimes: ")) * 0.1
            nickel = float(input("how many nickels: ")) * 0.05
            penny = float(input("enter how many pennies: ")) * 0.01
            money = quarters + dime + nickel + penny
            if is_enough_money(type, money):
                in_change = round(money - type['cost'], 1)
                print(f"here is ${in_change} in change")
                print(f'Here is your {choice} ☕, enjoy!')
                profit += type['cost']
            else:
                print("there is no enough money, money refunded")
                
        else:
            print(f'there is no enough {lack_of}.')




