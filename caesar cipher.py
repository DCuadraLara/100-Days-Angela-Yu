alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text, shift_amount, direction):
    secret_txt = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            last_pos = (alphabet.index(letter) + shift_amount) % 26 # keep on list
            secret_txt += alphabet[last_pos]
        else:
            secret_txt += letter # preserve space
    print(f"Your {direction}d message is: {secret_txt}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # correct errors with high numbers
    
    caesar_cipher(text, shift, direction)

    reset = input("Would you like to encode/decode another message? y/n ").lower()
    if reset != "y":
        break
