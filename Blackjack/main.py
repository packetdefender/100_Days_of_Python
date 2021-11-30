import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []


def deal_cards():
    hand = []
    dealing = True
    while dealing:
        draw_card = random.choice(cards)
        hand.append(draw_card)
        if len(hand) == 2:
            return hand


def calculate_score(hand):
    return sum(hand)
    # return(hand)


def check_blackjack(hand):
    if sum(hand) == 21:
        return 0
    else:
        return hand


game_on = True
while game_on:
    user_hand = deal_cards()
    dealer_hand = deal_cards()
    user_score = calculate_score(user_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your cards: {user_hand}, current score {user_score}")
    print(f"Dealer's first card: {dealer_hand}")
    user_blackjack = check_blackjack(user_hand)
    dealer_blackjack = check_blackjack(dealer_hand)
    print(user_blackjack)
    print(dealer_blackjack)
    check_blackjack = True

    while player_turn:
        player_choice = input("Do you want to Hit or Stand: ").upper()
        if player_choice == "H":
            user_hand.append(random.choice(cards))
            user_score = calculate_score(user_hand)
            print(f"Your cards: {user_hand}, current score {user_score}")
        else:
            print(f"Your final hand is {user_hand}, final score {user_score}")
            print(
                f"The dealers final hand is {dealer_hand}, final score {dealer_score}")
            player_turn = False
    if user_score > dealer_score:
        print(f"You win with: {user_hand}")
        game_on = False
    else:
        print(f"You lose!")
        game_on = False
# print(user_hand)
# print(dealer_hand[0])
