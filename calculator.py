# A simple calculator, you can input 2 numbers and an operator for it
# then ask you if you want to continue or not with the result as number 1

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

reset = ""

calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
while True:
    while reset == "y":
        for key in calculator_dict:
            print(key)
        operation = input("Pick an operation ")
        n2 = int(input("What's the second number?: "))

        operation_result = calculator_dict[operation](n1, n2)
        print(operation_result)

        reset = input("Would you like to continue or go into a new operation? Y/N").lower()
        if reset == "y":
            n1 = operation_result
        if reset == "n":
            break

    n1 = int(input("What's the first number?: "))
    for key in calculator_dict:
        print(key)
    operation = input("Pick an operation ")
    n2 = int(input("What's the second number?: "))

    operation_result= calculator_dict[operation](n1, n2)
    print(operation_result)

    reset = input("Would you like to continue or go into a new operation? Y/N" ).lower()
    if reset == "y":
        n1 = operation_result
