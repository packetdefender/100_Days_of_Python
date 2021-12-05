import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it correct!  The answer is: {answer}")


def set_diffuculty():
    level = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print("Welcome to the guessing game!")

    print("I am thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"The answer is {answer}")

    turns = set_diffuculty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} to guess the number!")
        guess = int(input("Pick a number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of turns, the correct answer is {answer}")
            return
        elif guess != answer:
            print("Guess again")


game()
