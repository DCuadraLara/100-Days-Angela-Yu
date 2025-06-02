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


# Your Hero
class Hero:
    def __init__(self):
        self.intelligence = 0
        self.strenght = 0
        self.agility = 0
        self.luck = 0

    def increase_intelligence(self):
        self.intelligence += 1
        return self.intelligence

    def increase_strenght(self):
        self.strenght += 1
        return self.strenght

    def increase_agility(self):
        self.agility += 1
        return self.agility

    def increase_luck(self):
        self.luck += 1
        return self.luck

player = Hero()

# input to start it
input("Breath one more time and feel the magic before you start your adventure...\n\n\n")

# first decision
print("\nYou wake up on a dark room alone... you feel strange, that's not your house...")
print("You see a little table, some strange artefacts on it, some kind of old book, huh... there is so much dust on it")
print("You need to make your first move on this...\n\n"
      "A: You go to read that book, you are super curious, maybe... ¿It have any spell to get out of there?\n"
      "B: You take a candle near the bed, and go to the door to get an eye on whats outside\n"
      "C: You take one of the artifacts and throw it aggressively\n")

# A,B,C check
player_decision = ""
while player_decision not in ["A", "B", "C"]:
    player_decision = input("Choose wisely: \nA \nB \nC\n\n")

if player_decision == "A":
    print(r'''
              .__=\__                  .__==__,
            jf'      ~~=\,         _=/~'      `\,
        ._jZ'            `\q,   /=~             `\__
       j5(/                 `\./                  V\\,   
     .Z))' _____              |             .____, \)/\
    j5(K=~~     ~~~~\=_,      |      _/=~~~~'    `~~+K\\,
  .Z)\/                `~=L   |  _=/~                 t\ZL
 j5(_/.__/===========\__   ~q |j/   .__============___/\J(N,
4L#XXXL_________________XGm, \P  .mXL_________________JXXXW8L
~~~~~~~~~~~~~~~~~~~~~~~~~YKWmmWmmW@~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    print("Ohh! You see a strange mechanism on the side of it, when you press it the book start doing some noise, it was a mistery box!\n")
    print("Inside you see an old note with an amulet, ¿what's the purpose of that?\n")
    player.increase_intelligence()
    print("\n\n****************************\n"
          f"You get smarter! Intelligence value its now {player.intelligence} Well done!"
          "****************************\n\n")
elif player_decision == "B":
    print("You see a large room next to you, its so dark, but you got ur candle! You start walking around\n"
          "The light was not enough and you fall on a trap!!\n")
    print("ENDPOINT, YOU DIED!\n")
elif player_decision == "C":
    print('''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

''')
    print("\nWhen the artefact drops to the floor, you see some images of the past! You know the way to a secret room, awesome!!\n")
    player.increase_luck()
    print("\n\n****************************\n"
          f"You are so lucky! Luck value its now {player.luck} Well done!"
          "****************************\n\n")
# second text
if player_decision == "A":
    print("\nYou decided to get out of the room with that amulet on the neck, its so dark out there! probably the candle was a better choice... huh\n"
          "So when you started walking the amulet start getting a bit hot, the light of the room its on! magic!"
          "You see the traps on the floor and manage to avoid them..."
          "You got it!")
    player.increase_agility()
    print("\n\n****************************\n"
          f"You get faster! Agility value its now {player.agility} Well done!"
          "****************************\n\n")
    print("You get to a new room, there are plenty of strange things around... Some blades...\n"
          "A small potion called Super Venom huh ¿better avoid it?\n"
          "Some bones on the wall... when I say some.. there are plenty of them!\n")
    print("lets think a bit...\n"
          "A: You can get the blades, maybe you can survive longer no?\n"
          "B: Lets drink that super potion\n"
          "C: Get some bones\n")

if player_decision == "C":
    print("\nYou find a secret room with a long way down, you get to a room with 2 doors, One red and One black\n")
    print("lets think a bit...\n"
          "A: You choose the Red Door\n"
          "B: You choose the Black Door\n"
          "C: Get back upstairs\n")

# A,B,C check
player_decision = ""
while player_decision not in ["A", "B", "C"]:
    player_decision = input("Choose wisely: \nA \nB \nC\n\n")
