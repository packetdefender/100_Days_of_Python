import art
import os
def cls(): return os.system('clear')


print(art.logo)

bids = {}

auction_on = True


def find_highest_bidder(bidding_record):
    previous_bid = 0
    for bidder in bidding_record:
        if bidding_record[bidder] > previous_bid:
            previous_bid = bids[bidder]
            winner_name = bidder
            winner_bid = bids[bidder]
    print(f"The wiiner is {winner_name} with a bid of ${winner_bid}")


while auction_on:
    name = input("What is your name: ")
    bid = int(input("What is your bid: "))
    more_bidders = input("Are there any more bidders (Yes or No): ").lower()
    bids[name] = bid

    if more_bidders == "yes":
        cls()
    elif more_bidders == "no":
        find_highest_bidder(bids)
        auction_on = False
