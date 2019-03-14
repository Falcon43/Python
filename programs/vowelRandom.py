import random

VOWELS = ("a", "e", "i" ,"o", "u")
message = input("Enter your message:  ")
new_message =""
for letter in message:
    if letter not in VOWELS:
        new_message += letter

    else:
        new_message += random.choice(VOWELS)

print(new_message)