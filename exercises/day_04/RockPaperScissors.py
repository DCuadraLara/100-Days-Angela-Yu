
# Rock Paper Scissors game with a creative touch, here you have 3 modes normal - hard - Vsplayer.

import random


# Win condition function.
def ascii_print(choice_num):
    if choice_num == 0:
        print(
            '''
                            _______         
                        ---'   ____)
                              (_____)
                              (_____)
                              (____)
                        ---.__(___)
                        '''
        )
    elif choice_num == 1:
        print(
            '''
                            _______         
                        ---'   ____)____
                                  ______)
                                  _______)
                                 _______)
                        ---.__________)
                     '''
        )
    elif choice_num == 2:
        print(
            '''
                         _______        
                     ---'   ____)____
                                 ______)
                               __________)
                           (____)
                      ---.__(___)
                      '''
        )
    elif choice_num == 3:
        print(
            '''
,________________________________       
|__________,----------._ [____]  ""-,__  __...-----==="
        (_(||||||||||||)___________/   ""             |
           `----------' Krogg98[ ))"-,                |
                                ""    `,  _,--...___  |
                                        `/          """
        '''
        )



def win_condition(player, ia):
    if player == ia:
        return "--- DRAW ---"
    elif (player - ia) % 3 == 1:
        return "--- PLAYER WINS ---"
    else:
        return "--- IA WINS ---"


def normalize_num(number):
    return number - 1


# We introduce game and mode selection.
print("\n*** Welcome to our Rock Paper Scissors Game!! ***\n")
print(" -------------\n")

# Choice list.
choice_list = ["Rock", "Paper", "Scissors"]

while True:
    try:
        print("Please Introduce the mode you wanna play --> ")

        while True:
            try:
                mode = int(input("1. Normal Mode.\n2. Impossible Mode.\n3. VsPlayer.\n\n"))

                if mode in (1, 2, 3):
                    break
            except ValueError:
                print("Introduce a valid number for the mode please.")

        # 1. -- Normal mode.
        if mode == 1:
            print("\nStarting game...\n")

            while True:
                try:
                    player_1 = int(
                        input(
                            "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
                        )
                    )

                    if player_1 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
                        player_1 = normalize_num(player_1)
                        break
                except ValueError:
                    print("Select a correct hero hand!")

            # IA roll for a random hand.
            ia_hand = random.randint(0, 2)

            print("----------------------------")
            print("\nThe player hero hand is... \n")
            ascii_print(player_1)
            print("The IA villain hand is... \n")
            ascii_print(ia_hand)

            print(win_condition(player_1, ia_hand))
            break  # End loop condition.

        # 2. -- Hard mode.
        elif mode == 2:
            print("\nStarting game...\n")

            while True:
                try:
                    player_1 = int(
                        input(
                            "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
                        )
                    )

                    if player_1 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
                        player_1 = normalize_num(player_1)
                        break
                except ValueError:
                    print("Select a correct hero hand!")

            # IA roll for a random hand with an extra option.
            choice_list.append("Shotgun")
            ia_hand = random.randint(0, 3)

            print("----------------------------")
            print("\nThe player hero hand is... \n")
            ascii_print(player_1)
            print("The IA villain hand is... \n")
            ascii_print(ia_hand)

            if ia_hand == 3:
                print("SECRET HAND... IA GUN APPEARED AND ALWAYS WINS!\n")
                print("--- IA WINS ---")
                break
            else:
                print(win_condition(player_1, ia_hand))
                break  # End loop condition.

        # 3. -- VS player.
        else:
            print("\nStarting game...\n")

        while True:
            try:
                print("Player 1 -- Turn")
                print("Player 2 dont cheat! Dont look here :D \n")
                player_1 = int(
                    input(
                        "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
                    )
                )

                print("Player 2 - Your turn")
                player_2 = int(
                    input(
                        "Select a number! Choose your hero hand!\n 1.Rock --- 2.Paper --- 3. Scissors\n"
                    )
                )

                if player_1 in (1, 2, 3) and player_2 in (1, 2, 3):  # Check player hand as a valid answer to break Loop.
                    
                    print("----------------------------")
                    print("\nThe player 1 hero hand is... \n")
                    player_1 = normalize_num(player_1)
                    ascii_print(player_1)
                    print("The player 2 hero hand is... \n")
                    player_2 = normalize_num(player_2)
                    ascii_print(player_2)

                    if player_1 == player_2:
                        print("--- DRAW ---")
                    elif (player_1 - player_2) % 3 == 1:
                        print("--- Player 1 Wins! ---")
                    else:
                        print("--- Player 2 Wins! ---")
                    break

            except ValueError:
                print("Select a correct hero hand!")

    except ValueError:
        print("Invalid Mode. Please select again.")
    break

print("\n\nThanks for playing my game :) ")
