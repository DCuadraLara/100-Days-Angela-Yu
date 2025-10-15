"""Basic example to calculate the tip we should pay."""

# Variables
bill = 150.00

print("Welcome to the tip calculator!")
people = int(input("Number of people: "))
split_bill = (bill / people) * 1.12

print(f"Each person should pay:{split_bill:.2f} Dollars")  # split_bill:2f shows 2 decimates.
