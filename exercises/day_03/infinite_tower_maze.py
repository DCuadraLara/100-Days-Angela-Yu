
"""We gonna create a Infinite Tower Maze.

The player will have several choices to go on a way A, B or C.
You must pick only one.
"""

print(r'''

                         |\
                         |_\
                         |
                         |
      _,__,              /
     (00000)            /\
    (00000)    __      /# \
   (q888889)  (00)    /### \
  (00q890OO0)(0000)  /a#### \
       (0000000)    /####### \    sSSsS,
                    |a'aaaaa |   ssSSSs8
                    |aa'  aa |   SSSSSSs'
                    |aa'  a' |   s\\Ss/Ss
                    |a'aaaaa |    s\\//S
                    |aaa'aa| |      |/
                  #8|a|aaaaa |#     ||
                 # 8|aaa|aaa||###8  ||
                #8###aaaaaaa |88##8###  ##
               ####88#8 #8#8#888###8|###  ###
          #######88# 8#88 ##8###8888## #     #
        _/000## #888 ###8  8##88#88##   #     #
       /  ##   # #8   88#### 8####88## , # ### #
     _/     ###  #########8###888888\ '    #  ####
    /     /    #####  \     'chelle  \_'    #   ####
   |                   |    |  _   98  \       _/  \
                        \_   \/         \__   /     \

''')

print("\n*** Welcome to the Infinite Tower Maze ***\n")
print("Your mission is to get out of this infinite loop, but please dont die on the process haha\n "
      "¿Would you be able to do it? or you just gonna get lost on the way home...\n")

# Random input to start it and have some gameplay.
input("Breath one more time and feel the magic before you start your adventure...\n\n\n")


# Quest list.
quests = {
    "quest01":{
        "text": "You wake up on a strange room, that's not your house... wait you see some dumb decoration.\n"
                "You see a mechanism on the wall near the door, you want to see what's outside the room...",
        "options": {
            "A": "Press that mechanism.. oh wait the door its still closed. Suddenly the wall start moving."
                 "There is a hole now with some stairs!",
            "B": "You prefer to ignore it and just try to sleep again, maybe you wake up on your room.",
            "C": "You decided to see if there is other way... oh well the room have some windows."
        }
    },
    "quest02":{
        "text": "You decided to go down stairs, but you need some light right? or... wanna go down darky.",
        "options": {
            "A": "Take a super candle, maybe that works? It have the super power of light hehe",
            "B": "You go down darky, you trust your 'cat' eyes"
        }
    },
    "quest03":{
        "text": "You went outside and see some runes on the air... You feel the power of them",
        "options": {
            "A": "Just ignore it and keep going on the roof",
            "B": "Touch the runes? definitely a nice idea?"
        }
    },
    "death":{
        "text": "You died Hero. Try again."
    },
    "escape":{
        "text": "You escaped! Well done Hero."
    },
}

# Def reset function
def reset_player():
    """Reset player input."""
    return ""


# Init values
player_choice = reset_player()


# Quest 01 -- Room with mechanism.
print(f"\n{quests['quest01']['text']}\n")

while player_choice not in ["A", "B", "C"]: # A,B,C check.
    for key, value in quests["quest01"]["options"].items():
        print(f"{key} {value}")

    player_choice = input("\nChoose wisely: \nA \nB \nC\n\n").upper().strip()


if player_choice == "A":
    print(f"\n{quests['quest02']['text']}\n") # Quest 02 -- Stairs.
    player_choice = reset_player() # Reset player choice so we can get into while.

    while player_choice not in ["A", "B"]:  # A,B check.
        for key, value in quests["quest02"]["options"].items():
            print(f"{key} {value}")

        player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()

        if player_choice == "A": 
            print(f"You burned yourself with super duper candle!\n {quests['death']['text']}")
        else:
            print(f"You manage to avoid some traps, oh that's... a door?\n {quests['escape']['text']}")

elif player_choice == "B": 
    print(f"At midnight you hear a strange noise, its a monster coming!\n {quests['death']['text']}")
else:
    print(f"\n{quests['quest03']['text']}\n") # Quest 03 -- Windows.
    player_choice = reset_player()  # Reset player choice so we can get into while.

    while player_choice not in ["A", "B"]:  # A,B check.
        for key, value in quests["quest03"]["options"].items():
            print(f"{key} {value}")

        player_choice = input("\nChoose wisely: \nA \nB\n\n").upper().strip()
        
        if player_choice == "A": 
            print(f"You slice with that floor and broke your head, holy that's not lucky\n {quests['death']['text']}")
        else:
            print(f"The rune started to do so much noise, you see many lights! What¿? You are on home...\n {quests['escape']['text']}")
