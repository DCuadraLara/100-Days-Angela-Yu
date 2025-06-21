class PaymentMachine:
    def __init__(self):
        self.money_received = 0

    def make_payment(self, cost):
        print(f"\nPlease insert €{cost:.2f}")
        self.money_received = float(input("Enter amount: €"))
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is your change: €{change}")
            print("Payment accepted ✅")
            return True
        else:
            print("Not enough money. Payment declined ❌")
            return False
