import random

string = "a quick brown fox jumps over the lazy dog"
string = list(string)
jumbled = ""

print(string)

for letter in range(0,len(string)-1):
    jumbled += string.pop(random.randint(0,len(string)-1))

    print(string)
    print(jumbled)
