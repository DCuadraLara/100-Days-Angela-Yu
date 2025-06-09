# Blackjack game
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
croupier_cards = []
player_cards = []

# Functions definitions
def initial_deal():
    get_player_cards()
    get_croupier_cards()
    get_player_cards()
    get_croupier_cards()


def get_player_cards():
    random_player =+ random.choice(cards)
    player_cards.append(random_player)


def get_croupier_cards():
    random_croupier =+ random.choice(cards)
    croupier_cards.append(random_croupier)


def sum_cards_croupier(total_croupier):
    while total_croupier < 17:
        get_croupier_cards()
    print("...Croupier Stay...")


def as_swicth_check():
    for i in range(len(player_cards)):
        if player_cards[i] == 11 and sum(player_cards) > 21:
            player_cards[i] = 1
            print("AS NOW IT'S 1")
        elif player_cards[i] == 1 and sum(player_cards) < 11:
            player_cards[i] = 11
            print("AS NOW IT'S 11")


def _main_():
    for _ in player_cards:
        total_player_card = sum(player_cards)
        total_croupier_card = sum(croupier_cards)

        # count check for both.
        if total_player_card > 21:
            break
        if total_croupier_card > 21:
            break

        else:
            ask_card = input("*CARD*..........*STAY*\n\n").lower()
            if ask_card == "card":
                get_player_cards()
                as_swicth_check()
                print(total_player_card) # just for test
                print(f"Your cards are {player_cards}")
                print(f"Croupier cards are [{croupier_cards[0]}, x]")
            else: # Stay
                sum_cards_croupier(total_croupier_card)
                break


# init
print("*** Welcome to our blackjack game! ***")
input("Press any key to start the game :=) ")
while True:
    print("\n.-.-.-....shuffling.-.--.-.\n")

    initial_deal()

    print(f"Your cards are {player_cards}")
    print(f"Croupier cards are [{croupier_cards[0]}, x]")
    _main_()

    # Win conditions
    if sum(player_cards) == sum(croupier_cards):
        print(f"\n\n\nYour cards are {player_cards}")
        print(f"Croupier cards are {croupier_cards}")
        print("*** DRAW! ***")
    elif sum(player_cards) > sum(croupier_cards) and sum(player_cards) < 21:
        print(f"\n\n\nYour cards are {player_cards}")
        print(f"Croupier cards are {croupier_cards}")
        print("*** DEALER WIN! ***")
    else:
        print(f"\n\n\nYour cards are {player_cards}")
        print(f"Croupier cards are {croupier_cards}")
        print("*** CROUPIER WIN! ***")

    reset = input("\nNew game?... Y/N\n").lower()
    if reset != "y":
        break
    # We need to clear both decks for a new game.
    player_cards.clear()
    croupier_cards.clear()

print("Thanks for playing!! :) ")