import matplotlib.pyplot as plt

# stack plot
# track changes over time for two or more groups
# two or more related groups  that make up one whole category


days = [1,2,3,4,5,6,7]

sleeping = [8,12,5,8,9,12,10]
eating = [2,5,2,1,2,1,1]
working = [12,2,13,14,11,10,12]
playing = [2,5,4,1,2,1,1]



plt.plot([],[], color='m',label='Sleeping',linewidth=5)
plt.plot([],[], color='c',label='Eating',linewidth=5)
plt.plot([],[], color='r',label='Working',linewidth=5)
plt.plot([],[], color='k',label='Playing',linewidth=5)


plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])


plt.xlabel("March")
plt.ylabel("Hours")
plt.title("Stack Plot / Area Plot --  Timeline")
plt.legend()

plt.show()



