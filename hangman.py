import random

word_list = ["aardvark", "baboon", "camel"]
lost_lives = ["Iron company its here, you feel that axe on the neck? ", "Ops...", "Come on... wake up "
    , "Lucky this little stick its not your friend"]

# list of our poor guy
# list of our poor guy
poorguy_stages = [
    r''' 

         |/      
         |      
         |    
         |       
         |     
         |
     jgs_|___''',

    r''' 
          _______
         |/    
         |   
         |     
         |      
         |       
         |
     jgs_|___''',

    r''' 
          _______
         |/      |
         |      (_)
         |      
         |       
         |      
         |
     jgs_|___''',

    r''' 
          _______
         |/      |
         |      (_)
         |      \|/
         |       
         |      
         |
     jgs_|___''',

    r''' 
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      
         |
     jgs_|___''',

    r''' 
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      / 
         |
     jgs_|___''',

    r''' 
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      / \ 
         |
     jgs_|___''',
]

chosen_word = random.choice(word_list)
display = ["_" for _ in range(len(chosen_word))]  # For each letter in range of len word
lives = 7

while lives != 0:
    print("-------------------------------------------")
    guess = input("Guess a letter: ").lower()  # player input
    found = False
    for _ in range(len(chosen_word)):  # For each letter in range of len word
        if guess == chosen_word[_]:
            display[_] = guess
            found = True
        else:
            pass

    print("".join(display))  # join list
    # lives count
    if not found:
        chosen_lost = random.choice(lost_lives)  # some funny stuff
        print(chosen_lost)
        lives -= 1
    print(poorguy_stages[7 - lives])

    # win condition
    if "_" not in display:
        print(f"Well done! You did it! the word is {chosen_word}")

    print(f"Actual lives: {lives} \n")
print("******************************")
print("         GAME OVER! ")
print("******************************")