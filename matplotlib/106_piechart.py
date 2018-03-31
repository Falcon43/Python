import matplotlib.pyplot as plt


# pie chart are similar to stack plot only they show data in a particular point in time
# parts to the whole and % share is shown

slices = [7,2,2,13]
activities = ["sleeping","eating","working","playing"]
colr = ['c','m','r','b']


plt.pie(slices,
        labels=activities,
        colors=colr,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')




plt.title("Pie Chart")

plt.show()