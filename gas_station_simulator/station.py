import time

class Station:
    def __init__(self):
        self.resources = {
            "diesel": 500,
            "gasoline": 600,
            "electric": 200
        }

    def report(self):
        print("\nFuel levels:")
        for fuel, amount in self.resources.items():
            print(f"{fuel.capitalize()}: {amount}L")

    def is_fuel_sufficient(self, fuel, amount):
        if self.resources[fuel.name] >= amount:
            return True
        print(f"Sorry, not enough {fuel.name}.")
        return False

    def dispense_fuel(self, fuel, amount):
        print(f"\nDispensing {amount}L of {fuel.name}.")
        for _ in range(4):
            time.sleep(0.4)
            print(".", end="", flush=True)
        time.sleep(0.3)
        self.resources[fuel.name] -= amount
        print("Done ✅")
