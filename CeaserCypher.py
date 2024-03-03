alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

doYouCont = "yes"


def ceser_cypher(text, shift, direction):
    new_text = ''
    if shift > len(alphabet):
        shift = shift % 26

    for letter in text:
        if letter in alphabet:
            num = alphabet.index(letter)
            if direction == "encode":
                new_p = num + shift
            else:
                new_p = num - shift
            new_text += alphabet[new_p]
        else:
            new_text += letter
    print(f"the {direction}d text is {new_text}")


while doYouCont == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("type your message:\n")
    shift = int(input("Enter the shift amount\n"))
    ceser_cypher(text=text, shift=shift, direction=direction)
    doYouCont = input("Do you Want to Continue 'Yse' or 'No'\n").lower()
    if doYouCont == "no":
        print("Good Bye")
