
for i in [0,1,2,3,4,5]:
    print(i**2)

for i in range(6):      # createsan iterator over that range producing it one at a time
    print(i**2)


print("\n\n Looping over list : The right way :")
colors = ['red','blue','green','yellow']

for i in range(len(colors)):    # don't do this
    print(colors[i])

for color in colors:      # DO this : easier to read : faster in python
    print(color)


print("\n\n Loop backward :  The right way :")


for i in range(len(colors)-1, -1, -1):      # don't do this
    print(colors[i])

for color in reversed(colors):       # DO this : easier to read : faster in python
    print(color)


print("\n\n Loop over indicies and collection :  The right way :")

for i in range(len(colors)):     # don't do this
    print(str(i)+" -->  "+colors[i])



for i,color in enumerate(colors):       # DO this : easier to read : FASTER in python :  whenever you are manipulating indices directly you are probably doing it wrong
    print(str(i)+" -->  "+color)
    print(str(i)+" -->  "+colors[i])




print("\n\n Loop over 2 collections :  The right way :")

months = ['jan','feb','march','april']
colors = ['red','blue','green','yellow','cyan']

n =  min(len(months) , len(colors))          # don't do this, this method works in other languages
for i in range(n):
    print(months[i]+" --> "+colors[i])


for month,color  in zip(months,colors):           # python way
    print(month+" --> "+color)




print("\n\n Loop in sorted order  :")

for color in sorted(colors):
    print(color)


for color in sorted(colors, reverse=True):
    print(color)



print("\n\n Custom sort order  :")

colors = ['red','blue','green','yellow','cyan']

#    def compare_length(c1 , c2):                   #  cmp functions not available in python 3
#        if len(c1) < len(c2):  return -1
#        if len(c1) > len(c2):  return 1
#        return 0
#
#    print(sorted(colors, key=compare_length))


print(sorted(colors , key=len))  # key function gets called exactly once per key





