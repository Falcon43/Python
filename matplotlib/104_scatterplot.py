import matplotlib.pyplot as plt

# scatterplot used for plotting 2 variables(x,y) or 3variables(x,y,z) if we are plotting 3D scatter plot,
# and then comparing those variables(finding correlation) to find groups or similarity and dissimilarity between variables


x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]


plt.scatter(x,y,label='cart size')
plt.xlabel("March")
plt.ylabel("Total items in cart'")
plt.legend()

plt.show()










