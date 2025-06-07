secret_auction = {}

def highest_bidder(bidding_dictionary):
    winner = ""
    top_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > top_bid:
            top_bid = bid_amount
            winner = bidder

    print(f"\n🏆 The winner is {winner} with a bid of ${top_bid}!")


while True:
    name = input("Introduce your name: ")
    bid = int(input("Introduce your budget: "))
    
    secret_auction[name] = bid # Assign key to value into dictionary

    reset = input("There are more users bid? Y/N: ").lower()
    clear_screen()
    if reset != "y":
        break

highest_bidder(secret_auction)
