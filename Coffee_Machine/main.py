from cm import MENU, resources
PENNY = 0.01
NICKLE = 0.05
DIME = 0.10
QUARTER = 0.25

WATER = 'water'
COFFEE = 'coffee'
MILK = 'milk'


def resource_check(item, choice):
    if resources[item] < MENU[choice]['ingredients'][item]:
        print(f"Not enough {item} to make drink")
        return False
    else:
        return True


def enough_money(item, amount):
    if MENU[choice]['price'] <= amount:
        return True
    else:
        return False


def decrement_resources(item, choice):
    resources[item] = resources[item] - MENU[choice]["ingredients"][item]


def give_change(choice, amount):
    if amount > MENU[choice]['price']:
        print(f"Your change is {amount - MENU[choice]['price']:.2f}")


def add_money(choice):
    resources['money'] += MENU[choice]['price']


coffee_on = True
while coffee_on:
    choice = input(
        "What would you like to drink an espresso, a latte or a cappuccino): ").lower()
    if choice == "off":
        coffee_on = False
        break
    elif choice == "report":
        print(
            f"The resources of the coffee machine are: \nWater: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${resources['money']:.2f}")
        continue

    print("Please insert coins,")
    inserted_quarter = int(input("How many quarters: "))
    inserted_dime = int(input("How many dimes: "))
    inserted_nickle = int(input("How many nickles: "))
    inserted_penny = int(input("How many pennies: "))

    quarter_amount = inserted_quarter * QUARTER
    dime_amount = inserted_dime * DIME
    nickle_amount = inserted_nickle * NICKLE
    penny_amount = inserted_penny * PENNY

    amount = quarter_amount + dime_amount + nickle_amount + penny_amount

    if choice == 'espresso':
        enough_water = resource_check(WATER, choice)
        enough_coffee = resource_check(COFFEE, choice)
        can_afford = enough_money(choice, amount)
        give_change(choice, amount)
        if enough_water and enough_coffee:
            if can_afford:
                print(f"Enjoy your {choice} ☕! ")
                decrement_resources(WATER, choice)
                decrement_resources(COFFEE, choice)
                add_money(choice)
            else:
                print(f"Not enough money, returning {amount}")

    elif choice == 'latte':
        enough_water = resource_check('water', choice)
        enough_milk = resource_check('milk', choice)
        enough_coffee = resource_check('coffee', choice)
        can_afford = enough_money(choice, amount)
        change = give_change(choice, amount)
        if enough_water and enough_coffee and enough_milk:
            if can_afford:
                print(f"Enjoy your {choice} ☕! ")
                decrement_resources(WATER, choice)
                decrement_resources(COFFEE, choice)
                decrement_resources(MILK, choice)
                add_money(choice)
            else:
                print(f"Not enough money, returning {amount}")
    elif choice == 'cappuccino':
        enough_water = resource_check('water', choice)
        enough_milk = resource_check('milk', choice)
        enough_coffee = resource_check('coffee', choice)
        can_afford = enough_money(choice, amount)
        change = give_change(choice, amount)
        if enough_water and enough_coffee and enough_milk:
            if can_afford:
                print(f"Enjoy your {choice} ☕! ")
                decrement_resources(WATER, choice)
                decrement_resources(COFFEE, choice)
                decrement_resources(MILK, choice)
                add_money(choice)
            else:
                print(f"Not enough money, returning {amount}")
# TODO: 3. Check if resources are sufficient for drink being made
# TODO: 4. Process coins for drink, if not enough return coins and display not enough money.  If more than drink given, proocess change
# TODO: 5. If transaction successful, process drink and decrement resources
