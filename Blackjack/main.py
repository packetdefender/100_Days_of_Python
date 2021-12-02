import art
import random

print(art.logo)


def deal_cards():
    hand = []
    dealing = True
    while dealing:
        draw_card = random.choice(cards)
        hand.append(draw_card)
        if len(hand) == 2:
            return hand


def calculate_score(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    return sum(hand)
    # return(hand)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

game_on = True
while game_on:
    player_hand = deal_cards()
    dealer_hand = deal_cards()
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your cards: {player_hand}, current score {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")
    player_turn = True
    while player_turn:
        if player_score == 0:
            print("HERE PS = 0")
            player_turn = False
        elif player_score > 21:
            print("HERE - P-S > 21")
            player_turn = False
        player_choice = input("Do you want to Hit or Stand: ").upper()
        if player_score < 21:
            print("Here")
            if player_choice == "H":
                player_hand.append(random.choice(cards))
                player_score = calculate_score(player_hand)
                print(
                    f"Your cards: {player_hand}, current score {player_score}")
            elif player_choice == "S":
                print("IN S")
                player_turn = False

    dealer_turn = True
    while dealer_turn:
        if sum(dealer_hand) < 16:
            draw_card = random.choice(cards)
            dealer_hand.append(draw_card)
        else:
            dealer_turn = False
    print(
        f"The dealers final hand is {dealer_hand}, final score {dealer_score}")
    if player_score == 0:
        print(f"You win with Blackjack! {player_hand}")
        game_on = False
    elif player_score > 21:
        print(f"You lose!")
        print(
            f"The dealers final hand is {dealer_hand}, final score {dealer_score}")
        game_on = False
    elif player_score > dealer_score:
        print(f"You win with: {player_hand}")
        game_on = False
    else:
        print(f"You lose!")
        game_on = False
# print(player_hand)
# print(dealer_hand[0])
