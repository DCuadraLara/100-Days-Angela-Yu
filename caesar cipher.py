alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount):
    secret_code = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            new_pos = (alphabet.index(letter) + shift_amount) % 26
            secret_code += (alphabet[new_pos])
        else:
            secret_code += letter # preserve spaces
    print(secret_code)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift)

    reset = input("Would you like to encode or decode another message? Y/N ").lower()
    if reset != "y":
        break

