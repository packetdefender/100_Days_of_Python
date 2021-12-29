from art import logo, vs
from game_data import data
import random
import os
def cls(): return os.system('clear')


def random_item():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, a {account['description']} from {account['country']}"


def check_answer(guess, a_follower, b_follower):
    """Check if user is correct, and return if correct"""
    if a_follower > b_follower:
        return guess == "A"
    else:
        return guess == "B"


# 1) Display Art
print(logo)

# 2) Generate a random account from game data

account_a = random_item()
score = 0
game_should_continue = True
while game_should_continue:
    account_b = random_item()
    if account_a == account_b:
        account_b = random_item()

    # 3) Format account data into printable data
    print(format_data(account_a))
    print(vs)
    print(format_data(account_b))

    # 4) Ask User for a Guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # 4a) Check if correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    cls()
    print(logo)
    # 5) Give Feedback

    if is_correct == True:
        score += 1
        print(f"You are right!, Your score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that is wrong.  Your final score is: {score}")
