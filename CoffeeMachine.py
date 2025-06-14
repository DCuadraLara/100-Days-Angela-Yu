import threading
import time
import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Global values
coffee_states = ["Serving", "Done☕"]
machine_state = "OFF"
total_profit = 0


def switch_status():
    global machine_state
    if machine_state == "OFF":
        print("\nStarting up coffee machine", end="", flush=True)
        for _ in range(4):
            time.sleep(0.4)
            print(".", end="", flush=True)
        time.sleep(0.3)
        machine_state = "ON"
        print(f"\n☕ *{machine_state}*\n")
    elif machine_state == "ON":
        print("\nShutting down coffee machine", end="", flush=True)
        for _ in range(4):
            time.sleep(0.4)
            print(".", end="", flush=True)
        time.sleep(0.3)
        machine_state = "OFF"
        print(f"\n🛑 *{machine_state}*\n")
        sys.exit()


def timer_end():
    print("\n⏰ Wait time's ended! Turning off.")
    sys.exit()


def payment(coffee):
    if coffee in MENU:
        coffee_cost = MENU[coffee]["cost"]
        print(f"Introduce the amount required: {coffee_cost}$")

        money = 0.0
        coin_values = {
            "pennies": {"cost": 0.01},
            "nickels": {"cost": 0.05},
            "dimes": {"cost": 0.10},
            "quarters": {"cost": 0.25}
        }

        for coin in coin_values:
            while True:
                try:
                    count = int(input(f"How many {coin} are you going to introduce?: "))
                    money += count * coin_values[coin]["cost"]
                    break
                except ValueError:
                    print("That's not a valid input.")

        print(f"The total amount you introduced is: {money:.2f}$")

        if money < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
            sys.exit()
        elif money > coffee_cost:
            change = money - coffee_cost
            print(f"Your change is: {change:.2f}$")
            sum_money(coffee_cost)
        else:
            print("Exact amount received. No change.")
            sum_money(coffee_cost)


def sum_money(money):
    global total_profit
    total_profit += money
    return total_profit


def report():
    print("\n--- RESOURCE REPORT ---")
    for x in resources:
        print(f"The remaining {x} is {resources[x]}")
    print(f"The total profit: {total_profit}$")
    print("-------------------------\n")


def deduct_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        amount_needed = MENU[coffee]["ingredients"][ingredient]
        resources[ingredient] -= amount_needed


def check_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources_needed = MENU[coffee]["ingredients"][ingredient]
        if resources[ingredient] < resources_needed:
            print("Sorry, there's not enough", ingredient)
            switch_status()
            sys.exit()


# -------- MAIN --------
switch_status()  # Turn ON the machine
timer = threading.Timer(70, timer_end)
timer.start()

while True:
    order = input("What would you like? Espresso / Latte / Cappuccino: ").lower()

    if order == "report":
        report()
        continue

    if order not in MENU:
        print("Please introduce a valid coffee.")
        continue

    timer.cancel()
    check_resources(order)
    payment(order)
    deduct_resources(order)

    print(coffee_states[1], end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    timer = threading.Timer(45, timer_end)
    timer.start()

    another = input("---\nDo you want another coffee? (yes/no): ").lower()
    if another != "yes":
        timer.cancel()
        print("Shutting down the coffee machine. Goodbye!")
        switch_status()  # Turn OFF the machine
        break
