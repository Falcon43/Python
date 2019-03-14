ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
#           123456789                25

message = input("Enter message : ").upper()
encrypted = ""

print("\nOriginal Message:  "+message)

for letter in message:
    if letter == " ":
        encrypted += " "
    elif ALPHABET.index(letter) + 5 > len(ALPHABET)-1:
        encrypted += ALPHABET[ALPHABET.index(letter)-len(ALPHABET)+5]
    else:
        encrypted += ALPHABET[ALPHABET.index(letter)+5]

print("Encrypted message: "+encrypted)