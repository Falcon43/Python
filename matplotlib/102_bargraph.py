import matplotlib.pyplot as plt


plt.bar([1,3,5,7,9], [5,2,7,8,2], label="Stock X")
plt.bar([2,4,6,8,10], [8,6,2,5,6], label="Stock y",color='g')

plt.legend()
plt.xlabel("March")
plt.ylabel("Price")
plt.title("Bargraph - Stock Market Analysis")

plt.show()