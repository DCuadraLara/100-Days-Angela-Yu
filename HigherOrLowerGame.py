# Higher or lower game
import random

# Game data
win_list = ["Nice one! You did it! ", "Oh you rock! ", "Master, teach me "]
game_data = [
    {
        "name": "ElRubius",
        "follower_count": 65000000,
        "description": "Youtuber, Streamer, Amante de Mangel",
        "country": "Noruega - España"
    },
    {
        "name": "Mangel",
        "follower_count": 2808362,
        "description": "Youtuber, Streamer, Amante de Rubius",
        "country": "España"
    },
    {
        "name": "Bad Bunny",
        "follower_count": 45000000,
        "description": "Cantante de reguetón y trap latino",
        "country": "Puerto Rico"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 100000000,
        "description": "Cantautora pop y country",
        "country": "Estados Unidos"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 395000000,
        "description": "Actor, exluchador profesional, empresario",
        "country": "Estados Unidos"
    },
    {
        "name": "Ibai Llanos",
        "follower_count": 17000000,
        "description": "Streamer, presentador, organizador de eventos",
        "country": "España"
    },
    {
        "name": "AuronPlay",
        "follower_count": 30000000,
        "description": "Youtuber, streamer, experto en troleos",
        "country": "España"
    },
    {
        "name": "Karol G",
        "follower_count": 37000000,
        "description": "Cantante de reguetón y pop latino",
        "country": "Colombia"
    },
    {
        "name": "MrBeast",
        "follower_count": 240000000,
        "description": "Youtuber filántropo y empresario",
        "country": "Estados Unidos"
    },
    {
        "name": "Keanu Reeves",
        "follower_count": 20000000,
        "description": "Actor, estrella de Matrix y John Wick",
        "country": "Canadá"
    }
]

# Global values
points = 0


def get_random_person():
    person = random.choice(game_data)
    return person["name"], person["follower_count"], person["description"], person["country"]


def set_first_from_second():
    global first_name, first_follower, first_description, first_country
    first_name = second_name
    first_follower = second_follower
    first_description = second_description
    first_country = second_country


print("*** Welcome to our Higher or Lower Game ***")
input("Press any key to start it!... ")

first_name, first_follower, first_description, first_country = get_random_person()

while True:
    print(f"The first person is: {first_name} and they have {first_follower} followers!")
    print(first_description)
    print(f"From: {first_country}")
    print("----------\n--- VS ---\n----------")

    # Check if first name != second name
    while True:
        second_name, second_follower, second_description, second_country = get_random_person()
        if second_name != first_name:
            break
    print(f"The second person is: {second_name}")
    print(second_description)
    print(f"From: {second_country}")

    while True:
        answer = str(input("Higher or Lower?: ")).lower()
        if answer not in ["higher" or "lower"]:
            print("Please introduce a valid answer! ")
            continue

        if answer == "higher":
            if first_follower < second_follower:
                print(random.choice(win_list))
                points += 1
                set_first_from_second()

            elif first_follower == second_follower:
                print("They are the same amount ")
                set_first_from_second()

            else:
                print(f"You lost! Your final score its {points}")
                exit()
        elif answer == "lower":
            if first_follower > second_follower:
                print(random.choice(win_list))
                points += 1
                set_first_from_second()

            elif first_follower == second_follower:
                print("They are the same amount ")
                set_first_from_second()

            else:
                print(f"You lost! Your final score its {points}")
                exit()

        print(f"Your actual points are: {points}")
        print("---")