import art
import random

print(art.logo)
print("I am thinking of a number between 1 and 100.")
difficulty_level = input(
    "Choose a difficulty.  Type 'easy' or 'hard': ").lower()


answer = random.choice(range(1, 101))


def easy_turn():
    attempts = 10
    number_guessing = True
    while number_guessing:
        if attempts > 0:
            user_guess = int(input(
                f"you have {attempts} to guess the number!  Pick a number to see if you are correct: "))
            if user_guess == answer:
                print(
                    f"You gussed the correct number!  The correct number is {answer}.  You win!")
                number_guessing = False
            elif user_guess > answer:
                print('Your guess is too high')
                print("Guess again")
                attempts -= 1
            elif user_guess < answer:
                print('Your guess is too low')
                print("Guess again")
                attempts -= 1
            else:
                print(f"You guessed incorrectly.")
                attempts -= 1
        else:
            print(
                f"You ran out of guesses, you lose.  The correct answer is {answer}")
            number_guessing = False


def hard_turn():
    attempts = 5
    print(answer)
    number_guessing = True
    while number_guessing:
        if attempts > 0:
            user_guess = int(input(
                f"you have {attempts} to guess the number!  Pick a number to see if you are correct: "))
            if user_guess == answer:
                print(
                    f"You gussed the correct number!  The correct number is {answer}.  You win!")
                number_guessing = False
            elif user_guess > answer:
                print('Your guess is too high')
                print("Guess again")
                attempts -= 1
            elif user_guess < answer:
                print('Your guess is too low')
                print("Guess again")
                attempts -= 1
            else:
                print(f"You guessed incorrectly.")
                attempts -= 1
        else:
            print(
                f"You ran out of guesses, you lose.  The correct answer is {answer}")
            number_guessing = False


if difficulty_level == 'easy':
    easy_turn()
elif difficulty_level == 'hard':
    hard_turn()


# number_guess(difficulty_level)
