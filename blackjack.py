# Blackjack game
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
croupier_cards = []
player_cards = []
player_money = 1000

# Functions definitions
def initial_deal():
    get_player_cards()
    get_croupier_cards()
    get_player_cards()
    get_croupier_cards()


def get_player_cards():
    random_player = random.choice(cards)
    player_cards.append(random_player)


def get_croupier_cards():
    random_croupier = random.choice(cards)
    croupier_cards.append(random_croupier)


def sum_cards_croupier():
    while sum(croupier_cards) < 17:
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


def money_check(player_money):
    if player_money <= 0:
        print("* YOU LOST ALL YOUR MONEY *")
        return True
    return False


def _main_():
    while True:
        total_player_card = sum(player_cards)
        total_croupier_card = sum(croupier_cards)

        # Total money check
        if money_check(player_money):
            break

        # count check for both.
        if total_player_card > 21:
            break
        elif total_croupier_card > 21:
            break
        else:
            ask_card = input("*CARD*..........*STAY*\n\n").lower()
            if ask_card == "card":
                get_player_cards()
                total_player_card = sum(player_cards)
                as_swicth_check()
                print(total_player_card) # just for test
                print(f"Your cards are {player_cards} and the total amount is: {sum(player_cards)} ")
                print(f"Croupier cards are [{croupier_cards[0]}, x]")
            else: # Stay
                sum_cards_croupier()
                break


# init
print("*** Welcome to our blackjack game! ***")
input("Press any key to start the game :=) ")
while True:
    actual_bet = input("Please select the amount you want to bet on this round:"
                           "* 50 *  * 100 *  * 250 *  * 500 *  * All in * \n\n").lower()

    if actual_bet == "all in":
        actual_bet = player_money
    else:
        try:
            actual_bet = int(actual_bet)
            if actual_bet not in [50, 100, 250, 500] or actual_bet > player_money:
                print("Invalid bet, try again")
                continue
        except ValueError:
            print("Invalid bet, try again")
            continue

    print("\n.-.-.-....shuffling.-.--.-.\n")

    initial_deal()

    print(f"Your cards are {player_cards}")
    print(f"Croupier cards are [{croupier_cards[0]}, x]")
    _main_()

    if sum(player_cards) > 21:
        print(f"\nPlayer lost with {sum(player_cards)}! Croupier wins.")
        player_money -= actual_bet
        continue

    # Win conditions
    if sum(player_cards) == sum(croupier_cards):
        print(f"\n\n\nYour cards are {player_cards} and the total is {sum(player_cards)} ")
        print(f"Croupier cards are {croupier_cards} and the total is {sum(croupier_cards)} ")
        print("*** DRAW! ***")
        print(f"Your actual money is: {player_money} ")
    elif sum(player_cards) > sum(croupier_cards) and sum(player_cards) < 21:
        print(f"\n\n\nYour cards are {player_cards} and the total is {sum(player_cards)} ")
        print(f"Croupier cards are {croupier_cards} and the total is {sum(croupier_cards)} ")
        print("*** PLAYER WIN! ***")
        player_money += actual_bet
        print(f"Your actual money is: {player_money} ")
    else:
        print(f"\n\n\nYour cards are {player_cards} and the total is {sum(player_cards)} ")
        print(f"Croupier cards are {croupier_cards} and the total is {sum(croupier_cards)} ")
        print("*** CROUPIER WIN! ***")
        player_money -= actual_bet
        print(f"Your actual money is: {player_money} ")

    reset = input("\nNew game?... Y/N\n").lower()
    if reset != "y":
        break
    # We need to clear both decks for a new game.
    player_cards.clear()
    croupier_cards.clear()

print("Thanks for playing!! :) ")
