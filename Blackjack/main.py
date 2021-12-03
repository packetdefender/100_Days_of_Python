import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
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
    if hand == 0:
        return 0
    else:
        return sum(hand)


def player_turn(hand):
    player_turn = True
    if sum(hand) == 21:
        return 0
    while player_turn:
        if 11 in hand and sum(cards) > 21:
            hand.remove(11)
            hand.append(1)
        if sum(hand) > 21:
            return hand
        player_choice = input("Do you want to Hit or Stand: ").upper()
        if player_choice == "H":
            hand.append(random.choice(cards))
            player_score = calculate_score(hand)
            print(f"Your cards: {hand}, current score {player_score}")
        elif player_choice == "S":
            return hand
        elif sum(hand) > 21:
            print("IN sum(hand) > 21 BOTTOM")
            return hand


def dealer_turn(hand):
    dealer_turn = True
    if sum(hand) == 21:
        return 0
    while dealer_turn:
        if sum(hand) < 16:
            draw_card = random.choice(cards)
            hand.append(draw_card)
        else:
            return hand


game_on = True
while game_on:
    player_start_hand = deal_cards()
    dealer_start_hand = deal_cards()
    player_score = calculate_score(player_start_hand)
    dealer_score = calculate_score(dealer_start_hand)

    print(f"Your cards: {player_start_hand}, current score {player_score}")
    print(f"Dealer's first card: {dealer_start_hand[0]}")

    player_hand = player_turn(player_start_hand)
    dealer_hand = dealer_turn(dealer_start_hand)

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if player_score == 0:
        print(f"You win! Blackjack! {player_hand}")
        print(f"The dealer had: {dealer_hand} with a score of {dealer_score}")
        game_on = False
    elif dealer_score == 0:
        print(f"You lose :(! Dealer Blackjack! {player_hand}")
        print(f"The dealer had: {dealer_hand} with a score of {dealer_score}")
        game_on = False
    elif player_score > 21:
        print(
            f"You lose, BUST! :(.  With a hand of {player_hand}, and a score of {player_score}!")
        print(
            f"The dealers wins.  Final hand is {dealer_hand}, final score {dealer_score}")
        game_on = False
    elif dealer_score > 21:
        print(
            f"You win! Dealer Busts!  With a hand of {player_hand}, and a score of {player_score}!")
        print(
            f"The dealers final hand is {dealer_hand}, final score {dealer_score}")
        game_on = False
    elif player_score > dealer_score:
        print(
            f"You win :)!  Your hand is: {player_hand}, and a score of: {player_score}")
        print(f"The dealer had: {dealer_hand} with a score of {dealer_score}")
        game_on = False
    elif player_score == dealer_score:
        print(
            f"PUSH!! Your hand is: {player_hand}, and a score of: {player_score}")
        print(f"The dealer had: {dealer_hand} with a score of {dealer_score}")
        game_on = False
    else:
        print(
            f"You lose, with a hand of {player_hand}, and a score of {player_score}!")
        print(
            f"The dealers final hand is {dealer_hand}, final score {dealer_score}")
        game_on = False
