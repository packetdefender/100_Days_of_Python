print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want, S, M, or L: ")
add_pepperoni = input("Would you like to add pepperoni, Y or N: ")
extra_cheese = input("Would you like to add extra cheese, Y or N: ")

pizza_total = 0

if size == "S":
    print("Small Pizza is $15")
    pizza_total += 15
    if add_pepperoni == "Y":
        print("To add Pepperoni the cost is +$2")
        pizza_total += 2
elif size == "M":
    print("Meduim Pizza is $20")
    pizza_total += 20
    if add_pepperoni == "Y":
        print("To add Pepperoni the cost is +$3")
        pizza_total += 3
elif size == "L":
    print("Large Pizza is $25")
    pizza_total += 25
    if add_pepperoni == "Y":
        print("To add Pepperoni the cost is +$3")
        pizza_total += 3

if extra_cheese == "Y":
    print("To add extra cheese the cost is + $1")
    pizza_total += 1

print(f"Your final bill is: ${pizza_total}")
