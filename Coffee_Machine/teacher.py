from cm import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Returns True of drink can be made, false if it can not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculated amount from coins inserted into coffee machine"""
    print("Please insert coins,")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or false when insufficient funds are presented"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}.")
        resources["money"] += drink_cost
        return True
    else:
        print(f"That is not enough money.  {money_received} refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!")


is_on = True
while is_on:
    choice = input(
        "What would you like to drink an espresso, a latte or a cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(
            f"The resources of the coffee machine are: \nWater: {resources['water']}ml \nMilk: {resources['milk']}ml "
            f"\nCoffee: {resources['coffee']}g \nMoney: ${resources['money']:.2f}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['price']):
                make_coffee(choice, drink['ingredients'])
