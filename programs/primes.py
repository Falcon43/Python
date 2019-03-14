import math

composite = False
user_input = int(input("Enter no:  "))
checker = math.ceil(user_input**(1/2))
for i in range(2,checker+1):
    if user_input%i == 0:
        composite=True
        print(str(user_input)+"  is composite")
        break
if composite == False:
    print(str(user_input)+" is prime")


""""
sqrt  
ceil


"""


