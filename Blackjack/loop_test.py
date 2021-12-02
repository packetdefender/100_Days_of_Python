import random

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
    return sum(hand)
    # return(hand)


def check_blackjack(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0
    else:
        return hand


def player_turn(hand):
    player_turn = True
    while player_turn:
        if check_blackjack(hand):
            print("CHECK Blackjack")
            player_turn = False
        # elif sum(hand) < 21:
        #   print("Here")
        #   Return(hand)
        playerchoice = True
        while playerchoice:
            if sum(hand) > 21:
                return hand
            player_choice = input("Do you want to Hit or Stand: ").upper()
            if player_choice == "H":
                print("HIT LOOP")
                hand.append(random.choice(cards))
                player_score = calculate_score(hand)
                print(f"Your cards: {hand}, current score {player_score}")
            elif player_choice == "S":
                print("IN S")
                return hand
            elif sum(hand) > 21:
                print("IN sum(hand) > 21 BOTTOM")
                return hand


player_hand = deal_cards()
dealer_hand = deal_cards()
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)
print(f"The Player has: {player_turn(player_hand)}")
