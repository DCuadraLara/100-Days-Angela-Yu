print("Welcome to the tip calculator!")

people_num = int(input("Number of people: "))
total_bill = 150.00
split_bill = (total_bill / people_num) * 1.12

print(f"{split_bill:.2f}")
