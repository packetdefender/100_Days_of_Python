print("Welcome to the roller coaster!")
height = int(input("How tall are you in cm: "))
age = int(input("How old are you: "))
ticket_price = 0

if height > 120:
    if age < 12:
        ticket_price = 5
    elif age <= 18:  # This will capture between 12-18
        ticket_price = 7
    elif age >= 45 and age <= 55:
        print("Have a free ride on us!")
    else:
        ticket_price = 12

    photo = input("Do you want to purchase a photo: ")
    if photo == ("Y" or "YES" or "Yes" or "yes"):
        ticket_price += 3

    print(f"Your total ticket price is ${ticket_price}")
else:
    print("I am sorry, you are not tall enought to ride.")
