from fuel_menu import FuelMenu
from station import Station
from payment_machine import PaymentMachine

print("Welcome to our Gas Station")
print("---")

# We start our objects.
fuel = FuelMenu()
gas_station = Station()
pay = PaymentMachine()

while True:
    # Menu for options.
    print("Actually we have diesel / gasoline / electric recharge.")
    order = input("Please select one.\n")

    if order == "report":
        gas_station.report()

    else:
        amount = float(input("How many Liters.\n"))
        refill = fuel.find_fuel(order)

        if refill:
            if gas_station.is_fuel_sufficient(refill, amount):
                if pay.make_payment(refill.price * amount):
                    gas_station.dispense_fuel(refill, amount)

        else:
            print("We dont have that service.")

    reset = input("Wanna check something more?...  Y / N").lower()
    if reset != "y":
        break