alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):

    new_word = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == 'encode':
                new_position = shift + position
                if new_position >= len(alphabet):
                    new_position = new_position - len(alphabet)
            elif direction == 'decode':
                new_position = position - shift
            new_word += alphabet[new_position]
        else:
            new_word += letter
    print(f"The encrypted message is: {new_word}")


end_game = False

while not end_game:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)

    again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if again == 'no':
        end_game = True
        print("END")
