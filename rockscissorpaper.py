import random

print("\n**** Welcome to our rock, paper and scissors game! ****\n")
ia_list = ["rock", "paper", "scissor"]
# loop check for correct input.
while True:
    player_choice = int(input("Please choose your hero hand!: \n0- rock\n1- paper\n2- scissor\n"))


    if player_choice == 0:
        print("Your hero hand is...\n")
        print('''
    _______         ROCK POWER!!!!!
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
        break
    elif player_choice == 1:
        print("Your hero hand is...\n")
        print('''
    _______         PAPER POWER!!!
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
        break
    elif player_choice == 2:
        print("Your hero hand is...\n")
        print('''
    _______         SCISSOR POWER!!!
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
        break
    else:
        print("YOU ENTERED A BAD INPUT")

# ia decision print
print(" .-..-.-.-.-- IA ITS CHOOSING -.-.-.-.-\n\n")
ia_number = random.randint(0, 2)
ia_choice = ia_list[ia_number]
print("IA Villain hand is...\n")
if ia_number == 0:
    print('''
    _______         ROCK POWER!!!!!
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif ia_number == 1:
    print('''
    _______         PAPER POWER!!!
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

elif ia_number == 2:
    print('''
    _______         SCISSOR POWER!!!
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

# win conditions
if ia_number == 0:
    if player_choice != 0:
        if player_choice == 1:
            print("PLAYER 01 WIN!")
        elif player_choice == 2:
            print("IA WIN!")
    else:
        print("DRAW!")

elif ia_number == 1:
    if player_choice != 1:
        if player_choice == 0:
            print("IA WIN!")
        elif player_choice == 2:
            print("PLAYER 01 WIN!")
    else:
        print("DRAW!")

elif ia_number == 2:
    if player_choice != 2:
        if player_choice == 0:
            print("PLAYER 01 WIN!")
        elif player_choice == 1:
            print("IA WIN!")
    else:
        print("DRAW!")