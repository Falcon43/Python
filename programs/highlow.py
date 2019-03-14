import random

cpu_num = random.randint(1,100)

player_num = int(input("Enter a number between 1-100: "))

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too high")
    else:
        print("Too low")
    player_num = int(input("Enter a number between 1-100: "))

print("Well Done  !!")