import random
import hangman_art
import hangman_words

if __name__ == "__main__":
    print(hangman_art.logo)
    chosen_word = random.choice(hangman_words.word_list)
    display = list("_" * len(chosen_word))
    game_on = True
    lives = 6
    picked_letters = []
    while game_on:
        guessed_letter = input("Please guess a letter: ").lower()
        if guessed_letter in picked_letters:
            print(f"The letter {guessed_letter} was picked already")
            print(picked_letters)
        for idx, letter in enumerate(chosen_word):
            if guessed_letter == letter:
                display[idx] = guessed_letter
                if "_" not in display:
                    game_on = False
                    print("You Win!")
        if guessed_letter not in chosen_word and guessed_letter not in picked_letters:
            lives -= 1
            print(f"The letter {guessed_letter} is not in the word")
            print(hangman_art.stages[lives])
            picked_letters.append(guessed_letter)
            if lives == 0:
                game_on = False
                print(f"You Lose!  The word is {chosen_word}")
        if game_on == True:
            print(f"{' '.join(display)}")
