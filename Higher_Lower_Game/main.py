from game_data import data
from art import logo, vs
import random
import os
def cls(): return os.system('clear')


LENGTH_OF_DATASET = len(data) - 1


def random_choice():
    return random.choice(data)


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def check_followers(user_pick, other_pick, score):
    if user_pick['follower_count'] > other_pick['follower_count']:
        print(score)
        cls()
        print(logo)
        score += 1
        print(f"You are right! Current score is: {score}")
        return score
    else:
        cls()
        print(logo)
        print(f"Sorry, that is wrong.  Your final score is: {score}")
        return False


def user_pick():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice.upper() == "A":
        return "A"
    else:
        return "B"


def game():
    print(logo)
    score = 0
    account_a = random_choice()
    game_on = True
    while game_on:
        account_b = random_choice()
        print(
            f"Compare A: {format_data(account_a)}")
        print(vs)
        print(
            f"Against B: {format_data(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess == "A":
            score = check_followers(account_a, account_b, score)
            account_a = account_b
            if score == False:
                game_on = False
        elif guess == "B":
            score = check_followers(account_b, account_a, score)
            account_a = account_b
            if score == False:
                game_on = False


game()
