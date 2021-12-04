# def bar():
#     my_variable = 9

#     if 16 > 9:
#         my_variable = 16

#     print(my_variable)


# bar()


# enemies = 1


# def increase_enemies():
#     print(f"Enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"Enemies outside function: {enemies}")


# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# wordlist = ['ardvark', 'baboon', "camel"]

# chosen_word = random.choice(wordlist)
# display = list("_" * len(chosen_word))
# game_on = True
# lives = 6
# while game_on:
#     guessed_letter = input("Please guess a letter: ").lower()
#     for idx, letter in enumerate(chosen_word):
#         if guessed_letter == letter:
#             display[idx] = guessed_letter
#             if "_" not in display:
#                 game_on = False
#                 print("You Win!")
#     if guessed_letter not in chosen_word:
#         lives -= 1
#         print(stages[lives])
#         if lives == 0:
#             game_on = False
#             print(f"You Lose!  The word is {chosen_word}")
#     if game_on == True:
#         print(f"{' '.join(display)}")
