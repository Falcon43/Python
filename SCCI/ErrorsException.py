import sys
print("\n  try except statements:   [handled] ")

while True:
    try:
        x = int(input(":  "))
    except ValueError:
        print("Not a valid number. ")
        break



print("\n\nAssert statements:  [!handled]\n")

def KelvinToFahrenheit(Temperature):
    assert (Temperature>=0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.46)))
print(KelvinToFahrenheit(0))
#print(KelvinToFahrenheit(-5))      #uncomment to assert
print(KelvinToFahrenheit(78))






print("\n\nRaising exceptions:  [handled]\n")

try:
    raise Exception("spam","eggs")
except Exception as inst:
    print(type(inst))   # the exception instance
    print(inst.args)    # arguments stored in .args
    print(inst)         # __str__ allows args to be printed directly
    x,y = inst.args
    print("x= "+x)
    print("y= "+y)





print("\n\nRe-Raise exceptions:   [!handled]\n")

try:
    raise NameError("Hi There!")
except NameError:
    print("An exception flew by!")
    raise   # in try block u handle exception , but if we dont intend to handle it we can re-raise the exception