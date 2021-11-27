import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
print(art.logo)


def caesar(t, s, d):
    end_text = ""
    if s >= 46:
        s %= 26
        print(s)
    for l in t:
        if l in alphabet:
            if d.lower() == "encode":
                idx = alphabet.index(l) + s
                end_text += alphabet[idx]
            elif d.lower() == "decode":
                idx = alphabet.index(l) - s
                end_text += alphabet[idx]
        else:
            end_text += l
    print(f"Your {d}d text is '{end_text}'")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    caesar(text, shift, direction)
    result = input("Type Yes if you want to go again, otherwise type no: ")
    if result == "no":
        should_continue = False
        print("Bye!")
# def encrypt(t, s):
#     encrypted_text = ""
#     for l in t:
#         idx = alphabet.index(l) + s
#         encrypted_text += alphabet[idx]
#     print(f"Your encrypted text is '{encrypted_text}'")


# def decode(t, s):
#     decrypted_text = ""
#     for l in t:
#         idx = alphabet.index(l) - s
#         decrypted_text += alphabet[idx]
#     print(f"Your decrypted text is '{decrypted_text}'")


# if direction.lower() == "encode":
#     encrypt(text, shift)
# elif direction.lower() == "decode":
#     decode(text, shift)
