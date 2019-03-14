import random

cpu_num = random.randint(1,100)
guesses = []
player_num = int(input("Enter a number between 1-100: "))
guesses.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too high")
    else:
        print("Too low")
    player_num = int(input("Enter a number between 1-100: "))
    guesses.append(player_num)

print("Well Done  !!")
print("It took you %i guesses."%len(guesses))
print("Here are your guesses")
print(guesses)