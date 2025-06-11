# Number Guessing Game, you choose a difficulty and think about a number between 1 - 100, you have got 5 attempts
# If you are too low print it, if you are too high same.

import random

# Frases
fail = [
    "You failed! That's not the number",
    "Meeeh you are doing it like a shit",
    "Iron league of guessing number!"
]
win = [
    "Got it! You rock bro",
    "Hold it, we got a master guess!",
    "Diamond league?, we got a champion!"
]

# Functions
def compare_nums(my_num, rand_num):
    if my_num < rand_num:
        print(random.choice(fail))
        print("Too low")
    elif my_num > rand_num:
        print(random.choice(fail))
        print("Too high")

# Main
print("*** Welcome to our Number Guessing Game! ***")
print("Please think about a number between 1 and 100 ")

#difficulty selection
while True:
    difficulty = str(input("Choose a difficulty... Type 'Easy' or 'Hard' or 'Impossible': ")).lower()
    if difficulty in ["easy", "hard", "impossible"]:
        print(f"You choose: {difficulty.capitalize()}")
        break
    else:
        print(f"Bad input you typed: {difficulty.capitalize()}")

if difficulty == "easy":
    lives = 10
elif difficulty == "impossible":
    lives = 3
else:
    lives = 5
print(f"You have {lives} ❤️ ")

# Random number
print("We are looking for a mad number... please wait")
random_num = random.randint(1, 100)
print("-.-.-.----.,-.--,--\n Done!!!\n")

# Pick a number
while lives > 0:
    try:
        print("-")
        player_num = int(input("Introduce your number: "))
        if player_num < 1 or player_num > 100:
            print("Number should be between 1 and 100.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if player_num == random_num:
        print(random.choice(win))
        break
    else:
        compare_nums(player_num, random_num)
        lives -= 1
        print(f"Your actual lives: {lives} ❤️")

if lives == 0:
    print(f"You lost the game!! The number was {random_num}.")

print("Thanks for playing! ")
