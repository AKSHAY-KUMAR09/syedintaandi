alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
#
# # encrypt(original_text=text, shift_amount=shift)
#
#
#
# def decrypt(orginal_text,shift_amount):
#     decrtypttext=""
#     for x in orginal_text:
#         shifted_position = alphabet.index(x) - shift_amount
#         shifted_position %= len(alphabet)
#         decrtypttext += alphabet[shifted_position]
#     print(decrtypttext)

# decrypt(text,shift)
def cypher(original_text,shift_amount,direction):
    if direction == "encode":

        def encrypt(original_text,shift_amount):
            cipher_text = ""
            for letter in original_text:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            print(f"Here is the encoded result: {cipher_text}")
        encrypt(original_text,shift_amount)

    elif direction == "decode":
        def decrypt(original_text, shift_amount):
            decrtypttext = ""
            for x in original_text:
                shifted_position = alphabet.index(x) - shift_amount
                shifted_position %= len(alphabet)
                decrtypttext += alphabet[shifted_position]
            print(decrtypttext)
        decrypt(original_text,shift_amount)


cypher(text,shift,direction)